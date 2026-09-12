---
name: ats-resume-optimization
description: "Optimasi CV lolos ATS: parsing, keyword, ranking, format."
version: 1.0.0
platforms: [linux]
---

# ATS Resume Optimization

Pengetahuan cara kerja sistem penilaian ATS (Applicant Tracking System) dan cara mengoptimalkan CV agar lolos saringan otomatis sebelum dilihat recruiter. Dipakai saat user bertanya soal ATS, cara lolos screening CV, atau ingin membuat fitur "ATS score check" / CV builder.

## Apa Itu ATS
ATS = database + resume parser. Bukan "robot penolak" tunggal - tiap vendor beda (Workday, Greenhouse, Lever, iCIMS, Taleo, BambooHR, SuccessFactors, Eightfold, Phenom). Alur scoring 3 fase:

### Fase 1: Parsing (ekstraksi data) - "silent killer"
- ATS ubah CV jadi data terstruktur: nama, kontak, jabatan terakhir, pengalaman, pendidikan, skills
- **Parsing itu BINER**: field keisi atau kosong, tidak ada nilai parsial
- Field kosong = tidak muncul saat recruiter filter (misal filter "5+ tahun pengalaman")
- Layout kompleks (multi-kolom, tabel, text box, grafik, header/footer) = parsing kacau
- Tanggal format non-standar, skills terkubur di paragraf = field kosong

### Fase 2: Keyword Matching (bobot & penempatan)
- BUKAN persentase sederhana - ini **weighted requirement check**:
  - Recruiter definisikan: required + nice-to-have + must-not-have keywords
  - Tiap keyword punya bobot (Python 5x utk engineer, JIRA 1x)
  - ATS scan keyword + variasinya (Python/python3/Py3)
- **Penempatan > frekuensi**: keyword di job title skor tertinggi; lalu summary/skills/role terbaru; terendah di bullet lama
- **Semantic matching** (Workday, Eightfold, Phenom): "stakeholder management" ≈ "client relations" ≈ "cross-functional collaboration"
- Sering kelewat: akronim tanpa kepanjangan (FP&A), sinonim industri (M&A), versi tool (MS Excel vs Excel)

### Fase 3: Ranking (kompetisi antar kandidat)
- Skor relatif 0-100, cuma top X dilihat manusia:
  - High-volume (1000+ pelamar): top 5-10% (50-100 CV)
  - Niche/senior (50 pelamar): top 25-50%
  - Remote job: 5-10x pelamar → bar lebih tinggi
- Faktor: keyword match, kelengkapan parsing, pengalaman, pendidikan, lokasi, ekspektasi gaji, sinyal kualitas dari hires lalu

## 6 Alasan CV Ditolak ATS
1. **Layout kompleks** (multi-kolom, tabel, text box) → wajib single-column
2. **Keyword tidak mirror** job description ("managing projects" vs "project management")
3. **Keyword di section salah** → taruh di summary, skills, role terbaru
4. **Judul jabatan non-standar** → tambah ekuivalen: "Revenue Growth Specialist (Sales Manager)"
5. **Format file salah** → .docx paling aman; PDF dari design tool bisa error parsing
6. **Tidak ada angka** → ATS modern skor "achievement density" (berapa bullet pakai angka/%)

## Praktik Terbaik untuk CV ATS-Friendly
- Single-column, tanpa tabel/kolom/text box (bisa dipakai utk tampilan, tapi teks harus linear)
- Mirror bahasa persis dari job description (bukan stuffing berlebihan)
- Judul jabatan standar + ekuivalen dalam kurung
- Bullet kuantitatif: "Managed team of 8, cut delivery time 22%" bukan "Managed a team"
- Simpan .docx (paling aman) atau PDF dari tool khusus resume
- Taruh keyword terpenting di summary + skills + 2 role terbaru
- Eja akronim sekali: "Financial Planning & Analysis (FP&A)"

## Peringatan
- **"Match score 0-100" dari tool pihak ketiga MENYESATKAN** - ATS asli tidak produksi angka itu; skoring internal tiap vendor beda & tidak transparan
- Jangan klaim ke klien bahwa CV "100% lolos ATS" - tidak ada jaminan, tiap ATS beda parsing logic
- CV yang bagus untuk manusia TIDAK otomatis bagus untuk ATS - dua target berbeda

## Kaitannya dengan Layanan CV
- Skill `pembagus-cv-resume` (user-owned) sudah menerapkan: single-column, .docx, action verbs, tanpa em dash - itu sudah benar
- Yang bisa ditambah ke layanan: keyword mirroring dari job description + achievement density (banyak angka)
- Fitur "ATS score check" yang mungkin dibangun: skor berdasarkan parsing-friendliness (format linear, section jelas, tanggal konsisten, angka di bullet) - bukan klaim match % dengan ATS asli

## Sumber Riset (Agustus 2026)
- quickcv.io/blog/how-ats-systems-work-2026
- atsverification.com/blog/how-ats-scoring-works/
- resumeplusai.com, gettailor.ai/resources/ats-guide
- Kompetitor lokal: cvbuilder.id (CV Kinobi) - ATS builder + job portal + courses
