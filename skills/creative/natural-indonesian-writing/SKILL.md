---
name: natural-indonesian-writing
description: "Write natural Indonesian copy/messages for this user."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [writing, indonesian, copywriting, whatsapp, style]
---

# Natural Indonesian Writing (untuk user ini)

Gunakan saat user (Ibramsyah Gani) minta dibuatkan teks berbahasa Indonesia:
ucapan terima kasih, deskripsi acara/program, promosi, caption, rekap dokumen,
kode voucher, konten marketing. Pelajaran gaya ini berasal dari koreksi eksplisit
user: "terlalu AI", "jangan rubah apa yg ada di slide", "tanpa fitur biar bisa di copas".

## Aturan Gaya (WAJIB)

1. **Natural & santai, JANGAN kedengaran AI.**
   User pernah menilai draft pertama "terlalu AI". Tulis seperti orang beneran
   ngetik WhatsApp: kalimat mengalir, nada hangat-personal, tidak kaku, tidak
   berlapis-lapis sempurna. Hindari struktur yang terlalu rapi (bullet di
   mana-mana, paragraf simetris, penutup klise).

2. **Kalau pesan buat di-copas (chat/status broadcast): TANPA markdown.**
   Tidak ada bold/italic/list/header - plain text saja, biar tinggal salin-tempel.
   Tanya atau asumsikan copas ketika user bilang "biar bisa di copas" / "tanpa fitur".

3. **Merangkum/mengutip dari dokumen/slide: JANGAN ubah isi aslinya.**
   User: "jangan rubah apa yg ada di slide". Kalau diminta rekap dari materi,
   kutip isi persis (verbatim), jangan tambah versi/terjemahan/reword sendiri
   kecuali diminta eksplisit.

4. **Panjang boleh, tapi tetap mengalir.** "Lebih panjang dan asik" = tambah
   detail & kehangatan, bukan paragraf formal berstruktur.

5. **Bahasa Indonesia, emoji secukupnya, panggilan akrab** (kamu/kalian) kecuali
   konteks formal diminta.

## Pola yang Kedengaran AI (hindari)
- Frasa klise: "dari lubuk hati", "tentu saja", "sangat berarti bagi kami",
  "Saya sebagai asisten AI...", penutup berlebihan ("Sampai jumpa di petualangan berikutnya").
- Kalimat panjang berlapis dengan banyak anak kalimat.
- Struktur sempurna: tiap poin sama panjang, transisi mulus semua.
- Nada promosi berlebihan (superlative bertumpuk).

## Contoh Sebelum/Sesudah (dari sesi nyata)
Permintaan: ucapan terima kasih untuk tim acara (instructor, class ops, TA, faci).

- TERLALU AI: paragraf formal rapi + "dari lubuk hati: terima kasih banyak,
  teman-teman. Kalian keren, dan Gani bangga bisa satu tim sama kalian."
- NATURAL: "Gais, mau ngucapin makasih dulu buat malam ini. Serius deh, acara
  tadi bisa jalan lancar itu bukan kebetulan, itu karena kalian semua gercep dan
  solid." — terus mengalir per peran, tutup: "Makasih banget, gais. Bangga bisa
  satu tim sama kalian. Sampai ketemu di acara berikutnya! 🚀"

## Pitfall Tambahan
- Data survei/form: kalau user tempel hasil mentah (Google Form), hitung statistik
  dengan script (Counter), jangan dihitung manual - lalu tawarkan chart PNG
  (matplotlib) yang bisa dikirim via MEDIA.
- Kode voucher/kupon: huruf kapital, 8-12 karakter, hindari O/0, I/1/l; prefix
  kampanye + nilai diskon; bedakan kode publik vs unik per peserta.
- Beri 2-3 versi (lengkap/singkat/formal) lalu biarkan user pilih - user sering
  minta iterasi nada setelah draft pertama.
