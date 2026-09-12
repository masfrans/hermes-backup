---
name: pembagus-cv-resume
description: "Reformat CV mentah ke standar Harvard/ATS dalam .docx."
version: 1.0.0
platforms: [linux]
---

# SKILL: Reformat CV ke Standar Harvard/ATS

Skill ini digunakan ketika menerima data CV mentah (gambar, PDF, atau file Word) dari klien dan perlu mengubahnya menjadi CV yang rapi, terstruktur, dan sesuai standar Harvard/ATS dalam format `.docx`. Trigger: permintaan "reformat CV", "buat CV ATS", "perbaiki CV", atau upload file CV mentah.

---

## 1. Prinsip Utama (Non-Negotiable)

- **Kesetiaan pada sumber (source fidelity)**: Semua informasi dalam CV hasil akhir HARUS berasal dari data sumber. Tidak boleh mengarang fakta.
- **Transparansi atas inferensi**: Jika ada penambahan atau inferensi (misalnya menyimpulkan tanggung jawab dari judul jabatan), ini WAJIB ditandai secara eksplisit dan dipisahkan dari konten asli.
- **Placeholder untuk angka**: Pencapaian kuantitatif yang tidak disebutkan secara eksplisit oleh klien di sumber data TIDAK BOLEH diisi dengan angka karangan. Gunakan placeholder `[____]` agar klien mengisi sendiri.
- **Jika ditanya soal asal-usul konten**: berikan breakdown terstruktur dengan 3 kategori:
  1. Langsung dari sumber
  2. Inferensi kontekstual (jelaskan dasar inferensinya)
  3. Ditandai untuk verifikasi klien

---

## 2. Struktur CV (Urutan Harvard Format)

1. **Header** - Nama, kontak (telepon, email, kota/negara; tanpa foto)
2. **Summary** (opsional, ringkas 2-3 baris)
3. **Education** - gelar, institusi, lokasi, tanggal (reverse chronological), IPK, coursework relevan, skripsi/thesis jika ada
4. **Work Experience** - reverse chronological, minimum 3 bullet point per entri
5. **Organizations / Leadership** - pengalaman organisasi, kepemimpinan
6. **Certifications** - misal BNSP, sertifikasi profesi lain
7. **Skills** - kelompokkan (teknis, bahasa, dsb.)

Kategori opsional tambahan (jika relevan dengan bidang klien): Public Service Experience, Technical Skills, Research Experience, Performing Arts Experience, Activities - lihat referensi Harvard MCS.

---

## 3. Aturan Formatting

- **Tidak boleh menggunakan em dash (—)**
- **Perataan paragraf**: justified
- Tidak ada foto, tidak ada informasi referensi, tidak ada usia/gender
- Tidak menggunakan kata ganti orang pertama (I, We, Saya)
- Tidak menyingkat kata secara sembarangan
- Tidak menggunakan gaya naratif atau bahasa gaul
- Setiap baris JANGAN dimulai dengan tanggal (tanggal diletakkan rata kanan)
- Tahun/tanggal diposisikan rata kanan menggunakan tab stop (contoh implementasi: posisi tab 10800 pada docx via library Node.js `docx`)
- Konsisten dalam penggunaan bold, italic, spacing, kapitalisasi untuk penekanan
- Tidak ada celah informasi (misalnya musim panas yang hilang dari timeline) - jika ada gap, tandai untuk klarifikasi klien, jangan ditutupi dengan mengarang
- Skema warna disesuaikan dengan bidang klien (lihat bagian 6)
- Tidak boleh menyimpang dari template yang sudah ditentukan

## 3.1 Bahasa Resume (Prinsip Harvard)

- Spesifik, bukan umum
- Aktif, bukan pasif
- Ditulis untuk "express", bukan "impress" (menyatakan fakta, bukan mengesankan pembaca)
- Berbasis fakta - kuantifikasi dan kualifikasi pencapaian
- Ditulis agar mudah dipindai cepat oleh manusia maupun sistem ATS

### 5 Kesalahan CV Paling Umum (untuk dicek/dihindari)
1. Kesalahan ejaan dan tata bahasa
2. Informasi email/telepon yang hilang
3. Bahasa pasif alih-alih kata kerja aktif
4. Tidak terorganisir, tidak ringkas, sulit dipindai
5. Tidak menunjukkan hasil/dampak (results)

---

## 4. Action Verbs (Kata Kerja Aktif)

Gunakan kata kerja aktif sesuai kategori tugas/pencapaian klien. Kategori utama:

- **Leadership**: Accomplished, Achieved, Administered, Directed, Led, Orchestrated, Oversaw, Spearheaded, Supervised, dll.
- **Communication**: Addressed, Authored, Collaborated, Drafted, Negotiated, Persuaded, Presented, Wrote, dll.
- **Research**: Analyzed, Conducted, Evaluated, Investigated, Interviewed, Surveyed, dll.
- **Technical**: Assembled, Built, Designed, Engineered, Programmed, Streamlined, Upgraded, dll.
- **Teaching**: Advised, Coached, Facilitated, Guided, Instructed, Trained, dll.
- **Quantitative**: Allocated, Audited, Balanced, Budgeted, Forecasted, Projected, dll.
- **Creative**: Conceived, Created, Designed, Established, Founded, Initiated, dll.
- **Helping**: Assessed, Counseled, Educated, Facilitated, Mentored, Supported, dll.
- **Organizational**: Arranged, Cataloged, Compiled, Implemented, Monitored, Streamlined, dll.

Referensi lengkap: `ActionVerbsList_1.pdf` pada project ini.

### Aturan penerapan
- Setiap bullet point dimulai dengan satu kata kerja aktif berbeda (hindari pengulangan kata kerja yang sama dalam satu entri)
- Kalimat majemuk yang berisi beberapa tindakan berbeda dipecah menjadi bullet point terpisah, masing-masing dengan kata kerja aktifnya sendiri
- Minimum 3 bullet point per entri pengalaman kerja
- Bullet dikelompokkan berdasarkan sub-kategori jika relevan (misal: "Analisis Data", "Manajemen Tim")

---

## 5. Penggunaan AI dalam CV (menurut panduan Harvard)

AI generatif sebaiknya digunakan sebagai alat bantu editing, bukan penulis utama:
- Brainstorming revisi bullet point
- Memasukkan kata kunci dari deskripsi pekerjaan (untuk lolos ATS)
- Memperbaiki apa yang sudah ada

AI TIDAK boleh menjadi penulis utama karena hasilnya cenderung generik. Prinsip ini konsisten dengan aturan source fidelity di atas - AI membantu merapikan, bukan mengarang isi baru.

---

## 6. Skema Warna per Bidang (Field Color Palette)

Setiap bidang klien memiliki skema warna berbeda pada CV hasil akhir:
- `agrikultur`
- `psikologi_hr`
- `logistik`
- `hse_esg`
- `default`

(Detail kode warna spesifik per kategori mengikuti konfigurasi `config.yaml` pada aplikasi web otomasi - lihat bagian 8.)

---

## 7. Alur Kerja Manual (Proses Konsultasi CV)

1. Terima data CV mentah dari klien (gambar/PDF/Word)
2. **Verifikasi format file sebenarnya** sebelum diproses:
   - File dengan ekstensi `.pdf` di penyimpanan proyek terkadang sebenarnya adalah arsip ZIP `.docx`
   - Gunakan command `file` dan inspeksi hex untuk memverifikasi tipe file asli - tool PDF standar akan gagal secara diam-diam (silent fail) pada kasus ini
3. **Ekstrak konten**:
   - **File digital (.docx/.txt)**: ekstrak langsung dengan tool baca file
   - **Scan/foto/PDF gambar**: pakai script OCR CV teroptimasi:
     ```bash
     python3 /root/.hermes/scripts/ocr_cv_to_data.py <file_scan> --json
     ```
     Script ini otomatis: OCR bahasa ind+eng, upscale 3x, deteksi section (kontak, summary, pendidikan, pengalaman, organisasi, skills), ekstrak tanggal, lalu output JSON terstruktur. Catatan: hasil OCR bisa salah baca karakter (O/0, l/1, Z/7, g/q) - verifikasi manual jika ragu.
4. Ekstrak & susun ulang konten sesuai struktur Harvard (bagian 2)
5. Terapkan action verbs dan aturan bahasa aktif (bagian 3.1 & 4)
6. Tandai semua inferensi/tambahan secara eksplisit; beri placeholder `[____]` untuk angka yang tidak disebutkan sumber
7. Hasilkan file `.docx` menggunakan library `docx` (Node.js), dengan tab stop rata kanan untuk tahun (posisi 10800)
8. Konversi ke PDF via LibreOffice (`soffice.py`) untuk verifikasi visual
9. Render halaman PDF dengan `pdftoppm` untuk pengecekan visual akhir
10. Simpan output di `/mnt/user-data/outputs/`, sampaikan ke klien via `present_files`

---

## 8. Rencana Otomasi (Web App)

Spesifikasi aplikasi otomasi yang sedang dikembangkan:
- **Input**: Upload-only (JPG/PNG/PDF)
- **AI Processing**: Google Gemini (free tier via Google AI Studio) - mendukung vision & PDF secara native
- **Output**: Download-only `.docx` (tanpa pengiriman email)
- **Konfigurasi**: `config.yaml` yang dapat diatur admin (termasuk skema warna per bidang)
- **Privasi**: Tampilkan notice bahwa file mentah akan dihapus otomatis setelah diproses (karena Gemini free tier berpotensi menggunakan input untuk training)
- **Repo GitHub**: `.env` dan folder upload harus masuk `.gitignore`

### Catatan implementasi
- Jika dijalankan di lingkungan remote (misal Claude Code di server remote), `http://localhost:8000` tidak akan bisa diakses langsung dari browser lokal - perlu port forwarding/tunnel atau konfigurasi host yang sesuai.

---

## 9. Istilah Domain yang Sering Muncul

Harvard resume standard, ATS, PROPER KLHK, SIMPEL/SPEED/SPARING, SROI, BNSP certification, IPK (GPA), PKL (internship).

---

## 10. Checklist Sebelum Mengirim CV Final ke Klien

- [ ] Semua bullet point pakai kata kerja aktif berbeda, tidak ada pengulangan berlebihan
- [ ] Minimum 3 bullet per entri pengalaman
- [ ] Tidak ada kata ganti orang pertama
- [ ] Tidak ada foto/usia/gender/referensi
- [ ] Urutan reverse chronological di tiap kategori
- [ ] Semua tanggal rata kanan, tidak ada baris dimulai dengan tanggal
- [ ] Placeholder `[____]` terpasang untuk semua angka yang tidak eksplisit dari sumber
- [ ] Semua inferensi ditandai dan dapat dijelaskan jika ditanya
- [ ] Tidak ada em dash
- [ ] Paragraf justified
- [ ] Skema warna sesuai bidang klien
- [ ] File akhir dalam format `.docx`, sudah diverifikasi visual via PDF render
