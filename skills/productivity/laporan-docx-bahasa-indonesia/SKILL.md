---
name: laporan-docx-bahasa-indonesia
description: "Buat laporan/SOP .docx rapi berbahasa Indonesia natural."
version: 1.0.0
platforms: [linux]
---

# Laporan & Dokumen DOCX Bahasa Indonesia (gaya user)

Membuat dokumen .docx (laporan analisis, SOP, rangkuman) dengan python-docx,
berbahasa Indonesia natural/manusiawi, dan sesuai preferensi gaya user
(Ibramsyah / BelajarLagi). Berlaku untuk: laporan CSAT/testimoni, SOP dari
dokumen sumber, rangkuman materi, laporan evaluasi program.

## Trigger

- User minta laporan analisis (testimoni, evaluasi, riset) dalam bentuk .docx
- User minta SOP dirapikan/dielaborasi menjadi dokumen
- User minta dokumen yang "mudah dipahami", "tidak AI banget", "rapi"

## Aturan Gaya (koreksi user - WAJIB)

- **Bahasa natural/manusiawi, JANGAN kedengaran AI**: hindari frasa template
  ("keseluruhan sentimen sangat positif", "aspek paling diapresiasi peserta",
  "indikator menunjukkan"). Tulis seperti orang yang membaca sendiri datanya:
  "Singkatnya: dua-duanya disambut baik. Separuh peserta bahkan bilang tidak
  ada kendala sama sekali."
- **Judul section manusiawi**: "APA YANG PALING DISUKAI" (bukan "Analisis
  Apresiasi"), "KENDALA YANG DISAMPAIKAN", "KESIMPULAN SINGKAT" (bukan
  "Key Insight"). Kolom tabel: "Jumlah/Persen" (bukan "Frekuensi/Persentase").
- **TANPA tanda petik** di kutipan testimoni (cukup italic).
- **Tabel**: style 'Light Grid Accent 1', header bold, isi 9.5-10pt.
- **Simpan ke**: /mnt/user-data/outputs/ dengan nama deskriptif.

## Pola Dokumen

- Cover: judul besar center + subjudul + info dokumen (no dokumen, PIC, tanggal
  jika tersedia).
- Gunakan fungsi helper: judul/subjudul/paragraf/bullet/tabel dengan warna
  brand (RGB 0x1F4E5F teal, 0x0E7C66 hijau accent, 0xB45F06 amber warning).
- Margin 2-2.5cm, font Calibri 10.5-11pt.
- Verifikasi isi setelah generate: baca ulang via python-docx, cek jumlah
  tabel/paragraf dan kesamaan teks (testimoni harus identik dengan sumber).

## Pitfall

- Jangan mengubah teks kutipan/testimoni - salin persis dari sumber, verifikasi
  kesamaan 1:1 dengan script pembanding.
- Jangan menulis ulang SOP dari nol saat user minta "rapikan" - pertahankan
  struktur TUJUAN/LINGKUP/DEFINISI/DOKUMEN/PROSEDUR yang sudah ada, rapikan
  kerapiannya saja.
- Saat user minta "elaborasi": terjemahkan ke bahasa sederhana + tabel +
  penjelasan "kenapa" tiap langkah, tanpa menambah/mengubah isi sumber.
- Data dengan beberapa kelompok (Kelas 9 & 10): pisahkan analisis per kelompok
  + tabel ringkasan gabungan di awal.
- Jika sumber punya kolom ID (ID Student) dan skor (Material/Instructor
  Score): tampilkan ID di tabel testimoni, hitung rata-rata + distribusi skor.
