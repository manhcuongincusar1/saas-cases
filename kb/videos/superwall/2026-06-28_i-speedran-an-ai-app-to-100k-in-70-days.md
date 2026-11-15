---
schema: 2
video_id: mOpYezjqU9c
channel: superwall
title: "I speedran an ai app to $100k in 70 days."
date: 2026-06-28
url: https://www.youtube.com/watch?v=mOpYezjqU9c
transcript: superwall/youtube-transcript/superwall/i-speedran-an-ai-app-to-100k-in-70-days/transcript.md
kind: founder_case
speakers:
  - {name: Cedric, role: founder}
  - {name: Joseph Choi, role: host}
bias: "Podcast của Superwall (bán công cụ paywall). Host điều hành Consumer Club (cộng đồng founder, dinner mời theo ngưỡng MRR) và quảng bá Rork có mã giảm giá. Số liệu app do founder tự nêu, chưa thấy dashboard."
analyzed: 2026-11-15
cases:
  - id: pep-ai
    depth: full
    product: "Pep AI (app theo dõi peptide và GLP-1: liều, vị trí tiêm, dinh dưỡng, cân nặng, tập luyện)"
    what: "App do người dùng tự nhập dữ liệu; có calculator quy đổi liều ra số đơn vị trên bơm tiêm, AI chat không đưa lời khuyên y tế, gói đăng ký"
    type: [mobile-app]
    customer: "Người đang dùng peptide hoặc GLP-1; founder nói trên 50% (khoảng 60%) trên 25 tuổi"
    founder: {who: Cedric, base: null, technical: null, team: "CEO; 2 developer; 2 marketing manager; CFO; product; khoảng 4 người chuyên outreach", background: "Quản lý đội esports Fortnite thời trung học và tự học marketing qua đó; app này là sản phẩm nghiêm túc đầu tiên"}
    revenue: {amount: 100000, unit: usd, basis: lifetime, note: "Tổng trong 70 ngày. Tháng 1 khoảng 30K, tháng 2 khoảng 50K; tháng 3 chỉ là 'on pace' 80K (ước)", q: "Yeah, in 70 days we're able to hit 100,000 in revenue.", ts: "00:00:00", evidence: claimed}
    pricing: "Gói năm $40 (dùng thử 3 ngày) và gói tháng $10; đang thử giá và muốn giảm thêm"
    idea_origin: [niche_down]
    scale_channels: [influencer_paid, tiktok_organic, paid_meta, paid_apple_search]
    community_at_discovery: {value: "Chưa từng dùng peptide hoặc GLP, nhưng từng quan tâm và xem creator trong ngách trước khi làm app", insider: false, q: "I've never even taken any peptides or GLPs", ts: "00:17:42"}
    demand_signal: null
    prior_failures: {count: null, what: "Đưa script cho người làm nội dung copy theo các app GLP khác: những video đó fail, mất tiền", q: "Some of them we tried like giving scripts to people", ts: "00:06:35"}
    unfair_advantage:
      - {value: capital, what: "Một người bạn (làm dropshipping) đầu tư tiền để chạy marketing", q: "He put money into it.", ts: "00:39:28"}
      - {value: cofounder, what: "Hai developer được chia cổ phần công ty và phụ trách toàn bộ phát triển", q: "give you some of the like percentage of the company", ts: "00:39:56"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 2.3, value: "in 70 days (70 ngày, quy ra tháng)", q: "Yeah, in 70 days we're able to hit 100,000 in revenue.", ts: "00:00:00"}
    first_users:
      - {channel: influencer_paid, what: "Ký mọi creator peptide để đăng về app (retainer và hoa hồng); đây là nguồn người dùng đầu tiên", q: "I went and got every single one of them to post about Pep AI", ts: "00:00:17"}
    build: {time: "Bắt đầu cuối tháng 1, ra mắt khoảng cuối tháng 2", cut: [], q: "So, I started building mine late January.", ts: "00:03:57"}
steps:
  - {stage: find-idea, ts: "00:03:57", case: pep-ai, what: "Chọn ngách peptide: GLP app đã làm tốt nhưng peptide chưa ai làm marketing; bắt đầu làm app cuối tháng 1.", tactic: s9-niche-narrowing}
  - {stage: launch, ts: "00:04:25", case: pep-ai, what: "Ra mắt khoảng cuối tháng 2, sau đó đưa mọi creator peptide vào quảng bá app.", tactic: g7-creator-ops}
  - {stage: grow, ts: "00:05:35", case: pep-ai, what: "Không chạy ads cho đến khi có video organic thắng; đa số GLP app khác chỉ chạy ads.", tactic: g6-paid-ads, tactic_note: "Chạy ads sau khi có winner organic"}
  - {stage: grow, ts: "00:06:27", case: pep-ai, what: "Đưa các video organic thắng trên TikTok và Instagram lên Meta ads.", tactic: g6-paid-ads, threshold: "cost per download dưới $5 là ổn; app đang khoảng $2.50", cost: "khoảng $400/ngày Meta, thêm khoảng $150/ngày Apple Search Ads"}
  - {stage: grow, ts: "00:08:33", case: pep-ai, what: "Theo dõi từng creator bằng creator code và link riêng trong bio (one-link của AppsFlyer); giữ người chuyển đổi tốt, giảm deal kém.", tactic: g8-funnel-measurement}
  - {stage: grow, ts: "00:09:33", case: pep-ai, what: "Ưu tiên video slideshow (vài slide thông tin rồi CTA cuối) thay vì talking head; creator top có nhiều view.", tactic: g3-organic-content-formats}
  - {stage: grow, ts: "00:15:08", case: pep-ai, what: "Hợp đồng thử 1 tháng: 4 bài, 4 story và link trong bio; creator khoảng 5.000 view mỗi bài nhận khoảng $200, tốt thì lên gói 3 tháng.", tactic: g7-creator-ops, threshold: "khoảng 5.000 view mỗi bài", cost: "$200/tháng (gói thử)"}
  - {stage: grow, ts: "00:20:04", case: pep-ai, what: "Đội outreach gửi trên 100 DM mỗi ngày; tin đầu hỏi về paid promo hoặc affiliate deal, rồi chuyển sang WhatsApp và gọi.", tactic: g7-creator-ops}
  - {stage: grow, ts: "00:21:31", case: pep-ai, what: "Đa số creator có hoa hồng affiliate khoảng 20% trên đăng ký qua link của họ, trả một lần.", tactic: g7-creator-ops, threshold: "20% một lần"}
  - {stage: grow, ts: "00:34:14", case: pep-ai, what: "Gọi user và creator để đi qua app cùng họ, lấy feedback rồi thêm tính năng; cập nhật 2 đến 3 lần mỗi tuần.", tactic: g5-retention, tactic_note: "Gọi điện lấy feedback để thêm tính năng; không phải thông báo giữ chân"}
  - {stage: grow, ts: "00:46:52", case: pep-ai, what: "Làm ảnh tĩnh quảng cáo dày chữ bằng ChatGPT trong khoảng 2 phút; cài đặt dưới $2 và trở thành creative tốt nhất.", tactic: g6-paid-ads, tool: "ChatGPT", threshold: "cost per download dưới $2"}
  - {stage: monetize, ts: "00:23:11", case: pep-ai, what: "Đặt gói năm $40 có dùng thử 3 ngày và gói tháng $10; liên tục thử nghiệm giá.", tactic: g4-pricing-paywall}
  - {stage: monetize, ts: "00:28:36", case: pep-ai, what: "Onboarding theo tuổi: người dưới 25 được onboarding ngắn; người trên 25 được onboarding dài hơn (dinh dưỡng, nước, ngủ).", tactic: g4-pricing-paywall}
quotes:
  - {ts: "00:05:35", who: Cedric, stage: mindset, theme: [], text: "And so I didn't want to start running ads until we had winners.", vi: "Tôi không muốn chạy ads cho đến khi có video thắng."}
  - {ts: "00:15:57", who: Cedric, stage: mindset, theme: [risk-and-leap], text: "we we've been taking risks since we started", vi: "Chúng tôi đã mạo hiểm từ ngày đầu."}
  - {ts: "00:18:36", who: Cedric, stage: grow, theme: [], text: "One thing I've tried really hard to do is have really really good relationships with all of our creators.", vi: "Tôi cố gắng rất nhiều để có quan hệ thật tốt với tất cả creator."}
rules: []
numbers:
  - {ts: "00:00:17", metric: "doanh thu tháng 1 (USD)", value: 30000, unit: usd, evidence: claimed}
  - {ts: "00:06:35", metric: "chi phí mỗi lượt cài trên Meta (USD)", value: 2.5, unit: usd, evidence: claimed}
  - {ts: "00:08:08", metric: "số creator đang đăng video cho app", value: 100, unit: count, evidence: claimed}
  - {ts: "00:15:42", metric: "retainer cao nhất cho creator lớn (USD/tháng)", value: 4000, unit: usd, evidence: claimed}
frameworks: [niche-down-proven-category, organic-find-format-then-paid-scale, right-audience-over-views]
idea_patterns: [niche-inside-hot-category]
---
## Một câu

Cedric làm Pep AI (app theo dõi peptide và GLP-1) và đạt 100K doanh thu trong 70 ngày nhờ ký hàng loạt creator peptide để đăng về app, rồi đưa video organic thắng sang Meta; số liệu do founder tự nêu.

## Bài học cho tôi

- Chọn ngách con trong danh mục đã có người trả tiền: GLP app đã làm tốt, nhưng peptide chưa ai làm marketing (`00:03:57`).
- Không chạy ads khi chưa có video thắng; khi đưa sang Meta thì đo từng creator bằng creator code để giữ người chuyển đổi tốt (`00:05:30`, `00:08:33`).

## Đừng tin vội

- Số liệu do founder tự nêu, không có dashboard trong video. Doanh thu tháng 3 chỉ là ước ("on pace").
- Ngách peptide có rủi ro: founder nói TikTok từ chối Spark ads vì nội dung peptide, và app phải cẩn thận không đưa lời khuyên y tế (`00:50:06`). Ngách có rủi ro quy định khó sao chép hơn.
- Mô hình này dựa vào đội ngũ: 100 creator đăng định kỳ, khoảng 4 người outreach, 2 marketing manager, và ngân sách ads khoảng $550 mỗi ngày. Người làm một mình khó tái lập quy mô này.
- Host bán paywall và điều hành cộng đồng trả phí; founder được mời lên podcast. Video là một phần của phễu đó.
- Video không nêu bằng chứng nhu cầu trước khi build (nên `demand_signal` để trống); "app GLP làm tốt" chỉ là cảm nhận, không có số doanh thu.
- Video không nói CAC, LTV, churn hay tỉ lệ chuyển đổi của app.
