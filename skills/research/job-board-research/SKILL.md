---
name: job-board-research
description: "Indonesian job board vacancy research with verified dates."
version: 1.0.0
platforms: [linux]
---

# Job Board Research (Indonesia)

Find and verify job vacancies on Indonesian job boards (Jobstreet, Kalibrr, Glints, Kitalulus, Uploker). User's recurring use case: HR/Recruitment vacancies, filtered by experience (e.g. 1-3 years) and recency (e.g. posted in last 7 days).

## When to use
- User asks "cari lowongan X terbaru N" / "loker HR terbaru" / "carikan info lowongan ... beserta linknya"
- Any request for job listings in Indonesia with filters (experience, location, recency)

## Workflow
1. **Web search for leads** — search title + platform site: filters to find candidate URLs.
2. **NEVER trust search-result descriptions.** Snippets show "1-3 tahun pengalaman" and "Full time" even when the job is CLOSED months ago. Always verify on the platform page itself.
3. **Fetch each platform page and extract structured data** (see per-platform quirks below).
4. **Filter**: active (not closed), experience matches, posted within the requested window.
5. **Deliver**: title, company, location, posted date, experience requirement, direct link.

## Platform quirks

### Jobstreet (id.jobstreet.com) — best source, has real dates
- Category listing pages: `https://id.jobstreet.com/hr-recruitment-jobs` (pattern: `<category>-jobs`)
- Job links: `/job/<numeric-id>` — strip query params (`?type=standard&ref=...`)
- **Reliable dates in page JSON**: `"id":"<jobid>".{0,200}?"listingDate":"<ISO>".{0,60}?"listingDateDisplay":"2d ago"` — `listingDateDisplay` gives "2d ago", "3h ago", etc.
- Higher job IDs (93xxxxxx+) = more recent postings.
- Card text is in `<article>` blocks; titles contain HTML entities (`&amp;`) — `html.unescape`.
- When extracting title/company near a job ID via context window, titles can misalign with IDs; cross-check against the `<article>` block text.

### Kalibrr (kalibrr.com)
- URL pattern: `/c/<company-slug>/jobs/<numeric-id>/<job-slug>`
- Experience requirement in page text: regex `[^.]{0,30}(?:pengalaman|experience)[^.]{0,100}\.`
- JSON-LD JobPosting sometimes present, sometimes absent — fall back to text scan.

### Glints (glints.com) — MUST check closed status
- Detail pages embed `__NEXT_DATA__` JSON with `createdAt`, `updatedAt`, `closedAt`.
- **Many search-indexed Glints jobs are CLOSED** (dates 2018-2025). If `closedAt` is present, the job is dead — exclude it.
- Dates: regex `"(createdAt|updatedAt|closedAt)"\s*:\s*"([^"]+)"`.
- API `/api/jobs?keyword=X&country=ID` returns stale/random data (old listings, empty slugs) — not reliable for fresh results. Rate-limits fast (403); add delay between calls.
- Job listing data renders client-side; the explore page's `__NEXT_DATA__` holds i18n/location data, not the job list.

### Kitalulus (kitalulus.com)
- URL: `/lowongan/detail/<slug>`
- JSON-LD `datePosted` + visible text "X hari yang lalu".
- Note: "X hari yang lalu" can mean UPDATED, not posted — check `datePosted` too.

### Uploker (uploker.com)
- Full job JSON embedded in page: `title`, `minSalary/maxSalary`, `minExperienceYears/maxExperienceYears`, `applyEmail`, `workMode`, `createdAt` — extract via regex, great for experience-range filtering.
- `datePosted` also in JSON-LD.

### Jora (id.jora.com) — AVOID
- Closing down in Indonesia. Job detail links are built client-side (unfetchable); only category URLs work. Use only as last resort.

## Pitfalls
- Search snippets are stale — always verify status on the page.
- "X hari yang lalu" ≠ posted date when a job is re-listed; prefer `datePosted`/`listingDate`.
- Job pages 403 on rapid repeat fetches (Glints especially) — add `sleep` between requests and use a full Chrome user-agent.
- Job title/company regexes over context windows can grab the WRONG nearby job's data — verify against the card block.

## Verification
- Cross-check the same job on 2+ platforms when possible.
- Confirm active: no `closedAt`, status active, or listing within window.
- Report posted date + experience requirement alongside each link so the user can trust the list.

## Support files
- `scripts/extract_jobstreet.py` — fetch a Jobstreet category page and dump title/company/listingDate/link for all jobs.
