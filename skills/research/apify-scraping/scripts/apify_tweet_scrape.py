#!/usr/bin/env python3
"""Scrape tweet via Apify tweet-scraper - satu command lengkap.

Usage:
  python3 apify_tweet_scrape.py "https://x.com/AnthropicAI" [maxItems]
  python3 apify_tweet_scrape.py --search "Claude update" [maxItems]

Membaca APIFY_API_TOKEN dari ~/.hermes/.env. Output: tweet + like/RT ke stdout.
"""
import sys, json, re, time, urllib.request

def token():
    m = re.search(r'APIFY_API_TOKEN=(\S+)', open('/root/.hermes/.env').read())
    if not m:
        sys.exit("APIFY_API_TOKEN tidak ada di ~/.hermes/.env")
    return m.group(1)

def main():
    TOKEN = token()
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--search":
        input_data = {"searchTerms": [args[1]], "maxItems": int(args[2]) if len(args) > 2 else 20, "sort": "Latest"}
    else:
        input_data = {"startUrls": [{"url": args[0]}], "maxItems": int(args[1]) if len(args) > 1 else 20, "sort": "Latest"}

    # 1. Start run
    req = urllib.request.Request(
        f"https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token={TOKEN}",
        data=json.dumps(input_data).encode(), headers={"Content-Type": "application/json"})
    run_id = json.loads(urllib.request.urlopen(req, timeout=60).read())['data']['id']
    print(f"RUN: {run_id} (polling...)")

    # 2. Poll sampai SUCCEEDED (max ~3 menit)
    ds_id = None
    for _ in range(18):
        time.sleep(10)
        req = urllib.request.Request(f"https://api.apify.com/v2/actor-runs/{run_id}?token={TOKEN}")
        d = json.loads(urllib.request.urlopen(req, timeout=30).read())['data']
        st = d.get('status')
        if st in ('SUCCEEDED', 'FAILED', 'TIMED-OUT', 'ABORTED'):
            print(f"Status: {st} | kredit: {d.get('usageTotalUsd')}")
            ds_id = d.get('defaultDatasetId')
            break
    if not ds_id:
        sys.exit("Run tidak selesai dalam waktu tunggu - cek console.apify.com")

    # 3. Fetch items
    req = urllib.request.Request(f"https://api.apify.com/v2/datasets/{ds_id}/items?token={TOKEN}&format=json&limit=50")
    items = json.loads(urllib.request.urlopen(req, timeout=30).read())
    print(f"Total tweet: {len(items)}\n" + "=" * 60)
    for i, t in enumerate(items, 1):
        text = t.get('full_text') or t.get('text') or ''
        author = t.get('author', {}).get('userName') or t.get('userName') or '?'
        date = str(t.get('created_at', ''))[:16]
        print(f"{i}. [{date}] @{author}: {' '.join(text.split())[:130]}")
        print(f"   Likes: {t.get('like_count', 0)} | RT: {t.get('retweet_count', 0)}\n")

if __name__ == '__main__':
    main()
