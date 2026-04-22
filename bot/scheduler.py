"""
Entry point for the prayer times bot.
Run directly or triggered by n8n via cron schedule.

Usage:
    python -m bot.scheduler          # preview only, no Telegram send
    python -m bot.scheduler --send   # fetch and send to Telegram
"""

import sys
from bot.prayer_times import fetch_prayer_times, format_daily_message
from bot.telegram_sender import send_message


def run(send: bool = False):
    print("── Witham Prayer Times Bot ──────────────────")

    try:
        data    = fetch_prayer_times()
        message = format_daily_message(data)

        print(message)
        print("─────────────────────────────────────────────\n")

        if send:
            send_message(message)
        else:
            print("(Preview mode — run with --send to deliver to Telegram)")

    except Exception as e:
        error_msg = f"⚠️ Bot error: {e}"
        print(error_msg)
        if send:
            send_message(error_msg)
        sys.exit(1)


if __name__ == "__main__":
    run(send="--send" in sys.argv)