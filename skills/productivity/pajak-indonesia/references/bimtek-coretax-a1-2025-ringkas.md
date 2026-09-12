# Bimtek Coretax 2025 - Bukti Pemotongan PPh 21 Tahunan A1

Ringkasan materi Bimtek DJP "Pembuatan Bukti Pemotongan PPh Pasal 21 - Tahunan A1" (Muh Rahmatullah Barkat M, Fungsional Penyuluh Pajak Ahli Pertama, Direktorat P2humas, update 15-12-2025). Teks lengkap: `references/bimtek-coretax-a1-2025.md` (2603 baris).

## Dasar Hukum
- PP 58/2023 (TER PPh 21, berlaku 1 Jan 2024)
- PMK 168/2023 (juklak pemotongan PPh 21/26, berlaku 1 Jan 2024)
- PER-2/PJ/2024 (bentuk & tata cara bukti potong PPh 21/26)
- PER-11/PJ/2025 (pelaporan PPh/PPN/PPnBM/Bea Meterai dalam Coretax, berlaku 1 Jan 2025)
- PMK 81/2024 (Coretax/SIAP, berlaku 1 Jan 2025)
- PER-5/PJ/2024 (bupot instansi pemerintah)

## Kewajiban Pemotong PPh 21 (Hitung-Setor-Lapor-Bupot)
- **Hitung**: setiap masa, simpan catatan/dokumen perhitungan
- **Setor**: paling lambat **tanggal 15 bulan berikutnya**
- **Lapor**: paling lambat **tanggal 20 bulan berikutnya**
- **Buat bukti potong**:
  - Pegawai tetap/pensiunan: **BPMP** (bulanan, selain masa akhir) + **BPA1** (tahunan, masa akhir Desember/bulan berhenti)
  - Selain pegawai tetap: **BP21**
- SPT Masa PPh 21 nihil wajib dilaporkan tiap bulan KECUALI: tidak ada pemberian penghasilan DAN tidak punya pegawai (kecuali Desember)
- Bupot tetap dibuat walau nihil jika: penghasilan < PTKP, SKB/tarif 0%, DTP, fasilitas pajak, PPh 26 nihil P3B
- **BPMP hanya notifikasi** ke pegawai; **BPA1/BP21 terbit di Coretax = otomatis tersampaikan** via menu "Dokumen Saya" (jika pegawai aktivasi akun Coretax)

## Jenis Bukti Potong
| Jenis | Kapan | Dasar Hitung | Fungsi |
|---|---|---|---|
| BPMP | Jan-Nov / sebelum berhenti | TER Bulanan | Pengurang PPh terutang setahun saat buat BPA1 (prefill, non-editable) |
| BPA1/BPA2 | Masa Desember / bulan berhenti | PKP x Pasal 17 | Bukti potong di SPT Tahunan OP (terprefill) |

## Masa Pajak Terakhir
- Masa **Desember**; ATAU
- Masa pegawai tetap **berhenti bekerja**; ATAU
- Masa pensiunan **berhenti menerima** uang pensiun

## Perhitungan PPh 21
### Masa biasa (selain masa akhir)
```
PPh 21 = Penghasilan Bruto Bulanan x TER Bulanan
```
- Komponen bruto: gaji, tunjangan, uang lembur, bonus/THR, honorarium, premi asuransi pemberi kerja, natura/kenikmatan tertentu, tantiem/gratifikasi
- Natura yang dikecualikan (PMK 66/2023): makanan/minum semua pegawai, natura daerah tertentu, karena keharusan pekerjaan, jenis & besaran tertentu

### Masa pajak terakhir (Desember)
```
1. Ph Bruto setahun (teratur + tidak teratur + natura + premi asuransi)
2. Pengurang: Biaya Jabatan 5% (maks 500rb/bln / 6jt/thn) + Iuran pensiun/THT/JHT + Zakat wajib
3. Ph Neto setahun - PTKP = PKP (bulatkan ribuan ke bawah)
4. PPh 21 setahun = PKP x Tarif Pasal 17
5. PPh 21 Masa Terakhir = PPh setahun - PPh sudah dipotong masa sebelumnya
```
- Pengembalian lebih bayar + bupot A1: **paling lambat akhir bulan berikutnya** setelah masa pajak terakhir (31 Jan 2026 utk pegawai setahun penuh)
- Pegawai pindah kerja: bisa menggabungkan bupot (opsional, perlu BPA1 pemberi kerja lama); tanpa gabung = potensi kurang bayar di SPT Tahunan

### Jenis pemotongan (di BPA1)
- **FullYear**: bekerja setahun penuh (masa 1-12)
- **PartialYear**: kurang dari setahun (mulai/berhenti tengah tahun, SPDN sejak awal tahun)
- **Annualized (disetahunkan)**: (Ph Neto ÷ bulan bekerja) x 12 - untuk yang kehilangan/mendapat kewajiban subjektif di tahun berjalan (meninggalkan Indonesia, meninggal, WNA baru SPDN). Lalu scale down: (PPh setahun ÷ 12) x bulan bekerja

## PTKP (sesuai kondisi AWAL tahun pajak)
| Status | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| TK | 54 jt | 58,5 jt | 63 jt | 67,5 jt |
| K | 58,5 jt | 63 jt | 67,5 jt | 72 jt |
- Wanita kawin: PTKP dianggap TK/0 kecuali ada keterangan suami tidak berpenghasilan

## DTP (Ditanggung Pemerintah) - khusus instansi pemerintah
- Masa biasa: hitung TER terpisah DTP vs Non-DTP, buat 2 BPMP
- Masa akhir: 1 BPA1 dengan 5 tahap:
  1. PPh seluruh penghasilan (DTP+non) setahun
  2. PPh non-DTP saja setahun
  3. PPh DTP = tahap 1 - tahap 2
  4. PPh non-DTP masa terakhir = tahap 2 - (yang sudah dipotong non-DTP)
  5. PPh DTP masa terakhir = tahap 3 - (yang sudah dipotong DTP)
- **Lebih bayar DTP TIDAK dikembalikan ke pegawai**; LB non-DTP WAJIB dikembalikan. Catatan DTP & non-DTP harus terpisah.

## Iuran (per Maret 2024)
| Program | Pegawai | Perusahaan | Batas |
|---|---|---|---|
| JHT | 2% | 3,7% | tanpa batas atas |
| JP | 1% | 2% | 10.042.300/bln (Mar 2024) |
| BPJS Kes | 1% | 4% | 12.000.000/bln |
| JKK | - | 0,10-1,60% (by risiko) | tanpa batas |
| JKM | - | 0,20% | tanpa batas |
- Penambah bruto: JKK, JKM, BPJS Kes (pemberi kerja)
- Pengurang: iuran pensiun, JP, JHT/THT (dibayar pegawai)

## Contoh Kasus dari Bimtek (validasi hitung)
- **Tn.A setahun penuh (K/0, TER A)**: gaji 10jt + tunjangan 20jt + THR 60jt + bonus 20jt + lembur 10jt + JKK/JKM 960rb → bruto 450,96jt; TER 13-18% bulanan; PPh setahun 50,12jt
- **Tn.B mulai Sep (TK/0, TER A)**: gaji 15,5jt x 4 bln = 62jt; TER 7%; PPh 3,255jt; masa akhir: neto 59,6jt - PTKP 54jt = PKP 5,6jt → PPh 280rb; LB 2,975jt (dikembalikan PT Y)
- **Tn.C expat (TK/0, annualized)**: neto 56,9jt ÷ 4 x 12 = 170,7jt - PTKP = 116,7jt → PPh 3,835jt (sudah scale down 4 bln); KB 580rb
- **Tn.D berhenti Agustus (TK/0)**: gaji 17,5jt x 8 = 140jt; neto 135,2jt - PTKP = 81,2jt → PPh 6,18jt; sudah dipotong 9,8jt → LB 3,62jt
- **Tn.D2/D3 pindah kerja**: tanpa gabung bupot → KB; dengan gabung → nihil
- **Tn.E meninggalkan Indonesia (annualized)**: neto 136jt ÷ 8 x 12 = 204jt - 54jt = 150jt → PPh 11jt; dipotong 9,8jt → KB 1,2jt
- **Tn.F mata uang asing (K/3, TER C)**: US$2.000 x 15.000 = 30jt; 11% = 3,3jt
- **Tn.G gross up (TK/0)**: bruto full gross up 65,6jt; TER A 21% = 13,78jt/bulan; masa akhir PPh setahun 160,8jt - dipotong 151,5jt = 9,28jt
- **Tn.H tunjangan pajak (K/2, TER B)**: bruto 6,8jt; 0,5% = 34rb/bulan; masa akhir PPh 441rb - dipotong 374rb = 67rb

## Import XML BPA1 di Coretax
- Download converter XML (XLSX) di pajak.go.id/coretax
- Kolom wajib: NPWP pemotong, masa awal/akhir, tahun pajak, WNI/WNA, paspor (WNA), NIK/NPWP pegawai, status PTKP, posisi, kode objek pajak (21-100-01), status bupot (FullYear/Partial), gaji, tunjangan, honorarium, asuransi, natura, THR, iuran pensiun, zakat, nomor bupot sebelumnya, fasilitas pajak, PPh dipotong, ID TKU, tanggal pemotongan
- Export XML via Tab Developer Excel (Customize Ribbon → centang Developer)
- Import: eBupot → BPA1 → Import Data → Browse XML
- Pantau di menu Monitoring; cek "Message Detail" jika error
- Centang bupot yang akan terbit → Terbitkan

## Pitfalls
- TER hanya untuk masa biasa; masa akhir selalu Pasal 17
- FullYear wajib masa 1-12; kalau tidak, pilih PartialYear/Annualized
- LB DTP tidak dikembalikan; LB non-DTP wajib dikembalikan
- Bupot pembetulan: hapus konsep BPA1 lalu buat ulang
- SPT Masa PPh 21 nihil tetap wajib lapor (kecuali 2 kondisi + Desember)
- Biaya jabatan maks 500rb/bln atau 6jt/tahun (pegawai); pensiunan 200rb/bln / 2,4jt/tahun
