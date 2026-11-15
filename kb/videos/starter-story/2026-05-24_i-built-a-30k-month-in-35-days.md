---
schema: 2
video_id: vbEKEWtnndU
channel: starter-story
title: "I Built A $30K/Month in 35 Days"
date: 2026-05-24
url: https://www.youtube.com/watch?v=vbEKEWtnndU
transcript: starter-story-kb/videos/2026-05-24_i-built-a-30k-month-in-35-days/transcript.md
kind: founder_case
speakers:
  - {name: Cedric Roberge, role: founder}
  - {name: Pat Walls, role: host}
  - {name: Gus, role: host}
bias: "Video quảng bá iOS bootcamp miễn phí của Starter Story Build (phễu của kênh), Cedric là case để kể câu chuyện thành công. Số liệu là dashboard founder đọc trên video, không kiểm được ngoài video."
analyzed: 2026-11-15
cases:
  - id: pep-ai
    depth: full
    product: "Pep AI: app iOS theo dõi peptide (tính liều từ lọ, nhật ký tiêm, thư viện nghiên cứu)"
    what: "Máy tính liều từ lọ và nước pha, nhật ký liều và vị trí tiêm, quiz kiểu Duolingo, thư viện nghiên cứu có nguồn PubMed, theo dõi dinh dưỡng và cân nặng"
    type: [ios-app]
    customer: "Người dùng peptide (giảm cân, da, phục hồi chấn thương) muốn tự theo dõi liều an toàn"
    founder:
      who: Cedric Roberge
      base: null
      technical: null
      team: null
      background: "Sinh viên đại học; app sinh viên đầu tiên (marketplace, University of Oregon) có ~800 người dùng nhưng không ra tiền"
    revenue:
      amount: 33000
      unit: usd
      basis: last_28_days
      note: "Dashboard: 33K doanh thu 28 ngày gần nhất; tổng 51K; MRR 11K; gần 2.000 gói đang hoạt động. Tiêu đề ghi $30K/tháng"
      q: "This is in the last 28 days. We have 33 thousand revenue, almost 2,000 active subscriptions."
      ts: "01:50"
      evidence: measured
    pricing: "Gói năm $45, gói tháng $10, dùng thử 3 ngày"
    idea_origin: [trend_copy]
    scale_channels: [app_store_search]
    community_at_discovery:
      value: "Chưa ở trong cộng đồng peptide: bạn cùng phòng nhắc peptide, rồi TikTok For You đẩy về peptide"
      insider: false
      q: "And I had no idea what he was talking about."
      ts: "05:57"
    demand_signal:
      kind: self_reported_pain_or_free_waitlist
      level: 4
      what: "Waitlist ~300 người trước khi launch; video không nói có thu tiền không nên tính là waitlist (mức 4)"
      q: "we had a waitlist with like 300 people on it before we launched"
      ts: "10:05"
    prior_failures:
      count: 1
      what: "App marketplace cho sinh viên (University of Oregon): ~800 người dùng, không kiếm được tiền"
      q: "we didn't make any money with that app"
      ts: "02:38"
    unfair_advantage: []
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 1.6, value: "khoảng 7 tuần từ lúc ra mắt tới tổng doanh thu $50k", q: "We launched just 7 weeks ago and we've already hit $50,000 in total revenue.", ts: "01:01"}
    first_users:
      - {channel: reddit, what: "Vài bài Reddit trước khi launch, cùng waitlist ~300 người", q: "We made some Reddit posts and we had a waitlist with like 300 people on it before we launched", ts: "10:05"}
      - {channel: app_store_search, what: "Người ta tự tìm 'peptide' trên App Store và thấy app; founder nói app đứng top kết quả tìm kiếm", q: "people are actually just searching it in the App Store and finding your app", ts: "07:29"}
    build:
      time: "khoảng 2 tuần để build bản đầu bằng AI; App Store duyệt mất khoảng một tuần, nhiều lần bị từ chối"
      cut: []
      q: "it took about 2 weeks to build out"
      ts: "03:39"
steps:
  - {stage: find-idea, ts: "05:57", case: pep-ai, what: "Bạn cùng phòng nhắc 'nên làm peptide'; một tuần sau TikTok đẩy peptide về, thấy peptide đang bùng mà chưa có app peptide nào thành công.", tactic: s12-timing-shift, tactic_note: "Bắt trend đang bùng trên TikTok (peptide) khi các app hiện có chưa thành công"}
  - {stage: find-idea, ts: "06:12", case: pep-ai, what: "Đọc hết review của mọi app peptide đang có (thích gì, không thích gì, muốn gì), rồi nhờ Claude tìm kiếm để làm bản tốt hơn.", tactic: s3-competitor-reviews, tool: Claude}
  - {stage: build, ts: "03:39", case: pep-ai, what: "Build bản đầu trong khoảng 2 tuần bằng AI (vibe coding)."}
  - {stage: build, ts: "03:54", case: pep-ai, what: "Apple từ chối app nhiều lần vì có vẻ tư vấn y tế; đổi cách làm theo các app tương tự rồi được duyệt, sau đó xin expedite review để rút thời gian duyệt xuống vài giờ."}
  - {stage: launch, ts: "10:05", case: pep-ai, what: "Trước khi launch, nhờ vài influencer đăng về app để thử xem người ta có quan tâm không; tất cả đều đồng ý.", tactic: g7-creator-ops}
  - {stage: launch, ts: "10:05", case: pep-ai, what: "Đăng vài bài Reddit trước khi launch; có waitlist khoảng 300 người trước ngày ra mắt.", tactic: g1-first-10-users}
  - {stage: grow, ts: "10:36", case: pep-ai, what: "Một influencer đăng một story (~$1.000 doanh thu), rồi bài feed đầu tiên đạt 50.000 view (~$4.000 trong ngày; ước tính trên $10.000 từ bài đó).", tactic: g7-creator-ops}
  - {stage: monetize, ts: "01:50", case: pep-ai, what: "Đặt giá: gói năm $45, gói tháng $10, có dùng thử 3 ngày.", tactic: g4-pricing-paywall}
quotes:
  - {ts: "02:53", who: Cedric Roberge, stage: find-idea, theme: [], text: "So, once I realized that, you know, I decided to find something that was really popular and how I went about that was just scrolling social media until I found something that everyone was talking about and realized that there was no successful app for this.", vi: "Nhận ra cần một ngách thật cụ thể, tôi chọn thứ đang phổ biến: lướt mạng xã hội cho tới khi thấy thứ ai cũng bàn mà chưa có app thành công nào."}
  - {ts: "02:38", who: Cedric Roberge, stage: find-idea, theme: [], text: "The whole experience from the first app taught me that I needed to find a niche that was [music] really specific to like a group of people that would be interested in it.", vi: "Từ app đầu tiên, tôi học được rằng phải tìm một ngách rất cụ thể, đúng nhóm người sẽ quan tâm."}
  - {ts: "14:07", who: Cedric Roberge, stage: mindset, theme: [persistence], text: "I've just never given up, and I was literally never going to stop until something became successful.", vi: "Tôi chưa bao giờ bỏ cuộc, và tôi quyết không dừng cho tới khi có thứ thành công."}
rules:
  - {ts: "16:29", who: "Pat Walls hoặc Gus", stage: find-idea, theme: [], text: "The other underrated theme of this and hopefully it really comes out in the video because I think it's probably one of the most important things you can do, especially if you're building your first app, is build on a growing trend.", vi: "Điều hay bị bỏ qua: làm app đầu tiên thì nên xây trên một xu hướng đang lên, vì được hưởng sẵn lượng người đang quan tâm.", evidence: opinion}
numbers:
  - {ts: "01:50", metric: "doanh thu 28 ngày gần nhất (dashboard)", value: 33000, unit: usd, evidence: measured}
  - {ts: "01:50", metric: "tổng doanh thu (dashboard)", value: 51000, unit: usd, evidence: measured}
  - {ts: "01:50", metric: "gói trả phí đang hoạt động (gần 2.000)", value: 2000, unit: count, evidence: measured}
  - {ts: "10:05", metric: "waitlist trước khi launch", value: 300, unit: count, evidence: claimed}
  - {ts: "10:51", metric: "doanh thu một ngày từ bài feed (50.000 view)", value: 4000, unit: usd, evidence: claimed}
  - {ts: "10:51", metric: "ước tính tổng doanh thu từ bài feed đó", value: 10000, unit: usd, evidence: claimed}
frameworks: []
idea_patterns: []
---
## Một câu

Sinh viên làm app theo dõi peptide sau khi thấy peptide bùng trên TikTok mà chưa có app nào thành công: 33K doanh thu trong 28 ngày gần nhất (dashboard), gần 2.000 gói trả phí, và một bài feed của influencer cho ~$4.000 trong một ngày.

## Bài học cho tôi

- Bắt trend đang bùng mà app hiện có chưa làm tốt, rồi đọc hết review của đối thủ để biết họ thiếu gì (`05:57`, `06:12`).
- Trước khi launch, thử nhu cầu bằng Reddit và vài influencer: waitlist khoảng 300 người (`10:05`).

## Đừng tin vội

- Video là phễu quảng bá iOS bootcamp miễn phí của kênh. Số liệu là một thời điểm (28 ngày gần nhất) đọc từ dashboard; tiêu đề ghi $30K/tháng trong 35 ngày, nhưng founder nói 7 tuần từ lúc ra mắt, nên mốc thời gian không khớp tuyệt đối.
- Trend peptide đã lên đỉnh theo chính founder; người đi sau không có cơ hội y hệt. Video chỉ kể một app thành công, các app peptide cũ "chưa thành công" là lời kể, không có số.
- Điều kiện riêng: app có vùng nhạy cảm (sức khoẻ, Apple từ chối vì tư vấn y tế) nên phải qua duyệt nhiều lần; app khác không có vùng này sẽ không gặp đúng việc này.
- Video không nói: có chạy quảng cáo trả tiền không, tỉ lệ giữ chân/huỷ gói, chi phí trả influencer, và số người dùng so với "10.000 users" ghi trong mô tả gốc.
