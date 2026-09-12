#!/usr/bin/env python3
"""Probe endpoint mana yang benar-benar menerima input gambar (vision).

Pemakaian:
    python3 scripts/test_vision_endpoints.py [path_gambar]
    (default gambar: /tmp/vision_test.png; kalau belum ada, buat dulu via PIL)

Membaca API key dari ~/.hermes/.env, kirim base64 image (format OpenAI-style)
ke tiap provider/model di ENDPOINTS, lalu lapor:
  [OK]   = balasan berisi deskripsi asli (model menerima gambar)
  [FAIL] = error (model text-only, service down, quota, geo-block, dll)

Gunakan saat vision_analyze gagal untuk tahu opsi fallback mana yang layak
dikonfigurasi di auxiliary.vision.*. Edit ENDPOINTS sesuai provider yang ada.
"""
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

ENV_PATH = Path.home() / ".hermes" / ".env"
DEFAULT_IMAGE = "/tmp/vision_test.png"
PROMPT = "Describe concisely what text is visible in this image. Answer in Indonesian."

# (nama, base_url, key_env, model) — tambah/kurangi sesuai provider yang ada
ENDPOINTS = [
    # ("Sumopod", "https://ai.sumopod.com/v1", "HERMES_CUSTOM_AI_SUMOPOD_COM_API_KEY", "glm-5-turbo"),
    # ("Hallorouter", "https://api.hallorouter.com/v1", "HALLOROUTER_API_KEY", "hallo/gemini-3-flash"),
    # ("Groq", "https://api.groq.com/openai/v1", "HERMES_CUSTOM_API_GROQ_COM_API_KEY", "llama-3.2-11b-vision-preview"),
]


def get_env(key: str) -> str:
    env = ENV_PATH.read_text() if ENV_PATH.exists() else ""
    for line in env.splitlines():
        if line.startswith(key + "="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def test(name: str, base_url: str, key: str, model: str, b64: str) -> None:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
        ]}],
        "max_tokens": 300,
    }
    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
            content = data["choices"][0]["message"]["content"]
            print(f"[OK] {name} ({model}): {content[:120]}")
    except Exception as e:
        body = ""
        try:
            body = e.read().decode()[:200] if hasattr(e, "read") else str(e)[:200]
        except Exception:
            pass
        print(f"[FAIL] {name} ({model}): {body}")


def main() -> int:
    img_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_IMAGE
    if not Path(img_path).exists():
        print(f"Gambar tidak ditemukan: {img_path}", file=sys.stderr)
        print("Buat dulu: python3 -c \"from PIL import Image, ImageDraw; im=Image.new('RGB',(600,200),'white'); ImageDraw.Draw(im).text((30,80),'HALO TEST 123',fill='black'); im.save('/tmp/vision_test.png')\"", file=sys.stderr)
        return 2
    b64 = base64.b64encode(Path(img_path).read_bytes()).decode()
    ran = 0
    for name, base_url, key_env, model in ENDPOINTS:
        key = get_env(key_env)
        if not key:
            print(f"[SKIP] {name} ({model}): key {key_env} tidak ada di .env")
            continue
        test(name, base_url, key, model, b64)
        ran += 1
    if ran == 0:
        print("Tidak ada endpoint terisi di ENDPOINTS — edit script dulu.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
