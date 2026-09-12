#!/usr/bin/env python3
"""Probe whether an OpenAI-compatible endpoint/model actually accepts IMAGE input.

Sends a real base64 image (OpenAI chat-completions image_url shape) and reports
whether the model answers with a description (vision-capable) or refuses/errors
(text-only, or the image never reached the model).

Usage:
  python3 vision_probe.py BASE_URL KEY_ENV MODEL[,MODEL2,...] IMAGE_PATH

  BASE_URL   e.g. https://ai.sumopod.com/v1  (the /chat/completions suffix is added)
  KEY_ENV    env var name in ~/.hermes/.env holding the API key
  MODEL      one or more comma-separated model ids to test
  IMAGE_PATH local image file (png/jpg)

Reads the key from ~/.hermes/.env (never paste keys into shell commands).
Exit code 0 if ANY model answered with content (likely vision-capable).

Expected outputs:
  [OK] model: <description>          -> model received and described the image
  [FAIL] model: <error body>         -> 400 "content.type invalid, allowed ['text']"
                                       = text-only; "I can't see the image" reply
                                       = model ran but never got the pixels
"""
import base64
import json
import sys
import urllib.request


def get_env(key_env: str) -> str | None:
    try:
        with open("/root/.hermes/.env", encoding="utf-8") as f:
            for line in f.read().splitlines():
                if line.startswith(key_env + "="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return None


def probe(base_url: str, key: str, model: str, image_path: str, prompt: str) -> bool:
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    mime = "image/png" if image_path.lower().endswith(".png") else "image/jpeg"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
        ]}],
        "max_tokens": 300,
    }
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
            content = data["choices"][0]["message"]["content"]
            print(f"[OK] {model}: {content[:120]}")
            return True
    except Exception as e:
        body = ""
        try:
            body = e.read().decode()[:200] if hasattr(e, "read") else str(e)[:200]
        except Exception:
            pass
        print(f"[FAIL] {model}: {body}")
        return False


def main() -> None:
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(2)
    base_url, key_env, models_csv, image_path = sys.argv[1:5]
    key = get_env(key_env)
    if not key:
        print(f"[SKIP] no key for {key_env} in ~/.hermes/.env")
        sys.exit(1)
    prompt = "Describe concisely what text is visible in this image. Answer in Indonesian."
    ok = any(probe(base_url, key, m.strip(), image_path, prompt)
             for m in models_csv.split(","))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
