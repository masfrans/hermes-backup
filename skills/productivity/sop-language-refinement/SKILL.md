---
name: sop-language-refinement
description: "Rapikan bahasa SOP jadi formal/legal tanpa ubah makna."
version: 1.0.0
platforms: [linux]
---

# Penyusunan & Penyempurnaan SOP (Bahasa)

Merapikan/perbaiki bahasa dokumen SOP menjadi formal, profesional, sistematis,
dan sesuai gaya bahasa kebijakan perusahaan + terminologi legal yang tepat,
TANPA mengubah makna, tujuan, kewenangan, tanggung jawab, persyaratan, atau
substansi.

Prinsip kunci: "Improve the language, not the meaning."

## Trigger

- User minta perbaiki bahasa SOP / buat lebih formal
- Kalimat SOP terlalu pendek/informal/ambigu/percakapan
- User kirim prompt "Penyusunan & Penyempurnaan SOP"
- User minta konsistensi istilah di SOP

## Prinsip Utama

1. Jangan ubah makna/tujuan/kewenangan/tanggung jawab/persyaratan/substansi
2. Perubahan HANYA untuk: struktur kalimat, kejelasan, tata bahasa, formalitas,
   gaya bahasa SOP, terminologi legal/korporasi, hilangkan ambiguitas,
   konsistensi istilah, perbaiki kalimat terlalu pendek
3. Jangan tambah ketentuan baru; jangan kurangi info penting
4. Kalimat terlalu pendek → kembangkan lebih lengkap/formal SELAMA tidak
   menambah makna baru
5. Istilah kurang tepat → pakai istilah legal/administratif yang lazim
6. Hindari bahasa percakapan/slang; gunakan Bahasa Indonesia baku formal,
   objektif, normatif, instruktif, tidak emosional

## Gaya Bahasa SOP

Formal, profesional, objektif, tegas tapi tidak berlebihan, tidak ambigu,
ringkas tapi cukup menjelaskan, sistematis, konsisten, dapat dilaksanakan.

Struktur prioritas: "wajib", "harus", "dapat", "berwenang", "bertanggung
jawab", "dilakukan", "dilaksanakan", "ditetapkan", "disampaikan",
"diverifikasi", "didokumentasikan", "disetujui", "ditinjau", "dicatat",
"disimpan". Jangan berlebihan menggunakannya.

## Penyesuaian Kalimat Pendek

"Manager melakukan approval." → "Manager melakukan persetujuan terhadap dokumen
yang telah disiapkan sesuai dengan ketentuan dan prosedur yang berlaku."
Hanya jika info tambahan = konsekuensi langsung makna asli, TANPA kewajiban/
persyaratan/ketentuan baru.

## Penyesuaian Bahasa Informal

- "Staff harus cek dokumen dulu." → "Staff wajib melakukan pemeriksaan terhadap dokumen terlebih dahulu."
- "Kalau dokumennya tidak lengkap, dikembalikan." → "Dalam hal dokumen yang disampaikan belum lengkap, dokumen tersebut dikembalikan kepada pihak terkait untuk dilengkapi."

## Penyesuaian Istilah Legal/Korporasi

- cek → melakukan pemeriksaan
- kasih → memberikan
- minta → meminta
- buat → menyusun
- kirim → menyampaikan
- approve → memberikan persetujuan; approval → persetujuan
- reject → menolak/penolakan
- follow up → melakukan tindak lanjut
- submit → menyampaikan/mengajukan
- review → melakukan peninjauan
- check → melakukan pemeriksaan
- confirm → melakukan konfirmasi
- PIC → Penanggung Jawab (jika konteks memungkinkan)
- meeting → rapat; deadline → batas waktu; file → dokumen; issue → permasalahan/kendala

JANGAN ganti istilah teknis, nama sistem, nama jabatan, nama dokumen, istilah
perusahaan jika mengubah identitas/makna.

## Konsistensi Terminologi

Satu istilah → satu sebutan di seluruh dokumen (contoh: Penanggung Jawab,
jangan campur PIC / Person in Charge / pihak yang bertanggung jawab).

## Struktur Kalimat

Subjek/Pelaksana → Tindakan → Objek → Ketentuan/Kondisi.
- "Dokumen kemudian dicek oleh Manager." → "Manager melakukan pemeriksaan terhadap dokumen yang telah disampaikan."
- Pasif jika konteks: "Dokumen diperiksa oleh Manager sebelum proses dilanjutkan."

## Modalitas (PENTING - jangan diubah!)

- wajib/harus = mandatory
- dapat = permitted/optional
- tidak boleh/dilarang = prohibited
- sebaiknya = recommended
Jangan ubah "dapat" → "wajib" atau "harus" → "dapat" (ubah konsekuensi
hukum/operasional).

## Kalimat Ambigu

- Perbaiki struktur kalimat agar jelas
- Jika ambiguitas dari info tidak tersedia → jangan berasumsi; pertahankan
  substansi, buat sejelas mungkin, tandai bagian yang butuh klarifikasi

## Jangan Mengarang (DILARANG)

Nama jabatan, pihak bertanggung jawab, batas waktu, persentase, nominal, nomor
dokumen, regulasi, dasar hukum, persyaratan, tahapan proses, kewenangan,
sanksi, sistem/aplikasi, dokumen pendukung, approval level, dll - jika tidak
ada di input, JANGAN dibuat sendiri.

## Konteks Legal

Bahasa presisi, tidak multitafsir, tidak subjektif, tidak emosional, tidak
absolut tanpa dasar; bedakan kewajiban/hak/kewenangan/larangan/pilihan.
"Manager boleh approve dokumen." → "Manager berwenang memberikan persetujuan
terhadap dokumen." (hanya jika sesuai makna asli)

## Format Output

Jika diminta perbaiki kalimat:
Original: [kalimat asli]
Revised: [kalimat diperbaiki]
Reason: [alasan singkat, hanya jika perlu]

Jika diminta hasil final saja → tampilkan versi perbaikan tanpa penjelasan.

## Review Dokumen SOP Lengkap

Periksa: judul, tujuan, lingkup, definisi, referensi, kebijakan, tanggung
jawab, prosedur, dokumen/formulir, rekaman, lampiran, istilah & singkatan,
konsistensi antarbagian.

## Prioritas Revisi

Makna asli → Akurasi → Kepatuhan konteks SOP → Kejelasan → Konsistensi →
Bahasa legal/formal → Keringkasan.
Jangan korbankan makna demi formalitas.

## Self-Check (sebelum hasil akhir)

1. Makna asli masih sama?
2. Ada kewajiban/kewenangan baru yang ditambahkan?
3. Ada informasi yang hilang?
4. Ubah "wajib" ↔ "dapat"?
5. Istilah konsisten?
6. Kalimat cukup lengkap & sesuai gaya SOP?
7. Ada istilah informal yang belum diperbaiki?
8. Ada potensi multitafsir?
9. Ada yang mengarang?

Jika berpotensi ubah substansi → kembali ke versi lebih dekat teks asli.

## Perbedaan dengan skill SOP lain

- `sop-dari-dokumen`: buat SOP baru dari dokumen sumber (struktur template)
- `sop-development-assistant`: audit 6 tahap + temuan + konfirmasi
- `sop-writer-reviewer`: kembangkan draft singkat jadi operasional
- `sop-language-refinement` (ini): PERAPIAN BAHASA - formal/legal/konsisten,
  tanpa ubah makna (minimal substantive change)

## Template

File `templates/prompt-language.md` - prompt lengkap versi user.
