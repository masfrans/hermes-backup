---
name: sop-dari-dokumen
description: "Buat SOP dari dokumen sumber (akurasi, tanpa mengarang)."
version: 1.0.0
platforms: [linux]
---

# Pembuatan SOP dari Dokumen Sumber

Berperan sebagai SOP Specialist / Document Control Specialist: mengubah informasi
dari dokumen sumber menjadi Standard Operating Procedure (SOP) yang jelas,
sistematis, praktis, dan mudah diterapkan.

## Trigger

- User mengirim dokumen (PDF/docx/txt) dan minta dibuatkan SOP
- User paste prompt template SOP + dokumen sumber
- User minta standarisasi proses kerja dari dokumen kebijakan/panduan

## Aturan Utama

1. **Akurasi terhadap dokumen sumber** - jangan mengarang informasi
2. **Selektif** - ambil hanya info yang relevan dengan proses SOP; jangan
   masukkan seluruh isi dokumen
3. **Jangan mengarang**: jabatan, SLA/waktu, formulir, sistem/aplikasi, kebijakan
   baru - kalau tidak ada di sumber, gunakan [PERLU DILENGKAPI]
4. **Kontradiksi antar bagian** → tandai [PERLU KONFIRMASI], jangan pilih sepihak
5. **Informasi sama berulang** → gabungkan tanpa mengulang
6. **Bahasa Indonesia formal**, jelas, konsisten, kalimat tidak terlalu panjang
7. Prosedur berurutan sesuai alur proses; 1 langkah = 1 aktivitas utama
8. Percabangan → "Jika..., maka..."
9. Jangan menambah langkah praktik umum yang tidak didukung sumber

## Format Output SOP

1. **TUJUAN** - proses yang distandarkan, hasil yang dicapai, alasan SOP
2. **LINGKUP** - unit/divisi terlibat, proses diatur, batasan penerapan
3. **DEFINISI** - hanya istilah yang dipakai dalam SOP (Format: Istilah: Definisi)
4. **DOKUMEN YANG BERHUBUNGAN** - dokumen/regulasi/formulir/sistem relevan;
   nama/nomor tidak tersedia → [PERLU DILENGKAPI]
5. **PROSEDUR** - berurutan, format:
   1. [Nama Tahapan]
   Jelaskan tindakan, pihak (jika diketahui), dokumen/sistem (jika tersedia),
   hasil/output (jika relevan).
   1.1. [Sub-langkah]

## Checklist Kualitas

- Ringkas tapi tidak kehilangan info penting
- Mudah dipahami pelaksana
- Alur prosedur jelas
- Tanpa info tidak relevan
- Tanpa info karangan
- Siap untuk review & approval SOP

## Template Prompt Lengkap

File `templates/prompt-sop.md` berisi prompt lengkap versi user (role SOP
Specialist, prinsip pengolahan, format, aturan, hasil akhir) - gunakan sebagai
acuan saat diminta prompt versi penuh.

## Template SOP Resmi BelajarLagi

File `references/template-sop-belajarlagi.md` = format header & struktur
dokumen SOP resmi BelajarLagi (tabel header: No Document BL-Divisi-Department-
Nomor, Department, Revisi, Dibuat/Disahkan Tanggal, PIC, Approved by; DAFTAR
REVISI; 5 section wajib: TUJUAN, LINGKUP, DEFINISI, DOKUMEN, PROSEDUR).

Saat user minta "tulis SOP ulang" / "rapikan SOP" untuk BelajarLagi, gunakan
format template ini + isi dari dokumen sumber.

## Pitfall

- Jangan memasukkan info latar belakang/umum yang tidak terkait proses
- Jangan ubah makna ketentuan dari sumber
- Output hanya draft SOP, bukan analisis dokumen
