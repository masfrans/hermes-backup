# Platform Hints: Inject Persona & Aturan ke System Prompt per Platform

Worked example (2026-08): bot WhatsApp "Mas Bro" memanggil semua pengguna "Mas Bro"
padahal harus pakai display name WA. Screenshot + log gateway menunjukkan bot membalas
"halo" dari user lain dengan "Halo Mas Bro!" (50 chars, 1 API call, tanpa tool call).

## Akar masalah
- Persona bot dinamai "Mas Bro"; model (deepseek-v4-flash) memakai nama BOT sendiri
  untuk memanggil USER: "Halo Mas Bro!".
- Aturan "jangan panggil pengguna Mas Bro" SUDAH ada di memori + file identitas
  (/root/.hermes/scripts/wa_bot_identity.md), tapi model mengabaikannya (balas
  langsung tanpa baca file). Fix level file/memori tidak cukup; aturan harus ada
  di system prompt.

## Solusi: agent.platform_hints.<platform>.append
config.yaml:
```yaml
agent:
  platform_hints:
    whatsapp:
      append: 'Aturan tetap persona WhatsApp: ...'
```

Set via script (pakai venv hermes, hindari quoting shell):
```python
import sys; sys.path.insert(0, "/usr/local/lib/hermes-agent")
from hermes_cli.config import set_config_value
set_config_value("agent.platform_hints.whatsapp.append", TEXT, force=False)
```

## Cara kerja di kode
- Dibaca di agent/agent_init.py (~line 1921): `_agent_cfg.get("platform_hints", {})`
  → disimpan ke `agent._platform_hint_overrides`.
- Diresolve di agent/system_prompt.py `_resolve_platform_hint` (line ~80):
  string = append ke default hint; dict {replace|append} = ganti/tambah.
- Hasil masuk ke `post_workspace_parts` = STABLE tier system prompt (line ~690-694),
  di depan context & volatile tiers.
- Berlaku untuk SESI BARU platform tsb. Sesi lama: prompt di-cache per sesi
  (invariant: jangan ubah system prompt mid-conversation).

## Tanpa restart gateway (config.yaml)
`load_config_readonly` (hermes_cli/config.py `_load_config_impl` line ~3446) pakai
cache signature (st_mtime_ns, st_size): file berubah → baca ulang dari disk.
Setiap agent build (sesi baru) memanggilnya. Jadi config.yaml langsung efek ke sesi
baru TANPA restart. HANYA .env yang di-load saat gateway startup → butuh restart.
Catatan: restart gateway dari dalam sesi akan memutus obrolan aktif ~10-20 detik;
untuk perubahan config.yaml lebih baik TIDAK restart.

## Reset sesi yang sudah terlanjur kena
1. Cari session_id: `~/.hermes/sessions/sessions.json` (cari chat_id → session_id;
   file ini legacy mirror, source of truth ada di state.db gateway_routing).
2. `hermes sessions delete <session_id> --yes`
3. Aman: gateway punya stale-routing self-heal (gateway/session.py #54878, ~line 2632):
   entry routing yang menunjuk sesi ended/missing dibuang otomatis, sesi baru dibuat
   saat pesan berikutnya masuk.

## Verifikasi
```python
from hermes_cli.config import load_config_readonly
cfg = load_config_readonly()
v = cfg["agent"]["platform_hints"]["whatsapp"]["append"]
assert "JANGAN" in v   # newline terjaga setelah round-trip YAML
```

## Catatan
- CLI `hermes config set agent.platform_hints.whatsapp.append "..."` menampilkan
  warning "not a recognized config key" tapi nilai TETAP disimpan dan DIBACA oleh
  agent_init. Daftar key validator (`_validate_config_key`) tidak lengkap.
- Isi aturan dengan contoh SALAH vs BENAR eksplisit (model lemah butuh pola konkret):
  "SALAH: Halo Mas Bro! / BENAR: Halo ibramsyah 👋 Aku Mas Bro, ...".
- Tempat lain yang perlu disinkronkan: file panduan identitas
  (~/.hermes/scripts/wa_bot_identity.md) dan memori (entry ringkas + contoh).
