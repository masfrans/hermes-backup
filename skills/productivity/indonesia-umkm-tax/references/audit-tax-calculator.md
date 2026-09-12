# Audit kalkulator pajak UMKM (tax-calculator-1-2.lovable.app) — Agustus 2026

Metode + temuan audit tuntas kalkulator pajak JS (Lovable app). Dipakai sebagai template audit
untuk kalkulator pajak lain dan sebagai bank data NPPN yang terverifikasi.

## Metode audit (reproducible)
1. Ambil halaman `/`, cari `<script src="/assets/index-*.js">` (bundle loader).
2. Dalam loader cari `import('./routes-*.js')` → unduh bundle routes (logika ada di sini, bukan di index).
3. Baca konstanta langsung: `i=.005` (final 0,5%), `a=48e8` (batas 4,8 M), `o=5e8` (bebas 500 jt),
   `s=.22` (tarif badan), `c={...}` (PTKP), `l=[...]` (lapisan Pasal 17), `u={...}` (DB norma NPPN).
4. Bandingkan dengan aturan resmi (lihat SKILL.md). Jangan percaya teks deskripsi di UI — baca kodenya.

## Temuan (apa yang benar)
- Tarif final 0,5% + batas omzet 4,8 M; fasilitas bebas 500 jt hanya OP; CV/Firma/PT/BUMDes keluar; tarif badan 22%; PTKP; Pasal 31E proporsional — semua benar.
- Lapisan Pasal 17 benar: 5% (≤60 jt), 15% (60–250 jt), 25% (250–500 jt), 30% (500 jt–5 M), 35% (>5 M).

## Temuan (apa yang belum tepat)
1. **DB norma NPPN cuma 12 KLU + semua salah**: 14111 (tool 20/18/16 vs resmi 13,5/13/12,5),
   46100 (30/25/23 vs 25/20/20), 49422 (20/18/15 vs 20/15/15), 56101 (25/23/20 vs 25/20/20),
   56303 (27/24/22 vs 25/20/20), 62010 (50/47/45 vs 50/50/50), 70209 (55/52/50 vs 50/50/50),
   73100 (50/47/45 vs 50/50/50), 85499 (45/42/40 vs 30/27,5/25).
2. **3 kode KLU fiktif**: 47190, 90020, 96020 tidak ada di PER-17/PJ/2015 (kode benar: 47191/47192,
   90001–90009, 96111 dst).
3. **10 ibukota provinsi salah**: tool menaruh "Batam", resminya **Pontianak** (Pasal 4 PER-17/PJ/2015:
   Medan, Palembang, Jakarta, Bandung, Semarang, Surabaya, Denpasar, Manado, Makassar, Pontianak).
   Kota2 tool cuma 22 (seharusnya ~24 ibukota provinsi lainnya).
4. **"NPPN (Badan)" tidak legal** — badan wajib pembukuan (Pasal 28 UU KUP).
5. **Koperasi tanpa batas 4 tahun pajak** (PP 20/2026 tidak mengubah batas koperasi).
6. **Dasar hukum salah**: tool menulis "PMK 15/2018 & Pasal 14 UU PPh" — seharusnya PER-17/PJ/2015.
7. **PKP tidak dibulatkan ribuan ke bawah** (Pasal 17 ayat 4).
8. **NPM vs norma tercampur**: untuk NPPN, laba = norma% × omzet, bukan NPM × omzet.
9. **Dropdown KLU menyesatkan**: klaim "1.436 kode" tapi cuma 12 punya data; sisanya fallback ke
   normaManual default 25% tanpa peringatan. Dropdown kota detail (`in_kota_detail`) dekoratif,
   tidak memengaruhi hitung.

## Database NPPN PER-17/PJ/2015 (dihitung dari PDF resmi, masih berlaku)
- Lampiran I (OP pilih norma): **1.434 entri** (1.433 KLU unik; KLU 23112 duplikat di nomor 442 & 443 di dokumen resmi).
- Lampiran II (OP tidak/belum pembukuan, Pasal 14 ayat 5): **1.434 entri** (duplikat sama).
- Lampiran III (WP Badan, Pasal 14 ayat 5): **1.432 entri** (tanpa KLU 10615/10616).
- Total: **4.300 entri**. Lampiran IV = contoh pemakaian.
- Setiap entri: nomor, KLU 5 digit, uraian, 3 kolom % (10 ibukota provinsi / ibukota provinsi lainnya / daerah lainnya).

## Cara parsing PDF PER-17/PJ/2015
- Sumber: `https://www.pajak.go.id/id/peraturan-direktur-jenderal-pajak-nomor-17pj2015` (halaman
  berisi link PDF badan + Lampiran 1–4; URL file di hasil search sering 404 — buka halaman peraturannya).
- Konversi: `pdftotext -layout file.pdf file.txt` (tersedia di sistem, tanpa pip).
- Pola entri: `^\s*(\d{1,4})\s+(\d{4,5})\s+` — **KLU bisa kehilangan leading zero** ("3118" = 03118),
  pakai `\d{4,5}` lalu `zfill(5)`; nomor urut harus sekuensial untuk deteksi entri terlewat.
- Persentase di akhir baris: `((?:\d{1,2}(?:,\d+)?\s*){3})$` (urutan kota1/kota2/kota3).

## Daftar perbaikan yang direkomendasikan (aturan, rumus, UI, panduan, urutan fitur)
1. Muat DB norma lengkap 1.434 entri; spot-check persentase ke PDF resmi; hapus KLU fiktif.
2. Ganti Batam → Pontianak; lengkapi daftar ibukota provinsi lainnya.
3. Hapus skema "NPPN (Badan)"; tambahkan batas 4 tahun koperasi.
4. Bulatkan PKP ribuan ke bawah; pisahkan konsep NPM (untuk Pasal 17/31E) vs norma (untuk NPPN).
5. Perbaiki dasar hukum (PER-17/PJ/2015, bukan PMK 15/2018).
6. UI: tandai jelas KLU tanpa data ("wajib isi manual"), hubungkan dropdown kota detail ke hitung,
   gabung tab "Norma"+"NPPN", tambah validasi input (omzet ≥ 0, norma 0–100%).
7. Tambah panduan penggunaan (langkah, penjelasan tiap skema, disclaimer simulasi ≠ konsultasi resmi,
   contoh kasus).
8. Urutan fitur ideal: Data Usaha → Hasil Perbandingan + rekomendasi → Detail per skema → Referensi
   (tabel norma lengkap, kalender pajak).
9. Fitur tambahan: filter skema per bentuk usaha, simulasi masa transisi (CV/PT lama), ekspor PDF/CSV,
   rincian per lapisan tarif.
