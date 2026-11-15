"""Gợi ý tìm kiếm (autofill) của App Store: người ta thực sự gõ gì sau một cụm gốc.
Dùng: python3 -I engine/tools/autofill.py [--cc us] "quit zyn" "sleep sounds" ...
In ra từng cụm gốc kèm danh sách gợi ý theo thứ tự Apple trả về (thứ tự = mức phổ biến tương đối).
Chạy không cần tài khoản. Đây là bước 1 của công thức s2-aso-keyword-gap.
"""
import plistlib
import sys
import time
import urllib.parse
import urllib.request

STOREFRONT = {"us": "143441", "gb": "143444", "ca": "143455", "au": "143460", "de": "143443"}

args = sys.argv[1:]
cc = "us"
if "--cc" in args:
    i = args.index("--cc")
    cc = args[i + 1]
    del args[i:i + 2]

for term in args:
    url = "https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?" + urllib.parse.urlencode(
        {"clientApplication": "Software", "term": term})
    req = urllib.request.Request(url, headers={
        "X-Apple-Store-Front": f"{STOREFRONT.get(cc, '143441')}-1,29",
        "User-Agent": "AppStore/3.0 iOS/17.0",
    })
    try:
        data = plistlib.loads(urllib.request.urlopen(req, timeout=20).read())
        hints = [h.get("term", "") for h in data.get("hints", [])]
    except Exception as e:  # noqa: BLE001
        print(f"\n## {term}: ERROR {e}")
        continue
    print(f"\n## \"{term}\" ({cc}) — {len(hints)} gợi ý")
    for k, h in enumerate(hints, 1):
        print(f"{k}. {h}")
    time.sleep(1.0)
