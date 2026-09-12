# Alur Kerja: Laporan DOCX dari File Sumber (BelajarLagi)

## Pola umum (terbukti di sesi testimoni & SOP)

1. **Baca sumber**:
   - .xlsx → openpyxl (read_only=True), iter_rows(values_only=True)
   - .docx → python-docx, paragraphs + tables
   - .txt → read_file
2. **Ekstrak ke /tmp/*.json** dengan script Python terpisah, lalu proses.
   Struktur data testimoni kelas (pola file evaluasi BelajarLagi):
   - Baris 0 = nama kelas ("Kelas 9", "Kelas 10") di header kolom
   - Baris 1 = pertanyaan (apresiasi, kendala) + kolom skor
   - Baris 2+ = data: [ID Student, apresiasi, kendala, Material Score, Instructor Score]
   - Kelas 9 di kolom kiri, Kelas 10 di kolom kanan (blok 5 kolom masing-masing)
3. **Hitung agregat**:
   - Material/Instructor Score: rata-rata, % skor ≥4.5, distribusi per skor
   - Tema apresiasi: hitung kata kunci (daging/padat, jelas/mudah, hands-on,
     detail/teknis, insight/best practice, instruktur/kak yudis, seru, aplikatif)
   - Kritik: filter baris kendala yang bukan "tidak ada" — STRIP awalan "tidak
     ada/gak ada/no" lalu cek sisa kalimat untuk kata kritik (jangan buang
     entri "tidak ada, tapi waktunya singkat")
4. **Generate .docx**: /usr/local/lib/hermes-agent/venv/bin/python3
   - Tabel style 'Light Grid Accent 1'
   - Kutipan testimoni TANPA tanda petik, italic, indent 0.5cm
   - Simpan ke /mnt/user-data/outputs/
5. **Verifikasi**: baca ulang docx via python-docx; bandingkan teks testimoni
   laporan vs sumber 1:1 (harus identik). Cek jumlah tabel & paragraf.

## Konvensi warna brand (BelajarLagi)

- Teal 0x1F4E5F (judul), Hijau 0x0E7C66 (sub-accent), Amber 0xB45F06
  (warning/kritik), Abu 0x555555 (keterangan/italic)

## Preferensi yang dikoreksi user (jangan diulang)

- "jadikan hasil analisisnya tidak AI banget" → bahasa manusiawi, hindari
  frasa template
- "jangan di kasih tanda petik" → kutipan testimoni tanpa tanda petik
- "tuliskan ID pesertanya (jadikan tabel)" → kolom ID Peserta | Testimoni
- "hasilnya dipisah antara kelas 9 dan 10" → analisis + testimoni terpisah
  per kelas, ringkasan gabungan di awal
- "coba hitung material dan instructor scorenya juga" → selalu cek kolom skor
  di sumber, hitung rata-rata + distribusi
