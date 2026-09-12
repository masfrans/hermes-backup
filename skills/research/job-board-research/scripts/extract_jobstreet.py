#!/usr/bin/env python3
"""Fetch a Jobstreet Indonesia category page and dump jobs with real listing dates.

Usage: python3 extract_jobstreet.py [category-url]
Default: https://id.jobstreet.com/hr-recruitment-jobs

Output: one line per job -> title | company | listingDate (ISO) | display | link
Verified working: prints listingDateDisplay ("2d ago", "3h ago") which Google
search snippets never show. Always verify job status on the page — search
descriptions are stale and often show closed jobs as active.
"""
import sys, re, html, urllib.request

URL = sys.argv[1] if len(sys.argv) > 1 else "https://id.jobstreet.com/hr-recruitment-jobs"

def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    })
    return urllib.request.urlopen(req, timeout=25).read().decode("utf-8", errors="replace")

c = fetch(URL)

# Job entries: id + listingDate + listingDateDisplay live near each other in page JSON
jobs = []
for m in re.finditer(r'"id":"(\d+)".{0,200}?"listingDate":"([^"]+)"[^}]*?"listingDateDisplay":"([^"]+)"', c):
    jid, iso, disp = m.group(1), m.group(2), m.group(3)
    # title/company from the <article> card block containing this job id
    idx = c.find(f'"{jid}"')
    seg = c[max(0, idx - 3000):idx]
    tm = re.findall(r'"title":"([^"]+)"', seg)
    cm = re.findall(r'"companyName":"([^"]+)"', seg) or re.findall(r'"name":"([^"]+)"', seg)
    title = html.unescape(tm[-1]) if tm else "?"
    comp = html.unescape(cm[-1]) if cm else "?"
    jobs.append((title, comp, iso, disp, f"https://id.jobstreet.com/job/{jid}"))

print(f"Found {len(jobs)} jobs\n")
for title, comp, iso, disp, link in jobs:
    print(f"- {title[:42]} | {comp[:22]} | {iso[:10]} ({disp}) | {link}")
