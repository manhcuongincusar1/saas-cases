---
schema: 2
video_id: w8oUlfgvcTI
channel: starter-story
title: My two apps made $30M
date: 2025-10-01
url: https://www.youtube.com/watch?v=w8oUlfgvcTI
transcript: starter-story-kb/videos/2025-10-01_my-two-apps-made-30m/transcript.md
kind: founder_case
speakers:
- name: Will Cannon
  role: founder
- name: Pat Walls
  role: host
bias: Video có quảng cáo Vanta (sponsor, 06:25–07:27, ưu đãi $1.000) và CTA sang Starter Story Build (10:57–11:23).
  Số liệu doanh số, người dùng và lượt truy cập là lời founder.
analyzed: 2026-11-15
cases:
- id: uplead
  depth: full
  product: 'UpLead: dữ liệu B2B, email và số điện thoại đã xác minh theo thời gian thực, lọc theo ICP'
  what: Công cụ tìm và xác minh email/số điện thoại của khách B2B, xuất danh sách theo ICP; thay cho việc
    nhờ vendor và call center kiểm số
  type:
  - web-app
  customer: Đội bán hàng B2B cần danh sách khách đã xác minh; hơn 4.000 khách (lời founder)
  founder:
    who: Will Cannon
    base: null
    technical: null
    team: null
    background: Mở công ty mortgage năm 19 tuổi cùng vợ (khi đó là bạn gái); công ty sập sau khủng hoảng
      2008; khoảng 10 năm làm agency cold email và bán danh sách
  revenue:
    amount: 30000000
    unit: usd
    basis: lifetime
    note: '''over $30 million in sales'' là doanh số (sales) tích luỹ theo lời founder, không phải lợi
      nhuận'
    q: It's done over $30 million in sales
    ts: 07:42
    evidence: claimed
  pricing: null
  idea_origin:
  - own_pain
  - domain_expertise
  scale_channels:
  - b2b_deals
  community_at_discovery:
    value: làm mortgage và agency, gửi nhiều cold email cho loan officer và môi giới bất động sản; bán
      danh sách bên lề
    insider: true
    q: we were sending a lot of cold emails to loan officers and real estate agents
    ts: 01:49
  demand_signal: null
  prior_failures:
    count: 20
    what: trước hai công ty thành công, founder ước tính thất bại ở khoảng 15–20 doanh nghiệp (lời founder)
    q: I failed at probably over 20 different businesses
    ts: 05:09
  unfair_advantage:
  - value: domain_expertise
    what: khoảng 10 năm làm agency cold email, bán danh sách và gặp vấn đề chất lượng dữ liệu hằng ngày
    q: That's what we did for about 10 years from 2007ish to 2017
    ts: 02:04
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: b2b_deals
    what: cold email outbound (vocab chưa có kênh cold email, xếp tạm vào b2b_deals); 1 triệu ARR đầu
      tiên chỉ từ cold email
    q: Uple got its first 1 million in annual recurring revenue strictly from cold email
    ts: 08:29
  build:
    time: null
    cut: []
    q: We didn't find any software. We decided to build it ourselves
    ts: 03:04
- id: signaturely
  depth: full
  product: 'Signaturely: ký điện tử đơn giản, bản dễ dùng hơn DocuSign (theo lời founder)'
  what: 'Ký tài liệu online: vẽ hoặc gõ chữ ký, tải về và gửi đi; công cụ ký miễn phí làm phễu, template
    hợp đồng được xếp hạng SEO'
  type:
  - web-app
  customer: Người cần ký tài liệu điện tử đơn giản; hơn 1,6 triệu người dùng (lời founder)
  founder:
    who: Will Cannon
    base: null
    technical: null
    team: null
    background: 'Như UpLead: khoảng 10 năm làm agency cold email, bán danh sách; kỹ năng SEO và cold calling'
  revenue:
    amount: 1500000
    unit: usd
    basis: lifetime
    note: '''over 1.5 million in sales'' là doanh số tích luỹ theo lời founder, không phải lợi nhuận'
    q: It's done over 1.5 million in sales
    ts: 07:59
    evidence: claimed
  pricing: null
  idea_origin:
  - revenue_scouting
  - timing_trigger
  scale_channels:
  - seo
  community_at_discovery: null
  demand_signal:
    kind: similar_product_revenue
    level: 3
    what: DocuSign là công ty đại chúng, có rất nhiều doanh thu; founder thấy vậy trước khi build
    q: They had a ton of revenue
    ts: 03:19
  prior_failures: null
  unfair_advantage:
  - value: domain_expertise
    what: kỹ năng SEO, cold email và các kỹ năng khác có sẵn để lấy khách
    q: we used our SEO and cold email and other skill sets to acquire customers
    ts: 03:36
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: seo
    what: công cụ ký miễn phí làm phễu, rồi viết template hợp đồng (marketing, xây dựng, cho thuê) xếp
      hạng SEO; lấy 1.000+ khách đầu
    q: that was how we got our first thousand plus customers
    ts: 09:48
  build: null
steps:
- stage: find-idea
  ts: 02:04
  case: uplead
  what: Làm agency gửi cold email, gặp đi gặp lại vấn đề chất lượng dữ liệu; đó là khoảnh khắc 'aha' tạo
    ra ý tưởng công cụ data.
  tactic: s5-insider
  tactic_note: 'nỗi đau riêng khi làm agency: danh sách kém, phải gọi kiểm số'
- stage: build
  ts: 03:04
  case: uplead
  what: Không tìm thấy phần mềm nào làm việc này, nên tự build công cụ xác minh email và số điện thoại
    (transcript ghi tên 'Signature League' ở đoạn này, có thể là lỗi, xem Đừng tin vội).
- stage: grow
  ts: 08:29
  case: uplead
  what: 'Dùng cold email mẫu ngắn: tiêu đề có tên người nhận, dòng mở nhắc LinkedIn, so với ZoomInfo nhưng
    rẻ hơn, mời dùng thử miễn phí.'
  tactic: g12-outbound-b2b
  tactic_note: cold email outbound B2B (mẫu ngắn, so với công ty lớn nhất, mời dùng thử miễn phí); vocab
    chưa có tactic cold outreach
- stage: find-idea
  ts: 03:19
  case: signaturely
  what: Thấy DocuSign có nhiều doanh thu nhưng khó dùng; chép ý tưởng và làm bản đơn giản hơn ('dễ đến
    mức bà nội cũng dùng được').
  tactic: s11-copy-or-localize-proven
  tactic_note: 'remix sản phẩm đã chạy (DocuSign): đơn giản hơn, dễ dùng hơn'
- stage: find-idea
  ts: 04:07
  case: signaturely
  what: 'Bước 1 của framework: tìm thị trường đã có product-market fit (đã có khách trả tiền) trước khi
    chọn làm.'
  tactic: s1-revenue-spy
- stage: find-idea
  ts: 04:23
  case: signaturely
  what: 'Bước 2: đọc review 1–2 sao của đối thủ lớn để tìm góc khác biệt, không chỉ ''rẻ hơn''.'
  tactic: s3-competitor-reviews
- stage: grow
  ts: 09:17
  case: signaturely
  what: Dựng công cụ ký miễn phí (vẽ hoặc gõ chữ ký) làm phễu, rồi viết template hợp đồng xếp hạng cao
    trên tìm kiếm.
  tactic: g2-aso-seo-organic
quotes:
- ts: 00:31
  who: Will Cannon
  stage: find-idea
  theme: []
  text: The playbooks are already out there. Most people just don't study them.
  vi: Playbook có sẵn ngoài kia; hầu hết người ta chỉ không chịu nghiên cứu chúng.
- ts: 01:03
  who: Will Cannon
  stage: find-idea
  theme: []
  text: I took business models that already had product market fit and I added my own little twist to
    them.
  vi: Tôi lấy những mô hình kinh doanh đã có product-market fit rồi thêm một chút cách làm riêng.
- ts: 04:23
  who: Will Cannon
  stage: find-idea
  theme: []
  text: Our twist is what people dislike about the biggest companies in the space because those are the
    easiest customers to go after and acquire.
  vi: Cái khác biệt của chúng tôi là điều người ta không thích ở các công ty lớn nhất, vì họ là khách
    dễ tiếp cận và giành nhất.
- ts: 05:09
  who: Will Cannon
  stage: mindset
  theme:
  - persistence
  text: I failed at probably over 20 different businesses before having two successful businesses.
  vi: Tôi thất bại khoảng hơn 20 doanh nghiệp trước khi có hai doanh nghiệp thành công.
- ts: '10:18'
  who: Will Cannon
  stage: mindset
  theme: []
  text: Have these big, hairy, audacious goals, these crazy goals, these moonshots, right?
  vi: Hãy đặt những mục tiêu lớn, điên rồ, kiểu moonshot.
rules: []
numbers:
- ts: 07:42
  metric: doanh số tích luỹ UpLead
  value: 30000000
  unit: usd
  evidence: claimed
- ts: 07:42
  metric: khách trả tiền UpLead (over)
  value: 4000
  unit: count
  evidence: claimed
- ts: 07:59
  metric: lượt truy cập website UpLead mỗi tháng
  value: 100000
  unit: count
  evidence: claimed
- ts: 07:59
  metric: doanh số tích luỹ Signaturely
  value: 1500000
  unit: usd
  evidence: claimed
- ts: 07:59
  metric: người dùng Signaturely (over)
  value: 1600000
  unit: count
  evidence: claimed
- ts: 08:14
  metric: lượt truy cập website Signaturely mỗi tháng
  value: 800000
  unit: count
  evidence: claimed
- ts: 08:29
  metric: ARR đầu tiên của UpLead (chỉ từ cold email)
  value: 1000000
  unit: usd
  evidence: claimed
- ts: 09:48
  metric: khách đầu tiên của Signaturely (qua template SEO và công cụ ký miễn phí)
  value: 1000
  unit: count
  evidence: claimed
frameworks:
- niche-down-proven-category
idea_patterns: []
---
## Một câu

Will Cannon sau khủng hoảng mortgage 2008 làm hai công ty: chọn thị trường đã có khách trả tiền, chép và làm khác đi một chút (review 1–2 sao của đối thủ lớn), rồi kéo khách bằng cold email và SEO; các con số là lời kể của founder.

## Bài học cho tôi

- Đọc review 1–2 sao của đối thủ lớn để tìm góc khác biệt, vì họ là khách dễ tiếp cận nhất (`04:23`).
- Cold email ngắn, so với công ty lớn và mời dùng thử miễn phí là kênh đã đưa 1 triệu ARR đầu tiên của UpLead (`08:29`).

## Đừng tin vội

- Số liệu là lời founder, không có dashboard. "Sales" là doanh số tích luỹ, không phải lợi nhuận; "users" của Signaturely không nói bao nhiêu trả tiền.
- Transcript ghi lẫn tên: đoạn 02:34–03:04 kể UpLead nhưng lại có "Signature League". Không chắc phần đó thuộc sản phẩm nào.
- Điều kiện riêng không sao chép được: 10 năm agency cold email và bán danh sách, nhiều kỹ năng SEO/cold email. Video không nói vốn, không nói team, không nói thời gian build.
- Số "hơn 20 doanh nghiệp thất bại" là ước lượng; cùng video ở 10:34 nói 15–20. Video chỉ kể hai công ty thành công (survivor bias).
- Video có sponsor (Vanta) và CTA Starter Story Build; cold email mẫu và chiến thuật "chép rồi làm khác" có thể đã bão hoà trong ngành đã có nhiều người làm.
