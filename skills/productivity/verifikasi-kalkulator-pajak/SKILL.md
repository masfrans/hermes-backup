---
name: verifikasi-kalkulator-pajak
description: "Verifikasi kalkulator pajak UMKM vs PP 20/2026."
version: 1.0.0
platforms: [linux]
---

# Verifikasi Kalkulator Pajak (PP 20/2026)

Checklist & teknik untuk memverifikasi kalkulator/simulator pajak UMKM (single-file HTML, Lovable/Replit, dll) terhadap aturan PP 20/2026. Dipakai saat user minta review/perbaikan kalkulator pajak, atau membandingkan tools pajak dengan materi perpajakan terbaru. Komplemen skill `pajak-indonesia` (materi pajak) — skill ini soal PROSES verifikasi tool-nya.

## Trigger
- User kirim file kalkulator pajak (HTML/JS) dan minta "cek apakah sudah sesuai aturan"
- User minta perbaiki logika pajak di tools buatan Lovable/Replit
- User minta verifikasi angka perhitungan pajak terhadap materi kelas

## Checklist 5 Koreksi PP 20/2026 (yang paling sering salah)

### 1. Pasal 56(4) - Pekerjaan Bebas OP (paling sering terlewat!)
- OP yang usahanya **pekerjaan bebas/profesi** (dokter, akuntan, pengacara, konsultan, notaris, kreator/influencer, seniman, dll) TIDAK bisa pakai final 0,5%
- Bukan aturan baru — sejak PP 46/2013; PP 20/2026 hanya menegaskan
- Kalkulator harus punya input "pekerjaan bebas" untuk subjek OP (atau deteksi otomatis dari KLU profesi)
- Test case: drg. Sari praktik dokter gigi mandiri omzet 1,8M → HARUS ditolak final (arahkan ke NPPN/Pasal 17)

### 2. Pasal 57(2)b - PT Perorangan Profesi (jebakan baru)
- PT Perorangan milik pemilik **keahlian khusus** yang menyerahkan **jasa sejenis pekerjaan bebas** → TIDAK bisa final 0,5%
- Uji fiskus: "keahlian khusus" + "jasa sejenis" (nilai jasa melekat pada orangnya vs organisasinya)
- Butuh 2 checkbox: ahli khusus + jasa pekerjaan bebas
- Test: konsultan IT dengan PT Perorangan omzet 2,6M → HARUS ditolak

### 3. Pasal 58 - Omzet Gabungan Keluarga (anti pecah usaha)
- Omzet diuji **GABUNGAN**: suami + istri + seluruh PT perorangan keluarga
- Gabungan > 4,8M → SEMUA entitas kehilangan fasilitas tahun berikutnya (tanpa pilih entitas)
- Butuh input omzet pasangan + omzet PT perorangan lain
- Test: Pak A PT Perorangan 2M + istri 3,2M = 5,2M → keduanya HARUS ditolak

### 4. Pasal II - Masa Transisi Badan Non-Subjek
- CV/Firma/PT/BUMDes **terdaftar SEBELUM 22 Apr 2026** masih bisa final s.d. jangka waktu PP 55/2022 berakhir: CV/Firma 4 TP, PT/BUMDes 3 TP
- Terdaftar SETELAH 22 Apr 2026 → tidak ada masa transisi
- Butuh input "tanggal terdaftar" (type=month) untuk badan non-subjek
- Jangan langsung bilang "tidak berlaku" tanpa nuansa masa transisi!
- Koperasi: tetap 4 TP sejak terdaftar; OP/PT Perorangan: tanpa batas waktu

### 5. Referensi & angka dasar yang sering outdated
- PMK 15/2018 SUDAH DIGANTI **PMK 81/2024** (berlaku 1 Jan 2025) untuk NPPN
- 10 kota kelompok 1 = Medan, Palembang, Jakarta, Bandung, Semarang, Surabaya, Denpasar, Manado, Makassar, **Pontianak** (BUKAN Batam!)
- Jumlah kelompok KLU NPPN: **1.435** (sumber Ortax/DDTC)
- Ambang PKP 4,8M TIDAK berubah (wacana 3,6M dibantah DJP, PMK-197/2013 tetap)

## Yang biasanya SUDAH benar (jangan rombak)
- Tarif 0,5%, batas 4,8M, bebas 500jt pertama OP (Pasal 60(2) PP 55/2022)
- PTKP 12 status (TK/K/K-I), bracket Pasal 17 (5–35% / 22% badan)
- Rumus Pasal 31E: (4,8M/omzet) × PKP dapat diskon 50% dari 22%
- Pembulatan PKP ribuan ke bawah (Pasal 17 ayat 4)
- Angka terverifikasi: 31E omzet 10M laba 1M = 167,2jt; 25M = 198,88jt; OP laba 1M K/1 = 225,1jt (PKP 937jt); final OP 600jt = 500rb; PT Perorangan 2M = 10jt

## Teknik Test Kalkulator HTML (Node vm, tanpa browser)

```javascript
const fs = require('fs'), vm = require('vm');
let js = fs.readFileSync('kalkulator.html','utf8').match(/<script>([\s\S]*)<\/script>/)[1];
js = js.replace(/initApp\(\);/, '');                    // buang panggilan DOM
js += ';globalThis.__state = state; globalThis.__calcAll = calcAll;'; // export const
const fakeEl = {className:'',innerHTML:'',value:'',setAttribute(){},addEventListener(){},appendChild(){},focus(){},style:{}};
const sandbox = {document:{getElementById:()=>fakeEl,createElement:()=>({className:'',setAttribute(){},addEventListener(){},appendChild(){},style:{}}),activeElement:null},window:null,console,Date,Math,Number,String,Object,Array,RegExp,parseInt,parseFloat,isNaN,Infinity,JSON};
sandbox.window = sandbox;
vm.createContext(sandbox);
vm.runInContext(js, sandbox);
const state = sandbox.__state, calcAll = sandbox.__calcAll;
```

## Pitfalls (teknik test)
- **`const` di eval/vm TIDAK ter-expose ke global** — wajib export via `globalThis.__x = x` di akhir script
- **State bocor antar test case** — `Object.assign(state, {...reset penuh...})` SEBELUM tiap kasus; omzet pasangan dari kasus sebelumnya bisa mencemari kasus berikutnya
- **Regex `detect_sections`**: key hasil match bisa "work experience" yang TIDAK ada di mapping kondisi → section jatuh ke "lainnya". Kalau bullets 0 padahal CV punya pengalaman, cek mapping key
- Verifikasi syntax: ekstrak semua `<script>` blocks → gabung → `node --check file.js` + cek balance kurung kurawal (diff harus 0)

## Alur Kerja
1. Baca file kalkulator (HTML/JS) — fokus di bagian constants, state, calc engine
2. Jalankan checklist 5 koreksi di atas terhadap logika
3. Buat test cases dari materi kelas (kasus latihan: Bu Rina OP warung, PT Sinar Abadi, Pak Doni gabungan, drg. Sari profesi, CV Berkah Jaya transisi, PT Digital Kreatif konsultan)
4. Verifikasi angka vs materi (31E, Pasal 17, final 0,5%)
5. Kalau user minta perbaikan: patch HTML, test ulang, kirim file hasil
6. Saran UI: tab Panduan sebaiknya di paling kiri & jadi activeTab default (orang awam pajak butuh panduan dulu)
