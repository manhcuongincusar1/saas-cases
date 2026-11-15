"""Gate 2.1/2.2 helper: most recent App Store reviews of an app.
Usage: python3 -I reviews.py <appId> [--cc us] [--pages 2] [--show 25]
Prints star distribution and the most recent review titles/snippets.
"""
import json
import sys
import time
import urllib.request
from collections import Counter

args = sys.argv[1:]
app = args[0]
cc, pages, show = "us", 2, 25
if "--cc" in args:
    cc = args[args.index("--cc") + 1]
if "--pages" in args:
    pages = int(args[args.index("--pages") + 1])
if "--show" in args:
    show = int(args[args.index("--show") + 1])

revs = []
for p in range(1, pages + 1):
    url = f"https://itunes.apple.com/{cc}/rss/customerreviews/page={p}/id={app}/sortby=mostrecent/json"
    try:
        feed = json.load(urllib.request.urlopen(url, timeout=20)).get("feed", {})
    except Exception as e:  # noqa: BLE001
        print("ERROR", e)
        break
    entries = feed.get("entry", [])
    if isinstance(entries, dict):
        entries = [entries]
    for e in entries:
        if "im:rating" not in e:
            continue
        revs.append((int(e["im:rating"]["label"]), e.get("updated", {}).get("label", "")[:10],
                     e.get("title", {}).get("label", ""), e.get("content", {}).get("label", "")))
    time.sleep(1)

stars = Counter(r[0] for r in revs)
print(f"{len(revs)} reviews | " + " ".join(f"{s}★:{stars.get(s,0)}" for s in range(5, 0, -1)))
for s, d, t, c in revs[:show]:
    print(f"- {s}★ {d} {t[:60]} — {c[:220].replace(chr(10), ' ')}")
