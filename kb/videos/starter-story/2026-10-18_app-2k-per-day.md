---
schema: 2
video_id: NuYO7DWzlaM
channel: starter-story
title: I built an app that makes $2K PER DAY
date: 2026-10-18
url: https://www.youtube.com/watch?v=NuYO7DWzlaM
transcript: starter-story-kb/videos/2026-10-18_i-built-an-app-that-makes-2k-per-day/transcript.md
kind: founder_case
speakers:
- name: Rasty
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story bán database app đơn giản (link 'free database' trong video) và dựng Rasty như bằng
  chứng. Doanh thu chỉ thấy trên một màn hình App Store analytics và lời kể; app không có analytics nên
  không kiểm được chuyển đổi từ web.
analyzed: 2026-11-15
cases:
- id: vault-air
  depth: full
  product: 'Vault Air: app iPhone mã hoá file và ảnh trên thiết bị'
  what: Kho lưu file và ảnh mã hoá trên máy, không server, không khoá chung; giống Dropbox nhưng không
    ai (kể cả Apple) khôi phục được dữ liệu
  type:
  - ios-app
  customer: Người cần cất giấy tờ nhạy cảm như ảnh ID, giấy khai sinh, khoá ví crypto
  founder:
    who: Rasty Turek
    base: null
    technical: null
    team: null
    background: Lớn lên ở Slovakia; làm cho Google (đội Gmail), lập vài startup (bảo mật, giải trí; Pics
      bán năm ngoái); tự nói kinh nghiệm chính là B2B/enterprise
  revenue:
    amount: 41000
    unit: usd
    basis: best_month
    note: Tháng cao nhất khoảng $41.000 (lời narrator). Founder nói '2–3.000 một ngày' ở đầu video; dashboard
      hiện ~2.000/ngày
    q: 6 months later, it made $41,000 in a single month
    ts: 00:16
    evidence: claimed
  pricing: Miễn phí tải về; gói tuần $1.99, năm $19.99, trọn đời $39.99; trọn đời chiếm ~60% lượt mua
    và trên 80% doanh thu theo lời Rasty
  idea_origin:
  - own_pain
  - domain_expertise
  scale_channels:
  - seo
  community_at_discovery:
    value: người làm crypto cất khoá ví ở nhiều nơi, và người cần cất ảnh ID, giấy khai sinh; khó vừa
      gần thiết bị vừa truy cập được
    insider: null
    q: if you deal with crypto, a lot of people have wallet keys stored in all sorts of places
    ts: 05:34
  demand_signal:
    level: 0
    what: đưa app ra mà không biết có ai dùng không (build xong mới đưa ra); tháng đầu chỉ kiếm $66
    q: I didn't even know if anyone is ever going to use this
    ts: 05:50
    kind: built_first
  prior_failures: null
  unfair_advantage:
  - value: prior_success
    what: startup trước đó được Amazon mua (dùng một phần công nghệ đến nay); Pics bán năm ngoái
    q: Company got acquired by Amazon and they use some of the tech to this day
    ts: 05:18
  - value: domain_expertise
    what: startup đầu tiên làm về bảo mật (nền tảng cho app mã hoá); từng làm đội Gmail ở Google
    q: Mostly, the first one started in security because that was my background
    ts: 05:01
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 6
      value: '''6 months later'' sau tháng đầu ($66) tới tháng $41.000 (lời narrator; host nói ''started
        this in March'')'
      q: 6 months later, it made $41,000 in a single month
      ts: 00:16
  first_users:
  - channel: seo
    what: SEO là kênh chính từ đầu (trang marketing và loạt guide); video không nói 10 người dùng đầu
      tiên đến từ đâu
    q: my approach was like what if I try to pull in every keyword that is out there
    ts: 06:41
  build:
    time: khoảng 3 tuần cho app iOS đầu tiên
    cut: []
    q: It took roughly 3 weeks
    ts: 00:00
steps:
- stage: monetize
  ts: 02:15
  case: vault-air
  what: Định miễn phí hoàn toàn, nhưng đến phút cuối đặt vài đô để bớt yêu cầu hỗ trợ; chủ yếu bán gói
    trọn đời.
  tactic: g4-pricing-paywall
  tactic_note: Đặt vài đô (gói tuần/năm/trọn đời) thay vì miễn phí hoàn toàn để giảm yêu cầu hỗ trợ
- stage: find-idea
  ts: 05:34
  case: vault-air
  what: Từ nhu cầu cất khoá ví và ảnh ID ở chỗ vừa gần thiết bị vừa truy cập được, làm công cụ mã hoá;
    ban đầu không định thu tiền.
  tactic: s5-insider
  tactic_note: Ý tưởng đi từ thế giới bảo mật có sẵn của founder; chưa khảo sát ai trước khi làm
- stage: launch
  ts: 06:41
  case: vault-air
  what: 'Thay vì ads hay creator, phủ mọi từ khoá cùng nghĩa với app store nhưng trên web: trang marketing
    và guide cho từng câu hỏi.'
  tactic: g2-aso-seo-organic
  tool: coding agent viết nội dung; trang web
- stage: grow
  ts: 07:30
  case: vault-air
  what: Đặt CTA tải app ở chỗ người đọc thường kết thúc bài; khoảng 10% lượt từ web chuyển sang app, và
    web là phần lớn lưu lượng.
  tactic: g2-aso-seo-organic
  tactic_note: Đặt CTA dẫn người đọc từ bài SEO sang tải app ở chỗ họ thường kết thúc bài, đo tỉ lệ chuyển
    đổi từ web
- stage: grow
  ts: 08:02
  case: vault-air
  what: Mỗi sáng một script (gum, tự viết) đọc Keyword Planner, tìm từ khoá có impression nhưng không
    có click (hạng ~50), tạo guide mới, rồi nối internal link; mỗi ngày một bài.
  tactic: g2-aso-seo-organic
  tool: gum (CLI mã nguồn mở tự viết; MCP tới Google Keyword Planner và Google Search)
  threshold: từ khoá có impression nhưng không click
quotes:
- ts: 05:50
  who: Rasty
  stage: launch
  theme:
  - ship-ugly
  text: I didn't even know if anyone is ever going to use this. So like I put it out with the idea is
    like I will have it it will be there.
  vi: Tôi thậm chí không biết có ai dùng không. Tôi cứ đưa nó ra với ý nghĩ là có nó ở đó.
- ts: 02:15
  who: Rasty
  stage: monetize
  theme:
  - revenue-first
  text: So I literally just set few dollars here and we'll see.
  vi: Tôi chỉ đặt vài đô rồi xem sao.
- ts: '11:49'
  who: Rasty
  stage: mindset
  theme:
  - action-over-research
  text: I mean, start. That's the hardest part, right? Like I have at least two dozen projects that are
    somewhere in me ready, but they're not out there.
  vi: Tôi nghĩ là cứ bắt đầu. Đó là phần khó nhất. Tôi có ít nhất hai chục dự án trong đầu, sẵn sàng,
    nhưng chúng chưa ra ngoài.
- ts: '12:06'
  who: Rasty
  stage: mindset
  theme:
  - ship-ugly
  text: And then, honestly, like people overthink how things too should be done.
  vi: Và thật ra, mọi người thường nghĩ quá nhiều về việc mọi thứ phải làm thế nào.
- ts: '12:23'
  who: Rasty
  stage: mindset
  theme:
  - persistence
  text: as long as you have open mind and, you know, how to put one foot in front of the other and every
    day just be slightly better than the day before.
  vi: Miễn là bạn có đầu óc cởi mở, cứ bước từng bước một, và mỗi ngày tốt hơn hôm qua một chút.
rules:
- ts: 02:48
  who: Pat Walls hoặc Gus
  stage: find-idea
  theme:
  - focus-one-thing
  text: An app like this and a founder like Rasty is proof that you do not need a brand new or complicated
    idea to win.
  vi: Một app như thế và một founder như Rasty là bằng chứng rằng bạn không cần ý tưởng mới hay phức tạp
    để thắng.
  evidence: opinion
- ts: 09:23
  who: Pat Walls hoặc Gus
  stage: grow
  theme:
  - right-audience
  text: I think this focus on providing valuable content to a very niche audience.
  vi: Tôi nghĩ việc tập trung làm nội dung có giá trị cho một nhóm rất hẹp là điểm mạnh.
  evidence: opinion
numbers:
- ts: 00:16
  metric: doanh thu tháng đầu
  value: 66
  unit: usd
  evidence: claimed
- ts: 00:16
  metric: doanh thu tháng cao nhất (lời narrator)
  value: 41000
  unit: usd_per_month
  evidence: claimed
- ts: 02:31
  metric: tổng lượt tải
  value: 60000
  unit: count
  evidence: claimed
- ts: 02:15
  metric: tỉ trọng doanh thu từ gói trọn đời
  value: '>80%'
  unit: ratio
  evidence: claimed
- ts: 03:55
  metric: doanh thu ngày (dashboard, 'quanh')
  value: 2000
  unit: usd_per_day
  evidence: measured
- ts: 04:10
  metric: tỉ lệ tải thành người trả tiền ngày 1
  value: 0.0547
  unit: ratio
  evidence: measured
- ts: 07:30
  metric: tỉ lệ chuyển đổi từ web sang tải app
  value: 0.1
  unit: ratio
  evidence: claimed
frameworks:
- seo-landing-page
idea_patterns: []
---

## Một câu

Vault Air, app iPhone mã hoá file và ảnh không cần server, làm trong khoảng 3 tuần; không chạy ads, không TikTok, chỉ SEO: trang marketing và một guide mỗi ngày do script tự động tạo, đưa app lên khoảng 2.000/ngày.

## Bài học cho tôi

- Đi vào các từ khoá mà app lớn bỏ ngỏ bằng web: Rasty nói app lớn có triệu người dùng nên Apple ưu tiên họ, còn phần web thì mình phủ được (`06:41`).
- Biến SEO thành việc làm đều mỗi ngày: script đọc từ khoá có impression mà không có click, viết một guide, nối internal link; một bài mỗi ngày, không cần đội ngũ (`08:02`).

## Đừng tin vội

- Doanh thu chủ yếu là lời kể: màn hình chỉ thấy ~2.000/ngày, $41.000 là lời narrator, còn câu mở đầu của Rasty nói '2–3.000 một ngày'. Các con số không khớp nhau. Video không nêu chi phí; Rasty nói dùng PostHog miễn phí và Codex/Claude.
- Theo host, web không gắn analytics vì lý do riêng tư, nên không có số liệu đường đi từ web tới tải app ngoài con số 10% Rasty nêu.
- Đây là ngách rất hẹp (app mã hoá) và Rasty có nền bảo mật cùng kinh nghiệm startup trước đó; ngách đông hơn khó lặp lại kết quả như vậy.
- Gus nói 'SEO is dead' nhưng vẫn cho rằng cách này hiệu quả vì ngách hẹp; video không có số liệu so sánh.
- Pat dự đoán traffic và doanh thu sẽ tăng sau 6 tháng nhờ LLM và AI overview; đó là dự đoán, chưa kiểm chứng.
