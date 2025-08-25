"""
GhostTrack Web UI (Flask)

This Flask app provides a simple, modern web interface for the existing
GhostTrack CLI functionalities:
- IP Tracker (ipwho.is)
- Show Your IP (ipify)
- Phone Number Tracker (phonenumbers)
- Username Tracker (checks presence across popular platforms)

Notes for Solo Dev (Windows/Render):
- No secrets required. Keep any future credentials in environment variables (.env) and gitignore them.
- Designed to be CPU-friendly and to run locally on Windows 10.
- Render.com deployment is supported; add a Procfile/gunicorn later if needed.

Author: Adapted for web UI by Cascade assistant
"""
from __future__ import annotations

import os
import json
from typing import Dict, Any, List

import requests
from flask import Flask, render_template, request, send_from_directory

import phonenumbers
from phonenumbers import carrier, geocoder, timezone as pn_timezone

# ----------------------------------------------------------------------------
# App setup
# ----------------------------------------------------------------------------
app = Flask(__name__)

# User-Agent header for external requests
HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GhostTrack-WebUI"
}

# Timeout (seconds) for outgoing HTTP requests
HTTP_TIMEOUT = 10

# Social platforms to check for username existence
SOCIAL_SITES: List[Dict[str, str]] = [
    {"url": "https://www.facebook.com/{}", "name": "Facebook"},
    {"url": "https://www.twitter.com/{}", "name": "Twitter"},
    {"url": "https://www.instagram.com/{}", "name": "Instagram"},
    {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
    {"url": "https://www.github.com/{}", "name": "GitHub"},
    {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
    {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
    {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
    {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
    {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
    {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
    {"url": "https://www.behance.net/{}", "name": "Behance"},
    {"url": "https://medium.com/@{}", "name": "Medium"},
    {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
    {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
    {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
    {"url": "https://dribbble.com/{}", "name": "Dribbble"},
    {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
    {"url": "https://t.me/{}", "name": "Telegram"},
    {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
]


# ----------------------------------------------------------------------------
# Static helper to expose existing /asset images without moving them
# ----------------------------------------------------------------------------
@app.route("/asset/<path:filename>")
def asset_files(filename: str):
    asset_path = os.path.join(app.root_path, "asset")
    return send_from_directory(asset_path, filename)


# ----------------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------------
@app.get("/")
def index():
    """Render home with all four tools available."""
    return render_template("index.html", active_tab="ip")


@app.post("/track/ip")
def track_ip():
    ip = (request.form.get("ip") or "").strip()
    if not ip:
        return render_template(
            "index.html",
            active_tab="ip",
            ip_error="Please enter a valid IP address.",
        )

    try:
        resp = requests.get(f"http://ipwho.is/{ip}", headers=HTTP_HEADERS, timeout=HTTP_TIMEOUT)
        data = resp.json()
    except Exception as e:  # network or JSON errors
        return render_template(
            "index.html",
            active_tab="ip",
            ip_error=f"Lookup failed: {e}",
        )

    if not data or not data.get("success", True):
        msg = data.get("message", "Unknown error") if isinstance(data, dict) else "Unknown error"
        return render_template(
            "index.html",
            active_tab="ip",
            ip_error=f"API error: {msg}",
        )

    # Build a maps link if lat/lon exist
    lat = data.get("latitude")
    lon = data.get("longitude")
    maps_url = None
    if isinstance(lat, (int, float)) and isinstance(lon, (int, float)):
        maps_url = f"https://www.google.com/maps/@{lat},{lon},8z"

    return render_template(
        "index.html",
        active_tab="ip",
        ip_data=data,
        ip_maps_url=maps_url,
        ip_input=ip,
    )


@app.get("/your-ip")
def your_ip():
    try:
        resp = requests.get("https://api.ipify.org/", headers=HTTP_HEADERS, timeout=HTTP_TIMEOUT)
        ip_text = resp.text
    except Exception as e:
        return render_template(
            "index.html",
            active_tab="yourip",
            your_ip_error=f"Failed to fetch your IP: {e}",
        )

    return render_template("index.html", active_tab="yourip", your_ip=ip_text)


@app.post("/track/phone")
def track_phone():
    raw_phone = (request.form.get("phone") or "").strip()
    default_region = (request.form.get("region") or "ZA").strip() or "ZA"

    if not raw_phone:
        return render_template(
            "index.html",
            active_tab="phone",
            phone_error="Please enter a phone number.",
            selected_region=default_region,
        )

    try:
        # Choose region only if not using E.164 format
        region_arg = None if raw_phone.startswith("+") else default_region
        parsed = phonenumbers.parse(raw_phone, region_arg)

        region_code = phonenumbers.region_code_for_number(parsed)
        operator = carrier.name_for_number(parsed, "en")
        location = geocoder.description_for_number(parsed, "en")
        is_valid = phonenumbers.is_valid_number(parsed)
        is_possible = phonenumbers.is_possible_number(parsed)
        formatted_intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        mobile_format = phonenumbers.format_number_for_mobile_dialing(parsed, default_region, with_formatting=True)
        number_type = phonenumbers.number_type(parsed)
        tz_list = pn_timezone.time_zones_for_number(parsed)

        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            number_type_label = "Mobile number"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            number_type_label = "Fixed-line number"
        else:
            number_type_label = "Other number type"

        phone_result = {
            "location": location,
            "region_code": region_code,
            "timezone": ", ".join(tz_list) if tz_list else "-",
            "operator": operator or "-",
            "is_valid": is_valid,
            "is_possible": is_possible,
            "intl": formatted_intl,
            "e164": formatted_e164,
            "mobile_format": mobile_format,
            "country_code": parsed.country_code,
            "local_number": parsed.national_number,
            "type_label": number_type_label,
            "original": raw_phone,
        }
    except Exception as e:
        return render_template(
            "index.html",
            active_tab="phone",
            phone_error=f"Failed to parse phone number: {e}",
            selected_region=default_region,
        )

    return render_template(
        "index.html",
        active_tab="phone",
        phone_result=phone_result,
        selected_region=default_region,
    )


@app.post("/track/username")
def track_username():
    username = (request.form.get("username") or "").strip()
    if not username:
        return render_template(
            "index.html",
            active_tab="username",
            username_error="Please enter a username.",
        )

    results: List[Dict[str, Any]] = []
    with requests.Session() as session:
        session.headers.update(HTTP_HEADERS)
        for site in SOCIAL_SITES:
            url = site["url"].format(username)
            site_name = site["name"]
            found = False
            status = None
            try:
                r = session.get(url, timeout=HTTP_TIMEOUT, allow_redirects=True)
                status = r.status_code
                found = (status == 200)
            except requests.RequestException:
                status = None
                found = False
            results.append({
                "name": site_name,
                "url": url,
                "found": found,
                "status": status,
            })

    # Sort so found ones appear first
    results.sort(key=lambda x: (not x["found"], x["name"].lower()))

    return render_template("index.html", active_tab="username", username=username, username_results=results)


# ----------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Local dev defaults; override via env for deployment (e.g., render.com)
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host=host, port=port, debug=debug)
