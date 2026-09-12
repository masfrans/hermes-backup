---
name: hr-payroll-indonesia
description: "Konsep payroll Indonesia: PPh 21, BPJS, THR, lembur, THP."
version: 1.0.0
platforms: [linux]
---

# Basic Concept of Payroll (Indonesia)

Referensi konsep dasar payroll Indonesia dari Mekari University (univ.mekari.com), revisi 2024. Dipakai saat user bertanya soal gaji, PPh 21, BPJS, THR, lembur, cuti, atau perhitungan payroll. Sumber dokumen asli: `references/basic-concept-of-payroll.md` (teks lengkap + tabel TER 44/40/41 lapisan + 3 studi kasus).

## Referensi
- `references/basic-concept-of-payroll.md` - materi dasar payroll Mekari
- `references/bimtek-coretax-a1-2025-ringkas.md` - ringkasan Bimtek Coretax A1
- `references/exercise-bpjs-kesehatan.md` - latihan hitung BPJS Kesehatan (3 kasus: Damar, Sandi, Dedi; aturan 5%, 4%/1%, cap 12jt, cover 5 orang, tambahan 1%/orang)

## Coretax & Bukti Potong A1 (tambahan dari Bimtek DJP 2025)
- Ringkasan: `references/bimtek-coretax-a1-2025-ringkas.md` - kewajiban pemotong (setor tgl 15, lapor tgl 20), BPMP vs BPA1, masa pajak terakhir, DTP 5 tahap, 9 contoh kasus (Tn.A-Tn.H), import XML
- Teks lengkap: `references/bimtek-coretax-a1-2025.md` (2603 baris, simulasi form BPA1)
- Detail lengkap juga ada di skill `pajak-indonesia`

## 1. Pengenalan Payroll
Payroll = sistem penggajian agar proses penggajian efektif & efisien. Data pendukung:
- **Personal Data**: identitas pribadi karyawan
- **Employment Data**: hubungan kerja (status, jabatan, jadwal kerja, kehadiran)
- **Payroll Data**:
  - Gaji Pokok: imbalan tanpa tunjangan
  - Tunjangan: penambah pendapatan, menambah THP (transport, makan)
  - Benefit: penambah pendapatan, TIDAK menambah THP (BPJS Kes & Ketenagakerjaan)
  - Potongan: pengurang pendapatan (telat, absen)
  - Upah Lembur, Klaim, Pinjaman

## 2. Kebijakan Spesifik HR

### Hubungan Kerja
- **Probation**: maksimal 3 bulan, bisa dihentikan salah satu pihak
- **Contract**: PKWT, maksimal 5 tahun (termasuk perpanjangan)
- **Permanent**: PKWTT, bisa dihentikan sesuai prosedur

### Waktu Kerja
- 40 jam/minggu: 6 hari @ 7 jam ATAU 5 hari @ 8 jam
- **Pekerja harian lepas**: maksimum 21 hari kerja/bulan; jika lebih & 3 bulan berturut-turut → wajib PKWT/PKWTT

### Lembur (Overtime)
```
Upah Lembur = (Jam Lembur x Upah Sebulan x Multiplier) / 173 jam
```
- 173 jam = 52 minggu x 40 jam / 12 bulan
- **Hari kerja**: jam ke-1 = 1,5x upah sejam; jam seterusnya = 2x
- **Hari istirahat/libur nasional (5 hari kerja)**: 8 jam pertama = 2x; jam ke-9 = 3x; jam ke-10 & 11 = 4x
- **Hari istirahat/libur nasional (6 hari kerja)**: 7 jam pertama = 2x; jam ke-8 = 3x; jam ke-9 & 10 = 4x

### Cuti (Time Off)
- Cuti Tahunan: setelah 1 tahun kerja
- Cuti Tidak Berbayar: jika belum punya hak cuti tahunan
- Cuti Sakit: tanpa minimal masa kerja
- Cuti Penting/Khusus: menikah 3 hari; menikahkan/mengkhitankan/membaptiskan anak 2 hari; istri melahirkan/keguguran 2 hari; suami/istri/orang tua/mertua/anak/menantu meninggal 2 hari; anggota keluarga serumah meninggal 1 hari
- Cuti Besar: setelah 6 tahun berturut-turut, umumnya 30 hari/tahun di tahun ke-7

### Upah Minimum
- UMR sudah diganti: **UMP** (diumumkan 1 Nov) & **UMK** (paling lambat 21 Nov)
- UMP DKI Jakarta 2024: Rp 5.067.381

### THR
- Wajib ≤ 7 hari sebelum hari raya; denda 5% jika terlambat
- Masa kerja ≥ 12 bulan: 1 bulan upah
- Masa kerja 1-12 bulan (proporsional): (Masa Kerja x Upah Sebulan) / 12

## 3. BPJS (per Maret 2024)

| Jaminan | Pihak | Tarif | Dasar Min | Dasar Maks/bulan |
|---|---|---|---|---|
| BPJS Kesehatan | Perusahaan | 4% | UMR/UMK | Rp 12.000.000 |
| BPJS Kesehatan | Karyawan | 1% | UMR/UMK | Rp 12.000.000 |
| JKK | Perusahaan | 0,24-1,74% (sesuai risiko) | UMR/UMK | - |
| JKM | Perusahaan | 0,3% | UMR/UMK | - |
| JHT | Perusahaan | 3,7% | UMR/UMK | - |
| JHT | Karyawan | 2% | UMR/UMK | - |
| JP | Perusahaan | 2% | UMR/UMK | Rp 10.042.300 |
| JP | Karyawan | 1% | UMR/UMK | Rp 10.042.300 |
| JKP | Pemerintah Pusat + Perusahaan | rekomposisi JKK & JKM | - | - |

Penambah bruto: jaminan dibayar pemberi kerja. Pengurang: iuran dibayar pekerja.

## 4. Pajak (PPh 21)

### Metode: Gross / Gross Up / Netto
- **Gross**: PPh 21 ditanggung karyawan
- **Gross Up**: ditanggung perusahaan, jadi komponen tunjangan, bisa dibebankan
- **Netto**: ditanggung perusahaan, TIDAK jadi komponen tunjangan, TIDAK bisa dibebankan

### PTKP (per tahun)
| Status | 0 anak | 1 | 2 | 3 |
|---|---|---|---|---|
| Tidak Kawin (TK) | 54 jt | 58,5 jt | 63 jt | 67,5 jt |
| Kawin (K) | 58,5 jt | 63 jt | 67,5 jt | 72 jt |
| Kawin gabungan (K/I) | 112,5 jt | 117 jt | 121,5 jt | 126 jt |

### TER Bulanan (PP 58/2023, PMK 168/2023) - sejak 1 Jan 2024
- **TER A**: TK/0, TK/1, K/0 → 0% (≤5,4 jt) s.d. 34% (>1,4 M) - 44 lapisan
- **TER B**: TK/2, TK/3, K/1, K/2 → 0% (≤6,2 jt) s.d. 34% (>1,405 M) - 40 lapisan
- **TER C**: K/3 → 0% (≤6,6 jt) s.d. 34% (>1,419 M) - 41 lapisan
- PPh 21 bulanan = Penghasilan Bruto Bulanan x TER Bulanan (masa biasa)
- Detail tabel lengkap di file referensi

### Tarif Pasal 17 (UU PPh 36/2008 & UU HPP 7/2021)
- 0 - 60 jt: 5%
- >60 - 250 jt: 15%
- >250 - 500 jt: 25%
- >500 jt - 5 M: 30%
- >5 M: 35%

### Perhitungan Masa Biasa (bulanan)
Bruto bulanan = Gaji Pokok + Tunjangan + BPJS (4%) + JKK + JKM → PPh 21 = Bruto x TER

### Perhitungan Masa Pajak Terakhir
1. Bruto setahun (termasuk THR)
2. Kurangi: Biaya Jabatan (5%, maks 6 jt/tahun atau 500 rb/bulan), Iuran Pensiun, Zakat wajib
3. Netto setahun → kurangi PTKP → PKP (bulatkan ribuan ke bawah)
4. PPh 21 setahun = PKP x Tarif Pasal 17
5. PPh 21 Masa Terakhir = PPh setahun - PPh yang sudah dipotong (lebih/kurang bayar)
- Lebih bayar wajib dikembalikan + bukti potong 1721-A1 paling lambat akhir bulan berikutnya

## 5. Perhitungan Take Home Pay
```
THP = (Gaji Pokok + THR/Bonus + Tunjangan)
      - (Pinjaman + Potongan + PPh 21 Bulanan + JHT 2% + JP 1% + BPJS Kes 1%)
```
- JHT karyawan: 2% x Gaji Pokok
- JP karyawan: 1% x Gaji Pokok x Masa Kerja (maks pengali 10.042.300, berubah tiap tahun)
- BPJS Kes karyawan: 1% x Gaji Pokok (maks dasar 12.000.000)

## 6. Pengunduran Diri & Akhir Masa Kerja
- Resign: wajib 1 bulan notice; tidak terikat ikatan dinas; dapat uang pisah/kompensasi cuti tersisa
- PHK: wajib pesangon + uang penghargaan masa kerja + uang penggantian hak
- Pensiun: karyawan tetap usia 55-60 tahun

## 7. Studi Kasus (acuan perhitungan)
File referensi memuat 3 kasus lengkap dari dokumen asli:
1. **Kasus 1 - Penghasilan Teratur**: Dimas, kawin 2 anak (K/2), gaji 15 jt + tunjangan 1,8 jt, BPJS → PPh 21 = 17.361.000 x 7% (TER B) = 1.215.270; THP = 15.064.307
2. **Kasus 2 - THR**: + THR 10 jt → bruto 27.361.000 x 10% = 2.736.100; THP = 23.543.477
3. **Kasus 3 - Masa Akhir**: 8 bulan, PKP 74.184.000 → PPh setahun 5.127.600; sudah dipotong 10.027.720 → lebih bayar 4.900.120 (dikembalikan + 1721-A1)

## Pitfalls
- Batas maksimum berubah tiap tahun: JP 10.042.300 (Mar 2024), BPJS Kes 12.000.000 - selalu cek tahun berjalan
- TER hanya untuk masa biasa; masa terakhir pakai Tarif Pasal 17
- PKP dibulatkan ribuan ke bawah sebelum kena tarif
- Tabel TER lengkap (44/40/41 lapisan) jangan dihafal - baca file referensi saat butuh angka pasti
- UMR sudah tidak berlaku - pakai istilah UMP/UMK
