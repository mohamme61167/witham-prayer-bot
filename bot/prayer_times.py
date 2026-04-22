"""
Fetches and formats daily prayer times from the Aladhan API.
Location: Witham, Essex, UK
"""

import requests
from datetime import datetime
from config.settings import (
    CITY, COUNTRY, METHOD, SCHOOL, ALADHAN_BASE_URL, PRAYERS
)


def fetch_prayer_times(date: datetime = None) -> dict:
    """
    Fetch prayer times from Aladhan API.
    Returns the full data dict for the given date (defaults to today).
    """
    if date is None:
        date = datetime.now()

    params = {
        "city":    CITY,
        "country": COUNTRY,
        "method":  METHOD,
        "school":  SCHOOL,
        "date":    date.strftime("%d-%m-%Y"),
    }

    response = requests.get(ALADHAN_BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    if data.get("code") != 200:
        raise ValueError(f"Aladhan API error: {data.get('status')}")

    return data["data"]


def is_ramadan(data: dict) -> bool:
    """Returns True if today falls within Ramadan (Hijri month 9)."""
    return data["date"]["hijri"]["month"]["number"] == 9


def format_daily_message(data: dict) -> str:
    """
    Builds the full Telegram message string for the day.
    Handles standard days, Jumu'ah (Friday), and Ramadan automatically.
    """
    timings  = data["timings"]
    gregorian = data["date"]["gregorian"]
    hijri     = data["date"]["hijri"]

    is_friday = datetime.now().weekday() == 4
    ramadan   = is_ramadan(data)

    # ── Header ────────────────────────────────────────────────────────────────
    if ramadan:
        header = "🌙 *Ramadan Mubarak!* — Prayer Times\n"
    elif is_friday:
        header = "🕌 *Jumu'ah Mubarak!* — Prayer Times\n"
    else:
        header = "🕋 *Daily Prayer Times*\n"

    date_str  = gregorian["date"]
    hijri_str = f"{hijri['day']} {hijri['month']['en']} {hijri['year']} AH"
    header   += f"📅 {date_str}  |  {hijri_str}\n"
    header   += f"📍 {CITY}, Essex, UK\n"
    header   += "─" * 28 + "\n"

    # ── Prayer rows ───────────────────────────────────────────────────────────
    lines = []
    for prayer, emoji in PRAYERS.items():
        time_str = timings.get(prayer, "N/A").split(" ")[0]
        lines.append(f"{emoji} *{prayer:<8}* {time_str}")

    # ── Ramadan extras ────────────────────────────────────────────────────────
    ramadan_section = ""
    if ramadan:
        imsak    = timings.get("Imsak", "N/A").split(" ")[0]
        midnight = timings.get("Midnight", "N/A").split(" ")[0]
        ramadan_section  = "\n" + "─" * 28 + "\n"
        ramadan_section += f"⏰ *Imsak (stop eating):* {imsak}\n"
        ramadan_section += f"🌙 *Midnight:*           {midnight}\n"

    # ── Friday note ───────────────────────────────────────────────────────────
    friday_note = ""
    if is_friday:
        friday_note  = "\n" + "─" * 28 + "\n"
        friday_note += "🕌 Don't forget *Jumu'ah* today!\n"
        friday_note += "_Check your local mosque for Khutbah time._"

    # ── Footer ────────────────────────────────────────────────────────────────
    footer = "\n\n_May Allah accept your prayers. Ameen._ 🤲"

    return header + "\n".join(lines) + ramadan_section + friday_note + footer