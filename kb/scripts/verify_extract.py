#!/usr/bin/env python3
"""Dò các mục trích do subagent tạo ra.

Dùng: python3 -I kb/scripts/verify_extract.py <vào.yaml> <ra.yaml>

Mỗi mục có: transcript, ts, text, (speaker, kind, case, what).
- text phải khớp NGUYÊN VĂN transcript (chỉ gộp khoảng trắng) → mới giữ.
- ts luôn được sửa lại theo vị trí thật của câu trích (HH:MM:SS hoặc MM:SS như file gốc).
- đường dẫn transcript được đổi thành đường dẫn tương đối từ gốc repo.
In ra số mục giữ/loại và lý do loại.
"""
import importlib.util
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location("check", HERE / "check.py")
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def fmt(sec: int, long_form: bool) -> str:
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if long_form else f"{h * 60 + m:02d}:{s:02d}"


def main() -> int:
    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    items = yaml.safe_load(src.read_text(encoding="utf-8")) or []
    cache, kept, dropped = {}, [], []
    for i, it in enumerate(items, 1):
        try:
            tpath = pathlib.Path(str(it["transcript"]))
            text = str(it["text"])
        except Exception:  # noqa: BLE001
            dropped.append((i, "thiếu trường transcript/text"))
            continue
        if not tpath.is_file():
            dropped.append((i, f"không thấy file {tpath.name}"))
            continue
        if tpath not in cache:
            raw = tpath.read_text(encoding="utf-8")
            cache[tpath] = (check.load_segments(tpath), "→" in raw)
        segs, long_form = cache[tpath]
        declared = None
        try:
            declared = check.to_sec(it.get("ts"))
        except (ValueError, TypeError):
            pass
        near = getattr(check, "locate_near", None)  # có sau khi check_next.py thay check.py
        found = near(segs, text, declared) if near else check.locate(segs, text)
        if found is None:
            dropped.append((i, f"không khớp nguyên văn: {text[:60]!r}"))
            continue
        out = dict(it)
        out["ts"] = fmt(found, long_form)
        try:
            out["transcript"] = str(tpath.relative_to(ROOT))
        except ValueError:
            out["transcript"] = str(tpath)
        kept.append(out)
    dst.write_text(yaml.safe_dump(kept, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"giữ {len(kept)}/{len(items)}, loại {len(dropped)}")
    for i, why in dropped:
        print(f"  - mục {i}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
