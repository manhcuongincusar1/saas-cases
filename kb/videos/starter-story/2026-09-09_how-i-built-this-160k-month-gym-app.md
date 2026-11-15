---
schema: 2
video_id: OV09yPLf8BI
channel: starter-story
title: How I Built This $160K/Month Gym App
date: 2026-09-09
url: https://www.youtube.com/watch?v=OV09yPLf8BI
transcript: starter-story-kb/videos/2026-09-09_how-i-built-this-160k-month-gym-app/transcript.md
kind: founder_case
speakers:
- name: Mauro
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story (đối tác HubSpot) quảng bá database ý tưởng iOS miễn phí giữa video. Founder bán app
  và tự khoe số trên dashboard; Superwall được nhắc là công cụ đang dùng.
analyzed: 2026-11-15
cases:
- id: symmetry
  depth: full
  product: 'Symmetry (symmetry.club): app theo dõi buổi tập gym, ghi cân nặng và reps, có feed kiểu Strava'
  what: 'App tập gym: làm theo plan, ghi reps và cân nặng, rank theo nhóm cơ, streak, feed bạn bè; thị
    trường chính Tây Ban Nha và Mexico'
  type:
  - mobile-app
  customer: Người tập gym nói tiếng Tây Ban Nha (chủ yếu Tây Ban Nha và Mexico)
  founder:
    who: Mauro
    base: null
    technical: null
    team: đồng sáng lập (cùng từng là YouTuber fitness) và team nội bộ
    background: 22 tuổi; từng béo, gym giúp thay đổi; trước app là YouTuber fitness cùng các đồng sáng
      lập
  revenue:
    amount: 160000
    unit: usd
    basis: monthly
    note: Dashboard cho thấy ~160k doanh thu hằng tháng gần nhất; ~3 triệu lượt tải iOS + Android
    q: You can see we're currently at around 160k monthly revenue.
    ts: 01:55
    evidence: measured
  pricing: null
  idea_origin:
  - own_pain
  - domain_expertise
  scale_channels:
  - ugc_creators
  community_at_discovery:
    value: YouTuber fitness (kênh YouTube gym) trước khi làm app
    insider: true
    q: Before building Symmetry, I was actually a fitness YouTuber, and so were
    ts: 02:29
  demand_signal: null
  prior_failures:
    count: 2
    what: Kênh YouTube fitness có sẵn không đẩy được tải như kỳ vọng; sau đó thử influencer marketing
      cũng không hiệu quả
    q: we had this YouTube community. And we thought it was going to be really good for growing the app.
      It wasn't.
    ts: 03:34
  unfair_advantage:
  - value: existing_audience
    what: 'Kênh YouTube fitness có sẵn: lúc ra mắt tải tăng nhỏ nhờ kênh này'
    q: due to our previous YouTuber era
    ts: 03:02
  - value: domain_expertise
    what: Là người tập gym lâu năm; app do chính người tập làm
    q: I like to gym so much that I built Symmetry
    ts: 01:22
  - value: cofounder
    what: Các đồng sáng lập (YouTuber fitness) cùng nhau làm app
    q: And that is when we joined together to build Symmetry
    ts: 02:45
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 12
      value: '''gần một năm'' (just barely over a year) từ ngày ra mắt'
      q: So, we launched on 6th of June of last year, so just barely over a year.
      ts: 03:02
  first_users:
  - channel: youtube_founder
    what: 'Kênh YouTube fitness cũ của nhóm: tải tăng nhỏ lúc ra mắt, không bền'
    q: due to our previous YouTuber era
    ts: 03:02
  build: null
steps:
- stage: find-idea
  ts: 02:29
  case: symmetry
  what: Làm Symmetry vì chính trải nghiệm gym của mình (từng béo, gym giúp), muốn chia sẻ cho người khác.
  tactic: s5-insider
- stage: launch
  ts: 03:02
  case: symmetry
  what: Ra mắt dựa vào kênh YouTube fitness của nhóm; tải tăng nhỏ rồi không bền.
  tactic: g1-first-10-users
  tactic_note: Dùng audience YouTube fitness sẵn có
- stage: grow
  ts: 03:52
  case: symmetry
  what: Thử influencer marketing; không hiệu quả nên chuyển sang cách khác.
  tactic: g7-creator-ops
- stage: grow
  ts: 03:52
  case: symmetry
  what: 'Chuyển sang UGC: trong một năm đăng gần 80.000 video qua hơn 500 tài khoản, gần 8 tỷ lượt xem.'
  tactic: g7-creator-ops
- stage: grow
  ts: 04:08
  case: symmetry
  what: 'Chia video thành các format (ví dụ: ảnh khoá màn hình có thông báo), theo dõi từng format và
    sub-format; một video đạt 17 triệu view.'
  tactic: g3-organic-content-formats
- stage: grow
  ts: 04:24
  case: symmetry
  what: Trả creator gần một nửa doanh thu để họ làm nhiều nội dung và ở lại lâu dài.
  tactic: g7-creator-ops
  threshold: gần 50% doanh thu
- stage: grow
  ts: 07:26
  case: symmetry
  what: Đặt OKR quý (warm-up mỗi 90 ngày) với mục tiêu cao, theo dõi metric hằng ngày hoặc hằng tuần;
    chọn activation làm chỉ số chính.
  tactic: g8-funnel-measurement
  tactic_note: OKR quý, mục tiêu cao khi app còn mới
- stage: monetize
  ts: '13:16'
  case: symmetry
  what: A/B test paywall bằng Superwall.
  tactic: g4-pricing-paywall
  tool: Superwall
- stage: grow
  ts: '11:53'
  case: symmetry
  what: Mọi thí nghiệm A/B được theo dõi trong PostHog; chạy ít nhất 2 tuần rồi phân tích; biến thể không
    đổi chỉ số thì bỏ.
  tactic: g8-funnel-measurement
  tool: PostHog
  tactic_note: A/B test mọi thay đổi; test không đổi chỉ số thì tắt
- stage: retain
  ts: '12:27'
  case: symmetry
  what: Thêm một màn hình cam kết tập luyện cuối onboarding; retention tăng 3%.
  tactic: g8-funnel-measurement
  tactic_note: A/B test màn hình onboarding
quotes:
- ts: 05:31
  who: Mauro
  stage: mindset
  theme:
  - right-audience
  text: First, we built what we wanted. Terrible idea. Second, we built what users wanted like directly
    from feedback quest. Mediocre.
  vi: 'Lần đầu làm điều mình muốn: ý tưởng tệ. Lần hai làm điều người dùng muốn từ phản hồi: tạm được.'
- ts: 07:42
  who: Mauro
  stage: grow
  theme: []
  text: Like, it's very easy to increase 10% conversion rate in 90 days if your app was launched last
    week.
  vi: App mới ra thì rất dễ tăng 10% tỉ lệ chuyển đổi trong 90 ngày; nên OKR càng tham vọng khi app càng
    mới.
- ts: '12:27'
  who: Mauro
  stage: retain
  theme: []
  text: It increased 3% retention adding one screen. That is why you have to AB test everything.
  vi: Thêm một màn hình mà retention tăng 3%. Vì vậy phải A/B test mọi thứ.
- ts: '14:24'
  who: Mauro
  stage: mindset
  theme:
  - persistence
  text: I would say to play long-term games with long-term people.
  vi: 'Tôi sẽ nói: chơi trò dài hạn với những người dài hạn.'
- ts: '14:41'
  who: Mauro
  stage: mindset
  theme:
  - persistence
  text: We were really bad when we started but we never surrendered and we just kept pushing
  vi: Lúc mới bắt đầu chúng tôi rất tệ, nhưng không bỏ cuộc và cứ tiếp tục đẩy.
rules:
- ts: '16:36'
  who: Pat Walls hoặc Gus
  stage: grow
  theme: []
  text: Most of the tests that you run and the things that you try don't move the needle at all.
  vi: Phần lớn các test và thử nghiệm không làm chuyển kim chỉ số nào.
  evidence: opinion
- ts: '17:08'
  who: Pat Walls hoặc Gus
  stage: grow
  theme: []
  text: maybe focus more on marketing than product often.
  vi: Có lẽ thường nên dành nhiều tâm sức cho marketing hơn là sản phẩm.
  evidence: opinion
numbers:
- ts: 01:55
  metric: doanh thu hằng tháng (dashboard)
  value: 160000
  unit: usd_per_month
  evidence: measured
- ts: 01:55
  metric: lượt tải iOS + Android
  value: 3000000
  unit: count
  evidence: measured
- ts: 03:18
  metric: lượt tải mùa hè khi thử UGC
  value: 30000
  unit: count
  evidence: claimed
- ts: 03:52
  metric: video đăng trong năm qua
  value: 80000
  unit: count
  evidence: measured
- ts: 03:52
  metric: tài khoản creator
  value: 500
  unit: count
  evidence: measured
- ts: 04:08
  metric: lượt xem trong năm qua
  value: 8000000000
  unit: views
  evidence: measured
- ts: 04:24
  metric: lượt xem một video viral (format lock screen)
  value: 17000000
  unit: views
  evidence: measured
- ts: 04:24
  metric: tỉ lệ doanh thu trả cho creator
  value: 50
  unit: percent
  evidence: claimed
- ts: '12:27'
  metric: retention tăng khi thêm một màn hình onboarding
  value: 3
  unit: percent
  evidence: claimed
frameworks: []
idea_patterns: []
---
## Một câu

Mauro (22 tuổi) cùng các đồng sáng lập từng là YouTuber fitness làm Symmetry, app tập gym chủ yếu cho Tây Ban Nha và Mexico, tự báo ~160k/tháng sau một năm; tăng trưởng nhờ UGC chia theo format, trả creator gần một nửa doanh thu, và A/B test mọi thay đổi.

## Bài học cho tôi

- Chia nội dung thành format rồi theo dõi từng format; một format đạt 17 triệu view (`04:08`, `04:24`).
- A/B test mọi thay đổi và chạy ít nhất 2 tuần; phần lớn thí nghiệm không đổi chỉ số (`11:53`, `16:36`).

## Đừng tin vội

- Quy mô vận hành lớn: gần 80.000 video, 500+ tài khoản creator, gần 8 tỷ lượt xem, và trả gần nửa doanh thu cho creator. Solo founder khó sao chép; video không nêu margin sau khi trả creator.
- Nhóm có kênh YouTube fitness sẵn và đồng sáng lập; đây là lợi thế thật (`03:02`, `02:45`), không phải ai cũng có.
- ARPU khác nhau nhiều giữa các nước (Mauro nói, `09:05`); số liệu Tây Ban Nha và Mexico không chuyển thẳng sang thị trường trả cao.
- Câu "1 năm ra $160k" là lời host (`04:57`); video không nêu chi phí quảng cáo và chi phí creator.
