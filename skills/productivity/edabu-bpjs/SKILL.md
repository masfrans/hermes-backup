---
name: edabu-bpjs
description: "Panduan aplikasi EDABU BPJS Kesehatan (kepesertaan PPU)."
version: 1.0.0
platforms: [linux]
---

# Manual Aplikasi EDABU (BPJS Kesehatan)

Panduan penggunaan aplikasi EDABU - aplikasi BPJS Kesehatan untuk mengelola
data kepesertaan pekerja dan anggota keluarga sebagai Peserta Penerima Upah
(PPU). Sumber: Manual Pengguna Aplikasi EDABU (BPJS Kesehatan, 2019).

Dipakai saat user bertanya soal: EDABU, mutasi peserta BPJS, upload gaji BPJS,
pendaftaran pekerja BPJS, laporan tagihan BPJS, PHK peserta, KIS digital.

## Akses & Login

- URL: https://edabu.bpjs-kesehatan.go.id/Edabu
- Login: username + password + captcha (bisa reload/speak)
- Fitur halaman login: form login, lupa password, pendaftaran badan usaha baru,
  user manual, FAQ, video Mobile JKN
- User edabu v3.1 (lama): hanya username hak akses admin & super admin yang
  bisa dipakai di v4.0+
- User baru / belum pernah login v4.0+ → muncul form entri kelengkapan data user

### Pendaftaran akun badan usaha
1. Kantor cabang BPJS Kesehatan setempat
2. Portal Bersama BPJS: http://www.bpjs.go.id/
3. Aplikasi Registrasi Badan Usaha Web: https://new-edabu.bpjs-kesehatan.go.id/RegistrasiBadanUsaha/
4. Pembentukan/perpanjangan NIB via aplikasi OSS

### Form kelengkapan data user (validasi)
- Nama PIC: wajib, minimal 3 huruf
- Email PIC: format valid xxx@xxx.xxx
- Password lama: sesuai password v3.1/email pendaftaran
- Password baru: minimal 8 karakter = 1 huruf kapital + 1 huruf kecil + 1 angka + 1 karakter khusus
- Password verifikasi: harus sama dengan password baru
- Captcha: sesuai kode

## Struktur Menu (v4.0+)

1. **Home** - daftar tiket yang diproses PIC (nomor tiket, tanggal, badan usaha, cabang, jumlah data, status, progress)
2. **Peserta** - manajemen kepesertaan:
   - Input Data (mutasi individual)
   - Upload Data (mutasi batch via excel)
3. **Laporan** - download billing statement & rincian tagihan
4. **Referensi** - formulasi perubahan gaji, user manual, FAQ, video Mobile JKN
5. **Konten menu** - form sesuai menu
6. **Daftar Notifikasi** - peserta menunggak, PHK
7. **Data PIC** - nama PIC + logout

CATATAN PENTING: sejak v4.0 TIDAK ada lagi approval kantor cabang untuk mutasi
tambah-kurang peserta - seluruh mutasi langsung mengubah data kepesertaan.

## Pencarian Peserta

Kategori pencarian:
- NIK
- No JKN-KIS
- No Pegawai (hanya peserta badan usaha terkait)
- No Kartu Keluarga (hanya peserta badan usaha terkait)

## Mutasi Peserta (menu Peserta → Input Data)

### 1. Penambahan peserta & anggota keluarga baru
1. Pilih menu Peserta → Input Data; cari NIK
2. Pastikan "Terdaftar di" = **Belum Terdaftar**; pilih mutasi "Tambahkan Sebagai Pekerja"
3. Review & lengkapi data pribadi:
   - No HP: wajib, minimal 10 digit, diawali 08
   - Email: opsional, format valid
4. Review alamat (dari Disdukcapil Pusat)
5. Pilih FKTP: provinsi → kabupaten → faskes primer → faskes gigi
   (faskes gigi wajib jika faskes primer dokter umum; opsional jika tidak ada dokter gigi kerjasama)
6. Data kepegawaian: unit kerja, no pegawai, jabatan, status, gaji pokok+tunjangan
   (gaji wajib, minimal UMK sesuai unit kerja), asuransi lain, NPWP, paspor, disclaimer
7. Simpan → muncul NIK, nama, No JKN KIS
- Catatan: gaji < UMK → hubungi kantor cabang; pendaftaran mengikuti mekanisme
  cutoff (aktif bulan berikutnya)

### 2. Mutasi tambah anggota keluarga
1. Cari pekerja (NIK/No JKN/No Pegawai/No KK)
2. Pastikan pekerja terdaftar di PKS benar (status pekerja/penangguhan/nonaktif karena premi)
3. Pilih "Tambahkan Anggota Keluarga"
4. Input calon anggota: (a) inkuiri NIK, atau (b) inkuiri No Kartu Keluarga
5. Tentukan hubungan keluarga, input No HP, email opsional
6. Review alamat, pilih FKTP (opsi: cari faskes atau "Pilih Faskes Yang Sama Dengan Pekerja")
7. Centang disclaimer, simpan → muncul nomor anggota keluarga
- Anggota keluarga dalam kuota tertanggung langsung aktif jika peserta aktif

### 3. Mutasi pindah sebagai peserta (pindah penanggung)
1. Cari berdasarkan NIK/No JKN-KIS
2. Pastikan "Terdaftar di" = PKS yang BERBEDA dengan PKS user
3. Pilih "Pindahkan Sebagai Pekerja"
4. Lengkapi data pekerjaan (unit kerja, no pegawai, jabatan, status: tetap/kontrak/paruh waktu, gaji ≥ UMK)
5. Review anggota keluarga, centang 3 disclaimer, simpan

### 4. Mutasi pindah sebagai anggota keluarga pekerja
1. Cari calon anggota keluarga
2. Pastikan terdaftar di PKS berbeda + hubungan keluarga selain pekerja
3. Pilih "Pindahkan Sebagai Anggota Keluarga Pekerja"
4. Input No JKN KIS pekerja + status anggota keluarga

### 5. Mutasi ubah gaji
1. Cari pekerja → pilih mutasi "Ubah Gaji"
2. Input gaji baru (pokok + tunjangan)
3. Aplikasi otomatis hitung kelas rawat & premi
4. Centang disclaimer, simpan

### 6. Mutasi nonaktif peserta
Jenis: Resign / Meninggal / Habis Kontrak (pekerja); Meninggal (anggota keluarga)
1. Cari peserta → pilih mutasi nonaktif
2. Pilih jenis nonaktif; input No HP & email (kecuali meninggal)
3. Centang disclaimer, simpan
4. Review disclaimer final, centang "Kami Menyetujui Syarat dan Ketentuan", simpan

### 7. Mutasi cetak KIS
1. Cari peserta → pilih mutasi cetak KIS
2. Aplikasi download Kartu KIS digital (sah untuk pelayanan kesehatan)

### 8. Mutasi detail peserta
Lihat riwayat: data pribadi, alamat, FKTP (faskes primer & gigi), informasi
pekerjaan (jenis kepesertaan & iuran premi)

## Upload Data (batch)

### Upload mutasi gaji peserta
1. Akses menu Peserta → Upload Data
2. Pilih jenis mutasi gaji di combobox
3. Input jumlah data (validasi: **minimal 25 data**)
4. Upload file excel format mutasi gaji (download di menu Referensi → Formulasi Perubahan Gaji)
5. Validasi: peserta aktif/penangguhan/nonaktif-premi; gaji ≥ UMK Dati2; gaji angka wajib;
   No Kartu JKN KIS angka wajib; hanya pekerja badan usaha terkait;
   **admin = hanya cabang setempat, super admin = semua cabang**
6. Hapus data tidak valid, centang disclaimer, simpan (minimal 25 row)

## Notifikasi

1. **Peserta Menunggak**
2. **PHK Peserta**: PIC harus lapor permohonan penonaktifan PHK ke Kantor Cabang,
   lalu approval penonaktifan di aplikasi:
   - Buka notifikasi "Peserta PHK"
   - Review data pekerja, update No HP/email (wajib lengkap)
   - Lanjutkan → entri nomor surat persetujuan PHK dari Kantor Cabang
   - Centang disclaimer, simpan

## Laporan

### Laporan Tagihan (khusus hak akses SUPER ADMIN)
1. Menu Laporan → Tagihan
2. Pilih bulan tagihan (datepicker)
3. Selanjutnya → pilih: download **billing statement** atau **rincian tagihan**

## Referensi

1. Formulasi Perubahan Gaji (format excel 3 kolom update gaji)
2. User Manual EDABU
3. FAQ EDABU
4. Video Tutorial Aplikasi Mobile JKN

## Pitfall

- Mutasi v4.0+ langsung aktif tanpa approval cabang - teliti sebelum simpan
- Upload batch minimal 25 data
- Gaji minimum = UMK lokasi unit kerja
- No HP wajib diawali 08, minimal 10 digit
- Faskes gigi wajib jika faskes primer dokter umum
- Laporan tagihan khusus super admin
- Detail lengkap per form: `references/manual-edabu-full.md`
- Konsep JKN/BPJS, manfaat kepesertaan, simulasi iuran, pendaftaran BU:
  `references/summary-edabu-mekari.md`
