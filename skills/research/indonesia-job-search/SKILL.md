---
name: indonesia-job-search
description: "Find Indonesian job listings (loker) with working links."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [loker, indonesia, jobs, recruitment, scraping]
    related_skills: [web-search, web-extract]
---

# Indonesian Job Search (Loker)

Find the latest job vacancies in Indonesia (user's focus: HR / recruitment positions) with working per-job links, filtered by experience years (e.g. 1-3 tahun).

## Workflow

1. **Clarify the target**: position (e.g. "HR Recruitment"), experience range (e.g. 1-3 tahun), city, "terbaru N saja".
2. **Search first, scrape second**:
   - `web_search` with `site:` operators: `site:kalibrr.com`, `site:glints.com`, `site:uploker.com`, plus `lowongan ... 2026 pengalaman "1-3 tahun"`.
   - Glints deep links (`glints.com/id/opportunities/jobs/<title>/<uuid>`) come straight from search results — capture them there, the page is JS-heavy.
3. **Scrape list pages with urllib** (browser UA header required; `web_extract` often unavailable since ddgs backend is search-only). See `references/platforms.md` for per-platform extraction recipes.
4. **Verify experience requirements per job** by fetching the detail page and regexing for `pengalaman`/`experience` sentences and `\d+\s*[-–]\s*\d+\s*(tahun|years)` — titles alone are not enough (intern vs staff vs manager).
5. **Deliver**: numbered list, each entry = position | company | city | experience requirement | link. User wants 10 terbaru with links.

## Pitfalls
- **Jora detail links are JS-built** — you can extract titles/company/city from `data-braze-job-panel-view` JSON on the list page, but NOT deep links. Give the listing page URL instead of probing `/j/<id>` (404/403).
- Kalibrr list page needs `Mozilla/5.0` UA; job links match `href="(/c/<company>/jobs/<id>/<slug>)"` — filter out `/jobs?source=...` query links.
- Kalibrr detail pages: strip `<script>/<style>` before regexing; experience often only in "Minimum Qualifications" section; `experienceRequirements` JSON-LD is frequently empty.
- Uploker detail pages embed full JSON-LD `JobPosting` incl. `minExperienceYears`/`maxExperienceYears`/`baseSalary` — parse it for the experience filter.
- Exclude internships/magang when the user asks for 1-3 tahun experience.
- Reply in Bahasa Indonesia; user (Ibramsyah) wants concise results with links, no long narrative.

## Support files
- `references/platforms.md` — per-platform scraping recipes (Kalibrr, Jora, Uploker, Glints).
