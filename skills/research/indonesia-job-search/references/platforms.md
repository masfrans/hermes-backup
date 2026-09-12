# Per-platform scraping recipes (verified Aug 2026)

All requests need header `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`.
`web_extract` may be unavailable (ddgs backend is search-only) — use urllib/curl directly.

## Kalibrr
- List page: `https://www.kalibrr.com/home/i/<category>` (e.g. `human-resources`).
- Job links: `re.findall(r'href="(/c/[^"]*/jobs/[^"]*)"', html)` — filter out links containing `source=` or ending `/jobs?`.
- Full link: `https://www.kalibrr.com` + path.
- Detail page experience: strip `<script>...</script>` and `<style>...</style>` first, then regex the visible text:
  - `[^.]{0,50}(?:pengalaman|experience|kualifikasi|qualification)[^.]{0,120}\.`
  - year ranges: `(\d+\s*[-–]\s*\d+\s*(?:tahun|years?))`
- `application/ld+json` JobPosting blocks exist but `experienceRequirements` is usually empty — don't rely on it.
- Example verified: Recruitment HR Generalist @ PT Hades Guna Sehati — "pengalaman minimal 2 tahun sebagai HR Recruitment atau HR Generalist".

## Uploker
- Detail URL: `https://uploker.com/lowongan-kerja/<slug>`.
- Page embeds full JSON-LD `JobPosting` (single script tag) with:
  - `minExperienceYears` / `maxExperienceYears`
  - `baseSalary.value.minValue/maxValue` (IDR/month)
  - `hiringOrganization.name`, `jobLocation.address.addressLocality`
  - `applyEmail`
- The visible description also works: `bodyHtml` in the embedded `$R` state contains `\x3C`-escaped HTML (unescape with `\x3C` -> `<`).
- Example verified: HR Recruitment Staff @ PT Mitra Teknindo Sejati — minExperienceYears 1, max 3, gaji 4.5-5 jt.

## Jora (id.jora.com)
- List page: `https://id.jora.com/lowongan-<query>`.
- Each job card has `data-braze-job-panel-view="{JSON}"` with `job_id`, `job_title`, `location`, `company_name` — parse with `json.loads(html.unescape(...))`.
- **Detail links are JS-built — NOT extractable.** `/j/<id>` returns 404, `/job/<id>` returns 403. Do not probe. Give the listing page URL and let the user click through.
- Duplicates appear in the card list (same job id repeated) — dedupe by `job_id`.

## Glints
- Deep links `https://glints.com/id/opportunities/jobs/<title>/<uuid>` are best captured from `web_search` results — the explore pages are JS-heavy and don't expose links in raw HTML.
- Search operator: `site:glints.com/id/opportunities/jobs "HR Recruitment"` or `loker <posisi> <kota>`.
- Search snippets often include experience range directly (e.g. "Pengalaman 1 - 3 tahun") — capture it before opening the page.

## General notes
- BUMN/company career portals (Pertamina, TNI) are separate sites — search `site:rekrutmen-*` or the company career page.
- Filter out internships (`magang`, `internship`, `intern`) when the user asks for 1-3 tahun pengalaman.
