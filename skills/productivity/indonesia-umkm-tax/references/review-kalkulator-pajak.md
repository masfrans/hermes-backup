# Jebakan PP 20/2026 di Kalkulator UMKM + Teknik Review (teruji 2026-08)

Dari review kalkulator pajak BelajarLagi v4 → v5 terhadap materi kelas Mediawan Cesarian Syah. 4 gap yang ditemukan, 6 test case yang lolos, dan cara testing logika JS.

## 4 Gap yang Harus Dicek Saat Review Kalkulator UMKM

1. **Pasal 57(2)b — PT Perorangan profesi**: kalkulator sering anggap SEMUA "Perseroan Perorangan" bisa final 0,5%. SALAH: PT Perorangan milik pemilik keahlian khusus yang menyerahkan jasa sejenis pekerjaan bebas (dokter, konsultan, kreator/influencer, akuntan, pengacara) DICABUT dari final. Kalkulator butuh 2 checkbox: `ahliKhusus` + `jasaPekerjaanBebas`; keduanya dicentang → canUseFinal = false, beralih ke neto progresif Pasal 17.
2. **Pasal 58 — omzet gabungan keluarga (anti pecah usaha)**: kalkulator sering cuma hitung omzet tunggal. Harusnya uji GABUNGAN suami+istri+semua PT perorangan terhadap 4,8 M; kalau lewat, SEMUA entitas kehilangan fasilitas tahun berikutnya. Perlu input `omzetPasangan` + `omzetPTLain`.
3. **Pasal II — masa transisi**: kalkulator sering langsung bilang CV/Firma/PT/BUMDes "tidak berlaku". SALAH: yang terdaftar SEBELUM 22 Apr 2026 masih dapat final s.d. jangka waktu PP 55/2022 berakhir (CV/Firma 4 TP, PT/BUMDes 3 TP sejak terdaftar). Perlu input `tglTerdaftar` (type=month) + hitung sisa tahun pajak.
4. **Referensi NPPN**: PMK 15/2018 usang sebagai aturan pelaksanaan → yang benar **PMK 81/PMK.03/2024** (berlaku 1 Jan 2025).

## Test Case (dari latihan kelas 02 Mediawan) — semua lolos setelah patch

| # | Profil | Expected | Hasil |
|---|---|---|---|
| A | Bu Rina, OP warung, omzet 2,4M | Bisa final: (2,4M−500jt)×0,5% = 9,5jt | ✅ |
| B | PT Sinar Abadi, terdaftar 2025-03, omzet 3,1M | Bisa via masa transisi PT 3 TP, sisa ±2 TP | ✅ |
| C | Pak Doni PT Perorangan 2M + istri 3,2M = 5,2M | TIDAK bisa (Pasal 58 gabungan) | ✅ |
| D | drg. Sari, OP dokter gigi mandiri, 1,8M | Bisa final 6,5jt | ✅ |
| E | CV Berkah Jaya, terdaftar 2026-01, omzet 4,2M | Bisa via transisi CV 4 TP | ✅ |
| F | PT Digital Kreatif (konsultan IT), ahli khusus + jasa bebas | TIDAK bisa (Pasal 57(2)b) | ✅ |

## Teknik Testing Logika JS Kalkulator (Node vm)

`const` di eval/vm TIDAK ter-expose ke global — harus ekspor eksplisit:

```js
const vm = require('vm'); const fs = require('fs');
let js = fs.readFileSync('calc.js', 'utf8');
js = js.replace(/initApp\(\);/, '');              // potong init DOM
js += "\n;globalThis.__state = state; globalThis.__calcAll = calcAll;";
// stub document/window minimal (getElementById kembalikan objek dgn innerHTML setter)
const sandbox = { document: {...}, console, Date, Math, ... };
vm.createContext(sandbox); vm.runInContext(js, sandbox);
const state = sandbox.__state; const calcAll = sandbox.__calcAll;
```

Pitfalls:
- document mock harus kembalikan objek dengan setter `innerHTML` (bukan null) atau renderPanel() crash
- **Reset state penuh di tiap test case** — Object.assign parsial bocor antar case (field tidak di-set dari case sebelumnya)
- Verifikasi syntax: `node --check file.js` + balance `{}` (dengan Python: `js.count('{') == js.count('}')`)
- Ekstrak script dari HTML: `re.findall(r'<script>(.*?)</script>', html, re.S)`

## Hasil Akhir
File `tax-planning-calculator-v5.html` (199 KB) disimpan di `/mnt/user-data/outputs/` — referensi implementasi lengkap (UI checkbox profesi, kartu omzet gabungan, input tanggal terdaftar, info masa transisi di panel PP 20/2026).
