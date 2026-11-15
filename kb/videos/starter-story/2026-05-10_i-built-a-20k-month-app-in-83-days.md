---
schema: 2
video_id: r4R_Hlw7sbo
channel: starter-story
title: I Built a $20K/Month App in 83 Days
date: 2026-05-10
url: https://www.youtube.com/watch?v=r4R_Hlw7sbo
transcript: starter-story-kb/videos/2026-05-10_i-built-a-20k-month-app-in-83-days/transcript.md
kind: founder_case
speakers:
- name: Brian Shin
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story là kênh media, quảng cáo cheat sheet 'Mobile App Growth' miễn phí hai lần trong video.
  Founder có app để bán nên có lợi khi câu chuyện được kể đẹp. Doanh thu là lời founder; dashboard mở
  trong video là lịch sự kiện, không có số tiền.
analyzed: 2026-11-15
cases:
- id: once
  depth: full
  product: 'Once: app máy ảnh dùng một lần cho tiệc và đám cưới'
  what: 'Mô phỏng máy ảnh dùng một lần trên điện thoại: chủ sự kiện tạo film, khách mời chụp, ảnh gom
    vào một album và hiện theo lịch đã đặt.'
  type:
  - mobile-app
  customer: Người tổ chức sự kiện (sinh nhật, đám cưới, sự kiện công ty) và khách mời của họ
  founder:
    who: Brian Shin
    base: null
    technical: null
    team: '2 người: Brian và bạn gái làm co-founder, bootstrap'
    background: Từng đồng sáng lập một startup B2B venture-backed khoảng 50 người, nhiều bán hàng
  revenue:
    amount: 22000
    unit: usd
    basis: monthly
    note: '''Tháng này'' khoảng 22k, lời founder. Intro nói đạt 20k/tháng trong 83 ngày kể từ ra mắt.
      Dashboard mở ra là lịch sự kiện.'
    q: this month we're totaling around $22,000
    ts: 02:18
    evidence: claimed
  pricing: 'Trả theo số khách mời: tiệc 10 người khoảng $2, đám cưới 150 người khoảng $50'
  idea_origin:
  - passion_skin
  scale_channels: []
  community_at_discovery:
    value: Hai người đi du lịch 7–8 nước mỗi năm và mang máy ảnh dùng một lần ở mỗi thành phố, tức là
      chính họ là người dùng trải nghiệm này
    insider: true
    q: every single city we go to, we bring around a disposable camera
    ts: 04:23
  demand_signal:
    kind: friends_praise
    level: 1
    what: 4 người bạn nói 'Okay, I would love to try it' khi chưa có app; video không nêu ai trả tiền
    q: it was four friends who said, "Okay, I would love to try it."
    ts: 07:31
  prior_failures: null
  unfair_advantage:
  - value: network
    what: Có danh sách bạn bè trên X, LinkedIn, Instagram/Facebook để mời dùng thử đầu tiên
    q: I have my friends list. I just go through every single one of them
    ts: 07:16
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 2.7
      value: 83 ngày kể từ lúc ra mắt (tháng 12/2025) tới mức 20k/tháng; không tính từ lúc bắt đầu build
      q: we were able to hit 20K in monthly revenue within 83 days of launch
      ts: 01:01
  first_users:
  - channel: own_audience
    what: 'Bạn bè: tiệc Halloween của một người bạn, in mã mời cho khách dùng bản web'
    q: We had a Halloween party hosted by my friend coming up
    ts: 05:10
  build:
    time: bản web đầu khoảng 1–2 tuần; thời gian làm bản app chính không nêu
    cut:
    - bản web đầu, bỏ sau khi đã validate
    q: the first version took around a week or two
    ts: 05:10
steps:
- stage: find-idea
  ts: 04:23
  case: once
  what: 'Ý tưởng từ chuyến đi: hai người mang máy ảnh dùng một lần ở mỗi thành phố, rồi quyết làm bản
    số hoá giữ được trải nghiệm đó.'
  tactic: s5-insider
  tactic_note: Loại đam mê (trải nghiệm riêng với máy ảnh dùng một lần), không phải nỗi đau
- stage: build
  ts: 05:10
  case: once
  what: Làm bản web đầu trong 1–2 tuần, có các tính năng cốt lõi, để thử ý tưởng trước khi làm app.
- stage: validate
  ts: 05:10
  case: once
  what: Đưa bản web xấu, hay lỗi vào tiệc Halloween của bạn, in mã mời cho khách; khách chụp chung một
    album.
  tactic: s14-test-with-target-group
  tactic_note: Test thật với nhóm bạn bè trong một sự kiện có sẵn, dùng bản web chưa hoàn thiện
- stage: validate
  ts: 07:16
  case: once
  what: Lọc danh bạ X, LinkedIn, Instagram, Facebook để tìm người có sự kiện sắp tới; 4 người bạn nói
    sẽ dùng thử.
  tactic: g1-first-10-users
  tactic_note: Mời người quen trực tiếp (bạn bè có sự kiện sắp tới) trước khi build xong
- stage: validate
  ts: 07:47
  case: once
  what: 'Tìm trên Instagram theo #wedding, #birthdayparty khoảng 250–300 người, gửi DM 2–3 câu chào mời
    dùng thử; khoảng 15 người trả lời và 12 sự kiện được đặt lịch trong một tháng.'
  tactic: g1-first-10-users
  tactic_note: DM lạnh tới người lạ theo hashtag sự kiện, không phải đăng nội dung công khai
- stage: validate
  ts: '10:42'
  case: once
  what: 'Đặt mốc cam kết trước khi viết dòng code: 10 sự kiện có ngày cụ thể đang dùng app.'
  tactic: s14-test-with-target-group
  tactic_note: 'Commitment metric: cam kết dùng sản phẩm trong sự kiện làm chứng cứ thay cho tiền (khác
    s7 là không nhận tiền, s8 là không đăng nội dung)'
  threshold: 10 sự kiện có ngày cụ thể
- stage: monetize
  ts: 01:47
  case: once
  what: 'Thu theo số khách mời: gói bậc theo số khách, tiệc nhỏ vài đô, đám cưới 150 khách khoảng $50.'
  tactic: g4-pricing-paywall
quotes:
- ts: 08:51
  who: Brian Shin
  stage: validate
  theme:
  - sell-before-build
  text: And the commitment metric of the client to signal validation doesn't always need to be payment.
  vi: Cam kết của khách để chứng minh nhu cầu không nhất thiết phải là tiền. Với họ là chủ sự kiện dùng
    sản phẩm trong sự kiện.
- ts: '12:32'
  who: Brian Shin
  stage: mindset
  theme:
  - action-over-research
  text: I realized that those are really not the most important things if you're trying to go zero to
    one.
  vi: Tôi nhận ra marketing và bán hàng không phải là thứ quan trọng nhất khi đang đi từ số 0 lên 1.
- ts: '12:47'
  who: Brian Shin
  stage: launch
  theme:
  - ship-ugly
  text: Because all of your assumptions and all of your guesswork may go to nothing once you launch and
    once users start using it.
  vi: Vì mọi giả định và phỏng đoán có thể thành con số không khi bạn ra mắt và người dùng bắt đầu dùng.
rules:
- ts: '11:12'
  who: Pat Walls
  stage: validate
  theme: []
  text: It sounds hard, but it will save you so much time not building the wrong thing.
  vi: Nghe có vẻ khó, nhưng nó giúp bạn tiết kiệm rất nhiều thời gian vì không build nhầm thứ.
  evidence: opinion
- ts: '14:23'
  who: Gus
  stage: mindset
  theme:
  - builder-trap
  - emotional-bottleneck
  text: And with Claude Co and all these AI tools, it makes it so easy to do it and then avoid the hard
    part.
  vi: Với Claude Code và các công cụ AI, làm việc build thì quá dễ, và người ta lẩn tránh phần khó.
  evidence: opinion
- ts: '14:53'
  who: Gus
  stage: validate
  theme:
  - builder-trap
  text: Instead of talking to people, I'm just going to build it.
  vi: Thay vì nói chuyện với người ta, tôi cứ thế build.
  evidence: opinion
numbers:
- ts: 02:03
  metric: người dùng hoạt động hàng tuần
  value: 10000–12000
  unit: count
  evidence: claimed
- ts: 02:18
  metric: sự kiện đã đặt lịch qua Once (tháng 2, đọc từ dashboard lịch)
  value: 300
  unit: count
  evidence: measured
- ts: 02:18
  metric: sự kiện sắp tới (tháng 3, đọc từ dashboard lịch)
  value: 700
  unit: count
  evidence: measured
- ts: 07:47
  metric: người được DM lạnh (theo hashtag sự kiện)
  value: 250–300
  unit: count
  evidence: claimed
- ts: 08:03
  metric: người trả lời DM
  value: 15
  unit: count
  evidence: claimed
- ts: 08:03
  metric: sự kiện được đặt lịch từ DM trong một tháng
  value: 12
  unit: count
  evidence: claimed
- ts: '10:42'
  metric: mốc cam kết trước khi build (sự kiện có ngày cụ thể)
  value: 10
  unit: count
  evidence: claimed
frameworks: []
idea_patterns:
- passion-skin
---

## Một câu

Once, app máy ảnh dùng một lần cho tiệc và đám cưới, làm sau chuyến đi của hai người bootstrap: thử bản web với bạn bè, DM lạnh lấy 12 sự kiện trước khi làm app; theo founder đạt khoảng 20k/tháng trong 83 ngày kể từ ra mắt.

## Bài học cho tôi

- Đặt một mốc cam kết cụ thể trước khi build (10 sự kiện có ngày, không cần tiền) và coi đó là chứng cứ nhu cầu (`08:51`, `10:42`).
- Thử với người thật trước: bản web đầu đưa vào tiệc bạn bè, rồi DM 250–300 người lạ để lấy 12 sự kiện (`05:10`, `07:47`).

## Đừng tin vội

- Doanh thu 20–22k/tháng là lời founder. Dashboard mở ra là lịch sự kiện (300 và 700), không có số tiền (`02:18`).
- Mâu thuẫn trong video: host mở đầu nói họ "didn't start building until we hit it" (`00:00`), nhưng founder kể đã làm bản web đầu 1–2 tuần trước khi validate (`05:10`).
- "83 ngày" tính từ ra mắt (tháng 12/2025), không phải từ lúc bắt đầu làm.
- Video không nói: kênh nào đưa 20k/tháng sau ra mắt, người trả đầu tiên đến từ đâu. Phần growth được hẹn video sau.
- Lợi thế thật là mạng bạn bè có sự kiện sắp tới, bạn gái làm co-founder và kinh nghiệm B2B trước đó. Solo founder không có những thứ này khó chép đúng số 4 bạn và 12 sự kiện.
- Chủ đề sự kiện (tiệc, đám cưới) có tính mùa vụ và phụ thuộc người tổ chức, không phải mọi app đều giống vậy.
