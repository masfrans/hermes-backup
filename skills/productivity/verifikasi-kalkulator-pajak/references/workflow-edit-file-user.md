# Workflow Edit File Kalkulator (Pelajaran dari Koreksi User)

## Aturan Emas: JANGAN ubah yang sudah ada
Kalau user mengirim BALIK file yang sudah dia perbaiki sendiri, JANGAN ubah layout/isi yang sudah ada. Hanya tambahkan fitur yang diminta.

Koreksi keras user (kutipan): "jangan rubah apa yg ada, cukup tambahkan fitur kalender, karena pada file sebelumnya km rubah layoutnya dan lain sebagainya apa yg sudah coba aku perbaiki."

## Prosedur "Hanya Tambah" yang Terbukti
1. **Selalu pakai file KIRIMAN USER sebagai base** (cache dokumen), bukan versi kerja lama di /tmp — user bisa sudah mengubah label/urutan/teks sejak versi terakhir yang kita kerjakan.
2. Salin file user ke /tmp, patch minimal: (a) tambah entry di array TABS, (b) tambah case di renderPanel switch, (c) sisipkan fungsi panel baru.
3. **Verifikasi "hanya tambah" dengan diff** (bandingkan file user vs hasil):
   - HTML di luar `<script>` harus 100% identik (bandingkan dengan regex-substitusi script → placeholder)
   - JS inti hanya boleh BERTAMBAH N baris, tidak ada baris yang diubah/dihapus (pakai difflib, filter hanya baris `+` yang baru)
4. Laporkan bukti diff ke user ("hanya 2 baris ditambahkan, nol perubahan lain") — ini membangun kepercayaan.

## Pitfall Teknis Patch
- **Saat menyisipkan fungsi di tengah file, cek deklarasi fungsi tetangga tidak ikut terhapus oleh patch** (kasus nyata: `function renderNormaTable` hilang saat sisip panel kalender — selalu grep ulang setelah patch, mis. `grep -c 'function renderNormaTable'`).
- Kalau patch mengganti blok yang berisi deklarasi fungsi, tulis ulang deklarasi itu di new_string.
- Setelah patch: ekstrak semua `<script>` → `node --check` → cek balance kurung kurawal (diff 0).

## Verifikasi Regulasi Belum Masuk Tab Referensi
Saat user tanya "apa yang belum ada di tools", cek (prioritas tinggi, langsung terkait fitur):
- UU PPh 7/1983 stdd UU 36/2008 stdd UU HPP — dasar semua perhitungan
- PMK-197/PMK.03/2013 — ambang PKP/PPN Rp4,8M
- PMK 101/2016 — dasar PTKP
- PMK 18/PMK.03/2021 — dividen 0% (relevan pemilik PT)
- UU PPN 8/1983 stdd UU HPP + PMK 131/2024 — tarif PPN 11%/12% & DPP Nilai Lain
Prioritas sedang: UU KUP (6/1983 stdd 7/2021), PP 58/2023 + PMK 168/2023 (TER PPh 21), UU 6/2023 Cipta Kerja, UU 1/2026 pidana.
