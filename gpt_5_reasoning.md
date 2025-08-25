# O Kae — Ideas TODO Checklist
Date: 2025-08-25

This checklist tracks enhancements to the O Kae Web UI and CLI.

Paths referenced:
- Backend: `app.py`
- Templates: `templates/index.html`, `templates/base.html`
- Styles: `static/styles.css`
- CLI: `okae.py`
- Docs: `README.md`, `NOTICE.md`

## Quick wins (≤1–2h)
- [ ] Copy-to-clipboard buttons for all results
  - [ ] Add small icons in `templates/index.html`
  - [ ] JS: `navigator.clipboard.writeText(...)`
- [ ] IP map preview (Leaflet)
  - [ ] Include Leaflet CSS/JS in `templates/index.html`
  - [ ] Render map when `ip_data.latitude/longitude` present
  - [ ] Style map height in `static/styles.css`
- [ ] Country flag + ASN badge on IP results
  - [ ] Render `flag.emoji` and `connection.asn` in `templates/index.html`
- [ ] Result export (JSON/CSV)
  - [ ] “Download JSON/Copy JSON” buttons per tool
  - [ ] Optional: `/export/*` routes in `app.py`
- [ ] Pre-filled queries via URL params
  - [ ] Support `/?ip=...`, `/?phone=...`, `/?username=...` in `index()` (`app.py`)
- [ ] Dark/light theme toggle
  - [ ] CSS variables in `static/styles.css`, toggle in `templates/base.html` with localStorage

## Medium (half‑day)
- [ ] Parallel username checks
  - [ ] Use `concurrent.futures.ThreadPoolExecutor` in `track_username()` (`app.py`)
  - [ ] Respect timeouts and headers; limit threads
- [ ] Rate limiting & caching
  - [ ] Add `flask-limiter` for routes
  - [ ] Add `requests-cache` for IP/username calls
  - [ ] Update `requirements.txt`
- [ ] Bulk username mode
  - [ ] Multiline input in UI; batched table result in `templates/index.html`
- [ ] Service health panel
  - [ ] Health route in `app.py` (ipwho.is, ipify, a few socials)
  - [ ] Small widget in `templates/base.html`
- [ ] Investigation notebook (right drawer)
  - [ ] Pin artifacts (IP/phone/usernames) with notes; export JSON/MD

## Advanced (1–2 days)
- [ ] WHOIS / Reverse DNS / ASN details
  - [ ] WHOIS for IP/Domain; reverse DNS; enrich ASN (org, range)
- [ ] Breach check (opt‑in API key)
  - [ ] Integrate HaveIBeenPwned (email/username) using env var key
  - [ ] Add `.env.example`, document in `README.md`
- [ ] Case files (simple persistence)
  - [ ] Store cases under `cases/` as JSON with timestamps and artifacts
  - [ ] Load/save UI
- [ ] Internationalization (Setswana/English)
  - [ ] String dicts/Jinja; optional `flask-babel`
- [ ] Render.com productionization
  - [ ] Add `gunicorn`, `Procfile`
  - [ ] Set `FLASK_DEBUG=0` in production
  - [ ] Deployment docs and troubleshooting

## Visual polish
- [ ] Setswana microcopy (with English tooltips) in `templates/*.html`
- [ ] Loading spinners + success/fail badges; subtle row highlights

## Security & Solo-dev quality
- [ ] `.env.example` with keys (gitignored `.env` already in `.gitignore`)
- [ ] Structured logging (no sensitive output)
  - [ ] Env-controlled log level and format
- [ ] Document rate limits and responsible use in `README.md`

## Repo/ops (optional)
- [ ] Rename GitHub repo to `okae`
  - [ ] Update local remote: `git remote set-url origin https://github.com/<your-username>/okae.git`
- [ ] Add CI pre-commit or linting later (optional)

## Top picks to implement next
- [ ] Leaflet map on IP results
- [ ] Parallel username checks

## Commit message templates
- chore(ui): add Leaflet map preview for IP lookups
- feat(username): parallelize social checks with ThreadPoolExecutor
- feat(export): add JSON export and copy buttons for results
- feat(theme): add dark/light toggle via CSS variables
- perf(cache): add requests-cache + rate limiting
