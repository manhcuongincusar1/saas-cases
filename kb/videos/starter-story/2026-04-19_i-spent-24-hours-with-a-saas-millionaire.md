---
schema: 2
video_id: iVy5J7iE-3Q
channel: starter-story
title: "I Spent 24 Hours With A SaaS Millionaire"
date: 2026-04-19
url: https://www.youtube.com/watch?v=iVy5J7iE-3Q
transcript: starter-story-kb/videos/2026-04-19_i-spent-24-hours-with-a-saas-millionaire/transcript.md
kind: founder_case
speakers:
- name: Pat Walls
  role: host
- name: Jeremy Redman
  role: founder
bias: "Video là nội dung của Starter Story, có quảng cáo database 190+ ý tưởng micro-SaaS của HubSpot (lead magnet miễn phí). Jeremy đang quảng bá các sản phẩm mới của mình (LeadQuest, SideProduct, SnagThem). Số liệu là lời kể, không có dashboard."
analyzed: 2026-11-15
cases:
- id: task-magic
  depth: full
  product: "Task Magic: công cụ tự động hoá thao tác trên trình duyệt, là sản phẩm lõi (tentpole) của công ty"
  what: "Tự động hoá các thao tác trình duyệt (click nút, làm việc như người) cho khách của Zapier khi API bị giới hạn; bắt đầu từ một app no-code V1"
  type:
  - web-app
  - saas
  customer: "Business owner, agency, freelancer cần bán hàng (lời kể)"
  founder:
    who: Jeremy Redman
    base: "Los Angeles, Mỹ"
    technical: false
    team: "một nhân viên là CTO đi cùng (video gọi là 'one employee')"
    background: "Không có nền tảng kỹ thuật lúc đầu, tự làm no-code app (theo lời kể)"
  revenue:
    amount: 3000000
    unit: usd
    basis: arr
    note: "Khoảng 3 triệu USD/năm (lời kể); có tháng trên 400k; sau đó bán công ty"
    q: "And got it to about 3 million annually."
    ts: "02:37"
    evidence: claimed
  pricing: "Ban đầu gói subscription không hợp; chuyển sang lifetime deal rồi tính phí theo usage (không nêu giá cụ thể)"
  idea_origin:
  - own_pain
  - user_request
  scale_channels: []
  community_at_discovery:
    value: "Solo founder dùng no-code tools (Zapier), thấy người dùng Zapier bị giới hạn vì API"
    insider: true
    q: "As a solo founder, I kept finding myself like dabbling in like no-code tools"
    ts: "02:06"
  demand_signal: null
  prior_failures: null
  unfair_advantage:
  - value: cofounder
    what: "Có CTO làm cùng từ đầu; video gọi là một nhân viên, không nói là co-founder"
    q: "Me and my CTO."
    ts: "02:52"
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users: []
  build: null
- id: mail-lead
  depth: mention
  product: "Mail Lead: công cụ cold email đơn giản cho khách của Task Magic, có SEO riêng"
  what: "Sản phẩm hẹp (cold email cho một nhóm cụ thể), bán cho khách sẵn có rồi tự có lượt SEO; theo lời kể thu gần 7 chữ số"
  type:
  - web-app
  customer: "Khách của Task Magic cần gửi cold email"
  first_users:
  - channel: own_audience
    what: "Bán cho khách sẵn có của Task Magic"
    q: "we not only sold this to our existing customers"
    ts: "08:03"
  - channel: seo
    what: "Được SEO riêng nhờ sản phẩm hẹp"
    q: "got its own SEO lift"
    ts: "08:20"
- id: leadquest
  depth: mention
  product: "LeadQuest.ai: AI tìm lead để gửi email"
  what: "Sản phẩm thêm trong hệ sinh thái, nối vào automation của Task Magic để gửi email tới lead tìm được"
  type:
  - web-app
  customer: "Khách của Mail Lead cần tìm lead"
steps:
- stage: find-idea
  ts: "02:22"
  case: task-magic
  what: "Thấy người dùng Zapier khó tự động hoá vì giới hạn API, nên làm công cụ tự động hoá thao tác trên trình duyệt."
  tactic: s5-insider
  tactic_note: "Nỗi đau: chính founder là người dùng no-code tools"
- stage: find-idea
  ts: "04:44"
  case: task-magic
  what: "Năm 2021, khách hỏi cách tự động hoá; đội chuyển hướng sang automation để đi đầu xu hướng."
  tactic: s12-timing-shift
  tactic_note: "Xu hướng automation đang nổi; kết hợp với yêu cầu khách"
- stage: find-idea
  ts: "07:12"
  case: task-magic
  what: "Tentpole bước 1: làm sản phẩm cho vấn đề kế tiếp của khách Task Magic (business owner, agency, freelancer)."
  tactic: s9-niche-narrowing
  tactic_note: "Mở sang ngách kề của sản phẩm đang chạy (cold email cho khách Task Magic)"
- stage: find-idea
  ts: "07:46"
  case: mail-lead
  what: "Làm Mail Lead thật hẹp: cold email cho một nhóm cụ thể, vì sản phẩm cụ thể dễ được SEO hơn."
  tactic: s9-niche-narrowing
  tactic_note: "Thu hẹp ngách để sản phẩm dễ được tìm thấy"
- stage: launch
  ts: "08:03"
  case: mail-lead
  what: "Bán Mail Lead trước cho khách sẵn có của Task Magic, rồi mới có thêm khách mới."
  tactic: g1-first-10-users
- stage: grow
  ts: "08:20"
  case: mail-lead
  what: "Mail Lead được SEO riêng nhờ sản phẩm hẹp; theo lời kể thu gần 7 chữ số từ sản phẩm này."
  tactic: g2-aso-seo-organic
- stage: grow
  ts: "08:20"
  case: task-magic
  what: "Bước 3: nút automation tích hợp sẵn trong Mail Lead dẫn người dùng lên Task Magic khi họ cần thêm."
  tactic: other
  tactic_note: "Cross-sell: sản phẩm nhỏ dẫn người dùng lên sản phẩm lõi khi chạm nhu cầu"
- stage: monetize
  ts: "09:08"
  case: task-magic
  what: "Chuyển sang lifetime deal rồi tính phí theo usage vì khách không muốn trả subscription liên tục; giúp có tiền ban đầu."
  tactic: g4-pricing-paywall
  tactic_note: "Lifetime deal + usage-based pricing (video không nêu nền tảng LTD)"
- stage: find-idea
  ts: "09:23"
  case: leadquest
  what: "Bước cuối của tentpole: thêm LeadQuest cho khách của Mail Lead (tìm lead), nối vào automation của Task Magic."
  tactic: s9-niche-narrowing
  tactic_note: "Mở sang ngách kề trong hệ sinh thái sản phẩm đang chạy"
- stage: grow
  ts: "03:41"
  case: task-magic
  what: "Thay vì chỉ quảng bá sản phẩm lõi, xây các sản phẩm phụ để dẫn người dùng trả tiền về sản phẩm lõi."
  tactic: other
  tactic_note: "Tentpole: sản phẩm phụ là phễu về sản phẩm lõi"
quotes:
- ts: "06:55"
  who: Jeremy Redman
  stage: find-idea
  theme: []
  text: "now you can sell functionality, not information."
  vi: "Giờ với công cụ no-code, bạn có thể bán chức năng thay vì thông tin."
- ts: "10:56"
  who: Jeremy Redman
  stage: mindset
  theme: []
  text: "these aren't like separate side hustles. They're serving the same ecosystem."
  vi: "Đây không phải các side hustle riêng lẻ; chúng cùng phục vụ một hệ sinh thái."
- ts: "14:19"
  who: Jeremy Redman
  stage: mindset
  theme:
  - emotional-bottleneck
  text: "focus on the problems, you know? Have your bad day, have your bad video, share it."
  vi: "Hãy nói về vấn đề. Có ngày tồi tệ thì cứ đăng video về nó."
rules:
- ts: "05:15"
  who: Pat Walls
  stage: find-idea
  theme: []
  text: "why not build your first idea inspired by already successful businesses?"
  vi: "Sao không xây ý tưởng đầu tiên lấy cảm hứng từ các doanh nghiệp đã thành công?"
  evidence: opinion
- ts: "15:21"
  who: Pat Walls
  stage: mindset
  theme: []
  text: "He treats products as almost like content."
  vi: "Anh ấy coi sản phẩm gần như nội dung."
  evidence: opinion
numbers:
- ts: "02:37"
  metric: "số người dùng Task Magic (lời kể)"
  value: 60000
  unit: count
  evidence: claimed
- ts: "02:37"
  metric: "số khách trả tiền Task Magic (lời kể)"
  value: 8000
  unit: count
  evidence: claimed
- ts: "02:37"
  metric: "doanh thu tháng cao nhất Task Magic (lời kể: 'north of 400 grand')"
  value: 400000
  unit: usd_per_month
  evidence: claimed
- ts: "08:20"
  metric: "doanh thu Mail Lead (lời kể: 'almost seven figures')"
  value: "gần 7 chữ số"
  unit: usd
  evidence: claimed
frameworks:
- many-small-bets
idea_patterns:
- adjacent-platform-expansion
---

## Một câu

Jeremy Redman xây Task Magic (tự động hoá thao tác trình duyệt, theo lời kể khoảng 3 triệu USD/năm với một nhân viên là CTO), rồi làm thêm các sản phẩm phụ nhỏ dẫn người dùng về sản phẩm lõi (tentpole), sau đó bán công ty.

## Bài học cho tôi

- Sản phẩm phụ hẹp (Mail Lead) là một phễu về sản phẩm lõi, không phải một dự án riêng; cùng một hệ sinh thái (`03:41`, `10:56`).
- Ý tưởng đầu tiên xuất phát từ nỗi đau khi chính mình dùng công cụ (Zapier giới hạn API) (`02:22`).

## Đừng tin vội

- Video là nội dung quảng bá cho Starter Story, và có quảng cáo database của HubSpot (`05:15`).
- Các con số (3 triệu/năm, 60.000 người dùng, 400k/tháng, gần 7 chữ số của Mail Lead) là lời kể, không có dashboard. Video không nêu thời gian để đạt doanh thu, chi phí, hay 10 khách đầu tiên của Task Magic.
- Tentpole chỉ hiệu quả khi đã có một sản phẩm lõi có khách trả tiền; điều kiện này không sao chép được nếu chưa có sản phẩm lõi.
- Survivor bias: chỉ kể về một người đã bán được công ty; không kể các sản phẩm phụ không ra tiền.
