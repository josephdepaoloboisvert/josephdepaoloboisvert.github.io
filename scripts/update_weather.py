"""
Fetches live weather from NOAA GLERL Harrison-Dever Crib station
(2.75 miles offshore Navy Pier) and the Lake Michigan marine forecast,
then updates the data-weather span in every HTML page.

Run by GitHub Actions on a cron schedule.
"""

import re
import sys
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

GLERL_URL = "https://www.glerl.noaa.gov/metdata/chi/{year}/{date}.04t.txt"
MARINE_URL = "https://forecast.weather.gov/shmrn.php?mz=lmz741"
ROOT = Path(__file__).parent.parent


def degrees_to_compass(deg):
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    idx = round(float(deg) / 45) % 8
    return dirs[idx]


def ms_to_knots(ms):
    return round(float(ms) * 1.944)


def c_to_f(c):
    return round(float(c) * 9 / 5 + 32)


def fetch_glerl():
    """Fetch latest observation from GLERL crib station. Tries today then yesterday."""
    for offset in (0, 1):
        dt = datetime.now(timezone.utc) - timedelta(days=offset)
        url = GLERL_URL.format(year=dt.year, date=dt.strftime("%Y%m%d"))
        try:
            r = requests.get(url, timeout=15)
            r.raise_for_status()
        except Exception:
            continue

        last = None
        for line in r.text.splitlines():
            parts = line.split()
            if len(parts) >= 8 and parts[0].isdigit():
                try:
                    float(parts[4])  # AirTemp sanity check
                    last = parts
                except ValueError:
                    continue

        if last:
            return {
                "temp_f": c_to_f(last[4]),
                "wind_kt": ms_to_knots(last[5]),
                "wind_dir": degrees_to_compass(last[7]),
            }

    return None


def fetch_sky():
    """Extract a brief sky condition from the NWS marine forecast."""
    try:
        r = requests.get(MARINE_URL, timeout=15)
        text = r.text.lower()

        # Advisory flag — worth surfacing in the dateline
        advisory = "sca" if "small craft advisory" in text else None

        conditions = [
            ("TSTMS",       "thunderstorm"),
            ("FOG",         "fog"),
            ("RAIN",        "rain"),
            ("SHOWERS",     "showers"),
            ("OVERCAST",    "overcast"),
            ("MOSTLY CLDY", "mostly cloudy"),
            ("PARTLY CLDY", "partly cloudy"),
            ("MOSTLY CLR",  "mostly clear"),
            ("CLEAR",       "clear"),
            ("FAIR",        "fair"),
        ]
        for label, keyword in conditions:
            if keyword in text:
                sky = label
                break
        else:
            sky = None

        return sky, advisory

    except Exception:
        return None, None


def build_dateline(obs, sky, advisory):
    parts = []
    if advisory == "sca":
        parts.append("SML CRAFT ADV")
    if sky:
        parts.append(sky)
    parts.append(f"{obs['wind_dir']} WINDS {obs['wind_kt']}KT")
    parts.append(f"{obs['temp_f']}°")  # degree symbol
    return " · ".join(parts)              # middot separator


def update_html(dateline):
    pattern = re.compile(r'(<span\s+data-weather>)[^<]*(</span>)', re.IGNORECASE)
    changed = 0
    for html in ROOT.glob("*.html"):
        text = html.read_text(encoding="utf-8")
        new_text, n = pattern.subn(rf"\g<1>{dateline}\g<2>", text)
        if n and new_text != text:
            html.write_text(new_text, encoding="utf-8")
            print(f"  updated {html.name}")
            changed += 1
    return changed


if __name__ == "__main__":
    obs = fetch_glerl()
    if obs is None:
        print("ERROR: could not fetch GLERL data — aborting")
        sys.exit(0)  # exit 0 so the Action doesn't fail noisily

    sky, advisory = fetch_sky()
    dateline = build_dateline(obs, sky, advisory)
    print(f"Dateline: {dateline}")

    n = update_html(dateline)
    print(f"Updated {n} HTML files")
