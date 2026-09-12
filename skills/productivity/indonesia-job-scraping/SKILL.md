---
name: indonesia-job-scraping
description: "Scrape Indonesian job portals (Jobstreet, Kalibrr, etc)."
version: 1.0.0
platforms: [linux]
---

# Scraping Portal Lowongan Kerja Indonesia

## When to Use
- User minta daftar lowongan kerja ("cari lowongan X terbaru", "loker HR", "lowongan pengalaman N tahun")
- Minat rekuren user: loker HR Indonesia (lihat user profile)

## Script Siap Pakai (REKOMENDASI)
`/root/.hermes/scripts/cari_loker.py` - multi-sumber dalam satu perintah:

```bash
python3 /root/.hermes/scripts/cari_loker.py "HR Recruitment" --days 14 --max 10
python3 /root/.hermes/scripts/cari_loker.py "Staff HRD" --days 7 --max 5
```

- Sumber: Jobstreet (default) + Dealls + Glints (lewati closed) + Kitalulus
- Otomatis: filter keyword, dedupe link, urut dari terbaru (pakai tanggal resmi)
- Glints di-skip jika `closedAt`/`expiredAt` ada (hati-hati: banyak lowongan closed)
- Catatan: filter keyword KETAT (judul harus mengandung keyword). Kalau hasil 0 padahal sumber ada, coba keyword lebih pendek (misal "HR" bukan "HR Recruitment").

## Teknik Umum
- `web_extract` backend ddgs = **search-only, TIDAK bisa extract URL**. Pakai curl/urllib dengan browser User-Agent:
  `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0`
- **Deskripsi Google Search MENYESATKAN**: menampilkan lowongan yang sudah closed, tanggal lama, "1-3 tahun" padahal lowongan mati. SELALU verifikasi tanggal & status di halaman asli.
- Filter "posting 7 hari terakhir": pakai listingDate / "X ago" display, bukan asumsi dari ID.

## Jobstreet (paling baik: link stabil + tanggal resmi)
- Halaman daftar: `https://id.jobstreet.com/hr-recruitment-jobs` (ganti kategori sesuai)
- Embedded JSON punya: `"id":"NNN"` + `"listingDate":"ISO"` + `"listingDateDisplay":"2d ago"`
- Link lowongan: `https://id.jobstreet.com/job/NNN`
- Regex extract: `"id":"(\d+)".{0,200}?"listingDate":"([^"]+)"[^}]*?"listingDateDisplay":"([^"]+)"`
- Cari detail pengalaman di halaman lowongan: regex `pengalaman[^.]{0,90}\.` (atau `experience`)
- ID besar (93.9M+) = lebih baru; ID kecil di embedded JSON bisa salah pasangan dengan judul - cocokkan hati-hati

## Kalibrr
- Daftar: `https://www.kalibrr.com/home/i/human-resources`
- Extract path: `/c/<company>/jobs/<id>/<slug>`, prefix `https://www.kalibrr.com`
- Halaman detail berisi syarat pengalaman dalam teks; cek tiap kandidat sebelum rekomendasi

## Dealls (BARU, sudah diuji)
- Daftar: `https://dealls.com/en/loker?keyword=<kata+kunci>` (pakai `/en/loker` - tanpa /en sering 404/403)
- Data di `__NEXT_DATA__` JSON: tiap job punya `slug`, `role` (judul), `company.name`, `locationName.name`, `publishedAt` (ISO)
- Link lowongan: `https://dealls.com/en/loker/<slug>~<company-slug>`
- `experienceLevel` KOSONG di halaman list - syarat pengalaman cuma di halaman detail
- Halaman kadang timeout - retry 2x dengan jeda
- Keyword search TIDAK terfilter ketat (campur posisi lain) - filter manual di judul

## Glints (HATI-HATI)
- Halaman di-render client-side (React) - minim data di HTML statis
- API: `https://glints.com/api/jobs?keyword=X&country=ID` (bisa 403 kena rate-limit; tambah header Referer)
- **BANYAK lowongan hasil pencarian SUDAH CLOSED** - cek `closedAt` di halaman detail sebelum merekomendasikan!
- Deskripsi pencarian ("1-3 tahun pengalaman") TIDAK menjamin lowongan aktif

## Kitalulus
- `https://www.kitalulus.com/lowongan/detail/<slug>`
- Punya `datePosted` JSON-LD + teks "diperbarui X hari yang lalu"

## Uploker
- `https://uploker.com/lowongan-kerja/<slug>`
- Embedded JSON kaya: datePosted, minExperienceYears/maxExperienceYears, gaji, applyEmail

## Hindari
- **Jora (id.jora.com)**: proses tutup di Indonesia, sudah tidak kredibel (user menyatakan ini)
- **LinkedIn scraping penuh**: login wall + melanggar ToS. Untuk cari profil orang: cukup Google `site:linkedin.com/in` keyword, kumpulkan nama+jabatan+link publik

## Pitfalls
- Jobstreet kadang render link duplikat (`?type=standard&ref=...`) - dedupe dengan ambil bagian `/job/NNN` saja
- Filter lowongan yang benar-benar masuk kriteria (misal 1-3 tahun): jangan percaya label pencarian, baca syarat di halaman detail
- Kalau scraping JS-heavy site gagal, alternatif: minta user screenshot (baca via vision) atau copy teks
