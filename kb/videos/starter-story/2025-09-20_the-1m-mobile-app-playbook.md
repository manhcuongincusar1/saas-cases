---
schema: 2
video_id: hKqLceTPLWM
channel: starter-story
title: "The $1M Mobile App Playbook"
date: 2025-09-20
url: https://www.youtube.com/watch?v=hKqLceTPLWM
transcript: starter-story-kb/videos/2025-09-20_the-1m-mobile-app-playbook/transcript.md
kind: founder_case
speakers:
  - {name: Pat Walls, role: host}
  - {name: Steven, role: founder}
bias: "Starter Story có sponsor và quảng cáo Starter Story Build trong video; founder bán Posted (nền tảng kết nối creator) và được lợi nếu người xem tin vào mô hình creator-ads."
analyzed: 2026-11-15
cases:
  - id: puffcount
    depth: full
    product: "Puff Count: app bỏ thuốc lá điện tử (quit vaping)"
    what: "App hỗ trợ bỏ vape; marketing bằng video TikTok organic rồi chạy ads cho video thắng"
    type: [mobile-app]
    customer: "Người muốn bỏ vape"
    founder: {who: Steven, base: null, technical: null, team: "solo, tự bootstrap; có thuê creator qua nền tảng Posted", background: "Đã build, scale và exit nhiều app mobile; tự làm TikTok trong căn hộ"}
    revenue: {amount: 44000, unit: usd, basis: mrr, note: "Đạt trước khi bán, từ 3K lên 44K; lời founder, không nêu giá bán", q: "scaled it to $44,000 in monthly recurring revenue", ts: "01:22", evidence: claimed}
    pricing: null
    idea_origin: [own_pain]
    scale_channels: [tiktok_organic, paid_tiktok, paid_meta]
    community_at_discovery: {value: "Từng bị cuốn vào thói quen vape ở đại học; bạn bè đều nghiện", insider: true, q: "I got swept up in the habit", ts: "03:09"}
    demand_signal: {kind: content_views, level: 2, what: "Video TikTok về bỏ vape đang viral (1,3 và 3,7 triệu like), tức là nội dung đúng vấn đề", q: "We have 1.3 million likes here.", ts: "03:39"}
    prior_failures: null
    unfair_advantage:
      - {value: prior_success, what: "Đã build, scale và exit nhiều app mobile", q: "built, scaled, and exited multiple mobile apps", ts: "01:22"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: tiktok_organic, what: "Đăng video TikTok organic theo khuôn đã nghiên cứu; tài khoản đạt 120K follower và 50M view. Video không nói 10 người dùng đầu tiên", q: "I grew the PuffCount account to 120,000 followers, over 50 million views", ts: "08:38"}
    build: null
  - id: posted
    depth: mention
    product: "Posted (postedapp.com): nền tảng kết nối founder với creator"
    what: "Founder đăng brief sản phẩm; creator nộp video miễn phí, founder duyệt rồi trả tiền cho video muốn dùng và sở hữu video để chạy ads (creator báo giá khoảng 40–110 USD mỗi video)"
steps:
  - {stage: find-idea, ts: "03:09", case: puffcount, what: "Chọn vape vì từng bị cuốn vào thói quen và thấy vape đang viral trên TikTok.", tactic: s5-insider, tactic_note: "Nỗi đau riêng: bạn bè nghiện vape, bản thân từng bị cuốn vào"}
  - {stage: find-idea, ts: "03:24", case: puffcount, what: "Lọc TikTok theo từ khoá ngách, sắp xếp video theo 'most liked' mọi thời gian, lướt 7 ngày rồi ghi từng video vào spreadsheet (link, hook, storyline, CTA).", tactic: s4-tiktok-comment-mining, tool: "Bộ lọc most liked trên TikTok; spreadsheet", tactic_note: "Lướt và ghi lại video viral trong ngách trước khi đăng"}
  - {stage: grow, ts: "08:54", case: puffcount, what: "Viết video theo khuôn hook, vấn đề, giải pháp, CTA; CTA 2 giây cho thấy sản phẩm.", tactic: g3-organic-content-formats}
  - {stage: grow, ts: "11:33", case: puffcount, what: "Đăng video TikTok gần như mỗi ngày, ưu tiên khối lượng hơn độ hoàn hảo; video nào nổ thì làm lại khuôn của nó.", tactic: g3-organic-content-formats}
  - {stage: grow, ts: "12:35", case: puffcount, what: "Đăng chéo video lên TikTok, Instagram Reels, YouTube Shorts và Twitter.", tactic: g3-organic-content-formats, tactic_note: "Đăng chéo nền tảng; Twitter được founder nói là kênh bị bỏ quên"}
  - {stage: grow, ts: "14:39", case: posted, what: "Thuê creator qua nền tảng deal: đăng brief, creator nộp video, duyệt rồi trả tiền; sở hữu video để chạy ads.", tactic: g7-creator-ops, tool: "Posted"}
  - {stage: grow, ts: "16:28", case: puffcount, what: "Gửi sự kiện cài đặt qua MMP cho nền tảng ads; chiến dịch đầu không tối ưu mua mà tối ưu lượt xem và lượt cài.", tactic: g6-paid-ads, tool: "MMP (Adjust hoặc Appsfire, theo founder)"}
  - {stage: grow, ts: "17:15", case: puffcount, what: "Chạy ads trên video organic đã thắng; tổng chi 82K trước khi bán, đưa MRR từ 3K lên 44K.", tactic: g6-paid-ads, cost: "tổng 82.000 USD chi ads", threshold: "CAC khoảng 20–24 USD; LTV khoảng 55–70 USD"}
  - {stage: grow, ts: "17:46", case: puffcount, what: "Coi mỗi bước là phễu: view, click, cài đặt, mua; tối ưu từ trên xuống, bước dưới chỉ khi bước trên đã đủ dữ liệu.", tactic: g8-funnel-measurement}
  - {stage: grow, ts: "19:50", case: puffcount, what: "Dồn phần lớn ngân sách ads vào TikTok vì nội dung đã làm cho TikTok; chọn một nền tảng trước khi mở nền tảng khác.", tactic: g6-paid-ads, tactic_note: "TikTok rẻ hơn nhưng chất lượng thấp hơn Meta (theo founder)"}
  - {stage: grow, ts: "21:36", case: puffcount, what: "Theo dõi CPI, tỷ lệ dùng thử, tỷ lệ đăng ký, retention và LTV bằng Superwall hoặc RevenueCat.", tactic: g8-funnel-measurement, tool: "Superwall hoặc RevenueCat"}
  - {stage: scale, ts: "22:08", case: puffcount, what: "Bán PuffCount cho một studio mobile lớn ở châu Âu sau khi đạt 44K MRR."}
quotes:
  - {ts: "02:38", who: Steven, stage: grow, theme: [], text: "So, we have market research, post volume, organically, scale the winners with paid ads.", vi: "Vậy là: nghiên cứu thị trường, đăng nhiều organic, rồi đẩy ads cho những video thắng."}
  - {ts: "11:50", who: Steven, stage: grow, theme: [many-bets], text: "Volume negates luck, right?", vi: "Khối lượng triệt tiêu may rủi, đúng không?"}
  - {ts: "11:33", who: Steven, stage: grow, theme: [], text: "Do not be a perfectionist.", vi: "Đừng cầu toàn."}
  - {ts: "17:46", who: Steven, stage: grow, theme: [], text: "Everything is a funnel.", vi: "Mọi thứ đều là phễu."}
  - {ts: "20:05", who: Steven, stage: grow, theme: [], text: "I'm a solopreneur. I'm bootstrapping these products.", vi: "Tôi là solopreneur, tự bootstrap sản phẩm; không muốn đốt tiền vào ads."}
rules:
  - {ts: "23:12", who: "Pat Walls", stage: mindset, theme: [action-over-research], text: "Learning is cool, but action is what will get you that dream outcome.", vi: "Học thì hay, nhưng hành động mới đưa bạn tới kết quả mong muốn.", evidence: opinion}
numbers:
  - {ts: "08:38", metric: "follower TikTok của tài khoản PuffCount", value: 120000, unit: count, evidence: claimed}
  - {ts: "16:43", metric: "CAC (chi phí lấy một khách) PuffCount", value: "20–24", unit: usd, evidence: claimed}
  - {ts: "17:00", metric: "LTV mỗi khách PuffCount", value: "55–70", unit: usd, evidence: claimed}
  - {ts: "17:15", metric: "tổng chi paid ads trước khi bán", value: 82000, unit: usd, evidence: claimed}
  - {ts: "21:52", metric: "tỷ lệ CAC:LTV founder coi là lý tưởng", value: "3:1", unit: ratio, evidence: opinion}
frameworks: [organic-find-format-then-paid-scale]
idea_patterns: [utility-own-problem]
---

## Một câu

Playbook ba bước của founder PuffCount (app bỏ vape): lướt TikTok tìm video viral trong ngách, đăng organic theo khuôn đã thắng, rồi dồn ads vào video thắng; đưa MRR từ 3K lên 44K trước khi bán cho một studio ở châu Âu (lời founder).

## Bài học cho tôi

- Trước khi đăng gì, lướt TikTok 7 ngày và ghi từng video viral vào bảng: hook, storyline, CTA (`07:51`).
- Chỉ scale ads khi đã biết CAC và LTV: CAC khoảng 20–24, LTV khoảng 55–70, tỷ lệ 3:1 là ngưỡng founder coi là tốt (`17:00`, `21:52`).

## Đừng tin vội

- Video là phễu bán Posted (sản phẩm của founder) và Starter Story Build; tiêu đề "$1M" không có trong transcript, video chỉ nói 44K MRR và không nêu giá bán.
- CAC, LTV, $82K chi ads là lời founder; dashboard có hiện trong video nhưng không đủ để đối chiếu từng con số.
- Ngách vape có sẵn nhiều video viral và TikTok ads rẻ; đó là điều kiện riêng của ngách, không phải công thức chung.
- Video không nói 10 người dùng đầu tiên đến từ đâu, không nói thời gian đi từ 0 đến 44K MRR, và không nói ai đã làm dự án cùng founder.
