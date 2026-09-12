# Cara Kerja & Penilaian ATS 2026 (riset dari quickcv.io, atsverification.com, resumeplusai.com)

Ringkasan riset Maret-Mei 2026 tentang mekanisme ATS sungguhan. Dipakai saat menjawab "bagaimana ATS menilai CV?" dan saat membangun/menilai simulator.

## 3 Fase Pipeline ATS (konsisten di Workday, Greenhouse, Lever, iCIMS, Taleo, BambooHR)

### Fase 1: Parsing (ekstraksi field) - "silent killer"
- ATS ubah CV (PDF/docx) jadi data terstruktur: nama, email, telepon, jabatan terakhir, total pengalaman, pendidikan, skills
- **Parsing itu BINER**: field keisi atau kosong, TIDAK ada nilai parsial
- Konsekuensi brutal: kalau field "years of experience" kosong karena parser gagal merekonstruksi riwayat kerja, kandidat TIDAK muncul saat recruiter filter "5+ tahun"
- Ini jebakan CV functional (menyembunyikan gap) - format itu justru mengosongkan field
- Layout kompleks (multi-kolom, tabel, text box, header/footer, grafik) = parsing kacau, field drop
- CV bagus secara visual bisa jadi "scrambled text" di database ATS

### Fase 2: Keyword matching (weighted requirement check)
- BUKAN persentase sederhana ("match 80%") - itu menyesatkan
- Recruiter/manager definisikan: required keywords + nice-to-have + must-not-have, tiap keyword punya BOBOT (Python 5x untuk engineer, JIRA 1x)
- ATS scan keyword + variasinya (Python / python / Python 3 / Py3)
- **Penempatan > frekuensi**: keyword di job title skor lebih tinggi dari di daftar skills; "financial modeling" 1x di title > 5x di paragraf
- **Semantic matching** (Workday, Eightfold, Phenom): "stakeholder management" ≈ "client relations" ≈ "executive communication" ≈ "cross-functional collaboration"
- Yang konsisten kelewat: akronim tanpa kepanjangan (FP&A), sinonim industri (M&A), versi tool (MS Excel vs Excel)

### Fase 3: Ranking (kompetisi antar kandidat)
- Skor relatif 0-100, cuma top X yang dilihat manusia:
  - High-volume role (1.000+ pelamar): top 5-10% (50-100 CV)
  - Niche/senior (50 pelamar): top 25-50%
  - Remote posting: 5-10x pelamar → bar jauh lebih tinggi
- Faktor: keyword match, kelengkapan parsing, pengalaman, pendidikan, lokasi, ekspektasi gaji, "candidate quality signals" dari hires sebelumnya

## ⚠️ Peringatan kredibilitas (kritikal untuk klaim ke klien)
- **TIDAK ADA ATS asli yang produksi "match score 0-100"** - angka itu artefak tool pihak ketiga (Kinobi, Novoresume, Resume Check, dll). Menyesatkan.
- Algoritma ATS = proprietary (rahasia dagang); tiap vendor beda
- Recruiter bisa ubah bobot, threshold, bahkan matikan auto-filter
- Sumber artikel = blog komersial (jual jasa resume) → bias "CV kamu pasti ditolak"
- Prinsip umum (parsing, keyword, single-column, .docx) TERVERIFIKASI lintas sumber → aman diajarkan
- Angka spesifik (persentase, top-5-10%) = perkiraan, bukan angka resmi vendor

## 6 Alasan CV Ditolak ATS
1. Layout kompleks (multi-kolom, tabel, text box) → single-column
2. Keyword tidak mirroring job description ("managing projects" vs "project management")
3. Keyword di section salah → taruh di summary, skills, role terbaru
4. Judul jabatan non-standar → tambahkan ekuivalen: "Revenue Growth Specialist (Sales Manager)"
5. Format file salah → .docx paling aman; PDF dari design tool bisa error parse
6. Tidak ada angka → ATS modern skor "achievement density" (bullet dengan %/angka)

## Relevansi untuk jasa CV
- Jual "CV ramah ATS" (format benar) = aman
- JANGAN jual "skor ATS 95" atau "dijamin lolos" = tidak bisa dibuktikan
- Yang paling menaikkan kelolosan: keyword mirroring dari job description + achievement density
