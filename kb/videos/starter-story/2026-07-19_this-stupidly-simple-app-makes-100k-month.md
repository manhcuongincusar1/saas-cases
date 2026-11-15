---
schema: 2
video_id: EQfZCe3MkTU
channel: starter-story
title: This Stupidly Simple App Makes $100K/Month
date: 2026-07-19
url: https://www.youtube.com/watch?v=EQfZCe3MkTU
transcript: starter-story-kb/videos/2026-07-19_this-stupidly-simple-app-makes-100k-month/transcript.md
kind: founder_case
speakers:
- name: Michael
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story bán database 100+ ý tưởng app (link trong mô tả và giữa video) nên video là phễu;
  hai host khen founder và ý tưởng; số liệu Michael tự báo; kênh TikTok của Michael là kênh chính.
analyzed: 2026-11-15
cases:
- id: go-tall
  depth: full
  product: Go Tall (app dự đoán chiều cao cho thiếu niên)
  what: Dự đoán chiều cao và gợi ý thói quen (ăn, ngủ, tư thế) để tăng chiều cao; onboarding dài có quiz
    dậy thì; paywall; gói tuần và năm
  type:
  - mobile-app
  customer: Thiếu niên và người muốn cao hơn; người trả tiền ở gói tuần hoặc năm
  founder:
    who: Michael
    base: null
    technical: true
    team: không nêu rõ; có vài UGC creator làm nội dung
    background: Sinh viên 20 tuổi học tài chính ở NYU; bị từ chối các việc làm mơ ước; từng làm app khi
      còn nhỏ
  revenue:
    amount: 100000
    unit: usd
    basis: monthly
    note: trung bình 'about 100K a month' theo founder; host nói $100,000; dashboard được mở nhưng transcript
      không ghi founder đọc doanh thu từ đó
    q: I built an app called Go Tall that now makes on average about 100K a month.
    ts: 01:03
    evidence: claimed
  pricing: Gói tuần $5; gói năm $35; có gói premium rẻ hơn với tính năng khác (video không nêu giá)
  idea_origin:
  - own_pain
  - revenue_scouting
  scale_channels:
  - tiktok_organic
  - ugc_creators
  - paid_unspecified
  community_at_discovery:
    value: Video TikTok về chiều cao; người xem tự kể chiều cao của mình; chính Michael từng tìm máy tính
      chiều cao hồi 13 tuổi
    insider: true
    q: on Tik Tok, if you just look at any sort of height video in general
    ts: 05:26
  demand_signal: null
  prior_failures:
    count: null
    what: Làm app khi còn nhỏ nhưng không giỏi marketing (không nêu kết quả)
    q: but I was just never really good at marketing
    ts: 03:09
  unfair_advantage:
  - value: technical_skill
    what: Tự làm app từ khi còn đi học, trước cả thời AI
    q: When I was a teenager, I was developing my own apps even before like AI
    ts: 03:09
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: tiktok_organic
    what: Trả lời comment TikTok bằng cách dự đoán chiều cao; là một trong những format viral đầu tiên
    q: one of my first viral formats was just replying to those comments and predicting their height.
    ts: 05:41
  - channel: ugc_creators
    what: DM khoảng 50 người mỗi ngày để họ làm video theo format; trả giá rẻ
    q: So I just went on DM'd like 50 people a day
    ts: 09:30
  build:
    time: Làm vào mùa hè trước; video không nêu số tuần
    cut: []
    q: last summer I built an app called Go Tall
    ts: 01:03
steps:
- stage: find-idea
  ts: 04:40
  case: go-tall
  what: Soi acquire.com (website rao bán app), thấy một app tương tự đang rao bán khoảng $20K; quyết định
    tự làm lại app đó vì thấy vấn đề là có thật.
  tactic: s1-revenue-spy
  tool: acquire.com
  threshold: app tương tự rao bán khoảng $20,000
- stage: find-idea
  ts: 05:10
  case: go-tall
  what: 'Nhớ nỗi đau cá nhân: hồi 13 tuổi tìm máy tính chiều cao trên Google, nên thấy vấn đề có thật.'
  tactic: s5-insider
  tactic_note: Nỗi đau cá nhân của founder, kiểm lại bằng comment TikTok
- stage: find-idea
  ts: 05:26
  case: go-tall
  what: Đọc comment video chiều cao trên TikTok (người xem tự kể chiều cao, bố mẹ cao bao nhiêu) để xác
    nhận người ta muốn được dự đoán.
  tactic: s4-tiktok-comment-mining
  tactic_note: Đọc comment để xác nhận nhu cầu; không đăng nội dung ở bước này
- stage: grow
  ts: 08:44
  case: go-tall
  what: Tự làm khoảng 10 TikTok mỗi ngày trong khoảng một tháng để tìm format; format thắng là trả lời
    comment dự đoán chiều cao, nhân bản sang hai tài khoản và nhờ bạn gái làm.
  tactic: g3-organic-content-formats
  tactic_note: Thử nhiều video organic, tìm format thắng rồi nhân bản
- stage: grow
  ts: 09:30
  case: go-tall
  what: 'Thuê UGC creator: DM khoảng 50 người mỗi ngày, dạy họ format, trả giá rẻ; cùng với bản thân đạt
    khoảng 3K/tháng.'
  tactic: g7-creator-ops
  tactic_note: Creator trả giá rẻ để làm đúng format đã biết thắng
- stage: monetize
  ts: 09:46
  case: go-tall
  what: 'Tối ưu paywall rồi scale: doanh thu từ khoảng 3K lên khoảng 10K/tháng; tháng thứ năm khoảng 30K
    khi thử thêm format.'
  tactic: g4-pricing-paywall
  tactic_note: Tối ưu paywall trước khi scale
- stage: grow
  ts: 09:46
  case: go-tall
  what: Khi lên khoảng 30K/tháng thì đưa format thắng lên paid ads để đẩy lên hơn 100K/tháng.
  tactic: g6-paid-ads
  tactic_note: Organic tìm format thắng rồi mới chạy ads; nền tảng quảng cáo không nêu
- stage: monetize
  ts: '11:36'
  case: go-tall
  what: Onboarding rất dài (hỏi thông tin để tính chiều cao, quiz dậy thì, link nghiên cứu) rồi paywall;
    gói tuần $5, năm $35.
  tactic: g4-pricing-paywall
  tactic_note: Onboarding dài thu thập dữ liệu rồi paywall; paywall hiển thị cho khoảng 91% người dùng
quotes:
- ts: 03:09
  who: Michael
  stage: find-idea
  theme:
  - many-bets
  text: I was just doing any app idea that I could find.
  vi: Tôi cứ làm bất kỳ ý tưởng app nào mình tìm được; cái này là một trong những cái đầu tiên tôi thấy
    có tiềm năng.
- ts: 03:24
  who: Michael
  stage: mindset
  theme:
  - risk-and-leap
  text: even if this app failed, at least I would come out with the skills of like how to do marketing.
  vi: Dù app có thất bại thì ít nhất tôi cũng có kỹ năng marketing.
- ts: '13:25'
  who: Michael
  stage: mindset
  theme: []
  text: Last summer, I basically just got rid of my ego.
  vi: Mùa hè trước, tôi gần như bỏ cái tôi xuống, không quan tâm người khác nghĩ gì về việc làm app dự
    đoán chiều cao.
- ts: '13:40'
  who: Michael
  stage: mindset
  theme:
  - ship-ugly
  text: Go make the stupid Tik Toks. Go do the idea that you think has potential even though it's so unglamorous.
  vi: Cứ làm TikTok ngớ ngẩn đi; cứ làm ý tưởng bạn thấy có tiềm năng dù nó rất không hào nhoáng.
rules:
- ts: 06:11
  who: Pat Walls hoặc Gus
  stage: find-idea
  theme: []
  text: All good business ideas come from problems, solving problems.
  vi: Ý tưởng kinh doanh tốt đều bắt đầu từ việc giải quyết vấn đề.
  evidence: opinion
- ts: 08:14
  who: Pat Walls hoặc Gus
  stage: validate
  theme: []
  text: Often, a lot of times when we build startups, we build something and then we get no DMs.
  vi: Khi build xong nhiều startup không ai nhắn tin; DM là tín hiệu nhu cầu đáng để ý.
  evidence: opinion
- ts: '10:01'
  who: Pat Walls hoặc Gus
  stage: grow
  theme: []
  text: you kind of crack UGC, you figure out what kind of organic content works and then you just put
    ads behind that content
  vi: 'Playbook phổ biến: tìm được nội dung organic thắng (UGC) rồi mới đẩy ads lên đúng nội dung đó.'
  evidence: opinion
- ts: '14:12'
  who: Pat Walls hoặc Gus
  stage: mindset
  theme: []
  text: in order to be successful, you need to uh climb up cringe mountain and you need to make it to
    the top of cringe mountain
  vi: Muốn thành công phải vượt qua giai đoạn xấu hổ; phải chịu cảm giác cringe khi đăng nội dung.
  evidence: opinion
numbers:
- ts: 02:23
  metric: doanh thu trung bình hàng tháng (host nói $100,000)
  value: 100000
  unit: usd_per_month
  evidence: claimed
- ts: 02:23
  metric: tổng lượt tải App Store và Android (khoảng 700K + vài trăm nghìn)
  value: 1000000
  unit: count
  evidence: claimed
- ts: 04:40
  metric: giá rao bán app tương tự trên acquire.com
  value: 20000
  unit: usd
  evidence: claimed
- ts: 08:59
  metric: số TikTok mỗi ngày trong giai đoạn thử format
  value: 10
  unit: count_per_day
  evidence: claimed
- ts: 09:30
  metric: doanh thu khi chỉ có founder và vài UGC creator
  value: 3000
  unit: usd_per_month
  evidence: claimed
- ts: 09:46
  metric: doanh thu tháng thứ năm, trước khi chạy paid ads
  value: 30000
  unit: usd_per_month
  evidence: claimed
- ts: '11:52'
  metric: tỉ lệ hiển thị paywall (paywall show rate)
  value: 91
  unit: percent
  evidence: claimed
frameworks:
- organic-find-format-then-paid-scale
idea_patterns: []
---

## Một câu

Michael (20 tuổi) thấy một app tương tự rao bán khoảng $20K trên acquire.com, nhớ nỗi đau hồi 13 tuổi, rồi làm Go Tall (dự đoán chiều cao); ~100K/tháng theo lời tự báo, nhờ TikTok organic tìm format thắng rồi UGC và paid ads.

## Bài học cho tôi

- Ý tưởng đi từ việc soi app đã có người trả tiền (rao bán ~$20K) rồi kiểm lại bằng nỗi đau cá nhân và comment TikTok (`04:40`, `05:10`).
- Tìm format organic thắng trước (khoảng 10 TikTok mỗi ngày trong một tháng), chỉ khi lên ~30K/tháng mới dồn tiền vào paid ads (`08:44`, `09:46`).

## Đừng tin vội

- Số liệu (100K/tháng, khoảng 1 triệu lượt tải, 91% paywall show rate) là Michael tự báo; có mở dashboard nhưng transcript không ghi con số doanh thu đọc từ đó. Video Superwall (2sLUhYP6a6k) ghi GoTall "~150K/tháng" theo host ("last time I checked"); hai con số khác nhau, thời điểm khác nhau, chưa đối chiếu được.
- "10–20 DM mỗi ngày" về việc dự đoán chiều cao (`07:12`) là tín hiệu mạnh, nhưng video không nói DM đến trước hay sau khi app ra mắt; app "tương tự rao bán $20K" cũng không nói doanh thu của nó.
- Điều kiện riêng: Michael là người trong cuộc (từng tìm máy tính chiều cao) và có kinh nghiệm làm app từ nhỏ; ngách chiều cao là nhạy cảm và gắn với thiếu niên, không sao chép nguyên được cho mọi người.
- Video không nói chi phí quảng cáo, CAC, ROAS hay số tháng từ lúc làm app đến 100K ("last summer", "sau 2 ngày có sale đầu tiên" không quy ra số tháng), nên các mốc G5 để null.
