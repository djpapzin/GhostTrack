# O Kae — Feature Roadmap & Checklist (gpt_5_reasoning)

Date: 2025-08-25
Context: Solo developer on Windows 10. Keep code self-documenting, with robust comments, logging, and README updates. No secrets in code; use environment variables and gitignore `.env`.

## Completed (baseline)
- [x] Rebrand UI/UX to O Kae (templates, styles)
- [x] Update backend docstring and User-Agent (app.py)
- [x] Add NOTICE with attribution to GhostTrack by HunxByts
- [x] Rename CLI `GhostTR.py` -> `okae.py` and rebrand banner
- [x] README updated (usage now `python3 okae.py`)

---

## Quick wins (≤ 1–2h)
- [ ] Copy-to-clipboard buttons for results
  - Files: `templates/index.html` (buttons), small JS; optional toast
- [ ] Leaflet mini-map for IP results using lat/lon (no extra backend)
  - Files: `templates/index.html`, `static/styles.css` (map height)
- [ ] Country flag + ASN badge on IP card
  - Files: `templates/index.html` (use `ip_data.flag.emoji`, `connection.asn`)
- [ ] Result export as JSON (per tool)
  - Backend: store last result in session; add `/export/<tool>.json`
  - Files: `app.py`, `templates/index.html`
- [ ] Pre-filled queries via URL params (`/?ip=1.2.3.4`, etc.)
  - Files: `app.py` (`index()` reads `request.args`), `templates/index.html`
- [ ] Theme toggle (dark/light) with CSS variables + localStorage
  - Files: `static/styles.css`, `templates/base.html`

## Medium (half-day)
- [ ] Parallel username checks (ThreadPoolExecutor)
  - Files: `app.py::track_username()`; keep timeouts modest
- [ ] Rate limiting + caching
  - Add `flask-limiter` and `requests-cache`
  - Files: `requirements.txt`, `app.py`
- [ ] Bulk username mode (textarea, one per line)
  - Files: `templates/index.html`, `app.py`
- [ ] Service health panel (ipwho.is, ipify, sample social endpoints)
  - Files: `app.py` (health route), `templates/base.html`
- [ ] Investigation Notebook drawer (pin artifacts + notes; export JSON/MD)
  - Files: `templates/base.html`, `static/styles.css`, small JS

## Advanced (1–2 days)
- [ ] WHOIS / Reverse DNS / ASN details
  - Use python-whois / socket; show rdns, ASN org metadata
  - Files: `requirements.txt`, `app.py`, `templates/index.html`
- [ ] Data breach check (opt-in via env key)
  - Integrate HaveIBeenPwned (email/username); do NOT log sensitive inputs
  - Files: `.env.example`, `app.py`, README “Security & Keys”
- [ ] Case files (persist investigations)
  - Save/load JSON under `cases/`; include timestamps and artifacts
  - Files: new `cases/` dir, `app.py`, UI picker in `templates/base.html`
- [ ] Internationalization (Setswana/English)
  - Simple i18n lookup dicts or `flask-babel` later
- [ ] Render.com productionization
  - Add `Procfile`, `gunicorn`, `FLASK_DEBUG=0` for prod; README deploy steps

## Visual polish
- [ ] Setswana microcopy (with English tooltips) for cultural identity
- [ ] Loading spinners + success/fail badges; subtle animation
- [ ] Better empty/error states with actionable guidance

## Security & Solo-dev quality
- [ ] `.env.example` with documented keys; `.env` already gitignored
- [ ] Structured logging (no PII beyond user inputs); log level via env
- [ ] Simple self-review checklist before commit (keys, logs, comments)

## Starter picks (recommended now)
- [ ] Leaflet map on IP results
- [ ] Parallel username checks

Notes:
- Keep Windows 10 performance in mind (CPU-only). Avoid heavy dependencies.
- Respect provider rate limits; surface user-facing warnings when throttled.
- Attribution stays visible in UI footer and NOTICE.
