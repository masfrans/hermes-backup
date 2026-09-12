---
name: apify-scraping
description: "Scrape Twitter/web via Apify API: actor run, dataset, hasil."
version: 1.0.0
platforms: [linux]
---

# Apify Scraping (via API)

Scraping Twitter/X atau web via platform Apify menggunakan actor siap pakai
(contoh `apidojo/tweet-scraper`). Alternatif MURAH untuk X API resmi (yang
berbayar $100+/bulan); terbukti di plan FREE (~0.004 USD/run, ~10 item).

## Trigger

- User minta scraping Twitter/X (update akun, keyword, trending)
- User minta "scraping dengan bantuan apify"
- X API resmi terlalu mahal; butuh hasil tweet tanpa developer plan

## Setup (sekali)

1. Token disimpan di `~/.hermes/.env`: `APIFY_API_TOKEN=apify_api_...`
2. Cek saldo/plan: `GET https://api.apify.com/v2/users/me?token=$TOKEN`
3. Cek actor tersedia: `GET https://api.apify.com/v2/acts/apidojo~tweet-scraper?token=$TOKEN`

## Alur yang terbukti (3 langkah)

### 1. Start run actor
```python
import urllib.request, json, re
TOKEN = re.search(r'APIFY_API_TOKEN=(\S+)', open('/root/.hermes/.env').read()).group(1)

# Scrape profil akun:
input_data = {"startUrls": [{"url": "https://x.com/AnthropicAI"}], "maxItems": 20, "sort": "Latest"}
# ATAU search keyword lintas akun:
input_data = {"searchTerms": ["Claude Anthropic update"], "maxItems": 30, "sort": "Latest"}

req = urllib.request.Request(
    f"https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token={TOKEN}",
    data=json.dumps(input_data).encode(), headers={"Content-Type": "application/json"})
resp = json.loads(urllib.request.urlopen(req, timeout=60).read())
run_id = resp['data']['id']  # status awal: READY
```

### 2. Poll status + AMBIL defaultDatasetId
```python
req = urllib.request.Request(f"https://api.apify.com/v2/actor-runs/{run_id}?token={TOKEN}")
d = json.loads(urllib.request.urlopen(req, timeout=30).read())
data = d['data']
# status: READY -> RUNNING -> SUCCEEDED (poll tiap ~30-60s)
ds_id = data['defaultDatasetId']   # ⚠️ BUKAN run_id!
```

### 3. Fetch items dari dataset
```python
req = urllib.request.Request(f"https://api.apify.com/v2/datasets/{ds_id}/items?token={TOKEN}&format=json&limit=30")
items = json.loads(urllib.request.urlopen(req, timeout=30).read())
# Field tweet: full_text (atau text), created_at, like_count, retweet_count,
# author.userName (atau userName)
```

## PITFALL UTAMA (pernah kena)

- **Dataset ID ≠ Run ID.** Fetch items pakai `run_id` → error
  `{"error": {"type": "record-not-found", "message": "Dataset was not found"}}`.
  WAJIB ambil `defaultDatasetId` dari detail run dulu.
- **Batas plan FREE**: ~10 item per run (meski maxItems 20-30). Untuk lebih
  banyak, butuh plan berbayar / beberapa run.
- **`sort: "Latest"`** penting untuk tweet terbaru (default bisa relevansi).
- Akun user yang baru dibuat tidak punya actor sendiri; pakai actor publik
  milik user lain (apidojo) - lisensi/rate diatur Apify.
- Biaya per run kecil tapi real: cek `usageTotalUsd` di detail run.

## Format laporan ke user

Tampilkan per tweet: `[tanggal] @author: teks (130 char max)` + like/RT count.
Bedakan sumber: akun resmi vs akun lain (berita hangat sering dari akun
pihak ketiga). Tandai mana yang butuh verifikasi lanjut.

## Catatan

- `xurl` (skill hub) = X API resmi, butuh developer plan + OAuth; gunakan
  Apify kalau user tidak punya kredensial X API.
- Token Apify user disimpan di `.env` - jangan pernah tulis ulang nilainya.
