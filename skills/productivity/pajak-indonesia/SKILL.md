---
name: pajak-indonesia
description: "Pajak Indonesia: PPh 21, PPh Final UMKM 0,5%, PP 20/2026."
version: 1.0.0
platforms: [linux]
---

# Pajak Indonesia (Tax)

Referensi perpajakan Indonesia: kerangka UU (KUP, PPh, PPN, HPP, Cipta Kerja, Penyesuaian Pidana), PPh 21 karyawan (TER, PTKP, Pasal 17), PPh Final UMKM 0,5% (PP 20/2026), PPN 12% (PMK 131/2024), dan Coretax (PMK 81/2024). Dipakai saat user bertanya soal pajak, peraturan perpajakan terbaru, atau perhitungan pajak.

## Daftar Lengkap Peraturan Berlaku
Lihat `references/peraturan-berlaku.md` - daftar lengkap UU, PP, PMK yang berlaku 2026 + skema per status + sumber valid (DJP, BPK, Ortax, DDTC).

## Coretax & Bukti Potong A1 (Bimtek DJP 2025)
Materi resmi Bimtek DJP "Pembuatan Bukti Pemotongan PPh 21 Tahunan A1" (PER-11/PJ/2025):
- Ringkasan: `references/bimtek-coretax-a1-2025-ringkas.md` - kewajiban pemotong (setor 15, lapor 20), BPMP vs BPA1, masa pajak terakhir, DTP 5 tahap, 9 contoh kasus lengkap, panduan import XML
- Teks lengkap: `references/bimtek-coretax-a1-2025.md` (2603 baris, termasuk simulasi form BPA1)
- Poin kunci: FullYear/PartialYear/Annualized, LB DTP tidak dikembalikan, bupot Coretax otomatis tersampaikan via "Dokumen Saya"

## SPT Tahunan PPh OP - WP Peredaran Bruto Tertentu (Coretax)
Materi edukasi resmi DJP (P2Humas, versi 20251001):
- Ringkasan: `references/spt-tahunan-umkm-coretax-ringkas.md` - alur 5 langkah, panduan isi induk A-J, L-3B (rekap peredaran bruto bulanan, PPh final 0,5%), L-2 (kode akun 411128-420), L-1 (harta/utang/tanggungan)
- Teks lengkap: `references/spt-tahunan-umkm-coretax.md` (1057 baris, ilustrasi kasus Tuan A omzet 1,71 M)
- Poin kunci: bupot PPh final diinput di L-3B bukan Induk D; selisih LB → 14h → pengembalian; NIK=NPWP; simulator spt-simulasi.pajak.go.id

## Kelas Pajak Mediawan Cesarian Syah (Optimasi & Advanced Tax Planning)
Materi kelas pajak dari Mediawan Cesarian Syah (mantan DJP, CEO SIF Consulting) - sangat lengkap & praktis:
- **Ringkasan lengkap**: `references/kelas-pajak-mediawan-ringkas.md` - PP 20/2026 detail (Pasal 57/58/56/II/20A), perbandingan bentuk usaha, Pasal 31E, titik impas 0,5% vs tarif umum, owner compensation 3 jalur, dividen 0% syarat PMK 18/2021, PKP threshold, PPN 11/12 (PMK 131/2024), PPh 22 marketplace DITUNDA (PENG-46/2026), SP2DK 14 hari (PMK 111/2025), pemeriksaan PMK 15/2025, PMK 8/2026 (ILAP/SLIK), PMK 44/2026 kuasa, PMK 172/2023 TP, Pillar Two PMK 136/2024, 10 indikator risiko, kerangka 5 langkah, 7 prioritas 2026-2027
- **Teks lengkap kelas 02**: `references/kelas02-optimasi-pajak-bisnis.md` (1639 baris)
- **Teks lengkap kelas 03**: `references/kelas03-advanced-tax-planning.md` (1374 baris)
- **Koreksi penting dari materi**: PMK 17/2013 DICABUT PMK 15/2025; tenggat SP2DK 14 hari kalender BUKAN 60 hari; TIDAK ADA safe harbor TP 5% di Indonesia; "e-Faktur 4.0" bukan nomenklatur resmi; batas unggah e-Faktur tgl 20 (bukan 15)

## Sumber Valid
- PP 20/2026: https://peraturan.bpk.go.id/Details/349415/pp-no-20-tahun-2026
- Artikel DJP: https://www.pajak.go.id/en/node/119954
- PP 58/2023 & PMK 168/2023 (TER PPh 21)
- PMK 131/2024 (PPN 11-12% barang mewah): https://pajak.go.id/id/artikel/pmk-1312024-tarif-ppn-sebelas-dua-belas
- PMK 81/2024 jo. PMK 11, 53, 54/2025 (Coretax)
- PMK 101/2016 (PTKP - masih berlaku)
- UU 7/2021 (HPP), UU 6/2023 (Cipta Kerja), UU 1/2026 (Penyesuaian Pidana)
- UU PPh No. 36/2008 & UU HPP No. 7/2021 (Tarif Pasal 17)

## Kerangka Hukum (ringkas)
- **UU KUP** (6/1983 jo. 16/2009, 6/2023, 1/2026): ketentuan umum, NPWP (NIK = NPWP), SPT, sanksi
- **UU PPh** (7/1983 jo. 36/2008, 7/2021): tarif Pasal 17, PTKP, PPh final
- **UU PPN** (8/1983 jo. 42/2009, 7/2021): tarif 11% → 12% (barang mewah saja, PMK 131/2024)
- **UU 7/2021 (HPP)**: lapisan 60jt 5%, PPN 12%, PPS, NIK=NPWP, pajak karbon
- **UU 6/2023 (Cipta Kerja)**: penyesuaian KUP/PPh/PPN
- **UU 1/2026 (Penyesuaian Pidana)**: berlaku 2 Jan 2026, ancaman pidana selaras KUHP Nasional di 6 UU pajak
- **PP 55/2022 jo. PP 20/2026**: PPh final UMKM
- **PP 58/2023 + PMK 168/2023**: TER PPh 21
- **PMK 81/2024 jo. PMK 11/53/54-2025**: Coretax (SIAP) sejak 1 Jan 2025

---

## A. PPh 21 Karyawan (dipakai di payroll)

### Metode Pengenaan
- **Gross**: PPh 21 ditanggung karyawan (dipotong dari gaji)
- **Gross Up**: ditanggung perusahaan, menjadi komponen tunjangan, bisa dibebankan perusahaan
- **Netto**: ditanggung perusahaan, TIDAK jadi komponen tunjangan, TIDAK bisa dibebankan

### PTKP (per tahun)
| Status | 0 anak | 1 | 2 | 3 |
|---|---|---|---|---|
| Tidak Kawin (TK) | 54 jt | 58,5 jt | 63 jt | 67,5 jt |
| Kawin (K) | 58,5 jt | 63 jt | 67,5 jt | 72 jt |
| Kawin gabungan (K/I) | 112,5 jt | 117 jt | 121,5 jt | 126 jt |

### TER Bulanan (PP 58/2023, PMK 168/2023, berlaku 1 Jan 2024)
- PPh 21 masa biasa = Penghasilan Bruto Bulanan x TER Bulanan
- **TER A**: TK/0, TK/1, K/0 → 0% (≤5,4 jt) s.d. 34% (>1,4 M), 44 lapisan
- **TER B**: TK/2, TK/3, K/1, K/2 → 0% (≤6,2 jt) s.d. 34% (>1,405 M), 40 lapisan
- **TER C**: K/3 → 0% (≤6,6 jt) s.d. 34% (>1,419 M), 41 lapisan
- Tabel lapisan lengkap di `references/ter-tables.md`

### Tarif Pasal 17 (UU PPh 36/2008 & UU HPP 7/2021)
- 0 - 60 jt: 5%
- >60 - 250 jt: 15%
- >250 - 500 jt: 25%
- >500 jt - 5 M: 30%
- >5 M: 35%

### Masa Pajak Terakhir (tahunan)
1. Bruto setahun (termasuk THR)
2. Kurangi: Biaya Jabatan (5%, maks 6 jt/th atau 500 rb/bln), Iuran Pensiun, Zakat wajib
3. Netto setahun - PTKP = PKP (bulatkan ribuan ke bawah)
4. PPh 21 setahun = PKP x Tarif Pasal 17
5. PPh Masa Terakhir = PPh setahun - PPh sudah dipotong (lebih/kurang bayar)
- Lebih bayar wajib dikembalikan + bukti potong 1721-A1 maks akhir bulan berikutnya
- Pelaporan: SPT PPh 21 via e-Bupot 21/26; bukti potong 1721-VIII bulanan

---

## B. PPh Final UMKM 0,5% (PP 55/2022 jo. PP 20/2026)

### Ketentuan Dasar (tetap)
- Tarif: **0,5% x peredaran bruto (omzet)**
- Batas omzet: **Rp 4,8 miliar/tahun**
- Berlaku untuk WP OP dan perseroan perorangan dengan peredaran bruto tertentu
- WP yang memilih mekanisme umum tidak bisa balik ke final

### PERUBAHAN PENTING PP 20/2026 (ditetapkan 22 April 2026)

#### 1. Profesi Pekerjaan Bebas Dikecualikan
Tidak lagi bisa pakai PPh Final 0,5% (wajib mekanisme umum):
Pengacara, akuntan, arsitek, dokter, konsultan, notaris, penilai, aktuaris, agen iklan, influencer, selebgram, blogger, vlogger, seniman, olahragawan, pelatih, moderator, agen asuransi.
→ Dasar: Pasal 56 ayat (3) huruf a dan ayat (4) PP 20/2026.

#### 2. Anti Pecah Usaha (Pasal 56)
- WP OP dengan beberapa perseroan perorangan: peredaran bruto SELURUH entitas digabung
- Total gabungan > Rp 4,8 M dalam satu tahun pajak → semua entitas TIDAK berhak fasilitas 0,5% tahun-tahun berikutnya
- Mencegah pemecahan omzet ke banyak entitas untuk tetap di bawah batas

#### 3. Penggabungan Omzet Suami-Istri
- Pasangan dengan pemisahan harta / kewajiban pajak terpisah: batas 4,8 M dihitung dari penggabungan peredaran bruto keduanya
- Peredaran bruto anak belum dewasa juga bisa diperhitungkan dalam kondisi tertentu

#### 4. Koperasi
- Koperasi BOLEH pakai PPh Final 0,5%, tapi terbatas **4 tahun pajak** sejak terdaftar sebagai WP
- Setelah itu beralih ke mekanisme umum

#### 5. Antikorupsi
- Pengeluaran berupa **suap, gratifikasi, atau pemberian terkait tindak pidana korupsi TIDAK bisa dijadikan biaya pengurang** penghasilan bruto
- Termasuk pemberian kepada pejabat publik asing

### Dampak
- UMKM murni: relatif tidak terdampak
- Multi-entitas, profesi bebas, struktur usaha keluarga kompleks: WAJIB paham aturan baru

---

## Contoh Perhitungan PPh 21 (acuan)
- **Kasus masa biasa**: gaji 15 jt + tunjangan 1,8 jt, K/2 (TER B) → bruto 17.361.000 x 7% = PPh 21 1.215.270
- **Kasus THR**: + THR 10 jt → bruto 27.361.000 x 10% = 2.736.100
- **Kasus masa akhir**: 8 bulan, PKP 74.184.000 → PPh setahun 5.127.600; lebih bayar 4.900.120
- Detail lengkap di skill `hr-payroll-indonesia`

## Pitfalls
- Batas omzet 4,8 M dan tarif 0,5% TIDAK berubah di PP 20/2026 - yang berubah adalah SUBJEK yang boleh pakai
- TER hanya untuk masa biasa; masa terakhir pakai Tarif Pasal 17
- PKP dibulatkan ribuan ke bawah
- Tabel TER lengkap jangan dihafal - baca `references/ter-tables.md`
- Selalu cek tahun berjalan: batas maksimum JP/BPJS dan tarif bisa berubah
- PP 20/2026 berlaku mulai tahun pajak setelah ditetapkan (cek detail tanggal mulai berlaku di sumber resmi bila ditanya)
- **PPN 12% HANYA barang mewah** (PMK 131/2024) - non-mewah tarif efektif 11% via DPP nilai lain
- **PTKP belum berubah sejak 2016** (PMK 101/2016) - TK/0 tetap 54jt
- **NIK = NPWP** (UU HPP) - wajib pajak OP pakai NIK
- **Coretax** mulai 1 Jan 2025: kewajiban pajak terpusat, portal coretaxdjp.pajak.go.id
- UU 1/2026 (Penyesuaian Pidana) mengubah ancaman pidana pajak - cek detail saat kasus pidana
- Jangan gunakan istilah UMR (sudah diganti UMP/UMK)
