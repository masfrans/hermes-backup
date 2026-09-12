---
name: belajarlagi-class-ops
description: "Kelas/bootcamp Belajarlagi: KUDA, review slide, polling WA."
version: 1.0.0
platforms: [linux]
---

# Operasional Kelas/Bootcamp Belajarlagi

Gunakan saat user (Ibramsyah Gani) mengelola kelas/bootcamp Belajarlagi
(free class, webinar, mini bootcamp): menyusun/review slide, kuis Kahoot &
KUDA (Kuis Dadakan), polling & icebreaker grup WhatsApp, kode voucher/diskon,
CSAT, checklist dokumentasi acara, deskripsi program, ucapan terima kasih tim.

## KUDA (Kuis Dadakan) - Elemen WAJIB Slide

- Setiap deck materi kelas Belajarlagi WAJIB punya slide KUDA (kuis dadakan).
  Saat review slide vs silabus, cek dulu: grep "kuda|kuis|quiz" di teks slide.
  Kalau kosong = koreksi.
- Format: MCQ 4 opsi ala Kahoot, tulis kunci jawaban (tandai ✅ saat disajikan
  ke user), soal berbasis "koreksi"/angka yang sering disalahpahami materi.
- Posisi: selipkan di sela-sela sesi (setelah bab inti, sebelum QnA).

## Review Slide vs Silabus (checklist)

1. Semua poin silabus ter-cover, termasuk item "Review Materi" (bukan hanya
   materi inti) - agenda slide harus memuat semua poin silabus.
2. KUDA ada (lihat atas).
3. Hands-on/demo ada: latihan cepat, case study, workshop kasus, demo tools.
4. Placeholder dibersihkan: "*silahkan dihapus jika materi sudah final*",
   "Insert Instructor Photo".
5. Nama instruktur konsisten (contoh nyata: "Mediawan" vs "Meidiawan" - cek
   judul vs halaman profil).
6. Judul/layout tidak aneh (kolom terbalik, teks terpotong).
- Saat membandingkan, ekstrak PDF slide dulu (skill `pdf`, pdf_read.py --text),
  lalu bandingkan per poin; beri tabel sudah/belum + rekomendasi prioritas.

## Grup WhatsApp - Polling & Icebreaker

- **Format polling WA**: 1 pertanyaan + 2-12 opsi PENDEK; centang multi-select
  kalau jawabannya bisa lebih dari satu. Kirim pagi, tutup sore, reveal hasil +
  teaser kelas ("penasaran? dibahas di kelas 😉").
- **Pembuka grup**: sapaan hangat + icebreaker GAMPANG dulu (pilih emoji,
  cerita pengalaman, tebak-tebakan), admin jawab duluan sebagai contoh.
- **"Tipis-tipis materi tapi gampang"** = formula terbaik meramaikan grup:
  relate ke keseharian, ada jawaban tebak-tebakan, tapi nyambung ke topik kelas
  (contoh pajak: "Lebih takut mana: ditelepon KPP atau bank?").
- **Soal misconception terbaik untuk buka grup**: mayoritas jawab salah lalu
  kaget (PPN 12% vs efektif 11%; SP2DK 60 vs 14 hari) - memicu penasaran.
  Hindari soal hafalan angka teknis sebagai pembuka.
- Rangkaian: H-1 (kenalan/icebreaker) → hari H (polling materi, reveal) →
  H+1 (evaluasi, konten follow-up).

## Kode Voucher / Diskon

- Huruf kapital, 8-12 karakter, hindari O/0, I/1/l. Prefix kampanye + nilai
  diskon (CLAUDE15). Kode publik (satu untuk semua hadir) vs kode unik per
  peserta (anti-sharing). Set expiry. Lihat juga skill natural-indonesian-writing.
- Pemenang Kahoot: gelar 2 kata (CLAUDEMASTER, PROMPTCHAMP, KAHOOTKING).

## CSAT (Customer Satisfaction Score)

- Rumus: (responden puas / total responden) x 100%. Skala 1-5: puas = 4 & 5;
  skala 1-10: puas = 9 & 10. Jangan hitung yang tidak menjawab.
- Benchmark: >=80% bagus; 70-80% cukup; <70% perlu evaluasi.
- Sampel kecil (<30) = angka kurang representatif, katakan jujur.
- Data mentah hasil survei: hitung dengan script (Counter), jangan manual;
  tawarkan chart PNG (matplotlib) via MEDIA.

## Dokumentasi Acara (checklist)

Kategori foto/video yang wajib diambil:
1. Seremonial pembukaan (pejabat/narasumber resmi)
2. Foto bersama (pejabat + instructor + peserta)
3. Sesi mengajar (slide perkenalan, interaksi, hands-on, engagement)
4. Testimoni peserta (minta izin, catat nama)
5. Dokumentasi umum - UTAMAKAN potrait (>60-70%) untuk stock design publikasi
   tim marketing; landscape untuk dokumentasi/video.

## Deskripsi Program (format konsisten)

Contoh pola dari PRD (2 kalimat): "[Nama Program (SINGKATAN)] dirancang untuk
membantu [audiens] dalam [tujuan utama]. Program ini berlangsung selama [X]
sesi interaktif ([Y]x Live Class + [Z]x Asistensi) yang dilaksanakan secara
daring via Zoom selama [N] minggu."
- Buat versi INKLUSIF bila diminta: "para digital marketer dari berbagai latar
  belakang, baik yang baru mulai maupun yang sudah berpengalaman" - tapi tetap
  sisipkan catatan prasyarat lembut (mis. "disarankan sudah familiar dengan
  Ads Manager") kalau PRD menargetkan non-pemula.
- Jangan menulis jam kalau PRD masih placeholder (Pukul [HH.MM]).
- Ucapan terima kasih tim / pesan broadcast: lihat skill natural-indonesian-writing
  (natural, jangan kedengaran AI, plain text tanpa markdown untuk copas).

## Pitfalls

- Saat user minta "rekap jadi 1" / "jangan rubah isi slide": kirim PERSIS dari
  sumber, jangan tambah versi/reword kecuali diminta.
- Review slide yang sama di beberapa sesi: koreksi yang sama (KUDA, placeholder,
  nama instruktur) sering berulang - cek semuanya sekaligus.
- Jangan mengarang data kandidat/kode/angka untuk kepentingan resmi - verifikasi
  dari sumber (spreadsheet, PRD, slide).
