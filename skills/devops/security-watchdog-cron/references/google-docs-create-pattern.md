# Google Docs: buat + append via google_api.py (pola teruji)

Workflow yang terbukti di sesi BelajarLagi (bikin Google Docs SOP berulang kali).

## Pitfall utama

`google_api.docs_create(args)` **TIDAK return doc_id** - fungsi ini print JSON
ke stdout dan return None. Jangan akses `out["documentId"]` → TypeError
(Missing required parameter "documentId").

## Pola yang benar (capture stdout)

```python
import sys, types, json, io, contextlib, re

sys.path.insert(0, '/root/.hermes/skills/productivity/google-workspace/scripts')
import google_api

# 1. Create - tangkap doc_id dari stdout
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    google_api.docs_create(types.SimpleNamespace(title="Judul Dokumen", body=None))
m = re.search(r'"documentId":\s*"([A-Za-z0-9_-]+)"', buf.getvalue())
doc_id = m.group(1) if m else None

# 2. Append isi
google_api.docs_append(types.SimpleNamespace(doc_id=doc_id, text=isi_lengkap))

# 3. Verifikasi
d = google_api.docs_get(types.SimpleNamespace(doc_id=doc_id))
body = d.get('body', '')
# cek keyword penting ADA
```

## Token expired / revoked

- Gejala: `RefreshError: invalid_grant: Token has been expired or revoked.`
  saat panggil API; `setup.py --check` → `TOKEN_REVOKED`
- Fix: `setup.py --auth-url` → kirim link ke user → user klik & Allow →
  browser error localhost (NORMAL) → user copy URL lengkap (ada `code=...`) →
  `setup.py --auth-code "<URL_LENGKAP>"` → `setup.py --check`
- Catatan: user boleh tidak mengizinkan semua scope (mis. contacts/gmail.send
  tidak dicentang) → `AUTHENTICATED (partial)` - tetap jalan untuk
  docs/drive/sheets/calendar

## Catatan lain

- Ganti model utama tidak perlu re-auth Google (OAuth terpisah dari LLM)
- Scope yang hilang hanya mematikan layanan itu, sisanya tetap berfungsi
