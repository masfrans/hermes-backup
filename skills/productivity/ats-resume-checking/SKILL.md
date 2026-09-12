---
name: ats-resume-checking
description: "Cek CV ramah ATS via simulator + cara kerja ATS 2026."
version: 1.0.0
platforms: [linux]
---

# ATS Resume Checking (Simulator)

Analisis apakah CV akan lolos penyaringan ATS (Applicant Tracking System), berdasarkan cara kerja parser ATS sungguhan. Komplemen skill `pembagus-cv-resume` (user-owned): skill itu MEMFORMAT CV, skill ini MENGANALISIS CV.

## Trigger
- User upload CV lalu tanya "apakah CV ini ramah ATS / akan lolos ATS?"
- User tanya bagaimana sistem penilaian ATS bekerja
- Klien minta laporan ATS-readiness sebagai nilai jual jasa CV

## Script siap pakai
`/root/.hermes/scripts/ats_checker.py` (canonical, sudah teruji):

```bash
# Cek CV + bandingkan dengan job description
python3 /root/.hermes/scripts/ats_checker.py cv.docx --jd "deskripsi lowongan..."

# Pakai file deskripsi
python3 /root/.hermes/scripts/ats_checker.py cv.pdf --jd-file loker.txt

# Output JSON (untuk integrasi/laporan)
python3 /root/.hermes/scripts/ats_checker.py cv.docx --json
```

Fitur: deteksi section (pengalaman/pendidikan/skills), cek field yang akan KOSONG di database parser ATS (email, telepon, nama, rentang tanggal, pendidikan, skills, LinkedIn), cek format (tabel/emoji/panjang), action verbs bilingual (ID+EN), achievement density (bullet berangka), keyword match vs JD. Output laporan KRITIS/SEDANG/INFO, BUKAN skor fiktif 0-100.

## Cara ATS bekerja (inti, riset 2026)
Detail lengkap: `references/ats-scoring-2026.md`

1. **Parsing** (ekstraksi field): ATS ubah CV jadi data terstruktur. Parsing itu BINER - field keisi atau kosong, tanpa nilai parsial. Layout kompleks (multi-kolom, tabel, text box, header) = parsing kacau, field kosong, kandidat tidak muncul saat recruiter filter.
2. **Keyword matching**: weighted requirement check, bukan persentase. Tiap keyword punya bobot (Python 5x, JIRA 1x). Penempatan > frekuensi: keyword di job title > di daftar skills. ATS modern (Workday, Eightfold, Phenom) pakai semantic matching (sinonim).
3. **Ranking**: skor relatif vs kandidat lain; cuma top X yang dilihat manusia (high-volume role: top 5-10%; remote: bar jauh lebih tinggi).

## Pitfalls
- **JANGAN klaim skor ATS** ("skor 95", "match 80%") - ATS asli TIDAK produksi angka itu; tool pihak ketiga (Kinobi, Novoresume, dll) menyesatkan. Jual prinsip & laporan konkret, bukan angka ajaib.
- Tiap ATS beda (Workday, Greenhouse, Lever, iCIMS, Taleo, BambooHR) - bicara prinsip umum, jangan spesifik per-vendor.
- Format aman universal: single-column, .docx, tanpa tabel/gambar/emoji, tanggal standar, action verbs, angka (achievement density).
- CV Indonesia wajib pakai action verbs bahasa Indonesia juga (script sudah bilingual).
- **Bug yang pernah terjadi**: section heading "WORK EXPERIENCE" regex match-nya menghasilkan key `"work experience"` yang TIDAK ada di mapping kondisi - hasilnya section jatuh ke "lainnya", bullets 0. Kalau bullets terdeteksi 0 padahal CV punya pengalaman, cek `detect_sections` mapping key-nya.
- 6 alasan CV ditolak ATS: layout kompleks, keyword salah, keyword di section salah, judul jabatan non-standar, format file salah, tidak ada angka.

## Verifikasi
Setelah run, cocokkan field terdeteksi dengan isi CV asli. Kalau field yang user tahu ADA tapi tampil ❌, heading section-nya belum ada di regex `detect_sections` - tambahkan.
