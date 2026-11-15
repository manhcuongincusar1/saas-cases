---
schema: 2
video_id: RypUD_Fuaqw
channel: starter-story
title: This crazy simple app makes $50K/month
date: 2026-10-04
url: https://www.youtube.com/watch?v=RypUD_Fuaqw
transcript: starter-story-kb/videos/2026-10-04_this-crazy-simple-app-makes-50k-month/transcript.md
kind: founder_case
speakers:
- name: Lino
  role: founder
- name: Gus
  role: host
- name: Pat
  role: host
bias: Video có HubSpot database (iOS app ideas) tài trợ; Starter Story bán database và đang tuyển người;
  founder quảng bá AbMax trên chính kênh. Số doanh thu do founder đọc từ RevenueCat.
analyzed: 2026-11-15
cases:
- id: abmax
  depth: full
  product: 'AbMax: app kế hoạch tập cơ bụng cá nhân hoá (quét ảnh bụng, chấm điểm, chương trình tập sẵn)'
  what: Người dùng quét bụng để xem điều gì đang che cơ bụng (mỡ hay cơ), rồi được gợi ý chương trình
    tập sẵn như plan 30 ngày
  type:
  - ios-app
  customer: Người muốn có cơ bụng, nhất là cho mùa hè; trả gói đăng ký
  founder:
    who: Lino
    base: null
    technical: false
    team: Không nêu rõ; có hợp đồng với creator (dùng sign.com)
    background: 18 tuổi, bỏ đại học sau học kỳ đầu; chưa từng làm app hay viết code trước năm nay
  revenue:
    amount: 55000
    unit: usd
    basis: monthly
    note: '''Tháng này'' đọc từ RevenueCat (đang trong tháng); host nói đang trên đà 60k'
    q: our monthly revenue is just about $55,000 this month
    ts: 01:52
    evidence: measured
  pricing: Không nêu giá trong video
  idea_origin:
  - niche_down
  scale_channels:
  - influencer_partner
  - paid_meta
  - paid_tiktok
  community_at_discovery:
    value: Đi gym cùng bạn bè; mọi người so sánh cơ bụng. Lino là người trong cuộc
    insider: true
    q: I went to the gym with all my friends
    ts: 02:10
  demand_signal:
    kind: built_first
    level: 0
    what: Build bản đầu 2 tháng trên Lovable trước khi launch, chưa có tín hiệu nhu cầu nào
    q: I spent 2 months manually prompting this old project in Lovable
    ts: 04:25
  prior_failures:
    count: 1
    what: 'Bản Lovable đầu tiên: tự thấy không thể release, rebuild toàn bộ'
    q: there's absolutely no way I can release this
    ts: 04:42
  unfair_advantage: []
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 6
      value: Host nói 6 tháng trước Lino chưa từng làm app; founder nói ra app đầu khoảng 5 tháng trước
      q: 6 months ago, he had never built an app before in his life
      ts: 00:15
  first_users:
  - channel: influencer_partner
    what: Chia equity cho một influencer thể hình lớn để có content và ads; giúp khởi động sau khi UGC
      trả tiền bị lỗ margin
    q: we partnered up with a big fitness influencer on social media in return for some equity
    ts: 06:39
  - channel: tiktok_organic
    what: Founder tự đăng TikTok slideshow (không trả tiền), chạy cùng UGC lúc đầu
    q: which I was manually posting on my own
    ts: 06:22
  build:
    time: 2 tháng bản đầu trên Lovable; rebuild V2 trên Vork trong khoảng 1 tháng
    cut:
    - Bản Lovable đầu tiên (bỏ, làm lại từ đầu)
    q: I was able to build AppMax V2 basically in Vork in 1 month.
    ts: 04:59
steps:
- stage: find-idea
  ts: 02:10
  case: abmax
  what: Đi gym với bạn bè thấy mọi người so sánh cơ bụng; tìm trên mạng không thấy chỗ nào phục vụ người
    muốn có cơ bụng năm 2026, nên làm app.
  tactic: s5-insider
  tactic_note: Quan sát nhu cầu từ nhóm bạn trong phòng gym, rồi tự tìm khoảng trống; không nêu công cụ
    đo
- stage: find-idea
  ts: 05:31
  case: abmax
  what: Dùng Sensor Tower để nghiên cứu đối thủ và ý tưởng.
  tactic: s1-revenue-spy
  tool: Sensor Tower
- stage: build
  ts: 04:25
  case: abmax
  what: Build bản đầu 2 tháng trên Lovable khi chưa biết gì về app (chưa biết RevenueCat hay onboarding
    là gì).
- stage: build
  ts: 04:42
  case: abmax
  what: Trước khi launch thấy bản này quá tệ, rebuild toàn bộ trên Vork; vừa làm vừa theo dõi founder
    app trên X.
- stage: launch
  ts: 06:06
  case: abmax
  what: Chạy UGC trả tiền với influencer thể hình trước khi có format thắng; margin chỉ 5–10%. Lino tự
    nhận đây là một trong những sai lầm lớn nhất.
  tactic: g7-creator-ops
  threshold: margin 5–10%
- stage: launch
  ts: 06:22
  case: abmax
  what: Tự đăng TikTok slideshow; cùng UGC đưa doanh thu lên khoảng 3–4k.
  tactic: g3-organic-content-formats
- stage: launch
  ts: 06:39
  case: abmax
  what: Chia equity cho một influencer thể hình lớn để có content và ads gần như không mất tiền trả creator.
  tactic: g7-creator-ops
- stage: grow
  ts: 07:29
  case: abmax
  what: Cắt mọi deal UGC và influencer, dồn tiền vào Meta Ads (ROAS 2–2.5x) với content từ creator đã
    chia equity.
  tactic: g6-paid-ads
  threshold: ROAS 2–2.5x
- stage: grow
  ts: 08:00
  case: abmax
  what: Chuyển cùng creative từ Meta sang TikTok ads; đạt ROAS 4–5x, hợp với người dùng 15–30 tuổi.
  tactic: g6-paid-ads
  threshold: ROAS 4–5x
  tactic_note: Cùng creative chạy TikTok hiệu quả hơn Meta
quotes:
- ts: 04:42
  who: Lino
  stage: build
  theme:
  - learn-from-others
  text: this is when I started to get onto X and starting to follow all these other successful app founders
  vi: Đó là lúc tôi bắt đầu lên X và theo dõi các founder app thành công khác.
- ts: 06:06
  who: Lino
  stage: launch
  theme: []
  text: which is probably one of the biggest mistakes I've ever made
  vi: Đó có lẽ là một trong những sai lầm lớn nhất tôi từng mắc.
- ts: '13:46'
  who: Lino
  stage: mindset
  theme:
  - persistence
  text: as long as you never give up and you show up every day
  vi: Miễn là bạn không bao giờ bỏ cuộc và xuất hiện mỗi ngày.
rules:
- ts: '12:57'
  who: Host (không nêu tên)
  stage: grow
  theme: []
  text: the secret sauce has nothing really to do with how you built it
  vi: Bí quyết nằm ở marketing và phân phối, không phải ở cách bạn build.
  evidence: opinion
- ts: '15:23'
  who: Host (không nêu tên)
  stage: mindset
  theme: []
  text: there's nothing complicated here other than this guy just isn't scared to take action
  vi: 'Không có gì phức tạp: người này chỉ không sợ hành động.'
  evidence: opinion
numbers:
- ts: 01:52
  metric: lượt tải trong 28 ngày
  value: 16000
  unit: count
  evidence: measured
- ts: 02:10
  metric: người trả tiền đang hoạt động
  value: 3000
  unit: count
  evidence: measured
frameworks:
- influencer-equity-partner
- organic-find-format-then-paid-scale
idea_patterns:
- niche-inside-hot-category
---
## Một câu

Lino (18 tuổi, không biết code) build app quét bụng và kế hoạch tập cơ bụng bằng Lovable rồi Vork; đi lên nhờ TikTok slideshow tự đăng, chia equity cho một influencer thể hình, rồi dồn tiền vào Meta và TikTok ads; đạt khoảng 55k/tháng sau khoảng 6 tháng.

## Bài học cho tôi

- UGC trả tiền khi chưa có format thắng làm lỗ margin; đổi sang equity và chỉ đẩy ads khi creative đã chạy được (`06:06`, `06:39`).
- Ngách con trong danh mục fitness lớn: cơ bụng là một nỗi lo cụ thể; ý tưởng bắt đầu từ việc quan sát nhóm bạn ở phòng gym (`02:10`).

## Đừng tin vội

- Doanh thu là số founder đọc từ RevenueCat trong video do Starter Story quay; video có HubSpot tài trợ và kênh bán database ý tưởng.
- Lino tự nhận "không có đối thủ" trong ngách này, chưa kiểm. Video không nói chi phí ads, churn, hay giá gói.
- Chia equity cho influencer nghĩa là một phần doanh thu thuộc về người khác; số ROAS là lời founder, không có số chi tiêu đi kèm.
- Lino là trường hợp 18 tuổi, không có nền tảng kỹ thuật; khi kể lại, host gọi tên app không nhất quán (AbMax/AbMaxx/Max), nên dữ liệu chỉ nên đọc như một ca.
