---
name: sop-writer-reviewer
description: "Kembangkan draft SOP singkat jadi lengkap & operasional."
version: 1.0.0
platforms: [linux]
---

# SOP Writer/Reviewer

Mengubah data atau draft SOP yang singkat (poin-poin, wording belum lengkap)
menjadi draft SOP yang lebih lengkap, jelas, terstruktur, dan operasional,
TANPA mengubah konteks maupun maksud proses sebenarnya.

## Prinsip Utama

"Kembangkan dan perjelas proses, bukan menciptakan proses baru."
Bukan sekadar copy-editing/tata bahasa - kembangkan isi draft menjadi SOP yang
informatif dan bisa dijalankan.

## Trigger

- User memberi draft SOP singkat/poin-poin dan minta dikembangkan jadi SOP lengkap
- Draft terlalu umum, butuh uraian operasional
- User minta "perjelas" / "kembangkan" / "lengkapi" SOP

## Ketentuan Penyusunan

1. **Kembangkan draft singkat** - jelaskan proporsional: apa aktivitas, siapa/PIC,
   bagaimana (sesuai info tersedia), apa yang perlu dipastikan/dihasilkan, kapan/
   tahap apa (jika tersedia). Jangan terlalu singkat jika konteks memungkinkan
   dijelaskan lebih lengkap; jangan juga bertele-tele hanya menambah kata.
2. **Jangan keluar konteks** - pertahankan maksud, alur, role/PIC, sistem, dokumen,
   aktivitas. Jangan tambah aktivitas/approval/dokumen/sistem/deadline/pihak yang
   tidak disebutkan dan tidak bisa disimpulkan wajar.
3. **Bedakan "memperjelas" vs "menambahkan proses"**:
   - BOLEH: "PM melakukan monitoring project tracker" → "Project Manager melakukan
     pemantauan berkala terhadap project tracker untuk memastikan seluruh task pada
     setiap tahapan program telah diperbarui dan diselesaikan oleh PIC terkait
     sesuai timeline yang ditentukan."
   - TIDAK BOLEH: menambah reminder H-3 via WhatsApp / escalation ke Manager jika
     tidak ada di sumber.
4. **Alur SOP logis** - persiapan → pembuatan/penyusunan → koordinasi → pelaksanaan
   → pengecekan/validasi → monitoring → follow-up → penyelesaian/dokumentasi
   (hanya jika relevan).
5. **Pertahankan & kembangkan numbering** - jika draft pakai 2.1/2.2/2.3, pertahankan.
   Pecah poin padat menjadi sub-poin.
6. **Bahasa SOP profesional** - formal, jelas, objektif, konsisten, tidak ambigu,
   tidak conversational. Hindari: "dan lain sebagainya", "sesuai kebutuhan" tanpa
   penjelasan, "sebagaimana mestinya", "melakukan hal-hal yang diperlukan".
7. **Jangan mengarang** - jika info tidak tersedia, jangan buat asumsi. Bagian
   penting yang kurang jelas → konfirmasi dulu.
8. **Gunakan judgment sebelum konfirmasi**:
   - Konteks cukup jelas → langsung kembangkan
   - Kurang tapi tidak memengaruhi substansi → wording aman & umum
   - Kurang dan bisa mengubah alur/PIC/tanggung jawab/output → KONFIRMASI dulu

## Format Output

Jika informasi cukup:
- **A. Draft SOP yang disempurnakan** (format rapi, lebih lengkap dari draft awal)
- **B. Catatan pengembangan** (bagian mana yang dikembangkan/diperjelas)

Jika ada yang perlu konfirmasi:
- **A. Pertanyaan Konfirmasi** (spesifik, seminimal mungkin)
- **B. Draft sementara** (bagian yang sudah bisa disusun tanpa info yang belum ada)

## Standar Hasil Akhir

- Lebih lengkap dari draft awal
- Bukan sekadar ganti kata/perbaiki grammar
- Aktivitas dijelaskan operasional
- Mudah dipahami pelaksana
- Alur logis, ringkas, tidak bertele-tele
- Tidak menambahkan proses tanpa dasar
- Mempertahankan maksud asli draft
- Tujuan akhir: draft "terlalu singkat" → "cukup detail untuk dijalankan"

## Perbedaan dengan skill SOP lain

- `sop-dari-dokumen`: PEMBUATAN SOP baru dari dokumen sumber lengkap
- `sop-development-assistant`: AUDIT & perbaiki SOP (6 tahap, format temuan A-F)
- `sop-writer-reviewer` (ini): KEMBANGKAN draft singkat jadi SOP operasional lengkap

## Template

File `templates/prompt-writer-reviewer.md` - prompt lengkap versi user.
