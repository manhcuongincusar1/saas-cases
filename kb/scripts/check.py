#!/usr/bin/env python3
"""Kiểm các file kb/videos/**/*.md (schema 1 và schema 2, xem kb/SCHEMA.md).

Nguyên tắc: mọi điều khẳng định phải có chỗ dựa NGUYÊN VĂN trong transcript, máy dò được.
- quote.text / rule.text / `q` (của revenue và các trường G) phải khớp nguyên văn (chỉ gộp khoảng trắng).
- Một câu có thể xuất hiện nhiều lần (teaser đầu tập lặp câu ở giữa tập): ts hợp lệ nếu khớp BẤT KỲ lần nào;
  khi phải sửa ts thì chọn lần gần ts đã ghi nhất, không tự chuyển về teaser.
- Schema 2: quote/rule có `stage` (theme được phép []); step ở find-idea/validate/launch/monetize/grow/retain có
  `tactic` hợp lệ; case depth=full có đủ trường G; mốc time_to_revenue là {months: SỐ, q, ts} hoặc null;
  câu của host/expert vào rules, của founder vào quotes.

Chạy:
  python3 -I kb/scripts/check.py [file.md ...]            kiểm (không tham số = tất cả)
  python3 -I kb/scripts/check.py --stats file.md ...      chỉ đếm: quote/rule bị loại, G bị loại, ts lệch, chuyển vai
  python3 -I kb/scripts/check.py --prune vào.md ra.md     bỏ quote/rule và G không có chỗ dựa (G → null/[]),
                                                          sửa ts lệch, chuyển vai, ghi ra.md
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
KB = ROOT / "kb"
VOCAB = KB / "vocab_next.yaml" if (KB / "vocab_next.yaml").exists() else KB / "vocab.yaml"
SS_LINE = re.compile(r"^\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s?(.*)$")
SW_PARA = re.compile(r"^(.*?)\s*\[(\d{2}:\d{2}:\d{2}) → (\d{2}:\d{2}:\d{2})\]\s*$")


def to_sec(ts: str) -> int:
    sec = 0
    for part in str(ts).split(":"):
        sec = sec * 60 + int(part)
    return sec


def fmt_ts(sec: int, long_form: bool) -> str:
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if long_form else f"{h * 60 + m:02d}:{s:02d}"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s)).strip()


def load_segments(path: pathlib.Path):
    """Trả về [(giây_bắt_đầu, text)] cho cả 2 định dạng transcript."""
    segs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = SS_LINE.match(line)
        if m:
            segs.append((to_sec(m.group(1)), m.group(2)))
            continue
        m = SW_PARA.match(line)
        if m:
            segs.append((to_sec(m.group(2)), m.group(1)))
    return segs


def occurrences(segs, quote: str):
    """Mốc bắt đầu (giây) của MỌI lần câu trích xuất hiện, theo thứ tự."""
    buf, starts = "", []
    for sec, text in segs:
        starts.append((len(buf), sec))
        buf += norm(text) + " "
    q = norm(quote)
    res = []
    i = buf.find(q) if q else -1
    while i >= 0:
        res.append(max((s for s in starts if s[0] <= i), key=lambda s: s[0])[1])
        i = buf.find(q, i + 1)
    return res


def locate(segs, quote: str):
    """Lần xuất hiện đầu tiên (giữ cho tương thích với verify_extract)."""
    occ = occurrences(segs, quote)
    return occ[0] if occ else None


def locate_near(segs, quote: str, declared):
    """Lần xuất hiện gần mốc đã khai nhất; đúng mốc khai thì giữ nguyên."""
    occ = occurrences(segs, quote)
    if not occ:
        return None
    if declared in occ:
        return declared
    if declared is None:
        return occ[-1] if len(occ) > 1 else occ[0]
    return min(occ, key=lambda s: abs(s - declared))


def split_fm(text: str):
    if not text.startswith("---\n"):
        raise ValueError("thiếu YAML frontmatter")
    head, rest = text.split("\n---", 1)
    return yaml.safe_load(head[4:]), rest


def frontmatter(path: pathlib.Path) -> dict:
    return split_fm(path.read_text(encoding="utf-8"))[0]


def known_slugs() -> set:
    f = KB / "frameworks" / "candidates.md"
    if not f.exists():
        return set()
    return set(re.findall(r"^#+ .*?`([a-z0-9-]+)`", f.read_text(encoding="utf-8"), re.M))


def safe_sec(ts):
    try:
        return to_sec(ts)
    except (ValueError, TypeError):
        return None


# Mỗi vấn đề: (thông điệp, hành động). Hành động:
#   None | ("del", path) | ("null", path) | ("setts", path, giây) | ("move", từ_trường, chỉ_số, sang_trường)
def check_fm(fm: dict, vocab: dict, slugs: set):
    issues = []

    def err(msg, action=None):
        issues.append((msg, action))

    def warn(msg):
        issues.append(("~ " + msg, None))

    v2 = fm.get("schema") == 2

    def enum(field, value, where):
        if value not in vocab[field]:
            err(f"{where}: '{value}' không có trong vocab.{field}")

    enum("channel_slug", fm.get("channel"), "channel")
    enum("kind", fm.get("kind"), "kind")

    tpath = ROOT / str(fm.get("transcript", ""))
    if not tpath.is_file():
        err(f"không thấy transcript: {fm.get('transcript')}")
        return issues, None
    segs = load_segments(tpath)
    if not segs:
        err("transcript không có đoạn nào có mốc giây")
        return issues, None
    starts = {s for s, _ in segs}
    long_form = "→" in tpath.read_text(encoding="utf-8")

    def ts_ok(ts, where):
        if ts is None:
            return
        sec = safe_sec(ts)
        if not isinstance(ts, str):
            err(f"{where}: ts phải là chuỗi trong ngoặc kép")
        elif sec is None or sec not in starts:
            err(f"{where}: ts {ts} không phải mốc có thật")

    def chk_q(obj, path, where, drop):
        """Kiểm chỗ dựa `q` của một trường: drop = 'null' (trường dict) hoặc 'del' (phần tử danh sách)."""
        if not isinstance(obj, dict):
            err(f"{where}: phải là dict có q và ts")
            return
        q = obj.get("q")
        if not q or not str(q).strip():
            err(f"{where}: thiếu q (đoạn nguyên văn làm chỗ dựa)", (drop, path))
            return
        occ = occurrences(segs, q)
        if not occ:
            err(f"{where}: q KHÔNG khớp nguyên văn transcript", (drop, path))
            return
        if len(norm(q).split()) > 40:
            warn(f"{where}: q dài hơn 40 từ")
        declared = safe_sec(obj.get("ts"))
        if declared not in occ:
            err(f"{where}: ts {obj.get('ts')} lệch, q nằm ở {occ}",
                ("setts", path, locate_near(segs, q, declared)))

    for ci, c in enumerate(fm.get("cases") or []):
        cid = c.get("id", "?")
        w = f"case {cid}"
        cp = ["cases", ci]
        if c.get("depth"):
            enum("depth", c["depth"], f"{w}.depth")
        for val in c.get("idea_origin") or []:
            enum("idea_origin", val, f"{w}.idea_origin")
        for val in c.get("scale_channels") or []:
            enum("channel", val, f"{w}.scale_channels")
        rev = c.get("revenue")
        if rev:
            if rev.get("evidence"):
                enum("evidence", rev["evidence"], f"{w}.revenue.evidence")
            if v2:
                enum("revenue_basis", rev.get("basis"), f"{w}.revenue.basis")
                enum("revenue_unit", rev.get("unit"), f"{w}.revenue.unit")
                if "other" in (rev.get("basis"), rev.get("unit")) and not rev.get("note"):
                    err(f"{w}.revenue: basis/unit = other phải có note giải thích")
                chk_q(rev, cp + ["revenue"], f"{w}.revenue", "null")
            else:
                ts_ok(rev.get("ts"), f"{w}.revenue")

        if not v2:
            for val in c.get("first_users") or []:
                enum("channel", val, f"{w}.first_users")
            lvl = (c.get("demand_signal") or {}).get("level")
            if lvl is not None and lvl not in range(0, 9):
                err(f"{w}.demand_signal.level phải 0–8")
            continue

        # ---- schema 2 ----
        if c.get("depth") == "full":
            for key in vocab["case_required_v2"]:
                if key not in c:
                    err(f"{w}: thiếu trường bắt buộc '{key}' (ghi null/[] nếu video không nói)")

        cd = c.get("community_at_discovery")
        if cd is not None:
            if not isinstance(cd, dict) or "value" not in cd:
                err(f"{w}.community_at_discovery phải là {{value, insider, q, ts}} hoặc null")
            else:
                chk_q(cd, cp + ["community_at_discovery"], f"{w}.community_at_discovery", "null")
        ds = c.get("demand_signal")
        if ds is not None:
            if not isinstance(ds, dict):
                err(f"{w}.demand_signal phải là {{level, what, q, ts}} hoặc null")
            else:
                kind = ds.get("kind")
                if kind not in vocab["demand_kind"]:
                    err(f"{w}.demand_signal.kind: '{kind}' không có trong vocab.demand_kind (video không nói thì demand_signal = null)")
                else:
                    want_level = vocab["demand_kind"][kind]
                    if ds.get("level") is not None and ds["level"] != want_level:
                        err(f"{w}.demand_signal: kind {kind} ứng với level {want_level}, file ghi {ds['level']}")
                    qtxt = str(ds.get("q", ""))
                    if kind == "paid" and not re.search(
                            r"[$€£]|\b(paid|pay|payments?|purchas\w*|bought|buy|sale|sales|sold|revenue|mrr|bucks|dollars|customers?)\b",
                            qtxt, re.I):
                        err(f"{w}.demand_signal: kind=paid đòi q có tiền thật (số tiền/paid/revenue...)")
                    if kind == "similar_product_revenue" and not re.search(
                            r"\b(revenue|mrr|arr|recurring|making|makes|made|earn\w*|per month|a month|monthly|per year|a year|yearly|million)\b|/month|\d\s?k\b",
                            qtxt, re.I):
                        err(f"{w}.demand_signal: kind=similar_product_revenue đòi q nói rõ DOANH THU của sản phẩm tương tự (đang rao bán/có người dùng chưa đủ)")
                chk_q(ds, cp + ["demand_signal"], f"{w}.demand_signal", "null")
        pf = c.get("prior_failures")
        if pf is not None:
            if not isinstance(pf, dict):
                err(f"{w}.prior_failures phải là {{count, what, q, ts}} hoặc null")
            else:
                chk_q(pf, cp + ["prior_failures"], f"{w}.prior_failures", "null")
        ua = c.get("unfair_advantage")
        if ua is not None:
            if not isinstance(ua, list):
                err(f"{w}.unfair_advantage phải là danh sách")
            else:
                for j, a in enumerate(ua):
                    enum("unfair_advantage", (a or {}).get("value"), f"{w}.unfair_advantage[{j + 1}]")
                    chk_q(a, cp + ["unfair_advantage", j], f"{w}.unfair_advantage[{j + 1}]", "del")
        tr = c.get("time_to_revenue")
        if tr is not None:
            if not isinstance(tr, dict):
                err(f"{w}.time_to_revenue phải là dict hoặc null")
            else:
                for k, m in tr.items():
                    if k not in vocab["time_milestones"]:
                        err(f"{w}.time_to_revenue: khoá lạ '{k}' (hợp lệ: {vocab['time_milestones']})")
                    elif m is not None:
                        months = (m or {}).get("months") if isinstance(m, dict) else None
                        if isinstance(months, bool) or not isinstance(months, (int, float)):
                            err(f"{w}.time_to_revenue.{k}: months phải là SỐ; video không nêu khoảng thời gian thì mốc = null",
                                ("null", cp + ["time_to_revenue", k]))
                        else:
                            mq = str(m.get("q", ""))
                            if k == "to_10k_mrr" and not re.search(r"10\s?k|10,000|ten thousand|\$10|\b1[0-9]k\b|\b[2-9][0-9]k\b|\b[1-9]\d,\d{3}\b|\b\d{3},\d{3}\b|\b[1-9]\d{4,}\b|million", mq, re.I):
                                err(f"{w}.time_to_revenue.to_10k_mrr: q phải nêu mức doanh thu ≥10k (mốc này là lúc ĐẠT 10k, không phải thời điểm launch)",
                                    ("null", cp + ["time_to_revenue", k]))
                            elif k == "to_1k_mrr" and not re.search(r"\b1\s?k\b|1,000|a thousand|\$1\b|thousand|\b[1-9]k\b|\d{4,}", mq, re.I):
                                err(f"{w}.time_to_revenue.to_1k_mrr: q phải nêu mức doanh thu ~1k",
                                    ("null", cp + ["time_to_revenue", k]))
                            chk_q(m, cp + ["time_to_revenue", k], f"{w}.time_to_revenue.{k}", "null")
        fu = c.get("first_users")
        if fu is not None:
            if not isinstance(fu, list):
                err(f"{w}.first_users phải là danh sách")
            else:
                for j, u in enumerate(fu):
                    enum("channel", (u or {}).get("channel"), f"{w}.first_users[{j + 1}]")
                    chk_q(u, cp + ["first_users", j], f"{w}.first_users[{j + 1}]", "del")
        bd = c.get("build")
        if bd is not None:
            if not isinstance(bd, dict):
                err(f"{w}.build phải là {{time, cut, q, ts}} hoặc null")
            else:
                chk_q(bd, cp + ["build"], f"{w}.build", "null")

    case_ids = {c.get("id") for c in (fm.get("cases") or [])}
    for i, s in enumerate(fm.get("steps") or [], 1):
        enum("stage", s.get("stage"), f"step {i}.stage")
        ts_ok(s.get("ts"), f"step {i}")
        if v2 and s.get("case") and s["case"] not in case_ids:
            err(f"step {i}: case '{s['case']}' không có trong cases")
        if v2 and s.get("stage") in vocab["tactic_stages"]:
            if not s.get("tactic"):
                err(f"step {i} ({s.get('stage')}): thiếu `tactic`")
            else:
                enum("tactic", s["tactic"], f"step {i}.tactic")
                if s["tactic"] == "other" and not s.get("tactic_note"):
                    err(f"step {i}: tactic=other phải có tactic_note")

    for i, n in enumerate(fm.get("numbers") or [], 1):
        if n.get("evidence"):
            enum("evidence", n["evidence"], f"number {i}.evidence")
        ts_ok(n.get("ts"), f"number {i}")

    roles = {}
    for sp in fm.get("speakers") or []:
        if isinstance(sp, dict) and sp.get("name"):
            roles[norm(sp["name"]).lower()] = sp.get("role")

    def role_of(who):
        w_ = norm(who or "").lower()
        if not w_:
            return None
        if w_ in roles:
            return roles[w_]
        for name, role in roles.items():  # khớp theo họ/tên đầu (Choy vs Choi, Joseph vs Joseph Choy)
            if w_.split()[0] == name.split()[0]:
                return role
        return None

    for field in ("quotes", "rules"):
        for i, q in enumerate(fm.get(field) or []):
            tag = f"{field[:-1]} {i + 1}"
            for t in q.get("theme") or []:
                enum("quote_theme", t, f"{tag}.theme")
            if v2:
                if not q.get("stage"):
                    err(f"{tag}: thiếu stage (vocab.stage)")
                else:
                    enum("stage", q["stage"], f"{tag}.stage")
            if field == "rules" and q.get("evidence") != "opinion":
                err(f"{tag}: evidence phải là opinion")
            occ = occurrences(segs, q.get("text", ""))
            if not occ:
                err(f"{tag} ({q.get('ts')}): KHÔNG khớp nguyên văn transcript", ("del", [field, i]))
                continue
            declared = safe_sec(q.get("ts"))
            if declared not in occ:
                err(f"{tag}: ts {q.get('ts')} sai, câu nằm ở {occ}s",
                    ("setts", [field, i], locate_near(segs, q.get("text", ""), declared)))
            if v2:
                expected = vocab["role_rules"].get(role_of(q.get("who")))
                if expected and expected != field:
                    err(f"{tag}: người nói '{q.get('who')}' ({role_of(q.get('who'))}) phải ở `{expected}`",
                        ("move", field, i, expected))

    if slugs:
        for key in ("frameworks", "idea_patterns"):
            for val in fm.get(key) or []:
                if val not in slugs:
                    (warn if v2 else err)(f"{key}: '{val}' chưa có trong frameworks/candidates.md")
    return issues, long_form


def run_file(path: pathlib.Path, vocab, slugs):
    try:
        fm, _ = split_fm(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return None, [(f"YAML lỗi: {e}", None)], None
    issues, long_form = check_fm(fm, vocab, slugs)
    return fm, issues, long_form


def is_error(issue):
    return not issue[0].startswith("~")


def navigate(fm, path):
    obj = fm
    for k in path[:-1]:
        obj = obj[k]
    return obj, path[-1]


def apply_actions(fm, issues, long_form):
    """Áp các hành động tự sửa; trả về số lượng theo loại."""
    cnt = {"quote_rule_dropped": 0, "g_dropped": 0, "ts_fixed": 0, "moved": 0}
    acts = [a for _m, a in issues if a]
    for a in acts:
        if a[0] == "setts":
            parent, key = navigate(fm, a[1] + ["ts"])
            parent[key] = fmt_ts(a[2], long_form)
            cnt["ts_fixed"] += 1
    remove = {"quotes": set(), "rules": set()}
    moves = {"quotes": [], "rules": []}
    case_dels = []
    for a in acts:
        if a[0] == "null":
            parent, key = navigate(fm, a[1])
            parent[key] = None
            cnt["g_dropped"] += 1
        elif a[0] == "del":
            if a[1][0] in remove:
                remove[a[1][0]].add(a[1][1])
                cnt["quote_rule_dropped"] += 1
            else:
                case_dels.append(a[1])
        elif a[0] == "move":
            _, src, idx, dst = a
            item = dict(fm[src][idx])
            if dst == "rules":
                item["evidence"] = "opinion"
            else:
                item.pop("evidence", None)
            remove[src].add(idx)
            moves[dst].append(item)
            cnt["moved"] += 1
    for path in sorted(case_dels, key=lambda p: p[-1], reverse=True):
        parent, key = navigate(fm, path)
        del parent[key]
        cnt["g_dropped"] += 1
    for field in ("quotes", "rules"):
        if fm.get(field) is not None or moves[field]:
            kept = [x for i, x in enumerate(fm.get(field) or []) if i not in remove[field]]
            fm[field] = kept + moves[field]
    return cnt


def cmd_check(files, vocab, slugs):
    bad = nq = 0
    for f in files:
        fm, issues, _ = run_file(f, vocab, slugs)
        if fm:
            nq += len(fm.get("quotes") or []) + len(fm.get("rules") or [])
        rel = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
        errs = [i for i in issues if is_error(i)]
        if errs:
            bad += 1
            print(f"✗ {rel}")
        else:
            print(f"✓ {rel}")
        for msg, _a in issues:
            print(f"    - {msg}")
    print(f"\n{len(files)} file, {nq} quote+rule, {bad} file có lỗi")
    return 1 if bad else 0


def cmd_stats(files, vocab, slugs):
    tot = {"q": 0, "r": 0, "dq": 0, "dr": 0, "g": 0, "fx": 0, "mv": 0, "gq": 0}
    for f in files:
        fm, issues, _ = run_file(f, vocab, slugs)
        if not fm:
            print(f"? {f.name}: {issues[0][0]}")
            continue
        q, r = len(fm.get("quotes") or []), len(fm.get("rules") or [])
        dq = dr = g = fx = mv = other = 0
        for m, a in issues:
            if a and a[0] == "del" and a[1][0] == "quotes":
                dq += 1
            elif a and a[0] == "del" and a[1][0] == "rules":
                dr += 1
            elif a and a[0] in ("del", "null") and a[1][0] == "cases":
                g += 1
            elif a and a[0] == "setts":
                fx += 1
            elif a and a[0] == "move":
                mv += 1
            elif is_error((m, a)):
                other += 1
        gq = 0
        for c in fm.get("cases") or []:
            for key in ("revenue", "community_at_discovery", "demand_signal", "prior_failures", "build"):
                gq += 1 if c.get(key) else 0
            for key in ("unfair_advantage", "first_users"):
                gq += len(c.get(key) or [])
            gq += sum(1 for v in (c.get("time_to_revenue") or {}).values() if v)
        print(f"{f.name}: quote {dq}/{q} · rule {dr}/{r} bị loại · G {g}/{gq} không có chỗ dựa · {fx} ts lệch · {mv} chuyển vai · {other} lỗi khác")
        for k, v in (("q", q), ("r", r), ("dq", dq), ("dr", dr), ("g", g), ("fx", fx), ("mv", mv), ("gq", gq)):
            tot[k] += v
    qr = tot["q"] + tot["r"]
    print(f"\nTổng: quote+rule {tot['dq'] + tot['dr']}/{qr} bị loại ({100 * (tot['dq'] + tot['dr']) / qr if qr else 0:.1f}%), "
          f"G {tot['g']}/{tot['gq']} không có chỗ dựa ({100 * tot['g'] / tot['gq'] if tot['gq'] else 0:.1f}%), "
          f"{tot['fx']} ts lệch, {tot['mv']} chuyển vai")
    return 0


def cmd_prune(src: pathlib.Path, dst: pathlib.Path, vocab, slugs):
    fm, rest = split_fm(src.read_text(encoding="utf-8"))
    issues, long_form = check_fm(fm, vocab, slugs)
    cnt = apply_actions(fm, issues, long_form)
    dst.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=100) + "---" + rest,
                   encoding="utf-8")
    left = [i for i in check_fm(fm, vocab, slugs)[0] if is_error(i)]
    print(f"bỏ {cnt['quote_rule_dropped']} quote/rule, {cnt['g_dropped']} trường G không có chỗ dựa; "
          f"sửa {cnt['ts_fixed']} ts, chuyển {cnt['moved']} câu; còn {len(left)} lỗi khác → {dst}")
    for msg, _a in left:
        print(f"    - {msg}")
    return 1 if left else 0


def main() -> int:
    vocab = yaml.safe_load(VOCAB.read_text(encoding="utf-8"))
    slugs = known_slugs()
    argv = sys.argv[1:]
    if argv[:1] == ["--prune"]:
        return cmd_prune(pathlib.Path(argv[1]).resolve(), pathlib.Path(argv[2]).resolve(), vocab, slugs)
    if argv[:1] == ["--stats"]:
        return cmd_stats([pathlib.Path(a).resolve() for a in argv[1:]], vocab, slugs)
    files = [pathlib.Path(a).resolve() for a in argv] or sorted((KB / "videos").rglob("*.md"))
    return cmd_check(files, vocab, slugs)


if __name__ == "__main__":
    sys.exit(main())
