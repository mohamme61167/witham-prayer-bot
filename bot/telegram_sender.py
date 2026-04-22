"""
Handles all Telegram message delivery for the prayer times bot.
"""

import requests
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_message(text: str, chat_id: str = None) -> bool:
    """
    Send a Markdown-formatted message to a Telegram chat.
    Returns True on success, False on failure.
    """
    if not TELEGRAM_BOT_TOKEN:
        print("✗ Error: TELEGRAM_BOT_TOKEN is not set in .env")
        return False

    if chat_id is None:
        chat_id = TELEGRAM_CHAT_ID

    url     = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id":                  chat_id,
        "text":                     text,
        "parse_mode":               "Markdown",
        "disable_web_page_preview": True,
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        if result.get("ok"):
            print(f"✓ Message delivered to chat {chat_id}")
            return True
        else:
            print(f"✗ Telegram rejected message: {result.get('description')}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"✗ Network error: {e}")
        return False