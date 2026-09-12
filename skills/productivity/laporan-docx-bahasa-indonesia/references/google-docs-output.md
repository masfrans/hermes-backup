# Output Dokumen ke Google Docs (dari laporan/SOP .docx)

Situasi: user minta "jadikan hasilnya ke file google docs" padahal hasilnya
biasanya .docx. Google Workspace sudah terhubung (skill `google-workspace`).

## Alur kerja

1. **Buat dokumen kosong**:
   `python /root/.hermes/skills/productivity/google-workspace/scripts/google_api.py docs create --title "<judul>"`
   → ambil `documentId` dari output JSON.

2. **Isi konten — JANGAN via CLI untuk teks panjang.**
   `docs append --text "..."` lewat shell GAGAL diam-diam pada teks panjang
   atau yang berisi tanda kutip: output bilang "appended" tapi `docs get`
   menampilkan body kosong (masalah quoting shell, bukan API).
   Cara yang benar — panggil fungsi module langsung dari Python:

   ```python
   import sys, types
   sys.path.insert(0, '/root/.hermes/skills/productivity/google-workspace/scripts')
   import google_api
   args = types.SimpleNamespace(doc_id=DOC_ID, text=ISI_LENGKAP)
   google_api.docs_append(args)
   ```

   Satu panggilan cukup per dokumen — append menyisipkan di akhir body
   (index = endIndex-1, sebelum newline akhir).

3. **Verifikasi**: `docs get <id>` → pastikan `body` terisi (jangan percaya
   status "appended" dari CLI). Lalu kirim link ke user:
   `https://docs.google.com/document/d/<id>/edit`

## Batasan yang ditemukan

- **Tabel header SOP tidak terbawa**: format tabel header template .docx
  (No Document BL-xxx, Department, Dibuat/Disahkan Tanggal, PIC, Approved by,
  DAFTAR REVISI) tidak bisa ditiru lewat append teks. Tawarkan versi .docx
  sebagai backup kalau header itu wajib.
- **Gambar tidak ikut**: append hanya teks. Dokumen sumber yang punya
  screenshot (cek `word/media/` di .docx via zipfile — SOP kalender punya 10
  gambar) sebaiknya dibuat versi .docx dulu agar posisi gambar akurat.
  Google Docs bisa ditambah gambar via insertInlineImage manual (perlu upload
  ke Drive dulu, posisi perkiraan) — kerja lebih banyak, tawarkan sebagai opsi.

## Pitfall

- Jangan kirim URL docs.google.com/document/d/<id>/edit tanpa verifikasi body.
- Kalau user bilang "tetap sertakan gambar": default ke .docx, bukan Docs.
