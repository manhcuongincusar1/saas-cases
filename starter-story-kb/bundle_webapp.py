#!/usr/bin/env python3
"""Ghép web/app.body.html + web/<lang>/data.json + web/i18n.json thành trang chạy được.

    python3 bundle_webapp.py            # chỉ tiếng Việt
    python3 bundle_webapp.py --all      # mọi ngôn ngữ có trong i18n.json

Kết quả:
    web/<lang>/index.html   file HTML đầy đủ, tự host được (Cloudflare Pages, mở từ đĩa)
    web/index.html          trang chuyển hướng theo ngôn ngữ trình duyệt
    web/artifact.html       thân trang tiếng Việt, để publish bằng Artifact tool
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(ROOT, "web")

# Nhãn "Ngôn ngữ" trong bảng cài đặt — chuỗi duy nhất không nằm trong i18n.json
LANG_LABEL = {
    "vi": "Ngôn ngữ", "en": "Language", "zh-Hans": "语言", "zh-Hant": "語言",
    "hi": "भाषा", "id": "Bahasa", "es": "Idioma",
}


def escape_for_script(text):
    """JSON nằm trong <script> — chặn "</script" và "<!--" bằng cách thoát mọi dấu <."""
    return text.replace("<", "\\u003c")


def build_lang(code, i18n, roster, body_tpl):
    data_path = os.path.join(WEB, code, "data.json")
    if not os.path.exists(data_path):
        print(f"  bỏ qua {code}: chưa có {os.path.relpath(data_path, ROOT)}"
              f" — chạy build_webapp.py --lang {code} trước")
        return None

    T = dict(i18n[code])
    T["_all"] = roster
    T["_langLabel"] = LANG_LABEL.get(code, "Language")

    with open(data_path, encoding="utf-8") as fh:
        data = fh.read()

    page = body_tpl
    page = page.replace("__I18N__", escape_for_script(json.dumps(T, ensure_ascii=False)))
    page = page.replace("__DATA__", escape_for_script(data))
    page = re.sub(r"<title>.*?</title>", f"<title>{T['title']}</title>", page, count=1)

    head, rest = page.split('<div class="shell"', 1)
    standalone = (
        '<!doctype html>\n<html lang="' + code + '" dir="' + T.get("dir", "ltr") + '">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="description" content="' + T["sub"].replace('"', "&quot;") + '">\n'
        '<meta name="theme-color" content="#F1F3F0" media="(prefers-color-scheme: light)">\n'
        '<meta name="theme-color" content="#0E1412" media="(prefers-color-scheme: dark)">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="' + T["title"] + '">\n'
        + "".join(f'<link rel="alternate" hreflang="{l["code"]}" href="../{l["code"]}/">\n'
                  for l in roster)
        + '<style>html{color-scheme:light dark}body{margin:0;font:14px system-ui,sans-serif}'
        'img{max-width:100%}[hidden]{display:none!important}</style>\n'
        + head
        + '</head>\n<body>\n<div class="shell"' + rest
        + "\n</body>\n</html>\n"
    )

    out_dir = os.path.join(WEB, code)
    os.makedirs(out_dir, exist_ok=True)
    idx = os.path.join(out_dir, "index.html")
    with open(idx, "w", encoding="utf-8") as fh:
        fh.write(standalone)
    print(f"  {os.path.relpath(idx, ROOT):26} {os.path.getsize(idx)/1e6:.2f} MB  {T['title']}")

    if code == "vi":
        art = os.path.join(WEB, "artifact.html")
        with open(art, "w", encoding="utf-8") as fh:
            fh.write(page)
        print(f"  {os.path.relpath(art, ROOT):26} {os.path.getsize(art)/1e6:.2f} MB  (Artifact)")
    return code


def write_redirect(roster, default="en"):
    """Trang gốc: đoán ngôn ngữ từ trình duyệt, có link tay cho mọi bản."""
    codes = [l["code"] for l in roster]
    links = "\n".join(
        f'  <a href="{l["code"]}/">{l["native"]}</a>' for l in roster
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Starter Story Knowledge Base</title>
<style>
  :root{{color-scheme:light dark}}
  body{{margin:0;min-height:100svh;display:flex;flex-direction:column;align-items:center;
    justify-content:center;gap:18px;background:#F1F3F0;color:#16211D;
    font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;padding:24px}}
  @media (prefers-color-scheme:dark){{body{{background:#0E1412;color:#E7ECE8}}}}
  p{{margin:0;opacity:.65;font-size:13px}}
  nav{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;max-width:420px}}
  a{{padding:8px 14px;border-radius:8px;border:1px solid currentColor;text-decoration:none;
    color:inherit;opacity:.8;font-weight:500}}
  a:hover{{opacity:1}}
</style>
</head>
<body>
<p>Choose your language</p>
<nav>
{links}
</nav>
<script>
(function(){{
  var have = {json.dumps(codes)};
  var want = (navigator.languages || [navigator.language || ""]).map(String);
  for (var i = 0; i < want.length; i++) {{
    var w = want[i];
    for (var j = 0; j < have.length; j++) {{
      if (w.toLowerCase() === have[j].toLowerCase()) return go(have[j]);
    }}
    var base = w.split("-")[0].toLowerCase();
    if (base === "zh") return go(/hant|tw|hk|mo/i.test(w) ? "zh-Hant" : "zh-Hans");
    for (var k = 0; k < have.length; k++) {{
      if (have[k].split("-")[0].toLowerCase() === base) return go(have[k]);
    }}
  }}
  go({json.dumps(default)});
  function go(c) {{ location.replace(c + "/" + (location.hash || "")); }}
}})();
</script>
</body>
</html>
"""
    path = os.path.join(WEB, "index.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"  {os.path.relpath(path, ROOT):26} {os.path.getsize(path)/1e3:.1f} KB  (chuyển hướng)")


def main():
    with open(os.path.join(WEB, "i18n.json"), encoding="utf-8") as fh:
        i18n = json.load(fh)
    with open(os.path.join(WEB, "app.body.html"), encoding="utf-8") as fh:
        body_tpl = fh.read()
    for token in ("__DATA__", "__I18N__"):
        assert token in body_tpl, f"thiếu chỗ chèn {token} trong app.body.html"

    targets = list(i18n) if "--all" in sys.argv else ["vi"]
    # chỉ liệt kê trong bộ chuyển ngôn ngữ những bản thật sự đã build
    roster = [{"code": c, "native": i18n[c]["native"]}
              for c in i18n
              if os.path.exists(os.path.join(WEB, c, "data.json"))]

    print("Đã dựng:")
    built = [c for c in targets if build_lang(c, i18n, roster, body_tpl)]
    if len(roster) > 1:
        write_redirect(roster, "en" if "en" in roster[0]["code"] or any(
            r["code"] == "en" for r in roster) else roster[0]["code"])
    if not built:
        sys.exit("Không dựng được bản nào.")


if __name__ == "__main__":
    main()
