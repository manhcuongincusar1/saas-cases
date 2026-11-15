"""Gate 1.3 helper: App Store keyword competition (iTunes Search API approximates store search).
Usage: python3 -I kw.py [--cc us] [--n 6] "term one" "term two" ...
Prints, per term, the top N apps: ratings, release date, seller, price.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

args = sys.argv[1:]
cc, n = "us", 6
if "--cc" in args:
    i = args.index("--cc"); cc = args[i + 1]; del args[i:i + 2]
if "--n" in args:
    i = args.index("--n"); n = int(args[i + 1]); del args[i:i + 2]

for term in args:
    url = "https://itunes.apple.com/search?" + urllib.parse.urlencode(
        {"term": term, "country": cc, "entity": "software", "limit": n})
    try:
        data = json.load(urllib.request.urlopen(url, timeout=20))
    except Exception as e:  # noqa: BLE001
        print(f"\n## {term}: ERROR {e}")
        continue
    res = data.get("results", [])
    top3 = [r.get("userRatingCount", 0) for r in res[:3]]
    print(f"\n## \"{term}\" ({cc}) — top3 ratings {top3}")
    for k, r in enumerate(res, 1):
        print(f"{k}. {r.get('trackName','')[:48]:48} | {r.get('userRatingCount',0):>7} ★{r.get('averageUserRating',0):.1f}"
              f" | {r.get('releaseDate','')[:10]} | {r.get('sellerName','')[:28]:28} | {r.get('formattedPrice','')}"
              f" | id {r.get('trackId')}")
    time.sleep(1.2)
