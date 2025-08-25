# O Kae
O Kae (Setswana: "Where are you?") — a lightweight OSINT toolkit for quick "where/who" checks via IP, phone, and username lookups.

<img src="asset/bn.png"/>

New update :
```Version 2.2```

### Instalation on Linux (deb)
```
sudo apt-get install git
sudo apt-get install python3
```

### Instalation on Termux
```
pkg install git
pkg install python3
```

### Usage Tool
```
git clone https://github.com/<your-username>/okae.git
cd okae
pip3 install -r requirements.txt
python3 okae.py
```

Display on the menu ```IP Tracker```

<img src="asset/ip.png" />

on the IP Track menu, you can combo with the seeker tool to get the target IP
<details>
<summary>:zap: Install Seeker :</summary>
- <strong><a href="https://github.com/thewhiteh4t/seeker">Get Seeker</a></strong>
</details>

Display on the menu ```Phone Tracker```

<img src="asset/phone.png" />

on this menu you can search for information from the target phone number

Display on the menu ```Username Tracker```

<img src="asset/User.png"/>
on this menu you can search for information from the target username on social media

<details>
<summary>:zap: Author :</summary>
- <strong><a href="https://github.com/HunxByts">HunxByts</a></strong>
</details>

---

### What does "O Kae" mean?

O Kae is a Setswana phrase meaning "Where are you?" — a fitting prompt for an
OSINT tool focused on the "where/who" of IPs, phone numbers, and usernames.

### Fork attribution

This project is a fork and rebrand of
[GhostTrack by HunxByts](https://github.com/HunxByts/GhostTrack). Upstream did
not include an explicit LICENSE at the time of forking, so this repository keeps
prominent attribution in the README, UI footer, and NOTICE.

## O Kae (Flask Web UI)

O Kae includes a simple, modern web interface built with Flask. It wraps the same features as the CLI:

- IP Tracker (ipwho.is)
- Your IP (ipify)
- Phone Number Tracker (phonenumbers)
- Username Tracker (checks common platforms)

### Quick start (Windows PowerShell)

```
# create and activate virtual environment
py -3 -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt

# run the web app
.\.venv\Scripts\python app.py

# open in browser
http://127.0.0.1:5000
```

Environment variables (optional):

- `HOST` (default `127.0.0.1`)
- `PORT` (default `5000`)
- `FLASK_DEBUG` (default `1` for development)

Example:

```
$env:HOST = "0.0.0.0"; $env:PORT = "5000"; $env:FLASK_DEBUG = "1"; .\.venv\Scripts\python app.py
```

### Notes

- All network lookups use public endpoints; rate limits may apply.
- Keep secrets (if added later) in environment variables; never commit them.
- `.venv/` is local to your machine and should not be committed.

- Use responsibly and lawfully; comply with local laws and third‑party terms.
- Security: keep a `.env` file gitignored; do a quick secrets scan before push.

### Deploying on Render (brief)

- Create a New Web Service from this repo.
- Build command: `pip install -r requirements.txt`
- Start command (option 1): `python app.py`
- Or (option 2, recommended): add `gunicorn` and use `gunicorn app:app`.
- Ensure the service exposes the `PORT` environment variable (Render sets it).
