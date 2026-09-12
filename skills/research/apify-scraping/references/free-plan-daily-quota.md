# Apify Plan FREE: Quota Harian Habis (Sesi Riset Claude, Agustus 2026)

## Gejala

Setelah ±3-5 run sukses per hari, SEMUA run berikutnya balik
`{"noResults": true}` — TERMASUK scrape per-akun (startUrls) yang
sebelumnya berhasil dengan input IDENTIK.

Urutan gejala yang diamati di sesi nyata:
1. Run #1 (startUrls @AnthropicAI) → ✅ 10 tweet (MHS, alignment)
2. Run #2 (searchTerms "Claude Anthropic update") → ✅ 10 tweet (Sony, Claudeforce)
3. Run #3-5 (multi-topik) → ⚠️ berhasil tapi hasil tidak relevan
4. Run #6+ (keyword "Claude" murni) → ❌ noResults
5. Run #7-8 (keyword panjang, akun lain, ULANG @AnthropicAI) → ❌ semua noResults

## Diagnosis

Ini BUKAN masalah akun/keyword/script — ini KUOTA HARIAN PLAN FREE HABIS.
Plan FREE Apify membatasi jumlah run aktor per hari (±3-5). Setelah itu
semua request dijawab noResults tanpa error.

## Yang TIDAK boleh dilakukan

- Jangan retry membabi buta (buang waktu, tidak akan berhasil sampai reset)
- Jangan salahkan akun target ("akun tidak aktif") — @ClaudeAI dan @AnthropicAI
  sama-sama noResults, padahal @AnthropicAI sukses di run pertama hari yang sama

## Yang dilakukan

1. Laporkan ke user: kuota harian Apify habis (bukan kegagalan teknis)
2. Tawarkan opsi:
   a. Tunggu reset kuota (±24 jam) lalu lanjut scraping
   b. Upgrade plan Apify (mulai ~$5) untuk kuota lebih besar
   c. Gunakan sumber resmi lain (mis. anthropic.com/news, status.claude.com)
3. Data yang sudah terkumpul hari itu TETAP valid — simpan & pakai dulu
   (contoh: 2 run pertama sudah menghasilkan data konten yang cukup)

## Cek kuota sebelum mulai

Sebelum sesi scraping besar, cek dulu apakah masih ada kuota:
- Jalankan 1 run kecil uji coba dulu (maxItems 5) — kalau noResults langsung,
  berarti kuota habis, jangan lanjutkan batch.
- Alternatif: pantau usage di console Apify (Usage → Actor runs).
