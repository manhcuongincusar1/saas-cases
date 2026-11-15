#!/usr/bin/env python3
"""Kiểm các câu trích trong engine/recipes/*.md.

Mỗi đoạn nằm trong ngoặc kép "..." dài ≥30 ký tự phải là một phần NGUYÊN VĂN của một mục trong
engine/evidence/<id>.yaml (đã qua kb/scripts/verify_extract.py). Dấu "…" cho phép rút gọn: mỗi đoạn
giữa các dấu "…" được kiểm riêng. Bỏ qua chữ tiếng Việt (chỉ kiểm chuỗi không có ký tự có dấu).

Chạy: python3 -I engine/scripts/check_recipes.py
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
VN = re.compile(r"[àáảãạăâđêéèẻẽẹôơưíìỉĩịúùủũụýỳỷỹỵ]", re.I)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().strip(" .,;:!?\"'")


def main() -> int:
    bad = total = 0
    for rec in sorted((ROOT / "engine/recipes").glob("*.md")):
        if rec.name.startswith("_"):
            continue
        if not (ROOT / "engine/evidence" / f"{rec.stem}.yaml").exists():
            print(f"? {rec.name}: chưa có evidence/{rec.stem}.yaml")
            continue
        # gộp mọi evidence: một công thức được phép trích câu nằm trong evidence của công thức khác
        pool = norm(" ".join(
            str(i.get("text", ""))
            for ev in (ROOT / "engine/evidence").glob("*.yaml")
            for i in yaml.safe_load(ev.read_text(encoding="utf-8"))
        ))
        body = rec.read_text(encoding="utf-8").split("\n---", 1)[1]
        for m in re.finditer(r'"([^"\n]{30,}?)"', body):
            quote = m.group(1)
            if VN.search(quote):
                continue
            for part in quote.split("…"):
                p = norm(part)
                if len(p) < 12:
                    continue
                total += 1
                if p not in pool:
                    bad += 1
                    print(f"✗ {rec.name}: không nằm trong evidence: {p[:90]!r}")
    print(f"{total} đoạn trích đã kiểm, {bad} sai")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
