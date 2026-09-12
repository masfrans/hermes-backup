# Jobstreet (id.jobstreet.com) scraping recipe — verified Aug 2026

All requests need `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36` and
`Accept-Language: id-ID,id;q=0.9`. The job search API endpoint (`/api/jobsearch/v5/search`)
returns AU jobs without site-specific params — do NOT use it; parse the embedded state instead.

## List page
- URL: `https://www.jobstreet.co.id/id/<keywords>-jobs` (e.g. `/id/hr-recruitment-jobs`,
  `/id/human-resource-jobs`). Returns ~1MB HTML.
- The data lives in a `window.SEEK_REDUX_DATA = {...}` script tag.
- Extract the JSON: find the marker `"results":{"isLoading":false,"isZeroResults":false`,
  backtrack to the LAST `=` before it, then brace-match with a depth counter that skips
  `"..."` string literals and `\"` escapes. `json.loads` the whole object.
- Jobs array: `data["results"]["results"]["jobs"]`. Each item has:
  - `id`, `title`, `companyName`, `locations[0].label`, `listingDateDisplay` (e.g. "4 hari yang lalu"),
    `salaryLabel` (e.g. "Rp 6.000.000 – Rp 8.000.000 per month"), `teaser`.
  - 30 jobs per page. `data["results"]["jobIds"]` lists ids for a quick count check.
  - Related-search suggestions at `data["results"]["relatedSearches"]` (keywords + totalJobs).

## Detail page (experience verification)
- URL format: `https://id.jobstreet.com/id/job/<id>?type=standard`.
  **NEVER use `/id/jobs/<id>`** — it serves a generic search page; naive text extraction then
  picks up the same unrelated sidebar ads (SPECTRUM UniTec, IPH SCHOOLS boilerplate) on every id.
- Same SEEK_REDUX_DATA extraction. The job object is at `data["jobdetails"]["result"]["job"]`:
  - description HTML: `job["content2"]` (fallback `job["content"]`) — strip tags, unescape,
    then regex experience: `[^.]{0,70}(?:pengalaman|experience|tahun)[^.]{0,150}\.`
  - salary: `job["salary"]["label"]`; company: `job["advertiser"]["description"]` (often null —
    take `companyName` from the list page instead).
- Titles alone are not enough: verify the requirement text (e.g. "minimal 1–2 tahun" vs
  "minimal 3–5 tahun" vs "5 years") before recommending.

## Verified examples
- HR & RECRUITMENT STAFF @ Zhengan Indonesia (job 93935155) — "Berpengalaman minimal 1–2 tahun di bidang Recruitment/HR".
- Rekrutment Staff @ Diamas Star (93996234) — "minimal 1–2 tahun dalam recruitment", gaji 4–5,5 jt.
- HR Recruitment Specialist @ Kekal Abadi Packindo (93935062) — "minimal 2 tahun di bidang Recruitment/HR".
- Recruitment & Training Staff @ Minebea AccessSolutions (93790870) — "minimal 1 tahun ... di perusahaan manufaktur otomotif".
