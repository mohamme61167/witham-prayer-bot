"""
Central configuration for Witham Prayer Times Bot.
All tuneable values live here — easy for clients to customise.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── Telegram ──────────────────────────────────────────────────────────────────
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID   = os.environ.get("TELEGRAM_CHAT_ID", "")

# ── Location ──────────────────────────────────────────────────────────────────
CITY    = "Witham"
COUNTRY = "GB"

# ── Calculation method ────────────────────────────────────────────────────────
# 3 = Muslim World League (standard for UK mosques)
# 2 = ISNA, 5 = Egyptian, see https://aladhan.com/prayer-times-api for full list
METHOD = 15  # switching to Univ. of Islamic Sciences, Karachi for more accurate Asr time.

# 0 = Standard/Shafi (default), 1 = Hanafi (Asr shadow ratio 2)
SCHOOL = 1   # Hanafi — common in South Asian UK communities

# ── API ───────────────────────────────────────────────────────────────────────
ALADHAN_BASE_URL = "https://api.aladhan.com/v1/timingsByCity"

# ── Prayer display order ──────────────────────────────────────────────────────
PRAYERS = {
    "Fajr":    "🌙",
    "Sunrise": "🌅",
    "Dhuhr":   "☀️",
    "Asr":     "🌤️",
    "Maghrib": "🌇",
    "Isha":    "🌃",
}