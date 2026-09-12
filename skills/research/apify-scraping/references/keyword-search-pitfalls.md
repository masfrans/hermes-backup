# Keyword Search Twitter via Apify — Pelajaran Teruji (Sesi Riset Claude)

Semua temuan ini berasal dari sesi scraping nyata (riset update Claude, Agustus 2026).
Lampiran untuk SKILL.md `apify-scraping` — bagian "Pitfall Keyword Search".

## 1. Keyword pendek/umum → noResults (plan FREE)

Yang diuji dan SEMUA balas `{"noResults": true}`:
- "Claude"
- "Claude AI"
- "Anthropic"
- "Claude Code"

Search Twitter menganggap query terlalu broad di plan FREE. Jangan buang run
untuk keyword 1-2 kata umum.

## 2. Yang TERBUKTI menghasilkan tweet

- **Scrape per akun** via `startUrls`: `{"startUrls": [{"url": "https://x.com/AnthropicAI"}], "maxItems": 20}` → ✅ 10 tweet
- **Keyword panjang multi-kata spesifik**: `{"searchTerms": ["Claude Anthropic update"]}` → ✅ 10 tweet

Pola: query yang mengandung ≥2 kata kunci spesifik (nama produk + kata kerja/
konteks) lolos; query umum tidak.

## 3. Keyword multi-kata bisa BOCOR ke topik tidak relevan

`"Claude marketing OR sales"` → hasilnya tweet politik, crypto, dan random
lainnya. Kata "Claude" diabaikan search engine; hanya "marketing OR sales"
yang efektif. Solusi: gunakan kombinasi yang PASTI menunjuk subjek, misalnya
nama produk/model/integrasi: "Claude Code", "Claudeforce", "Opus 5",
"Claude small business".

## 4. Filter relevansi pasca-scrape (WAJIB)

Setiap hasil scraped harus difilter dengan substring keyword sebelum dipakai:
```python
low = text.lower()
if any(k in low for k in ['anthropic', 'claude code', 'opus', 'sonnet',
                          'claudeforce', 'claude ai', 'mcp', 'artifact',
                          'cowork', 'haiku']):
    relevan.append(...)
```
Tanpa filter ini, tweet tentang nama orang "Claude" atau kata sama lainnya
akan mencemari hasil.

## 5. Alur kerja yang benar untuk riset konten

1. Jalankan beberapa run paralel (beda topik) → simpan run IDs ke JSON
2. Poll sampai SUCCEEDED (ambil `defaultDatasetId`)
3. Fetch items → SIMPAN MENTAH ke JSON dulu (jangan langsung difilter)
4. Filter relevansi → baru rangkum untuk user
5. Tandai sumber: akun resmi vs pihak ketiga (berita hangat sering dari pihak
   ketiga); tandai mana yang perlu verifikasi lanjut
