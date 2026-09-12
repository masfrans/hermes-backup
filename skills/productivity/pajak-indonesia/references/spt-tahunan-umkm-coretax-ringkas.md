# SPT Tahunan PPh OP - WP Penghasilan Bruto Tertentu (omzet < 4,8M) via Coretax

Ringkasan materi edukasi Coretax DJP (Direktorat P2Humas, versi 20251001). Teks lengkap: `references/spt-tahunan-umkm-coretax.md` (1057 baris).

## Definisi Penghasilan Bruto (Pasal 1 PMK 81/2024)
Semua penghasilan dari kegiatan usaha + luar usaha, setelah dikurangi retur/pengurangan penjualan/potongan tunai, SEBELUM dikurangi biaya, dari Indonesia maupun luar negeri.

## Alur Pelaporan (5 Langkah)
1. **Siapkan dokumen**: daftar peredaran usaha setahun, bukti potong/pungut lawan transaksi, daftar harta & utang akhir tahun, daftar keluarga/tanggungan
2. **Login Coretax**: https://coretaxdjp.pajak.go.id (NIK 16 digit utk WNI / NPWP 16 digit utk WNA + password + captcha)
3. **Buat draf SPT**: Modul SPT → Buat Konsep SPT → PPh Orang Pribadi → Lanjut → SPT Tahunan → Periode & Tahun Pajak → Model SPT Normal → Buat Konsep
4. **Isi induk + lampiran**
5. **Bayar & Lapor**

## Induk SPT (10 bagian A-J)
- **Header**: Sumber penghasilan (Kegiatan Usaha/Pekerjaan/Pekerjaan Bebas) + Metode Pembukuan/Pencatatan (default: Pencatatan)
- **A. Identitas WP**: otomatis dari profil; A.7/A.8 hanya utk pisah harta/terpisah suami-istri
- **B. Ikhtisar Penghasilan Neto** (pertanyaan kunci):
  - 1.a penghasilan dari pekerjaan? (UMKM murni: Tidak)
  - 1.b.1 penghasilan dari usaha/pekerjaan bebas? (Ya)
  - **1.b.2 WP OP peredaran bruto tertentu?** → pilih "Ya, termasuk WP OP yang memiliki peredaran bruto tertentu yang dikenakan PPh final" → memunculkan Lampiran L-3B
  - 1.b.3 pakai Norma? → "Tidak, saya hanya menerima penghasilan dari usaha yang dikenakan pajak bersifat final dan tidak menyelenggarakan pembukuan"
  - 1.b.5 penghasilan neto usaha non-final → 0 (karena semua final)
  - 1.c/1.d penghasilan lain → Tidak
- **C. Perhitungan Pajak Terutang**: neto setahun 0, PTKP diisi (kecuali PH/MT diisi 0), PKP 0, PPh terutang 0
- **D. Kredit Pajak**: bupot PPh final TIDAK di sini (di L-3B Bagian A); angsuran 25 prepopulated
- **E. PPh Kurang/Lebih Bayar**: 0 utk WP semata-mata final peredaran bruto tertentu
- **F. Pembetulan**: hanya utk SPT pembetulan
- **G. Permohonan pengembalian LB**: dilewati (bukan LB)
- **H. Angsuran PPh 25**: semua "Tidak" (13a, 13b, 13c) karena final
- **I. Pernyataan Transaksi Lainnya**:
  - 14a Harta akhir tahun: WAJIB minimal 1 komponen (L-1 Bagian A)
  - 14b Utang: Ya jika ada (L-1 Bagian B)
  - 14c Penghasilan final: Ya → isi L-2 Tabel A
  - 14d non objek: Tidak
  - 14e penyusutan/amortisasi: dilewati (hanya pembukuan)
  - 14f entertainment/natura: Tidak (hanya pembukuan)
  - 14g dividen non objek: Tidak
  - **14h Kelebihan PPh Final**: terisi jika ada selisih LB di L-3B → bisa ajukan pengembalian pajak seharusnya tidak terutang
- **J. Lampiran Tambahan**: No

## Lampiran L-3B (Rekapitulasi Peredaran Bruto) - KUNCI
- Otomatis terbentuk saat pilih WP OP Peredaran Bruto Tertentu (induk 1.b.2)
- 4 bagian: daftar tempat usaha (otomatis), A (final peredaran bruto tertentu), B (OPPT), C (NPPN)
- Isi **peredaran bruto per bulan** (contoh: Jan 125jt ... Des 200jt, total 1,71 M)
- Sistem hitung otomatis:
  - [4] Peredaran Bruto Kena Pajak (>500jt non-final per tahun... lihat aturan)
  - [5] PPh Final terutang = 0,5% x [4]
  - [6] PPh final disetor sendiri (dari Buku Besar)
  - [7] PPh final dipotong/dipungut pihak lain
  - [8] Selisih = [5] - [6] - [7]
- **Selisih kurang bayar** → setor mandiri; **selisih lebih bayar** → tampil di induk 14h → ajukan pengembalian

## Lampiran L-2 (Penghasilan Final)
- Bagian A: 2 data otomatis: (1) setor sendiri PPh final kode akun **411128-420**, (2) bupot PPh final
- Edit DPP: masukkan total DPP penyetoran mandiri (misal 1.710.000.000 sesuai L-3B)

## Lampiran L-1
- Bagian A: Harta akhir tahun (prefill dari SPT tahun lalu; Tambah/Edit/Hapus/Import)
- Bagian B: Utang akhir tahun (prefill)
- Bagian C: Anggota keluarga tanggungan (dari Unit Pajak Keluarga, ubah di Portal Saya → Profil → Unit Pajak Keluarga)
- Bagian D: Penghasilan neto DN dari pekerjaan (jika ada)
- Bagian E: Daftar bupot/pungut PPh (jika ada)

## Submit
- Kembali ke induk → K. Pernyataan → Simpan Konsep → Bayar dan Lapor
- Pembayaran: Pemindahbukuan Deposit (jika saldo cukup) atau Buat Kode Biling
- Hasil di menu "SPT Dilaporkan" + Bukti Penerimaan Elektronik (BPE)

## Sumber Edukasi Resmi
- Video: Youtube @DitjenPajakRI
- Slide: www.pajak.go.id/id/lapor-tahunan
- Simulator: spt-simulasi.pajak.go.id

## Pitfalls
- NIK = NPWP utk WNI (16 digit); WNA pakai NPWP 16 digit
- Bupot PPh final TIDAK diinput di Induk D (kredit pajak) - masuk L-3B Bagian A
- PTKP diisi 0 untuk suami-istri PH/MT
- Pencatatan vs Pembukuan: stelsel kas hanya jika sudah izin
- Harta akhir tahun wajib minimal 1 komponen
- Kode akun pajak PPh final UMKM setor sendiri: 411128-420
- Dokumen ini versi 20251001 - cek update di pajak.go.id
