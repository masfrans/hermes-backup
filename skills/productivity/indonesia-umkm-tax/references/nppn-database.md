# Database NPPN (Norma Penghitungan Penghasilan Neto) - Lokasi & Cara Scrape Ulang

## Database Lengkap (1.435 kelompok KLU)
File lokal: `/mnt/user-data/outputs/database-nppn-lengkap.md` (209KB, 1.879 baris)
- Header: ringkasan + rumus + 3 wilayah
- Tabel ringkasan per kategori (84 kategori + jumlah)
- Tabel lengkap per kategori: No | KLU | Uraian | % 10 Ibukota | % Ibukota Lain | % Daerah Lain

## Ringkasan
- Total: **1.435 kelompok KLU** dalam **84 kategori** (2 digit KBLI)
- Sumber: Lampiran I **PER-17/PJ/2015** (masih berlaku, belum dicabut); penggunaan diatur **PMK 81/2024** (1 Jan 2025)
- Berlaku utk WP OP peredaran bruto < Rp 4,8 M/tahun
- 3 wilayah: (1) 10 ibukota provinsi: Medan, Palembang, Jakarta, Bandung, Semarang, Surabaya, Denpasar, Manado, Makassar, Pontianak; (2) ibukota provinsi lainnya; (3) daerah lainnya
- Rumus: **Ph Neto = Omzet x %NPPN**; PPh = (Neto - PTKP) x Tarif Pasal 17

## Persentase Contoh (cross-check terverifikasi dengan sumber publik)
| KLU | Uraian | 10 Ibukota | Ibukota Lain | Daerah Lain |
|---|---|---|---|---|
| 01120 | Pertanian Padi | 15% | 15% | 15% |
| 01117 | Biji-bijian minyak makan | 11,5% | 11% | 10% |
| 69100 | Jasa Hukum (pengacara) | 51% | 50% | 50% |
| 69200 | Jasa Akuntansi | 50% | 50% | 50% |
| 74902 | Konsultasi Bisnis | 50% | 50% | 50% |
| 86201/2 | Praktik Dokter Umum/Spesialis | 50% | 50% | 50% |
| 86103 | Rumah Sakit Swasta | 30% | 27,5% | 25% |

## Cara Scrape Ulang (kalau file hilang)
1. Link lampiran resmi pajak.go.id (`/sites/default/files/2019-06/Lampiran+1_PER_17_PJ_2015.pdf`) **SUDAH MATI** - balikin HTML bukan PDF. Jangan buang waktu di sana.
2. Sumber alternatif berisi tabel lengkap: **umkmcerdaspajak.id/daftar-persentase-norma-penghitungan-penghasilan-neto-nppn/** (932KB HTML, 2 tabel, 1.441 baris termasuk header)
3. Parse: ambil `<table>`, regex `<tr>...<td>`, data mulai baris indeks 6 (NO|KLU|URAIAN|W1|W2|W3)
4. archive.org wayback: rate-limited (429) dari IP server - tidak andal
5. idoc.tips: hanya placeholder min.pdf - tidak berguna

## Validasi
- Cross-check sampel (dokter 50%, akuntan 50%, pengacara 51%/50%) konsisten dengan medisy.id, pajak.com, taxindo, klikpajak
- Jumlah 1.435 cocok dengan referensi Ortax/DDTC
- Persentase "-" (misal RS pemerintah 86101/86102, puskesmas) = pengecualian/tidak termasuk objek
- Untuk pelaporan resmi tetap sarankan verifikasi lampiran asli DJP / konsultan pajak

## Pitfalls
- Uraian KBLI sering panjang (2-3 kalimat) - potong 100 karakter utk tabel ringkas
- Kategori terbanyak: 47 perdagangan eceran (182), 10 industri makanan (88), 01 pertanian (84)
- Kelompok tidak tercantum → gunakan kelompok paling mendekati
- Persentase berbeda per wilayah - pakai kolom sesuai domisili usaha
