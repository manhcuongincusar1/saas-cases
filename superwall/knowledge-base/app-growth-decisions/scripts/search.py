#!/usr/bin/env python3
"""Search the Superwall transcript corpus. Prints matching sentences with a
YouTube link that jumps to the exact second.

  search.py "weekly plan" "annual"        # sentences matching ALL terms (case-insensitive)
  search.py -r "\\$\\d+k ?MRR"            # regex
  search.py -v cal-ai "CPM"               # only folders whose name contains "cal-ai"
  search.py -c 2 "minimum view"           # 2 sentences of context either side
  search.py --at VIDEO 00:12:19           # read 90s from a timestamp; VIDEO = folder substring, video id, or YouTube URL
  search.py --at "https://www.youtube.com/watch?v=l0vswWcGmMs&t=739s"   # URL with t= needs no timestamp
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path("/Users/nguyencuong/Desktop/SAAS/superwall/youtube-transcript")

def secs(ts):
    h, m, s = (["0"] * 3 + ts.split(":"))[-3:]
    return int(h) * 3600 + int(m) * 60 + int(float(s))

def videos(filt=None):
    for d in sorted((ROOT / "superwall").iterdir()):
        if not d.is_dir():
            continue
        meta = json.loads((d / "meta.json").read_text())
        if filt and filt not in d.name and filt != meta["videoId"]:
            continue
        sents = json.loads((d / "transcript-sentences.json").read_text())
        yield d.name, meta, sents

def link(meta, ts):
    return f"https://www.youtube.com/watch?v={meta['videoId']}&t={secs(ts)}s"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("terms", nargs="*")
    p.add_argument("-r", "--regex", action="store_true")
    p.add_argument("-v", "--video")
    p.add_argument("-c", "--context", type=int, default=0)
    p.add_argument("-n", "--limit", type=int, default=60)
    p.add_argument("--at", nargs="+", metavar="VIDEO [HH:MM:SS]")
    a = p.parse_args()

    if a.at:
        target, ts = a.at[0], (a.at[1] if len(a.at) > 1 else None)
        m = re.search(r"v=([\w-]{11})(?:.*?[?&]t=(\d+))?", target)
        if m:
            target = m.group(1)
            if ts is None and m.group(2):
                s = int(m.group(2)); ts = f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"
        found = next(videos(target), None)
        if not found or ts is None:
            p.error(f"no video matching {target!r}" if not found else "timestamp needed (HH:MM:SS, or a URL with t=)")
        name, meta, sents = found
        t0 = secs(ts)
        print(f"# {meta['title']}  ({name})")
        for s in sents:
            if t0 <= secs(s["start"]) <= t0 + 90:
                print(f"[{s['start']}] {s['text']}")
        print(link(meta, ts))
        return

    if not a.terms:
        p.error("give search terms or --at")
    if a.regex:
        pats = [re.compile(t, re.I) for t in a.terms]
        hit = lambda txt: all(p.search(txt) for p in pats)
    else:
        terms = [t.lower() for t in a.terms]
        hit = lambda txt: all(t in txt.lower() for t in terms)

    n = 0
    for name, meta, sents in videos(a.video):
        for i, s in enumerate(sents):
            if not hit(s["text"]):
                continue
            lo, hi = max(0, i - a.context), min(len(sents), i + a.context + 1)
            text = " ".join(x["text"] for x in sents[lo:hi])
            print(f"{meta['title'][:60]} | {s['start']} | {link(meta, s['start'])}\n  {text}\n")
            n += 1
            if n >= a.limit:
                print(f"... stopped at {a.limit} hits (use -n)")
                return
    print(f"{n} hits", file=sys.stderr)

if __name__ == "__main__":
    main()
