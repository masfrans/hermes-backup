---
name: indonesia-umkm-tax
description: "Pajak UMKM Indonesia: PP 20/2026 final, NPPN, Pasal 31E."
version: 1.0.0
platforms: [linux]
---

# Pajak UMKM & Orang Pribadi (Indonesia, update 2026)

Gunakan saat user bertanya: PPh final UMKM 0,5%, NPPN, Pasal 31E, tarif Pasal 17 OP/badan, PTKP, atau audit kalkulator pajak. Untuk PPh 21 karyawan, BPJS, THR, lembur: lihat skill `hr-payroll-indonesia` (skill terpisah, user-owned).

## PP 20/2026 — PPh Final UMKM 0,5% (berlaku 22 April 2026, mengubah PP 55/2022)
- Orang pribadi (OP) & PT Perorangan: final 0,5% dari omzet bruto, TANPA batas waktu (permanen), selama omzet ≤ Rp 4,8 M/tahun.
- CV, Firma, PT non-perorangan, BUMDes: KELUAR dari skema 0,5% (tidak berhak lagi).
- Koperasi: tetap dapat 0,5%, tapi hanya 4 tahun pajak sejak terdaftar (tidak diubah dari PP 55/2022).
- OP omzet ≤ Rp 500 juta/tahun: bebas PPh final; bagian sampai 500 jt tidak kena, sisanya 0,5%. Badan TIDAK dapat fasilitas bebas 500 jt.
- Omzet > Rp 4,8 M: tidak eligible skema final.

## NPPN (Norma Penghitungan Penghasilan Neto)
- Untuk WP OP usaha/pekerjaan bebas yang TIDAK melakukan pembukuan. Laba = omzet × persentase norma (sesuai kode KLU & wilayah, acuan PER-17/PJ/2015; daftar lengkap di KPP).
- Syarat: omzet < Rp 4,8 M; wajib memberitahu KPP dalam 3 bulan sejak mulai usaha; konsisten dipakai 3 tahun.
- Alur: laba norma → dikurangi PTKP → tarif progresif Pasal 17.
- Badan usaha TIDAK bisa pakai norma (wajib pembukuan, Pasal 28 UU KUP).

## Pasal 31E (Badan, omzet ≤ Rp 50 M)
- Diskon 50% tarif (22% → efektif 11%) atas bagian PKP proporsional terhadap Rp 4,8 M pertama:
  `bagian = min(omzet, 4,8M) / omzet × laba`; `pajak = bagian × 22% × 50% + sisa_PKP × 22%`.

## Tarif Pasal 17 (UU HPP) & PTKP
- OP progresif: 5% (≤60 jt), 15% (60–250 jt), 25% (250–500 jt), 30% (500 jt–5 M), 35% (>5 M). PKP dibulatkan ribuan ke bawah (Pasal 17 ayat 4).
- Badan: flat 22%.
- PTKP: TK/0 54 jt, +4,5 jt per tanggungan (maks 3): TK/1 58,5 / TK/2 63 / TK/3 67,5; K/0 58,5 / K/1 63 / K/2 67,5 / K/3 72; K/I/0 112,5 / K/I/1 117 / K/I/2 121,5 / K/I/3 126.

## Audit kalkulator pajak berbasis JS (metode)
1. Ambil halaman `/`, cari `<script src="/assets/index-*.js">` (bundle loader).
2. Dalam loader, cari `import('./routes-*.js')` → unduh bundle routes.
3. Baca konstanta & fungsi kalkulasi langsung dari bundle (pola yang terlihat: `i=.005` tarif final, `a=48e8` batas 4,8 M, `o=5e8` bebas 500 jt, `s=.22` tarif badan, `c={...}` PTKP, `l=[...]` lapisan Pasal 17).
4. Bandingkan logika dengan aturan resmi di atas; jangan percaya deskripsi UI. Contoh audit tuntas: `references/audit-tax-calculator.md`.

## Pitfalls
- Koperasi sering disajikan permanen oleh tools, padahal hanya 4 tahun pajak.
- Skema "NPPN (Badan)" tidak legal (badan wajib pembukuan) — tolak/soroti saat muncul di tools.
- PKP tanpa pembulatan ribuan ke bawah = selisih kecil tapi tidak presisi.
- Database norma NPPN di tools sering cuma 12 kode KLU (PER-17/PJ/2015 memuat ratusan) — user input manual rawan salah persentase.
- Selalu akhiri dengan catatan: simulasi ≠ konsultasi resmi KPP/konsultan pajak.

## Support files
- `references/audit-tax-calculator.md` — temuan audit kalkulator pajak (tax-calculator-1-2.lovable.app): apa yang benar & belum tepat.
