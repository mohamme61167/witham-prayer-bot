"""
Compares prayer times across different Aladhan calculation methods.
Run this to help decide which method matches your local mosque.
Usage: python compare_methods.py
"""

import requests
from datetime import datetime

LATITUDE  = 51.7979
LONGITUDE = 0.6385
DATE      = datetime.now().strftime("%d-%m-%Y")

METHODS = {
    1: "Univ. of Islamic Sciences, Karachi",
    2: "Islamic Society of North America",
    3: "Muslim World League",
    4: "Umm Al-Qura, Makkah",
    5: "Egyptian General Authority",
    8: "Gulf Region / Hanbali",
   15: "Moonsighting Committee Worldwide",
}

PRAYERS_TO_SHOW = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

print(f"\nPrayer time comparison for Witham, Essex — {DATE}")
print(f"School: Hanafi (school=1) for all methods\n")
print(f"{'Method':<40} {'Fajr':<8} {'Dhuhr':<8} {'Asr':<8} {'Maghrib':<10} {'Isha':<8}")
print("─" * 82)

# Target from Al Falah Braintree mosque screen
print(f"{'AL FALAH BRAINTREE (target)':<40} {'04:10':<8} {'13:01':<8} {'17:53':<8} {'20:10':<10} {'21:24':<8}")
print("─" * 82)

for method_id, method_name in METHODS.items():
    try:
        response = requests.get(
            "https://api.aladhan.com/v1/timings",
            params={
                "latitude":  LATITUDE,
                "longitude": LONGITUDE,
                "method":    method_id,
                "school":    1,           # Hanafi
                "date":      DATE,
            },
            timeout=10,
        )
        timings = response.json()["data"]["timings"]
        times   = [timings.get(p, "N/A").split(" ")[0] for p in PRAYERS_TO_SHOW]
        print(f"{method_name:<40} {times[0]:<8} {times[1]:<8} {times[2]:<8} {times[3]:<10} {times[4]:<8}")

    except Exception as e:
        print(f"{method_name:<40} Error: {e}")

print("─" * 82)
print("\nCompare each row against Al Falah Braintree target above.")
print("Closest Fajr + Asr + Isha match = your method.\n")