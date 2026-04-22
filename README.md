# 🕋 Witham Prayer Times Bot

An automated daily prayer times reminder bot for the Witham Muslim Community,
built with Python, Telegram Bot API, and deployed on Railway with n8n automation.

## Live Project
- **Community:** Witham Muslim Community, Essex, UK
- **Delivery:** Telegram group (daily at 4am)
- **Status:** Live and running in production

## Features
- Fetches accurate daily prayer times for Witham, Essex using the Aladhan API
- Verified GPS coordinates (51.7979, 0.6385) — not city name lookup
- Hanafi school calculation (Moonsighting Committee Worldwide method)
- Automatic Jumu'ah (Friday) detection with special message
- Automatic Ramadan detection with Suhoor/Iftar times
- Clean formatted Telegram message with Hijri and Gregorian dates
- Deployed on Railway — runs 24/7 without manual intervention

## Stack
| Tool | Purpose | Why chosen |
|---|---|---|
| Python 3.10 | Core logic, API fetching, message formatting | Clean, readable, in-demand on Upwork |
| Aladhan API | Prayer times calculation | Free, accurate, coordinate-based |
| Telegram Bot API | Message delivery | Free, instant setup, no business verification |
| n8n | Visual workflow automation | Top Upwork automation skill |
| Railway | Cloud deployment | Git-based, free tier, no DevOps needed |

## Project Structure

WithamPrayerBot/
├── bot/
│   ├── prayer_times.py      # Aladhan API fetching and message formatting
│   ├── telegram_sender.py   # Telegram delivery
│   └── scheduler.py         # Entry point
├── config/
│   └── settings.py          # All configuration in one place
├── tests/
│   └── test_prayer_times.py # Pytest test suite
├── .env.example             # Environment variable template
├── Procfile                 # Railway deployment config
└── requirements.txt

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/mohamme61167/witham-prayer-bot.git
cd witham-prayer-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` with your values:

TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

### 4. Run locally
```bash
# Preview message only
python -m bot.scheduler

# Send to Telegram
python -m bot.scheduler --send
```

### 5. Run tests
```bash
pytest
```

## Deployment
Deployed on Railway with a daily cron schedule (`0 3 * * *` UTC = 4am BST).

Auto-deploys on every push to `main` via GitHub integration.

Environment variables (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`) stored
securely in Railway — never committed to the repository.

## Prayer Time Calculation
Times are calculated using the **Moonsighting Committee Worldwide** method
with **Hanafi** Asr calculation, matched against Al Falah Islamic Centre
Braintree as the nearest local mosque reference.

Coordinates used: `51.7979, 0.6385` (Witham, Essex) — verified against
the Aladhan API meta response to confirm accuracy.

> ⚠️ Times are calculated astronomically. Always verify with your local mosque.

## Freelance Portfolio Notes
This project was built as a real community tool and freelance portfolio piece
demonstrating:
- REST API integration (Aladhan)
- Telegram Bot API automation
- n8n visual workflow design
- Cloud deployment with Railway
- Clean Python project structure with tests
- Islamic calendar logic (Hijri month detection, Hanafi school)

Built for the Witham Muslim Community, Essex, UK.

## Adapt for Your Community
To deploy this for a different location, update `config/settings.py`:
```python
CITY      = "Your City"
LATITUDE  = your_latitude
LONGITUDE = your_longitude
METHOD    = 15   # see https://aladhan.com/prayer-times-api
SCHOOL    = 1    # 0 = Standard, 1 = Hanafi
```

## License
MIT — free to use and adapt for your community.