---
name: google-docs-automation
description: "Buat/isi Google Docs via google_api.py: pola capture doc_id."
version: 1.0.0
platforms: [linux]
---

# Google Docs Automation (via google_api.py)

Pola pembuatan & pengisian Google Docs secara programatik pakai
`~/.hermes/skills/productivity/google-workspace/scripts/google_api.py`
(bundled skill, author Nous Research). Terbukti di sesi SOP BelajarLagi
(bikin 8+ Google Docs SOP berulang).

## Trigger

- User minta hasil (SOP/laporan) dibuat sebagai Google Docs
- Perlu create + append isi dokumen otomatis
- Error "Missing required parameter documentId" / token revoked

## Pitfall utama

`google_api.docs_create(args)` **TIDAK return doc_id** - fungsi print JSON ke
stdout dan return None. Jangan akses `out["documentId"]` → TypeError.

## Pola yang benar (capture stdout)

```python
import sys, types, json, io, contextlib, re

sys.path.insert(0, '/root/.hermes/skills/productivity/google-workspace/scripts')
import google_api

# 1. Create - tangkap doc_id dari stdout
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    google_api.docs_create(types.SimpleNamespace(title="Judul", body=None))
m = re.search(r'"documentId":\s*"([A-Za-z0-9_-]+)"', buf.getvalue())
doc_id = m.group(1) if m else None

# 2. Append isi (teks panjang aman - tidak kena quoting shell)
google_api.docs_append(types.SimpleNamespace(doc_id=doc_id, text=isi_lengkap))

# 3. Verifikasi: cek keyword penting ADA di body
d = google_api.docs_get(types.SimpleNamespace(doc_id=doc_id))
print('ADA' if 'KEYWORD' in d.get('body', '') else 'KURANG')
```

Kenapa langsung panggil module (bukan CLI): teks panjang berisi tanda petik/
karakter khusus bakal bermasalah dengan quoting shell via `$GAPI docs append
--text "..."`. Import module + SimpleNamespace = bebas masalah.

## Token expired / revoked

- Gejala: `RefreshError: invalid_grant: Token has been expired or revoked.`
  saat API; `setup.py --check` → `TOKEN_REVOKED`
- Fix flow:
  1. `setup.py --auth-url` → kirim link ke user
  2. User klik, login, Allow (browser error localhost = NORMAL)
  3. User copy URL lengkap (berisi `code=...`) & kirim balik
  4. `setup.py --auth-code "<URL_LENGKAP>"`
  5. `setup.py --check` → AUTHENTICATED
- `AUTHENTICATED (partial)` = user tidak izinkan sebagian scope (mis.
  contacts/gmail.send) - sisanya tetap jalan; tidak perlu ulang

## Pitfall lain

- Verifikasi selalu setelah append (docs get → cek keyword) - jangan asumsi
- Ganti model utama tidak perlu re-auth Google (OAuth terpisah)
- Referensi lengkap CLI: skill `google-workspace` (bundled)
