"""Top-grossing App Store theo genre, lọc app ra mắt gần đây (bước 1 của công thức s1-revenue-spy).
Dùng: python3 -I engine/tools/topgrossing.py [--cc us] [--genre 6013] [--limit 100] [--since 2025-01-01] [--max-ratings 20000]
Genre hay dùng: 6013 Health&Fitness, 6012 Lifestyle, 6017 Education, 6015 Finance, 6000 Business, 6007 Productivity,
6002 Utilities, 6008 Photo&Video, 6005 Social, 6016 Entertainment, 6024 Shopping, 6003 Travel, 6018 Books, 6020 Medical.
In: hạng, tên, ngày ra mắt, số rating, seller, id. Doanh thu KHÔNG có ở đây: phải tra TrustMRR/Sensor Tower cho app còn hứa hẹn.
"""
import json
import sys
import urllib.request

args = sys.argv[1:]


def opt(name, default):
    if name in args:
        i = args.index(name)
        v = args[i + 1]
        del args[i:i + 2]
        return v
    return default


cc = opt("--cc", "us")
genre = opt("--genre", "6013")
limit = int(opt("--limit", "100"))
since = opt("--since", "2025-01-01")
max_ratings = int(opt("--max-ratings", "20000"))

url = f"https://itunes.apple.com/{cc}/rss/topgrossingapplications/limit={limit}/genre={genre}/json"
feed = json.load(urllib.request.urlopen(url, timeout=25)).get("feed", {})
entries = feed.get("entry", [])
if isinstance(entries, dict):
    entries = [entries]
ids = [e["id"]["attributes"]["im:id"] for e in entries]
rank = {i: n + 1 for n, i in enumerate(ids)}
lookup = json.load(urllib.request.urlopen(
    f"https://itunes.apple.com/lookup?id={','.join(ids)}&country={cc}", timeout=25)).get("results", [])
rows = []
for r in lookup:
    rel = (r.get("releaseDate") or "")[:10]
    n = r.get("userRatingCount", 0)
    if rel >= since and n <= max_ratings:
        rows.append((rank[str(r["trackId"])], r.get("trackName", "")[:46], rel, n, r.get("sellerName", "")[:26], r["trackId"]))
rows.sort()
print(f"genre {genre} ({cc}): {len(ids)} app trong top-grossing; {len(rows)} app ra mắt ≥{since} và ≤{max_ratings} rating")
for k, name, rel, n, seller, tid in rows:
    print(f"#{k:<3} {name:46} | {rel} | {n:>6} rating | {seller:26} | id {tid}")
