# Schema 2 của file video (kb/videos/<kênh>/<ngày>_<slug>.md)

> Thay cho mẫu trong `README.md`. File cũ (không có `schema: 2`) vẫn kiểm theo schema 1 cho tới khi được nâng cấp.
> Mỗi video MỘT file. Đọc một lượt, trả lời cả 3 câu hỏi của user: **tìm ý tưởng thế nào, validate thế nào, grow thế nào**.
> Quy tắc vàng: **video không nói thì ghi `null` (hoặc `[]`), cấm suy đoán — và "không suy đoán" phải máy kiểm được:**
> `revenue` và mọi trường G khác null đều có `q` = đoạn NGUYÊN VĂN ngắn (≤ ~25 từ) làm chỗ dựa. `check.py` dò `q` bằng cùng hàm dò quote; không khớp thì `--prune` đưa trường đó về null/[].

## Khung

```yaml
---
schema: 2
video_id: abc123
channel: starter-story            # starter-story | starter-story-build | superwall
title: "…"
date: 2026-10-28
url: https://www.youtube.com/watch?v=abc123
transcript: starter-story-kb/videos/<thư-mục>/transcript.md     # đường dẫn từ gốc repo
kind: founder_case                # founder_case | expert_talk | host_essay
speakers: [{name: Jake, role: founder}, {name: Gus, role: host}]    # role: founder | host | expert
bias: "Ai được lợi nếu ta tin video này (nhà tài trợ, phễu bán khoá/tư vấn, nhà tuyển dụng creator…)."
analyzed: 2026-11-15
cases:                            # mỗi sản phẩm được kể; depth: full = founder kể kỹ, mention = chỉ nhắc
  - id: kebab-slug
    depth: full
    product: "Tên + một câu"
    what: "Làm gì"
    type: [web-app]
    customer: "Ai dùng/trả tiền"
    founder: {who: …, base: …, technical: true|false|null, team: …, background: …}
    revenue: {amount: 30000, unit: usd, basis: last_28_days, note: …, q: "nguyên văn", ts: "02:28", evidence: measured|claimed}
    pricing: "…"
    idea_origin: [own_pain]       # vocab.idea_origin (có timing_trigger)
    scale_channels: [seo]         # vocab.channel (có paid_unspecified)
    # ---- 6 câu G bắt buộc cho depth: full (null nếu video không nói); mỗi trường khác null có q + ts ----
    community_at_discovery:       # G1: lúc thấy vấn đề, founder đang ở cộng đồng/nơi nào? người trong cuộc không?
      {value: "…", insider: true, q: "…", ts: "04:23"}
    demand_signal:                # G2: LOẠI bằng chứng nhu cầu TRƯỚC khi build xong; `level` (thang 0–8 của VALIDATE.md) suy ra từ kind
      {kind: paid, level: 8, what: "…", q: "…", ts: "04:56"}   # kind ∈ vocab.demand_kind; không nói thì demand_signal = null
    prior_failures:               # G3
      {count: 2, what: "…", q: "…", ts: "…"}
    unfair_advantage:             # G4: vocab.unfair_advantage; [] nếu video không nói; mỗi mục có q
      - {value: domain_expertise, what: "…", q: "…", ts: "04:23"}
    time_to_revenue:              # G5: ĐẾM ĐƯỢC. Mỗi mốc là null hoặc {months: SỐ, value: lời founder, q, ts}
      first_dollar: null          #   video không nêu khoảng thời gian bằng số tháng → mốc = null, KHÔNG điền mô tả thay
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 66, value: "5–6 năm", q: "I built it 5 or 6 years ago", ts: "00:50"}   # từ lúc bắt đầu tới mức ở `revenue`
    first_users:                  # G6: 10 người dùng đầu tiên đến từ đâu (vocab.channel); mỗi mục có q
      - {channel: seo, what: "…", q: "…", ts: "07:07"}
    build:                        # chỉ thời gian build và thứ đã cắt bỏ; KHÔNG ghi tech stack
      {time: "…", cut: ["…"], q: "…", ts: "05:45"}
steps:                            # họ đã làm gì, theo chặng
  - stage: find-idea              # vocab.stage
    ts: "04:23"
    case: excel-exercises
    what: "…"                     # 1 câu tiếng Việt
    tactic: s5-insider-pain       # BẮT BUỘC ở find-idea/validate/launch/monetize/grow/retain; vocab.tactic (xem định nghĩa trong vocab)
    tool: "Sensor Tower"          # tuỳ chọn, chỉ khi founder nêu
    threshold: ">10k/tháng"       # tuỳ chọn: con số ngưỡng founder nêu
    cost: "$100/tháng"            # tuỳ chọn
    tactic_note: "…"              # tuỳ chọn với mọi tactic (ghi biến thể); BẮT BUỘC khi tactic: other
quotes:                           # CÂU CỦA FOUNDER (role founder) — mindset và cách họ nghĩ; nguyên văn
  - {ts: "13:38", who: Sanskar, stage: mindset, theme: [builder-trap], text: "…nguyên văn…", vi: "…"}
rules:                            # CÂU CỦA HOST/EXPERT (role host hoặc expert) — luật, khuyến nghị, lời chốt; nguyên văn
  - {ts: "00:01:24", who: Joseph Choy, stage: validate, theme: [sell-before-build], text: "…nguyên văn…", vi: "…", evidence: opinion}
numbers:
  - {ts: "02:28", metric: "…", value: 2500, unit: count, evidence: measured}
frameworks: [slug]                # nên có trong frameworks/candidates.md; slug mới chỉ là cảnh báo
idea_patterns: [slug]
---
## Một câu
## Bài học cho tôi        (tối đa 2 gạch đầu dòng, mỗi gạch gắn một ts; không có gì cụ thể thì bỏ trống)
## Đừng tin vội           (bias, survivor bias, điều kiện riêng không sao chép được, thứ video không nói)
```

## Quy ước

- `ts`: chuỗi trong ngoặc kép, đúng như trong transcript (`"07:07"` hoặc `"00:07:07"`), là mốc **đầu dòng/đoạn** chứa chỗ bắt đầu ý đó. Một câu có thể xuất hiện hai lần (teaser đầu tập lặp câu ở giữa tập): `ts` hợp lệ nếu khớp bất kỳ lần nào; khi `check.py` phải sửa thì chọn lần gần `ts` đã ghi nhất, không tự đổi về teaser.
- `quotes`/`rules`: `text` là một chuỗi liền, copy nguyên văn từ transcript (kể cả lỗi chính tả, `[music]`). Bắt buộc có `stage` (vocab.stage); `theme` được phép `[]` (đừng ép theme khi không hợp; `theme` chủ yếu phủ mindset). Không khớp thì bị bỏ.
- **Luật vai trò (máy kiểm):** người nói có role `host`/`expert` thì câu vào `rules`; role `founder` vào `quotes`. Khai `speakers` đầy đủ.
- **Tactic:** mỗi giá trị trong `vocab.yaml` có định nghĩa "là gì / KHÔNG tính". **Không chắc thì dùng `tactic: other` + `tactic_note`: gắn sai tệ hơn gắn other.**
- **`demand_signal.kind`** (vocab.demand_kind): built_first→0 · friends_praise→1 · content_views→2 · similar_product_revenue→3 · self_reported_pain_or_free_waitlist→4 · buy_intent_comments→5 · repeated_interviews→6 · inbound_requests→7 · paid→8. Chọn LOẠI bằng chứng mà `q` thật sự chứng minh; `level` nếu ghi phải khớp (check.py kiểm). `kind: paid` đòi `q` có tiền thật (số tiền/"paid"/"revenue"…): "pre-order" hay "8K" không rõ là lượt hay tiền thì KHÔNG phải paid. Waitlist miễn phí = mức 4.
- **`demand_signal` chỉ tính tín hiệu có TRƯỚC lần ra mắt công khai đầu tiên.** Doanh thu sau khi đã launch và chạy marketing thuộc `first_users`/`time_to_revenue`, không phải `paid` (trừ khi video nói khoản đó đến trước launch). Follower/audience có sẵn là `unfair_advantage: existing_audience`, không phải demand_signal; `content_views` chỉ giữ khi nội dung nói về chính vấn đề/ý tưởng của sản phẩm. `similar_product_revenue` đòi `q` nêu doanh thu; `to_1k_mrr`/`to_10k_mrr` đòi `q` nêu mức doanh thu.
- **Không viết step khi video chỉ nói "không nêu cách/kênh"**; ghi sự kiện đó vào trường của case (`first_users` kèm lời "video không nói", `demand_signal`, hoặc `numbers`). Không có giá trị `unspecified`.
- **`revenue.basis`** ∈ vocab.revenue_basis (mrr, monthly, arr, annual, last_28_days, last_30_days, lifetime, best_month, other) và **`revenue.unit`** ∈ (usd, eur, gbp, other); `other` bắt buộc có `revenue.note`.
- **`channel`:** `app_store_search` là tìm kiếm ORGANIC (ASO). Mọi kênh trả tiền phải là `paid_*` (paid_meta, paid_tiktok, paid_google, paid_apple_search, paid_unspecified) hoặc `influencer_paid`; Apple Search Ads KHÔNG phải app_store_search.
- **`tactic`:** mỗi tactic trong `vocab.yaml` có `chapter` (find / validate / grow) và `def`. Ranh giới: g3 = ĐĂNG GÌ (format, hook); g6 = tiền trả cho nền tảng quảng cáo (kể cả chạy từ ngày đầu); g7 = làm việc với NGƯỜI (creator, clipper, agency: tuyển, trả, quản; clipping trả theo view thuộc g7). Step chỉ ghi VIỆC ĐÃ LÀM hoặc quy trình có bước cụ thể mà expert mô tả; lời khuyên chung vào quotes/rules.
- `evidence`: `measured` CHỈ khi host bảo mở dashboard và founder đọc số từ đó (hoặc ảnh chụp màn hình hiện trong video); còn lại mặc định `claimed`. Lời khuyên/quan điểm: `opinion`.
- `time_to_revenue`: `months` là SỐ. Chỉ ghi khi video nêu khoảng thời gian; `to_current` (từ lúc bắt đầu tới mức ở `revenue`) gần như video nào cũng có thể ghi. Không nêu thì mốc = null.
- Video build: chỉ ghi `build.time` và `build.cut`; bỏ tech stack. Scale: chỉ ghi nếu liên quan grow.
- Video nhiều founder: mỗi sản phẩm một `case`; video host_essay: `cases` có thể rỗng hoặc chỉ `depth: mention`.
- `idea_origin: [timing_trigger]` khi ý tưởng gắn với luật mới, mùa vụ, sự kiện, sản phẩm/nền tảng mới ra.
- Phần thân: subagent viết "Một câu" và "Đừng tin vội". "Bài học cho tôi" tối đa 2 gạch đầu dòng, mỗi gạch gắn một ts. Bài học tổng hợp để sau, làm trên nhiều case.

## Kiểm

```bash
python3 -I kb/scripts/check.py kb/videos/<kênh>/<file>.md      # kiểm một file
python3 -I kb/scripts/check.py --stats <file> ...               # đếm quote/rule bị loại, G không có chỗ dựa, ts lệch, chuyển vai
python3 -I kb/scripts/check.py --prune <vào.md> <ra.md>         # bỏ quote/rule và G không có chỗ dựa, sửa ts, chuyển vai, ghi file mới
```
