#!/usr/bin/env python3
"""Rebuild data/videos.csv and data/chapters.csv from the transcript folders.
Run after downloading new videos. Summaries/topics for new videos are left
blank; fill them in data/videos.csv by hand (existing rows are preserved)."""
import csv, json
from pathlib import Path

ROOT = Path("/Users/nguyencuong/Desktop/SAAS/superwall/youtube-transcript/superwall")
DATA = Path(__file__).resolve().parent.parent / "data"

def hms(s):
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"

old = {}
if (DATA / "videos.csv").exists():
    for r in csv.DictReader(open(DATA / "videos.csv")):
        old[r["video_id"]] = r

videos, chapters = [], []
for d in sorted(ROOT.iterdir()):
    if not d.is_dir():
        continue
    m = json.loads((d / "meta.json").read_text())
    vid = m["videoId"]
    prev = old.get(vid, {})
    videos.append({
        "video_id": vid, "folder": d.name, "title": m["title"],
        "published": m.get("publishDate", ""), "minutes": round(m.get("duration", 0) / 60),
        "url": m["url"], "topics": prev.get("topics", ""), "summary": prev.get("summary", ""),
    })
    for c in m.get("chapters", []):
        chapters.append({
            "video_id": vid, "folder": d.name, "video_title": m["title"],
            "chapter": c["title"], "timestamp": hms(int(c["start"])), "seconds": int(c["start"]),
            "url": f"https://www.youtube.com/watch?v={vid}&t={int(c['start'])}s",
        })

videos.sort(key=lambda r: r["published"], reverse=True)
for name, rows in (("videos.csv", videos), ("chapters.csv", chapters)):
    with open(DATA / name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{name}: {len(rows)} rows")
