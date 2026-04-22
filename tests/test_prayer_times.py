"""
Basic tests for prayer times fetching and formatting.
Run with: pytest
"""

from bot.prayer_times import fetch_prayer_times, format_daily_message, is_ramadan


def test_fetch_returns_data():
    data = fetch_prayer_times()
    assert "timings" in data
    assert "Fajr" in data["timings"]
    assert "Isha" in data["timings"]


def test_message_contains_city():
    data = fetch_prayer_times()
    message = format_daily_message(data)
    assert "Witham" in message


def test_message_contains_all_prayers():
    data = fetch_prayer_times()
    message = format_daily_message(data)
    for prayer in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]:
        assert prayer in message


def test_ramadan_returns_bool():
    data = fetch_prayer_times()
    result = is_ramadan(data)
    assert isinstance(result, bool)