---
schema: 2
video_id: 4BsxnGRbF4k
channel: starter-story
title: I Found a Business for Sale and Rebuilt It Into $20K/Month
date: 2025-10-19
url: https://www.youtube.com/watch?v=4BsxnGRbF4k
transcript: starter-story-kb/videos/2025-10-19_i-found-a-business-for-sale-and-rebuilt-it-into-20k/transcript.md
kind: founder_case
speakers:
- name: Adrian
  role: founder
- name: Pat Walls
  role: host
bias: Adrian bán ScrapeCreators nên được lợi khi kể câu chuyện này; Starter Story bán Starter Story Build;
  HubSpot for Startups tài trợ đoạn giữa video. Số $20K/tháng và số khách là lời kể, không có dashboard.
analyzed: 2026-11-15
cases:
- id: scrape-creators
  depth: full
  product: 'ScrapeCreators: API lấy dữ liệu công khai từ mạng xã hội và thư viện quảng cáo, tính tiền
    theo credit'
  what: Scrape public data từ Instagram, YouTube, Twitter và thư viện quảng cáo (Facebook, LinkedIn) để
    nhà phát triển không phải tự scrape; khách chủ yếu là công cụ link-in-bio và phân tích short-form
  type:
  - api
  customer: Nhà phát triển và công cụ phân tích (link-in-bio, theo dõi short-form content)
  founder:
    who: Adrian
    base: Austin (theo video)
    technical: true
    team: solo
    background: Học code ở bootcamp App Academy, làm engineer 3 năm ở Utah; NodeJS developer; đã thử vài
      khoá học và sản phẩm trước khi bám vào scraping
  revenue:
    amount: 20000
    unit: usd
    basis: monthly
    note: Doanh thu hàng tháng ~20K theo lời founder; mô hình trả theo credit, không subscription
    q: monthly revenue is about 20,000 a month right now
    ts: 01:18
    evidence: claimed
  pricing: 'Trả theo credit: $10 cho 5.000 credit, $50 cho 25.000, $500 cho 500.000'
  idea_origin:
  - revenue_scouting
  scale_channels:
  - founder_led_content
  community_at_discovery:
    value: Có follower trên Twitter gửi listing bán scraping API; đã có sản phẩm về social media
    insider: false
    q: I already had a product that had to do with social media.
    ts: 02:38
  demand_signal:
    kind: similar_product_revenue
    level: 3
    what: Scraping API tương tự trên Micro Acquire đang có ~30K MRR, dưới 100 khách, khách chỉ đến từ
      SEO
    q: they were doing 30,000 monthly recurring
    ts: 03:23
  prior_failures:
    count: 2
    what: Làm freelance, một khoá học và 'some products' (ít nhất 2 thứ) không thành công trước khi bám
      vào một hướng (scrape creators)
    q: built a course, built some products, but didn't have success until I stuck with this one thing
    ts: 02:06
  unfair_advantage:
  - value: technical_skill
    what: Đã học scraping 3 năm và từng làm các API scraper
    q: I had this skill set because I had been studying scraping for 3 years.
    ts: 03:08
  - value: domain_expertise
    what: Đã có một sản phẩm liên quan social media trước đó
    q: I already had a product that had to do with social media.
    ts: 02:38
  - value: existing_audience
    what: Có chút presence trên Twitter (video nói 'a little bit')
    q: I have a little bit of a presence on Twitter.
    ts: 03:38
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 12
      value: 'Khoảng 1 năm: từ lúc thấy app bán trên sàn tới nay'
      q: A year ago, he saw a successful app for sale
      ts: 00:15
  first_users:
  - channel: founder_led_content
    what: 'Đăng nội dung trên X; khách đầu tiên đến một cách ngẫu nhiên: CTO của công ty bị scrape comment
      dưới bài đăng'
    q: My first customer was just because I scraped a company's site and then the CTO actually commented
      on that post.
    ts: 04:40
  - channel: founder_led_content
    what: Comment dưới video launch liên quan đến scraping mạng xã hội, mời thử API và tặng 10K credit
      miễn phí
    q: I'll give you 10K free credits if you'll try my API.
    ts: 04:56
  build:
    time: Vài tuần, vì đã có scraper và kinh nghiệm từ 3 năm trước
    cut:
    - Tài liệu tối giản (Notion) và website cơ bản
    q: it probably took uh just a couple of weeks
    ts: 04:09
steps:
- stage: find-idea
  ts: 02:22
  case: scrape-creators
  what: Một follower trên Twitter nhắn link listing bán một scraping API trên Micro Acquire
  tactic: s13-others-pain-or-inbound
  tactic_note: Lời mời đến tay từ follower; founder không thuộc nhóm khách của app này
- stage: find-idea
  ts: 02:38
  case: scrape-creators
  what: 'Xem số liệu listing: app có ~30K MRR, dưới 100 khách, khách chỉ đến từ SEO; quyết định làm y
    hệt'
  tactic: s1-revenue-spy
  tool: Micro Acquire (Acquire.com)
  threshold: ~30K MRR, dưới 100 khách
- stage: find-idea
  ts: 06:27
  what: 'Playbook bước 1–3: vào Micro Acquire, lọc SaaS, rồi lọc theo giá hỏi hoặc ARR để chỉ xem app
    đã có tiền'
  tactic: s1-revenue-spy
  tool: Micro Acquire
  threshold: giá hỏi tối thiểu 300.000 (video nói 'at least 300,000') hoặc ARR
  tactic_note: 'Playbook: lọc theo SaaS rồi theo giá hỏi, để chọn ý tưởng đã được kiểm chứng'
- stage: find-idea
  ts: 06:43
  what: 'Playbook bước 4: chọn sản phẩm trong ngách mình có hiểu biết; Adrian chọn web scraping'
  tactic: s9-niche-narrowing
  tactic_note: Chọn sản phẩm trong ngách mình hiểu (ở đây là web scraping)
- stage: find-idea
  ts: 06:59
  what: 'Playbook bước 5: tìm website của app trong listing (Google theo tên/mô tả, hoặc tìm trang ''alternatives'')'
  tactic: other
  tactic_note: 'Tìm website của app trong listing: tìm theo tên/mô tả trên Google, hoặc trang ''competitor
    alternatives'''
- stage: validate
  ts: 08:01
  what: 'Playbook bước 6: tìm cách đối thủ có khách (đọc site, founder trên Twitter/LinkedIn, podcast)
    trước khi build'
  tactic: other
  tactic_note: 'Soi cách đối thủ có khách: đọc site, founder trên Twitter/LinkedIn, podcast/YouTube; Adrian
    gọi đây là bước quan trọng nhất'
- stage: grow
  ts: 04:40
  case: scrape-creators
  what: Đăng nội dung đều trên X để người ta thấy; khách đầu tiên đến từ việc CTO comment bài đăng về
    một site bị scrape
  tactic: g3-organic-content-formats
  tactic_note: Đăng nội dung đều trên X (founder-led)
- stage: grow
  ts: 04:56
  case: scrape-creators
  what: Comment dưới video launch có liên quan scraping mạng xã hội, mời thử API kèm 10K credit miễn phí
  tactic: g1-first-10-users
  tactic_note: Comment ưu đãi credit dưới video launch có liên quan
- stage: monetize
  ts: 09:34
  case: scrape-creators
  what: 'Bán theo credit, không subscription: gói $10 (5.000 credit), $50 (25.000), $500 (500.000)'
  tactic: g4-pricing-paywall
  tactic_note: Pay-as-you-go theo credit, không subscription
- stage: retain
  ts: 09:49
  case: scrape-creators
  tactic: g5-retention
  what: Giữ khách bằng độ tin cậy và liên lạc thường xuyên khi scraper hỏng; thuê developer ở Philippines
    trực monitor API ban đêm (~$500/tháng)
  tactic_note: Phản hồi nhanh khi API lỗi, dễ liên lạc trực tiếp
quotes:
- ts: 02:38
  who: Adrian
  stage: find-idea
  theme: []
  text: Once I did, I saw the numbers and was completely blown away. I had no confidence myself that a
    scraping API could make that much money.
  vi: Khi xem, tôi thấy số liệu và choáng; tôi không tin một scraping API có thể kiếm nhiều tiền đến vậy.
- ts: 08:17
  who: Adrian
  stage: find-idea
  theme: []
  text: Step eight, yeah, this is just don't copy word for word. Don't copy everything literally exactly.
    You just want to copy the concept, the idea.
  vi: 'Bước tám: đừng chép từng chữ; chỉ chép ý tưởng cốt lõi.'
- ts: 08:33
  who: Adrian
  stage: grow
  theme:
  - focus-one-thing
  text: Step nine, don't get distracted with other projects. Do something every single day to promote
    or improve the product.
  vi: 'Bước chín: đừng bị phân tâm bởi dự án khác; mỗi ngày làm một việc để quảng bá hoặc cải thiện sản
    phẩm.'
- ts: '11:24'
  who: Adrian
  stage: mindset
  theme:
  - focus-one-thing
  text: Stop bouncing around ideas and just pick one thing. Do it every single day. Focus on it every
    single day and you'll make it. Stop getting distracted because that's exactly what happened to me.
  vi: Đừng nhảy qua lại giữa các ý tưởng; chọn một việc, làm mỗi ngày. Đừng bị phân tâm, vì đó chính là
    điều đã xảy ra với tôi.
rules:
- ts: '12:11'
  who: Pat Walls
  stage: find-idea
  theme: []
  text: I think the lesson that anyone can take from this is stop waiting for that genius idea. Just start,
    build, and keep improving.
  vi: 'Bài học ai cũng có thể lấy: đừng chờ ý tưởng thiên tài. Cứ bắt đầu, build, và cải thiện liên tục.'
  evidence: opinion
numbers:
- ts: 01:18
  metric: doanh thu hàng tháng (trả theo credit)
  value: 20000
  unit: usd_per_month
  evidence: claimed
- ts: 01:18
  metric: người đã trả tiền nhưng không đều đặn
  value: 600
  unit: count
  evidence: claimed
- ts: 01:33
  metric: API request mỗi tháng
  value: 20000000
  unit: count
  evidence: claimed
- ts: 03:23
  metric: MRR của scraping API tương tự trên Micro Acquire (lúc xem)
  value: 30000
  unit: usd_per_month
  evidence: claimed
- ts: 05:11
  metric: số khách trả phần lớn MRR
  value: 12
  unit: count
  evidence: claimed
- ts: '10:52'
  metric: biên lợi nhuận gộp
  value: 80
  unit: percent
  evidence: claimed
- ts: '11:09'
  metric: chi phí proxy mỗi tháng
  value: 1500
  unit: usd_per_month
  evidence: claimed
frameworks:
- niche-down-proven-category
- copy-proven-app
idea_patterns: []
---

## Một câu

Adrian thấy một scraping API có ~30K MRR đang được rao bán trên Micro Acquire, làm lại theo ý tưởng chứ không chép từng chữ, và theo lời kể đạt ~20K/tháng nhờ khoảng 12 khách trả phần lớn doanh thu.

## Bài học cho tôi

- Soi listing đã có doanh thu rồi làm lại: lọc theo giá hỏi (từ 300.000) và chọn ngách mình hiểu (`06:27`).
- Khách đầu tiên đến từ đăng đều trên X và comment dưới video launch liên quan, kèm credit miễn phí (`04:56`).

## Đừng tin vội

- Số $20K/tháng, 600 người đã trả tiền, 80% margin đều là lời Adrian kể, không có dashboard. Video không nói tỉ lệ rời bỏ (churn) hay giữ chân.
- Survivor bias: video kể một listing thành công; không nói có bao nhiêu listing tương tự đã không ra tiền.
- Điều kiện riêng: Adrian có 3 năm kinh nghiệm scraping và có follower trên Twitter; không có các điều kiện này thì việc chép khó hơn nhiều.
- Video có nhắc đến pháp lý (chỉ scrape dữ liệu công khai) nhưng không phân tích rủi ro nền tảng.
- Video có đoạn quảng cáo HubSpot và quảng bá Starter Story Build; không nói ai khác đã làm theo mô hình này và thất bại.
