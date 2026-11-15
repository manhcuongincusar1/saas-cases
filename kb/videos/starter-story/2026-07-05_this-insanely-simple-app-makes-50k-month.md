---
schema: 2
video_id: uvIcGuN2iO8
channel: starter-story
title: This Insanely Simple App Makes $50K/Month
date: 2026-07-05
url: https://www.youtube.com/watch?v=uvIcGuN2iO8
transcript: starter-story-kb/videos/2026-07-05_this-insanely-simple-app-makes-50k-month/transcript.md
kind: founder_case
speakers:
- name: Jake
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story quảng bá database 30+ ý tưởng app miễn phí (link trong mô tả và trong video). Founder
  được lợi nếu người xem tin app đơn giản là dễ kiếm tiền. Số $50k là lời founder, có một ảnh dashboard
  nhưng không kiểm chứng được ngoài video.
analyzed: 2026-11-15
cases:
- id: early
  depth: full
  product: 'Early (Wake Up Early): báo thức iOS buộc chống đẩy mới tắt được chuông'
  what: 'Báo thức iOS: đặt giờ, chọn nhiệm vụ chống đẩy; app phân tích video để xác nhận đã làm xong rồi
    mới tắt chuông'
  type:
  - ios-app
  customer: Người muốn dậy sớm; trả gói đăng ký
  founder:
    who: Jake
    base: null
    technical: true
    team: solo, nay có người giúp
    background: Học kế toán (CPA), làm kiểm toán big four hơn một năm; tự học code khoảng 4 năm
  revenue:
    amount: 50000
    unit: usd
    basis: last_28_days
    note: Founder đọc 'last 28 days of sales, a little over $50,000' khi host xin xem screenshot doanh
      thu. Ảnh dashboard (screenshots/03) hiện Sales $61.2K trên biểu đồ kéo tới 17/5, không khớp đúng
      cửa sổ 28 ngày.
    q: This is the last 28 days of sales, done a little over $50,000.
    ts: 01:47
    evidence: measured
  pricing: Dùng thử miễn phí, sau đó $29.99/năm hoặc $9.99/tháng
  idea_origin:
  - own_pain
  - timing_trigger
  scale_channels:
  - influencer_paid
  community_at_discovery:
    value: Chính founder khó dậy sớm; mỗi đêm nhắn bạn video chống đẩy trước 6 giờ sáng để tự ép
    insider: true
    q: I was having trouble myself waking up early
    ts: 04:09
  demand_signal: null
  prior_failures:
    count: null
    what: Trước đó có vài doanh nghiệp khác, không cái nào ăn; nhận ra marketing mới là thứ quan trọng
      nhất
    q: Had some other businesses in the past, nothing really worked.
    ts: 02:33
  unfair_advantage:
  - value: technical_skill
    what: Tự học code khoảng 4 năm, bên cạnh nền kế toán
    q: But I've been coding, I'm self-taught like the last 4 years or so
    ts: 02:33
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 4
      value: '4 tháng: từ 0 lên khoảng $50k/tháng'
      q: went from zero to $50,000 a month in 4 months
      ts: 01:02
  first_users:
  - channel: influencer_paid
    what: Influencer TikTok/Instagram làm video đời sống có app trong video, trả theo view; video đầu
      tiên lên sau 7 ngày
    q: My first influencer video went live 7 days later.
    ts: 06:44
  build:
    time: khoảng 19 ngày từ commit đầu tới App Store (MVP), thêm khoảng 19 ngày cho tính năng báo thức
    cut:
    - 'Tính năng báo thức: MVP ra không có, thêm sau'
    q: it took about 19 days from my first commit to live on the App Store
    ts: 05:58
steps:
- stage: find-idea
  ts: 04:09
  case: early
  what: 'Ý tưởng từ nỗi đau của chính mình: khó dậy sớm, nên mỗi đêm nhắn bạn video chống đẩy trước 6
    giờ sáng.'
  tactic: s5-insider
- stage: find-idea
  ts: 04:55
  case: early
  what: Sau một ngày nghĩ các hướng, chọn tính năng báo thức khi iOS 26 mở API cho app nối với báo thức
    hệ thống.
  tactic: s12-timing-shift
  tactic_note: 'Đổi hướng theo API nền tảng mới (AlarmKit, iOS 26): báo thức đáng tin hơn là lý do chọn'
- stage: launch
  ts: 06:44
  case: early
  what: Thuê influencer làm video đầu tiên 7 ngày sau khi MVP ra; thấy người mua từ video đó nên xác nhận
    ý tưởng và đẩy mạnh.
  tactic: g7-creator-ops
- stage: monetize
  ts: 02:03
  case: early
  what: 'Đặt mô hình: dùng thử miễn phí rồi trả $29.99/năm hoặc $9.99/tháng.'
  tactic: g4-pricing-paywall
  threshold: $29.99/năm, $9.99/tháng
- stage: grow
  ts: 09:04
  case: early
  what: Tìm influencer TikTok/Instagram làm nội dung đời sống, gửi rất nhiều DM; đầu ít người trả lời.
  tactic: g7-creator-ops
- stage: grow
  ts: '10:05'
  case: early
  what: Format video POV đời sống do influencer làm (ngủ dậy, báo thức, chống đẩy), app hiện tự nhiên;
    người xem hỏi tên app và founder ghim comment đó.
  tactic: g3-organic-content-formats
  tactic_note: Format do creator đăng; CTA là ghim comment hỏi tên app
- stage: grow
  ts: '11:07'
  case: early
  what: 'Hợp đồng: 2–4 video/tháng, trả theo view có bảo đảm; phần lớn tiền nằm ở vài video triệu view.'
  tactic: g7-creator-ops
  threshold: 2–4 video/tháng
  cost: khoảng $2–3 CPM
- stage: grow
  ts: '12:09'
  case: early
  what: 'Khó đo influencer: theo dõi view và tìm đỉnh (spike) view trùng với đỉnh lượt cài và mua.'
  tactic: g8-funnel-measurement
quotes:
- ts: 06:28
  who: Jake
  stage: validate
  theme:
  - action-over-research
  text: So my framework here was just ship fast, validate the idea as fast as possible, but I wasn't sure
    if I could get views.
  vi: Khung của tôi là ship nhanh, validate ý tưởng nhanh nhất có thể, nhưng tôi không chắc có ai xem
    không.
- ts: 07:48
  who: Jake
  stage: find-idea
  theme: []
  text: If it's painful, people will pay.
  vi: Nếu đó là nỗi đau thì người ta sẽ trả tiền.
- ts: 02:33
  who: Jake
  stage: mindset
  theme: []
  text: Had some other businesses in the past, nothing really worked. I realized [music] through all these
    failures that marketing is the most important thing.
  vi: Trước đây tôi có vài việc kinh doanh khác, không cái nào ăn. Qua những thất bại đó tôi nhận ra marketing
    là thứ quan trọng nhất.
- ts: '14:59'
  who: Jake
  stage: grow
  theme:
  - focus-one-thing
  text: Focus on top of funnel only. That is the most valuable skill right now is marketing.
  vi: Chỉ tập trung vào phần đầu phễu. Kỹ năng giá trị nhất lúc này là marketing.
- ts: '15:15'
  who: Jake
  stage: grow
  theme: []
  text: And if nobody knows about your app, it doesn't exist.
  vi: Nếu không ai biết về app của bạn thì nó coi như không tồn tại.
rules:
- ts: 03:06
  who: Pat Walls
  stage: find-idea
  theme: []
  text: He did not build something complicated. Instead, he found a painful problem and built a dead simple
    solution around it.
  vi: Anh ấy không làm thứ phức tạp. Thay vào đó anh tìm một nỗi đau rồi làm một giải pháp cực đơn giản.
  evidence: opinion
- ts: '16:46'
  who: Gus
  stage: find-idea
  theme: []
  text: look at changes to APIs that Apple or other platforms enable. Usually, there's a slew of apps
    that will get released when there is a new change in the API.
  vi: Hãy xem các thay đổi API mà Apple hoặc nền tảng khác mở ra. Thường sẽ có một loạt app ra mắt ngay
    khi API thay đổi.
  evidence: opinion
- ts: '18:20'
  who: Gus
  stage: grow
  theme: []
  text: creating content, putting yourself out there, not only is it hard, but it's scary, and that's
    why it prevents a lot of people from doing it.
  vi: Tạo nội dung và đưa mình ra trước công chúng vừa khó vừa đáng sợ, và đó là lý do nhiều người không
    làm.
  evidence: opinion
numbers:
- ts: 01:47
  metric: doanh thu 28 ngày gần nhất (lời founder, có dashboard)
  value: 50000
  unit: usd
  evidence: measured
- ts: 01:47
  metric: lượt tải trong 30 ngày gần nhất
  value: 50000
  unit: count
  evidence: claimed
- ts: 01:47
  metric: lượt tải từ đầu 2026
  value: 200000
  unit: count
  evidence: claimed
- ts: '11:23'
  metric: 'CPM trả influencer (lời founder: khoảng)'
  value: 2-3
  unit: usd_cpm
  evidence: claimed
frameworks: []
idea_patterns:
- platform-api-unlock
---
## Một câu

App báo thức iOS buộc chống đẩy mới tắt được chuông, một người làm trong khoảng một tháng rồi thêm báo thức sau; founder nói đạt $50k trong 28 ngày nhờ influencer trả theo view.

## Bài học cho tôi

- Chọn nỗi đau có thật và đủ đơn giản để nhìn video là hiểu; founder đưa ra influencer ngay sau khi MVP ra và đã có người mua từ video đầu tiên (`06:44`).
- Trả influencer theo view có bảo đảm, đo bằng cách tìm đỉnh view trùng đỉnh lượt cài (`11:07`, `12:09`).

## Đừng tin vội

- Doanh thu là lời founder cộng một màn hình dashboard. Ảnh chụp hiện $61.2K trên biểu đồ tới 17/5, khác con số "28 ngày, a little over $50,000" đọc trong lời. Ghi theo lời, nhưng lệch cần lưu ý.
- Chi phí influencer, phí công cụ, tỉ lệ hoàn tiền và churn không được nói. Con số $2–3 CPM là "around", chưa chắc.
- Ý tưởng dựa vào một API mới của iOS 26 (AlarmKit). Cửa sổ như vậy đóng nhanh khi nhiều app cùng làm; founder có nền kế toán và tự code 4 năm, không phải người đi từ số 0.
- Video là case quảng bá database app miễn phí của Starter Story. Founder tự kể, không có số liệu đối chiếu ngoài dashboard.
