---
schema: 2
video_id: NvtsM8Nk72c
channel: starter-story
title: "How I Built It: $23K/month micro-saas"
date: 2025-08-13
url: https://www.youtube.com/watch?v=NvtsM8Nk72c
transcript: starter-story-kb/videos/2025-08-13_how-i-built-it-23k-month-micro-saas/transcript.md
kind: founder_case
speakers:
- {name: Andy Cloak, role: founder}
- {name: Pat Walls, role: host}
bias: "Starter Story bán chương trình Starter Story Build (dạy làm app bằng AI) được quảng cáo giữa và cuối video; founder được chọn làm case; số liệu founder tự nêu, không có dashboard."
analyzed: 2026-11-15
cases:
- id: data-fetcher
  depth: full
  product: "Data Fetcher: add-on Airtable kéo dữ liệu từ API các nền tảng khác về bảng Airtable và tự chạy theo lịch"
  what: "Kết nối Airtable với API các nền tảng khác (ví dụ Facebook Ads, Google Analytics) và tự lên lịch đồng bộ; người dùng marketing và vận hành"
  type: [airtable-extension]
  customer: "Người làm marketing và vận hành cần đưa dữ liệu từ nhiều nền tảng vào Airtable"
  founder: {who: Andy Cloak, base: "London", technical: true, team: solo, background: "Học kỹ sư nhưng tự học code; làm freelance React developer cho startup ở London; trước đó bán một SaaS scrape dữ liệu TikTok"}
  revenue: {amount: 23000, unit: usd, basis: mrr, note: "600 khách trả tiền; founder nói đây là doanh thu hiện tại, định kỳ hằng tháng", q: "it makes $23,000 a month in current revenue", ts: "00:47", evidence: claimed}
  pricing: null
  idea_origin: [own_pain, timing_trigger]
  scale_channels: [platform_marketplace, seo, youtube_founder]
  community_at_discovery:
    value: "Founder đã gặp chính vấn đề này khi dùng Airtable; sau đó đọc forum Airtable để xem người dùng đang gặp gì"
    insider: true
    q: "having run into this problem on Air Table before"
    ts: "02:36"
  demand_signal:
    kind: self_reported_pain_or_free_waitlist
    level: 4
    what: "Đọc forum Airtable thấy người ta tự kể vấn đề; có vẻ cần một công cụ linh hoạt. Đây là trước khi build xong"
    q: "there seemed to be this need for like a really flexible tool"
    ts: "02:51"
  prior_failures:
    count: null
    what: "Vài năm làm dự án phụ bỏ dở, khoảng 6 tháng bị mất; nguyên nhân thật là tăng trưởng chậm và chán"
    q: "I've wasted probably 6 months trying to launch side businesses"
    ts: "09:03"
  unfair_advantage:
  - {value: technical_skill, what: "Tự học code, làm freelance React developer", q: "I taught myself to code", ts: "01:03"}
  - {value: prior_success, what: "Đã bán một SaaS scrape TikTok khi nó đạt vài nghìn USD MRR; số tiền đó giúp nghỉ vài tháng để làm việc khác", q: "I sold it and that kind of bought me a few months off", ts: "01:18"}
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: {months: 12, value: "sau năm đầu tiên", q: "that drove it through to 10,000 in MR after the first year", ts: "07:29"}
    to_current: {months: 60, value: "khoảng 5 năm từ lúc bắt đầu tới nay", q: "the use cases honestly keep on surprising me like even 5 years in", ts: "02:06"}
  first_users:
  - {channel: platform_marketplace, what: "Đứng trên marketplace của Airtable từ sớm; khách đầu tiên đến trong vài ngày", q: "I got the first customer after a few days", ts: "06:58"}
  build: null
steps:
- stage: find-idea
  ts: "02:21"
  case: data-fetcher
  what: "Thấy add-on API Connector cho Google Sheets chạy rất tốt (khoảng 100.000 user) rồi đem ý tưởng sang Airtable."
  tactic: s11-copy-or-localize-proven
- stage: find-idea
  ts: "02:36"
  case: data-fetcher
  what: "Airtable vừa tăng trưởng nhanh và vừa mở marketplace; làm add-on ngay trên nền tảng mới."
  tactic: s12-timing-shift
- stage: find-idea
  ts: "02:36"
  case: data-fetcher
  what: "Founder từng gặp chính vấn đề này khi dùng Airtable."
  tactic: s5-insider
  tactic_note: "nỗi đau riêng khi dùng Airtable"
- stage: validate
  ts: "02:36"
  case: data-fetcher
  what: "Đọc forum của Airtable để tìm vấn đề người ta đang gặp; thấy có nhu cầu công cụ linh hoạt."
  tactic: s3-reddit-pain-mining
  tactic_note: "đọc forum của chính nền tảng (Airtable), không phải Reddit"
- stage: launch
  ts: "06:58"
  case: data-fetcher
  what: "Đưa sản phẩm lên marketplace của Airtable khi nền tảng còn sớm; khách đầu tiên đến sau vài ngày."
  tactic: g9-launch-platforms
- stage: grow
  ts: "06:58"
  case: data-fetcher
  what: "Viết blog và làm video YouTube về các integration lặp lại mà người dùng hỏi."
  tactic: g2-aso-seo-organic
  tactic_note: "blog SEO và video YouTube về integration phổ biến"
- stage: grow
  ts: "07:14"
  case: data-fetcher
  what: "Làm thêm tích hợp no-code để người ít kỹ thuật dùng được; MRR lên khoảng 10K sau năm đầu."
  tactic: other
  tactic_note: "đổi sản phẩm: thêm tích hợp no-code cho người ít kỹ thuật (không phải kênh marketing)"
- stage: retain
  ts: "10:04"
  case: data-fetcher
  what: "Nói chuyện trực tiếp với người dùng đang dùng; một buổi chiều tìm ra nhiều lỗi UX và sửa, doanh thu và usage tăng gần như ngay."
  tactic: g5-retention
quotes:
- {ts: "03:40", who: Andy Cloak, stage: launch, theme: [], text: "So, the main benefit I guess is distribution, right?", vi: "Lợi ích chính là phân phối: được đứng trên marketplace sớm thì khách đều đặn."}
- {ts: "09:03", who: Andy Cloak, stage: mindset, theme: [focus-one-thing], text: "The biggest lesson has been the power of focus over chasing shiny objects.", vi: "Bài học lớn nhất là tập trung, không phải chạy theo thứ mới lạ."}
- {ts: "09:18", who: Andy Cloak, stage: mindset, theme: [emotional-bottleneck], text: "But really, it was cuz growth had slowed and I was getting bored and losing motivation.", vi: "Thật ra là vì tăng trưởng chậm lại, tôi chán và mất động lực."}
- {ts: "09:18", who: Andy Cloak, stage: mindset, theme: [focus-one-thing], text: "So, every time I start to get distracted or I'm not working hard enough, I literally go to Claude", vi: "Mỗi lần mất tập trung hay thấy mình lười, tôi dùng Claude làm business coach để giữ mình ở việc đang chạy."}
- {ts: "09:49", who: Andy Cloak, stage: retain, theme: [right-audience], text: "I'd tell young Andy to do proper user testing. do it early and do it often", vi: "Tôi sẽ nói với Andy trẻ: test với người dùng thật, làm sớm và làm thường xuyên."}
rules:
- {ts: "10:20", who: Pat Walls, stage: retain, theme: [], text: "Talk to your customers.", vi: "Hãy nói chuyện với khách hàng của bạn.", evidence: opinion}
numbers:
- {ts: "00:47", metric: "khách trả tiền", value: 600, unit: count, evidence: claimed}
- {ts: "08:31", metric: "chi phí hosting mỗi tháng", value: 2500, unit: usd_per_month, evidence: claimed}
- {ts: "08:48", metric: "margin tổng", value: 0.85, unit: ratio, evidence: claimed}
frameworks: [platform-marketplace-distribution]
idea_patterns: [single-feature-on-platform]
---

## Một câu

Andy Cloak làm Data Fetcher, một add-on cho Airtable kéo dữ liệu từ API các nền tảng khác về bảng; ý tưởng chép từ add-on Google Sheets và đi vào marketplace của Airtable khi nền tảng này đang lên. Hiện khoảng 23K USD MRR từ 600 khách.

## Bài học cho tôi

- Chép một add-on đã chạy tốt sang nền tảng mới đang tăng trưởng và mở marketplace; vào sớm nên khách đầu tiên đến trong vài ngày (`02:36`).
- Một buổi nói chuyện với người dùng đang dùng tìm ra lỗi UX và sửa; doanh thu và usage tăng gần như ngay. Founder nói mình đã phí gần một năm không nói với người dùng (`10:04`).

## Đừng tin vội

- Số liệu founder tự nêu (600 khách, 23K/tháng, margin 85%), không có dashboard. Video là quảng cáo cho Starter Story Build (bias).
- Thành công phụ thuộc vào Airtable đang lên và marketplace của họ; chính Andy nói đây là "platform risk", nền tảng có thể tự làm tính năng.
- Video không nói thời gian build; mốc 1K MRR chỉ có "vài tháng" nên không đếm được.
- Founder có nền kỹ thuật (tự học code, làm freelance React) và từng bán một SaaS trước đó: điều kiện không phải ai cũng có.
