---
schema: 2
video_id: 9r0qPeSJGog
channel: starter-story
title: "I built a $14K/month SaaS using Discord"
date: 2026-01-14
url: https://www.youtube.com/watch?v=9r0qPeSJGog
transcript: starter-story-kb/videos/2026-01-14_i-built-a-14k-month-saas-using-discord/transcript.md
kind: founder_case
speakers:
  - {name: "Sam Adeniyi", role: founder}
  - {name: "Pat Walls", role: host}
  - {name: "Gus", role: host}
bias: "Starter Story quảng bá Starter Story Build (bootcamp) và playbook 'communities' (link trong mô tả). Sam bán Algrow; số doanh thu là lời kể có đưa dashboard, không kiểm chứng độc lập."
analyzed: 2026-11-15
cases:
  - id: algrow
    depth: full
    product: "Algrow (algrow.online): tìm kênh và format video viral, rồi tạo video AI từ format đó"
    what: "Phân tích kênh (số subscriber, view trung bình) để liệt kê format đang viral; từ đó tạo video bằng AI để đăng"
    type: [web-app]
    customer: "Creator YouTube faceless, influencer, người bán hàng dropship; trả gói tháng"
    founder: {who: "Sam Adeniyi", base: null, technical: false, team: "video không nói rõ; có bạn Mason góp ý tưởng", background: "Từng làm affiliate marketing và chạy kênh YouTube automation; không biết code, vibe code bằng AI"}
    revenue: {amount: 14000, unit: usd, basis: last_30_days, note: "Headline $14K; dashboard 4 tuần: £10K ≈ $13–14K. Intro nói tháng trước trên $40K, mâu thuẫn (xem Đừng tin vội)", q: "made over $14,000 in revenue in the last 30 days", ts: "01:04", evidence: measured}
    pricing: "3 gói: 25, 45, 80 mỗi tháng"
    idea_origin: [own_pain]
    scale_channels: [word_of_mouth]
    community_at_discovery: {value: "Đang chạy kênh YouTube automation (kiếm tiền từ video ngắn), trong nhóm khách mà Algrow phục vụ", insider: true, q: "I went to something called YouTube automation where you post videos online and make money from ad revenue", ts: "03:40"}
    demand_signal: {kind: self_reported_pain_or_free_waitlist, level: 4, what: "Trong server Discord về ngách, người ta lặp đi lặp lại câu hỏi làm sao tìm ngách; Sam coi đó là nhu cầu rồi gửi waitlist miễn phí", q: "people were repeating how do I find a niche", ts: "05:44"}
    prior_failures: {count: 1, what: "Affiliate marketing cho một công ty app (Resap): hơn $10K doanh thu nhưng không bền", q: "However, it wasn't sustainable.", ts: "03:24"}
    unfair_advantage:
      - {value: domain_expertise, what: "Đã chạy kênh YouTube automation (kiếm tiền từ quảng cáo video ngắn) trước khi làm Algrow", q: "I went to something called YouTube automation where you post videos online and make money from ad revenue", ts: "03:40"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 6, value: "6 tháng từ lúc code app đầu tiên tới khoảng $14K/tháng", q: "I v coded my first SAS six months ago called Algrow", ts: "01:04"}
    first_users:
      - {channel: word_of_mouth, what: "Người dùng đầu được dùng miễn phí rồi kể bạn bè; kênh chính ban đầu là Discord (video nói 400 người dùng đầu đến từ Discord, nhưng Discord chưa có trong vocab channel)", q: "Word of mouth was so big for me at the beginning", ts: "08:50"}
    build: {time: "khoảng 1 tuần để code MVP đầu tiên, ship bản lỗi lên Heroku", cut: [], q: "the initial MVP that you see it was coded in about a week", ts: "04:42"}
steps:
  - {stage: find-idea, ts: "03:40", case: algrow, what: "Làm YouTube automation (cần nhiều kênh shorts để chạy); bạn Mason gợi ý một công cụ tìm kênh shorts; Sam làm để dùng cho chính mình.", tactic: s5-insider, tactic_note: "Nỗi đau nghề của chính mình; ý tưởng được bạn gợi ý"}
  - {stage: build, ts: "04:11", case: algrow, what: "Không biết code: nhờ ChatGPT viết code rồi copy qua lại giữa Notepad, VS Code, sau đó chuyển sang Cursor."}
  - {stage: build, ts: "04:57", case: algrow, what: "Ship MVP lên Heroku; người dùng đầu gặp lỗi application error nhưng vẫn dùng được tính năng chính."}
  - {stage: validate, ts: "05:28", case: algrow, what: "Tìm server Discord ngách qua discboard.org, đọc chat để tìm câu hỏi lặp lại (người ta hỏi cách tìm ngách).", tactic: s3-reddit-pain-mining, tool: "discboard.org", tactic_note: "Đọc Discord (không đăng quảng cáo) để tìm nỗi đau lặp lại"}
  - {stage: validate, ts: "06:00", case: algrow, what: "Vào voice chat của server Discord, chia sẻ màn hình dùng Algrow vài ngày liên tiếp; người trong server hỏi và Sam trả lời.", tactic: s14-test-with-target-group, tactic_note: "Thử bản đang chạy với đúng nhóm khách trong cộng đồng ngách"}
  - {stage: validate, ts: "06:32", case: algrow, what: "Gửi link waitlist vào chat các server Discord; người xem đăng ký rồi được email khi phát hành.", tactic: other, tactic_note: "Waitlist miễn phí gửi vào chat server, không phải nội dung trên web (demand_signal mức 4)"}
  - {stage: launch, ts: "08:34", case: algrow, what: "Giúp từng người tìm đúng kênh bằng công cụ trước, không bán thẳng; người được giúp kể cho bạn bè.", tactic: g1-first-10-users, tactic_note: "Xây quan hệ trong cộng đồng trước khi giới thiệu sản phẩm"}
  - {stage: launch, ts: "11:40", case: algrow, what: "Cho người dùng đầu dùng miễn phí; họ mời bạn bè trả tiền; nhóm lớn lên nhanh nhờ đăng trong các cộng đồng.", tactic: g1-first-10-users, tactic_note: "Người dùng đầu làm đại sứ trong cộng đồng"}
  - {stage: monetize, ts: "01:50", case: algrow, what: "Ba gói giá: 25, 45 và 80 mỗi tháng.", tactic: g4-pricing-paywall}
quotes:
  - {ts: "05:12", who: "Sam Adeniyi", stage: build, theme: [ship-ugly], text: "So as long as what you're trying to solve works I think you can ship anything.", vi: "Miễn là thứ bạn đang giải quyết hoạt động, tôi nghĩ bạn có thể ship bất cứ thứ gì."}
  - {ts: "08:34", who: "Sam Adeniyi", stage: validate, theme: [right-audience], text: "I think the main thing you have to do first is build maybe a bit of rapport in the community.", vi: "Việc cần làm đầu tiên là xây chút quan hệ trong cộng đồng."}
  - {ts: "10:39", who: "Sam Adeniyi", stage: launch, theme: [right-audience], text: "I think that you should build your product with your users.", vi: "Tôi nghĩ bạn nên xây sản phẩm cùng người dùng."}
  - {ts: "11:09", who: "Sam Adeniyi", stage: retain, theme: [], text: "Discord is 10 times better in terms of building a relationship with your users.", vi: "Discord tốt hơn gấp 10 lần để xây quan hệ với người dùng so với email."}
  - {ts: "12:58", who: "Sam Adeniyi", stage: mindset, theme: [risk-and-leap], text: "You need to initially bet on yourself.", vi: "Bạn phải đặt cược vào chính mình ngay từ đầu."}
rules:
  - {ts: "13:58", who: "Pat Walls hoặc Gus", stage: launch, theme: [right-audience], text: "And if you're going to build this business and then you're going to go promote it on LinkedIn, that that's not going to work,", vi: "Nếu xây business này rồi lại quảng bá trên LinkedIn thì sẽ không ăn thua.", evidence: opinion}
  - {ts: "14:29", who: "Host (không nêu tên)", stage: find-idea, theme: [right-audience], text: "go to small community, solve a really, really niche problem for a really, really niche customer.", vi: "Vào một cộng đồng nhỏ, giải một vấn đề rất ngách cho một khách rất ngách.", evidence: opinion}
numbers:
  - {ts: "00:00", metric: "doanh thu tháng trước (lời Sam trong intro, mâu thuẫn với 14K)", value: 40000, unit: usd, evidence: claimed}
  - {ts: "00:15", metric: "số người dùng (lời Sam trong intro)", value: 10000, unit: count, evidence: claimed}
  - {ts: "00:15", metric: "người dùng đầu tiên đến từ Discord", value: 400, unit: count, evidence: claimed}
  - {ts: "02:36", metric: "doanh thu 4 tuần gần nhất (Stripe)", value: 10000, unit: gbp, evidence: measured}
  - {ts: "02:36", metric: "khách hàng mới trong tháng (Stripe)", value: 480, unit: count, evidence: measured}
frameworks: []
idea_patterns: []
---
## Một câu

Sam (không biết code) làm Algrow, công cụ tìm và nhân bản format video viral cho creator; kiểm nhu cầu bằng cách đọc chat và chia sẻ màn hình trong server Discord ngách, rồi gửi waitlist; khoảng $14K/tháng sau 6 tháng.

## Bài học cho tôi

- Đọc chat của server ngách để tìm câu hỏi lặp lại trước khi build, rồi demo trong voice chat để xem người ta hỏi gì (`05:44`).
- Không spam link: giúp từng người tìm đúng kênh bằng công cụ trước, để họ tự kể cho bạn bè (`08:34`).

## Đừng tin vội

- Số liệu mâu thuẫn: intro nói tháng trước trên $40K, phần sau nói 4 tuần gần nhất £10K (~$13–14K) và trên $14K trong 30 ngày.
- Video là phễu của Starter Story Build và playbook communities; Sam bán Algrow. Chưa có tỉ lệ chuyển đổi từ waitlist sang trả tiền.
- Điều kiện riêng: Sam có nền YouTube automation và biết nhóm khách (creator shorts) từ bên trong. Ngách này dựa vào Discord và giới trẻ không đọc email (lời Sam); không chắc áp dụng cho ngách khác.
- Video không nói tổng chi phí vận hành (AI, hosting) và bao nhiêu người dùng đến từ Discord so với các kênh khác.
- Discord bị coi là spam nếu làm sai; cách Sam làm (giúp người ta trước, không bán thẳng) không đảm bảo ở server khác.
