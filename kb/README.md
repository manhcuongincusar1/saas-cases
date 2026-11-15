# kb — cơ sở dữ liệu "người thành công đã làm gì"

> Bản nháp cấu trúc, 15/11/2026. Mới chạy thử trên 10 video (5 Superwall + 5 Starter Story mới nhất).
> Mục đích: giúp tôi thoát vòng "build xong không ai dùng, không ai biết". Mọi thứ ở đây phải trả lời được:
> **ý tưởng đến từ đâu → biết có người cần bằng cách nào → người dùng đầu tiên đến từ đâu → họ nghĩ gì để không bỏ cuộc.**

## Ba lớp dữ liệu

```
SAAS/
├── starter-story-kb/videos/…/transcript.md    ┐ LỚP 1 — NGUỒN GỐC (full text, không sửa)
├── superwall/youtube-transcript/…/transcript.md┘  Transcript đầy đủ có mốc thời gian.
│
├── kb/                                          LỚP 2 — PHÂN TÍCH (viết tay / subagent, có kiểm)
│   ├── README.md                ← file này: cấu trúc, schema, từ vựng chung
│   ├── videos/<kênh>/<ngày>_<slug>.md   ← 1 file / video: YAML (dữ liệu) + ghi chú tiếng Việt
│   ├── frameworks/<slug>.md     ← cách làm lặp lại, gom từ nhiều video (candidates.md = đang theo dõi)
│   ├── scripts/check.py         ← kiểm: câu trích có đúng nguyên văn + đúng giây không
│   └── data/kb.duckdb           ← LỚP 3 — sinh tự động từ lớp 1 + 2 (không sửa tay, không commit)
│
├── journey/                                     HÀNH TRÌNH CỦA TÔI (dùng cùng từ vựng với kb)
│   ├── MAP.md                   ← tôi đang ở chặng nào, mỗi chặng cần trả lời gì
│   └── ideas/<slug>.md          ← mỗi ý tưởng: nguồn từ case nào, qua cổng nào của VALIDATE.md
│
└── VALIDATE.md                  ← 4 cổng + thang tín hiệu 0–8 (kb dùng lại thang này)
```

**Vì sao giữ full text:** câu trích (mindset) và số liệu trong lớp 2 luôn trỏ về đúng giây trong lớp 1. Không tóm tắt lại thành lời mình rồi bỏ nguồn. Khi DB được dựng, toàn bộ transcript cũng nằm trong bảng `segments` để tìm full-text trên cả ~260 video.

## File video (lớp 2)

Mỗi video một file Markdown. Phần YAML ở đầu là **dữ liệu** (script đọc để dựng DB). Phần thân là ghi chú tiếng Việt cho người đọc.

```yaml
---
video_id: X2T92MVx7xs
channel: starter-story            # starter-story | starter-story-build | superwall
title: "How I Made $1M Building 30 Micro-Apps"
date: 2026-11-08
url: https://www.youtube.com/watch?v=X2T92MVx7xs
transcript: starter-story-kb/videos/…/transcript.md   # đường dẫn từ gốc repo
kind: founder_case                # founder_case | expert_talk | host_essay
speakers: [{name: Sanskar, role: founder}, {name: Gus, role: host}]
bias: "…"                         # ai được lợi nếu mình tin video này (nhà tài trợ, bán khoá học, agency…)
cases:                            # sản phẩm được kể trong video (depth: full | mention)
  - id: magicslides
    product: …
    revenue: {amount: 1000000, unit: usd, basis: lifetime, ts: "03:00", evidence: claimed}
    idea_origin: [user_request, adjacent_expansion]
    demand_signal: {level: 0, what: "…"}     # thang 0–8 của VALIDATE.md
    first_users: [facebook_groups, appsumo]
    scale_channels: [youtube_founder, platform_marketplace]
steps:                            # họ đã làm gì, theo chặng
  - {stage: find-idea, ts: "02:11", case: magicslides, what: "…"}
quotes:                           # NGUYÊN VĂN từ transcript — check.py sẽ dò lại
  - {ts: "13:38", who: Sanskar, theme: [stuck-on-one-thing], text: "…", vi: "…"}
numbers:                          # benchmark đáng tra
  - {ts: "…", metric: …, value: …, unit: …, evidence: measured}
frameworks: [sell-before-build, many-small-bets]
idea_patterns: [single-feature-on-platform]
---
## Một câu
## Bài học cho tôi        (solo founder ở VN, bán global)
## Đừng tin vội           (bias, survivor bias, điều kiện riêng không sao chép được)
```

Quy ước:
- `ts` luôn để trong ngoặc kép (`"13:38"`, `"00:13:08"`), nếu không YAML sẽ đọc thành số.
- `ts` = mốc đầu dòng/đoạn transcript chứa chỗ bắt đầu câu trích. Link YouTube `?t=` được sinh tự động.
- `text` của quote phải khớp nguyên văn transcript (kể cả lỗi auto-caption như `[music]`). Dịch/diễn giải để ở `vi`.
- `evidence`: `measured` (có dashboard/ảnh màn hình), `claimed` (nói miệng), `opinion` (quan điểm).

## Từ vựng chung (dùng cho cả kb lẫn journey)

**stage** — chặng của hành trình:

| stage | Câu hỏi của chặng |
|---|---|
| `mindset` | (xuyên suốt) họ nghĩ gì để tiếp tục, để quyết |
| `find-idea` | ý tưởng đến từ đâu? |
| `validate` | biết có người cần bằng cách nào, *trước khi* build xong? |
| `build` | làm bản đầu bao lâu, bằng gì, cắt bớt cái gì? |
| `launch` | 10–100 người dùng/khách đầu tiên đến từ đâu? |
| `monetize` | thu tiền thế nào (giá, gói, paywall)? |
| `grow` | kênh nào đưa từ vài nghìn lên vài chục nghìn $/tháng? |
| `retain` | giữ người dùng thế nào? |
| `scale` | team, đối tác, bán/exit |

**idea_origin** — `own_pain` (nỗi đau của chính mình) · `domain_expertise` (nghề/kiến thức sâu) · `audience_signal` (nội dung mình đăng được hưởng ứng) · `user_request` (người dùng xin bản hẹp hơn) · `niche_down` (ngách con trong danh mục đã có tiền) · `passion_skin` (tiện ích phổ thông + chủ đề người ta mê) · `adjacent_expansion` (mở sang nền tảng/ngách kề) · `revenue_scouting` (soi doanh thu: top charts, Sensor Tower, TrustMRR) · `trend_copy` (chép trend)

**demand_signal.level** — thang của `VALIDATE.md`: 0 = build rồi mới chờ · 1 bạn bè khen · 2 view nhiều · 3 app tương tự đang bán được · 4 người ta tự kể nỗi đau · 5 comment hỏi mua · 6 Mom Test lặp lại · 7 người lạ DM xin · 8 có người trả tiền khi sản phẩm còn thô

**channel** — `facebook_groups` · `reddit` · `seo` · `appsumo` · `platform_marketplace` (Chrome Web Store, Google Workspace…) · `app_store_search` · `own_audience` · `founder_led_content` · `youtube_founder` · `instagram_reels` · `tiktok_organic` · `influencer_partner` (chia equity) · `influencer_paid` · `ugc_creators` · `clipping` · `paid_meta` · `paid_tiktok` · `paid_google` · `word_of_mouth` · `b2b_deals`

**quote theme** (mindset) — `ship-ugly` · `sell-before-build` · `builder-trap` · `many-bets` · `focus-one-thing` · `persistence` · `action-over-research` · `emotional-bottleneck` · `right-audience` · `clarity` · `revenue-first` · `risk-and-leap` · `learn-from-others` · `passion-fuel` · `stuck-on-one-thing`

Từ vựng được thêm khi gặp cái mới, nhưng phải ghi vào bảng trên trước rồi mới dùng.

## Framework (lớp 2)

- Một cách làm vào `frameworks/candidates.md` ngay khi thấy ở 1 video.
- Thành file riêng `frameworks/<slug>.md` khi có **≥3 founder độc lập** làm giống nhau (host/agency nói không tính là founder).
- File framework ghi: các bước · khi nào dùng · ai đã làm (link đúng giây) · **phản ví dụ** · solo founder bán global làm được không.

## DB (lớp 3) — sẽ dựng ở bước sau

`kb/scripts/build.py` đọc toàn bộ `kb/videos/**/*.md`, `journey/ideas/*.md` và transcript gốc → `kb/data/kb.duckdb`:

| Bảng | Một dòng là |
|---|---|
| `videos` | 1 video (kênh, ngày, loại, bias) |
| `cases` | 1 sản phẩm (doanh thu, nguồn ý tưởng, mức tín hiệu, kênh đầu, kênh scale) |
| `steps` | 1 việc founder đã làm ở 1 chặng, kèm link giây |
| `quotes` | 1 câu nói nguyên văn + chủ đề mindset |
| `numbers` | 1 con số benchmark |
| `video_frameworks`, `video_idea_patterns` | liên kết video ↔ framework / mẫu ý tưởng |
| `segments` | 1 đoạn transcript (full text của mọi video, có mốc giây) |
| `my_ideas` | 1 ý tưởng của tôi + cổng VALIDATE đã qua |

Ví dụ câu hỏi DB sẽ trả lời:

```sql
-- Mọi câu nói về "bán trước khi build", kèm link đúng giây
SELECT who, text, url FROM quotes WHERE list_contains(theme, 'sell-before-build');
-- Người dùng đầu tiên đến từ đâu, đếm theo kênh
SELECT ch, count(*) FROM cases, unnest(first_users) AS t(ch) GROUP BY ch ORDER BY 2 DESC;
-- Ai build xong mới chờ (level 0) mà vẫn thành công, và họ làm gì sau đó?
SELECT product, idea_origin, first_users FROM cases WHERE demand_signal_level = 0;
-- Tìm full-text trên ~260 video
SELECT url, text FROM segments WHERE text ILIKE '%buy button%';
```

## Kiểm chất lượng

```bash
python3 kb/scripts/check.py          # mọi quote phải khớp nguyên văn và đúng mốc giây
```

Khi cho subagent điền các video còn lại: subagent chỉ điền YAML theo đúng mẫu, tôi chạy `check.py`, quote nào không khớp thì trả lại.
