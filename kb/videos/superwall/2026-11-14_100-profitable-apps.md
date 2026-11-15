---
schema: 2
video_id: 2sLUhYP6a6k
channel: superwall
title: I Studied 100+ Profitable Apps, Here’s What Actually Works
date: 2026-11-14
url: https://www.youtube.com/watch?v=2sLUhYP6a6k
transcript: superwall/youtube-transcript/superwall/i-studied-100-profitable-apps-heres-what-actually-works/transcript.md
kind: host_essay
speakers:
- name: Joseph Choi
  role: host
bias: Host bán buổi Zoom miễn phí dẫn tới tư vấn/agency organic growth; Superwall (paywall) tài trợ kênh.
  Số liệu app khác là nghe kể hoặc ước tính.
analyzed: 2026-11-15
cases:
- id: beam
  depth: mention
  product: Beam (trước là Breezy)
  what: Mạng xã hội chia sẻ danh sách (như ghi chú list trong điện thoại)
  demand_signal:
    level: 4
    what: 'TikTok 15 giây nói về ý tưởng khi app chưa có: 350k view, 4.000 người vào waitlist (>1% người
      xem)'
    q: That video got her 350,000 views and 4,000 weightless signups.
    ts: 00:01:08
    kind: self_reported_pain_or_free_waitlist
  first_users:
  - channel: tiktok_organic
    what: TikTok của founder về ý tưởng trước khi có app
    q: Before the app was out, she posted a 15-second TikTok.
    ts: 00:00:49
- id: cat-on-chair
  depth: mention
  product: Cat on Chair
  what: Pomodoro timer chủ đề con mèo
  revenue:
    amount: 40000
    unit: usd
    basis: other
    note: '100k download trong 8 tháng (basis gốc: two_months)'
    q: it had made over $40,000 in the past 2 months and passed a 100,000 downloads in 8 months
    ts: 00:02:51
    evidence: claimed
  idea_origin:
  - passion_skin
- id: gotall
  depth: mention
  product: GoTall
  what: Dự đoán chiều cao + thói quen ăn uống/tư thế cho teen, ngách con của looksmaxing (cạnh UMAX)
  revenue:
    amount: 150000
    unit: usd
    basis: monthly
    note: host nói 'last time I checked'
    q: last time I checked, go tall was around 150k a month
    ts: 00:05:08
    evidence: claimed
  idea_origin:
  - niche_down
- id: verba
  depth: mention
  product: Verba
  what: App sửa video bằng AI; chiến dịch 3M view kéo về thợ sửa video ở Ấn Độ thay vì creator muốn xây
    thương hiệu cá nhân, nên đổi định vị
steps:
- stage: validate
  ts: 00:00:49
  case: beam
  what: Đăng TikTok về ý tưởng trước khi có app, mở đầu bằng gọi tên người xem ('if you're a notes app
    person'). 350k view, 4.000 waitlist.
  tactic: s8-content-demand-test
  tactic_note: 'Content-market fit: đăng video về ý tưởng trước khi build rồi đếm waitlist'
- stage: find-idea
  ts: 00:03:27
  case: cat-on-chair
  what: 'Khung ''pain hay passion'': app giải nỗi đau (peptide tracker) hoặc app người ta mua vì mê chủ
    đề (mèo). Nhìn tính năng thì không hiểu vì sao Cat on Chair bán được.'
  tactic: other
  tactic_note: 'Phân loại pain/passion: xem người ta đã chi tiền vì nỗi đau hay vì mê chủ đề'
- stage: find-idea
  ts: 00:05:08
  case: gotall
  what: Trong danh mục đã có tiền (looksmaxing; UMAX ~$700k/tháng lúc đỉnh), chọn một nỗi lo con (chiều
    cao) mà app lớn không phục vụ.
  tactic: s1-revenue-spy
  threshold: UMAX ~$700k/tháng lúc đỉnh (host nói Blake Anderson báo)
- stage: find-idea
  ts: 00:05:31
  what: Tìm ngách con bằng cách xem khách hàng đang xem gì trên TikTok (routine, skincare, đối xứng mặt…),
    không chỉ xem app đối thủ.
  tactic: s4-tiktok-comment-mining
- stage: build
  ts: 00:06:05
  what: 'Cần ít nhất một ''killer feature'' hiểu ngay (Cal AI: chụp ảnh → ra calo). Các tính năng khác
    chỉ có tác dụng sau khi người ta đã tải.'
- stage: grow
  ts: 00:07:44
  case: verba
  what: View nhiều mà không ra tiền → xem video đang tới tay ai. Nội dung đổi sang chủ đề 'xây thương
    hiệu cá nhân' để chạm đúng người sẵn sàng trả.
  tactic: g3-organic-content-formats
- stage: monetize
  ts: 00:09:45
  what: Gói tuần chủ yếu để neo giá cho gói năm trông rẻ; đa số huỷ gói tuần sau 1–2 tuần; app $1M+ ARR
    có phần lớn doanh thu từ gói năm.
  tactic: g4-pricing-paywall
- stage: grow
  ts: 00:10:29
  what: '''Trần thông điệp'': paid ads mệt dần vì đã chạm hết người quan tâm tới một lý do mua. Quay về
    organic để tìm lý do mua mới từ cách khách tự nói về vấn đề.'
  tactic: g6-paid-ads
quotes: []
rules:
- ts: 00:01:24
  who: Joseph Choi
  stage: validate
  theme:
  - sell-before-build
  text: But Lily showed that you can go even earlier than that. You can make content about the idea and
    see whether people want it before you've even finished building anything.
  vi: 'Có thể đi sớm hơn cả MVP: làm nội dung về ý tưởng để xem người ta có muốn không, trước khi build
    xong.'
  evidence: opinion
- ts: 00:02:16
  who: Joseph Choi
  stage: mindset
  theme:
  - builder-trap
  - emotional-bottleneck
  text: When you post content, there is a chance that nobody will care and nobody likes that feeling as
    a founder. But with Vibe Coding, you can spend the whole day building and feel like you actually productive.
  vi: Đăng nội dung thì có thể không ai quan tâm, và không founder nào thích cảm giác đó. Còn vibe coding
    thì build cả ngày vẫn thấy mình năng suất.
  evidence: opinion
- ts: 00:03:27
  who: Joseph Choi
  stage: find-idea
  theme:
  - revenue-first
  text: This is part of the framework that I think about where apps are either a pain or a passion app.
  vi: App hoặc là giải nỗi đau, hoặc là phục vụ đam mê.
  evidence: opinion
- ts: 00:04:06
  who: Joseph Choi
  stage: find-idea
  theme:
  - revenue-first
  text: So when you're researching an app idea, pay attention to what people already spend money on.
  vi: Khi nghiên cứu ý tưởng, để ý xem người ta đã đang chi tiền cho cái gì.
  evidence: opinion
- ts: 00:05:49
  who: Joseph Choi
  stage: find-idea
  theme:
  - learn-from-others
  text: If you only look at other apps, you'll only see the surface level. But if you look at what the
    customer watches, you can find something they want that doesn't have an obvious app attached to it
    yet.
  vi: Chỉ nhìn app khác thì chỉ thấy bề mặt. Nhìn khách đang xem gì thì thấy được nhu cầu chưa có app
    nào gắn vào.
  evidence: opinion
- ts: 00:08:32
  who: Joseph Choi
  stage: grow
  theme:
  - right-audience
  text: That's what I mean when I say the creative is the targeting.
  vi: Nội dung video chính là công cụ nhắm đối tượng.
  evidence: opinion
numbers:
- ts: 00:01:08
  metric: tỉ lệ người xem vào waitlist (Beam, trước khi có app)
  value: '>1%'
  unit: ratio
  evidence: claimed
- ts: 00:04:28
  metric: doanh thu đỉnh UMAX
  value: 700000
  unit: usd_per_month
  evidence: claimed
- ts: 00:07:44
  metric: view chiến dịch UGC Verba (sai đối tượng)
  value: 3000000
  unit: views
  evidence: claimed
frameworks:
- content-before-product
- niche-down-proven-category
- product-as-main-character
- right-audience-over-views
- annual-plan-push
idea_patterns:
- passion-skin
- niche-inside-hot-category
- snap-and-get-result
---

## Một câu

Host tổng hợp 100+ app có lãi: kiểm nhu cầu bằng nội dung trước khi build, chọn ngách con trong danh mục đã có tiền, một tính năng hiểu ngay, nội dung quyết định ai tới, đừng bán rẻ.

## Bài học cho tôi

- Hai cách tìm ý tưởng làm được ngay: **pain hay passion** (người ta đã chi tiền vì mê cái gì) và **ngách con** (xem khách xem gì để tìm nỗi lo mà app lớn bỏ qua).
- Câu về vibe coding nói đúng cơ chế né tránh của tôi: build làm mình thấy năng suất, đăng bài làm mình sợ không ai quan tâm.

## Đừng tin vội

- Video là phễu bán Zoom/tư vấn. Các con số app khác (Cat on Chair, GoTall, UMAX) là nghe kể/ước tính, chưa kiểm.
- 4.000 waitlist chưa phải tiền (VALIDATE.md: đếm tiền, không đếm email).
