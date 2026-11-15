---
schema: 2
video_id: LRX8TWC2hTM
channel: starter-story
title: "I Make $60K/Month From the Most Boring SaaS on the Internet"
date: 2026-03-15
url: https://www.youtube.com/watch?v=LRX8TWC2hTM
transcript: starter-story-kb/videos/2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/transcript.md
kind: founder_case
speakers:
  - {name: Thomas, role: founder}
  - {name: Pat Walls, role: host}
  - {name: Gus, role: host}
bias: "Video được Vanta tài trợ (quảng cáo giữa video) và quảng cáo database ý tưởng của HubSpot. Thomas bán Packager. Con số 60k/tháng là lời kể của founder, chưa thấy dashboard."
analyzed: 2026-11-15
cases:
  - id: packager
    depth: full
    product: "Packager (Pckgr): công cụ trình duyệt đẩy ứng dụng lên Microsoft Intune bằng một click"
    what: "Cho IT admin chọn ứng dụng từ danh mục hoặc tự tải lên rồi đẩy thẳng vào Microsoft Intune, không phải đóng gói và kiểm tra cài đặt bằng tay"
    type: [web-app]
    customer: "IT admin và doanh nghiệp nhỏ dùng Microsoft Intune để triển khai phần mềm cho máy công ty"
    founder: {who: Thomas, base: null, technical: true, team: "team nhỏ, chi phí thấp, làm việc từ nhà", background: "IT admin làm việc hằng ngày với Microsoft Intune, từng tự đóng gói ứng dụng bằng tay"}
    revenue: {amount: 60000, unit: usd, basis: monthly, note: "Founder nói 'about 60k a month'; số 447k và 910k trong video không rõ là gì nên không dùng", q: "And now we're making about 60k a month", ts: "01:34", evidence: claimed}
    pricing: "Beta miễn phí; sau đó thu $25 USD/tháng"
    idea_origin: [own_pain, domain_expertise]
    scale_channels: [reddit, influencer_partner]
    community_at_discovery:
      value: "IT admin làm việc với Intune mỗi ngày; thấy nỗi đau đóng gói ứng dụng ngay trong nghề"
      insider: true
      q: "As I was working with Intune, I realized it can sometimes take"
      ts: "02:06"
    demand_signal:
      level: 4
      what: "Trên forum thấy nhiều IT admin gặp đúng vấn đề này và giải pháp hiện có quá phức tạp hoặc đắt (trước khi build)"
      q: "I started looking on forums and I noticed there were a lot of other IT admins that had"
      ts: "02:22"
      kind: self_reported_pain_or_free_waitlist
    prior_failures: null
    unfair_advantage:
      - {value: domain_expertise, what: "Làm IT admin và sống với Microsoft Intune hằng ngày, nên hiểu nỗi đau này", q: "I was living and breathing Microsoft Intune", ts: "05:30"}
      - {value: technical_skill, what: "Tự viết nhiều phần của sản phẩm bằng tay trước khi có công cụ AI lập trình", q: "A lot of this had to be manually written by myself", ts: "02:39"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: reddit, what: "Launch miễn phí trên Reddit khi sản phẩm còn beta; nhận nhiều phản hồi, có cả phản hồi gay gắt", q: "We knew that Reddit would be the best place to do this. So, we launched the product completely free.", ts: "03:12"}
      - {channel: influencer_partner, what: "Hợp tác với Microsoft MVP, họ làm demo sản phẩm cho đối tượng đúng đang dùng Intune. Video không nói có trả tiền hay không", q: "with people who specialize in the product. So, for us that was Microsoft MVPs.", ts: "04:13"}
    build: null
steps:
  - stage: find-idea
    ts: "02:06"
    case: packager
    what: "Làm IT admin, mỗi lần đóng gói một ứng dụng cho Intune mất cả giờ; thấy các giải pháp có sẵn quá phức tạp hoặc quá đắt."
    tactic: s5-insider
    tactic_note: "Nỗi đau trong nghề của chính founder (IT admin Intune)"
  - stage: find-idea
    ts: "02:22"
    case: packager
    what: "Đọc forum, thấy nhiều IT admin gặp đúng vấn đề này."
    tactic: s3-reddit-pain-mining
    tactic_note: "Đọc forum (không nêu tên) để thấy nỗi đau lặp lại"
  - stage: build
    ts: "02:39"
    case: packager
    what: "Làm một công cụ rẻ, đơn giản, chỉ làm đúng một việc là đẩy ứng dụng lên Intune; viết tay phần lớn code vì chưa có công cụ AI."
  - stage: launch
    ts: "03:12"
    case: packager
    what: "Launch miễn phí trên Reddit khi sản phẩm còn beta để có người dùng đầu tiên."
    tactic: g1-first-10-users
    tactic_note: "Đưa sản phẩm beta miễn phí lên cộng đồng Reddit"
  - stage: monetize
    ts: "03:43"
    case: packager
    what: "Sau khi sửa lỗi beta và ổn định nền tảng, bắt đầu thu $25 USD/tháng."
    tactic: g4-pricing-paywall
    threshold: "$25 USD/tháng"
  - stage: grow
    ts: "04:13"
    case: packager
    what: "Hợp tác với Microsoft MVP để họ làm demo sản phẩm cho đúng nhóm người dùng."
    tactic: g7-creator-ops
    tactic_note: "Đối tác là chuyên gia/creator (Microsoft MVP) làm demo; video không nói trả tiền hay không"
  - stage: find-idea
    ts: "06:15"
    case: packager
    what: "Bỏ khách hàng hàng triệu thiết bị mà đối thủ lớn đang chạy theo, chọn doanh nghiệp nhỏ làm khách mục tiêu."
    tactic: s9-niche-narrowing
quotes:
  - {ts: "03:27", who: Thomas, stage: launch, theme: [emotional-bottleneck], text: "And that's something I've had to really learn, if you want to make it, you sort of have to be able to accept that some people are just not going to like what you built.", vi: "Đây là điều tôi phải học: muốn làm được thì phải chấp nhận có người không thích thứ mình làm."}
  - {ts: "03:58", who: Thomas, stage: monetize, theme: [revenue-first], text: "the first notification on my phone of a customer signed up and was actually willing to pay for something I built.", vi: "Lần đầu tôi nhận thông báo trên điện thoại có khách đăng ký và sẵn sàng trả tiền cho thứ mình làm."}
  - {ts: "04:28", who: Thomas, stage: grow, theme: [], text: "Just something that you paid for a long time ago. So, that return on investment is huge.", vi: "Đó là thứ bạn đã làm từ lâu; nên lợi tức của nó rất lớn."}
  - {ts: "05:30", who: Thomas, stage: find-idea, theme: [], text: "Step one is to build in an area where you already have credibility.", vi: "Bước một: làm trong lĩnh vực mà bạn đã có uy tín."}
  - {ts: "05:45", who: Thomas, stage: find-idea, theme: [], text: "Step two is to look for pain points instead of ideas.", vi: "Bước hai: tìm nỗi đau thay vì ý tưởng."}
  - {ts: "06:00", who: Thomas, stage: find-idea, theme: [], text: "Step three is to avoid competing with the masses.", vi: "Bước ba: tránh cạnh tranh với đám đông."}
  - {ts: "06:15", who: Thomas, stage: monetize, theme: [revenue-first], text: "Step four is to charge early even if the price is low.", vi: "Bước bốn: thu tiền sớm dù giá thấp."}
  - {ts: "06:31", who: Thomas, stage: scale, theme: [], text: "Step five is to optimize for freedom instead of scale at all costs.", vi: "Bước năm: tối ưu cho sự tự do thay vì quy mô bằng mọi giá."}
  - {ts: "10:12", who: Thomas, stage: launch, theme: [ship-ugly], text: "You want to launch early and share it with your target audience, and then listen closely to the feedback that they provide.", vi: "Bạn nên ra mắt sớm, chia sẻ với đối tượng mục tiêu và lắng nghe phản hồi của họ."}
rules:
  - {ts: "11:13", who: Gus, stage: find-idea, theme: [], text: "Anyone watching this should realize that if it's boring and it doesn't make sense, that might be actually direction to go.", vi: "Ai đang xem nên nhận ra rằng nếu một việc nhàm chán và không hấp dẫn thì đó có thể là hướng đi đúng.", evidence: opinion}
numbers:
  - {ts: "01:34", metric: "doanh thu hiện tại (lời founder)", value: 60000, unit: usd_per_month, evidence: claimed}
  - {ts: "03:43", metric: "giá gói sau beta", value: 25, unit: usd_per_month, evidence: claimed}
frameworks: [one-feature-per-app, sell-before-build]
idea_patterns: [single-feature-on-platform]
---
## Một câu

IT admin mất cả giờ để đóng gói một ứng dụng cho Microsoft Intune, nên làm công cụ trình duyệt đẩy app bằng một click; thu $25/tháng sau beta, ~60k/tháng theo lời kể, team nhỏ.

## Bài học cho tôi

- Nỗi đau làm ra ý tưởng nằm ngay trong nghề của mình (`02:06`), rồi đọc forum để xem nhiều người cùng gặp không (`02:22`).
- Chọn khách mà đối thủ lớn bỏ qua (doanh nghiệp nhỏ, không phải hàng triệu thiết bị) (`06:15`); và thu tiền ngay từ beta để kiểm nhu cầu (`03:43`).

## Đừng tin vội

- Con số 60k/tháng là lời kể, không có dashboard. Hai số 447k và 910k không rõ nghĩa nên không dùng. Video được Vanta tài trợ và quảng cáo HubSpot.
- Video không nói thời gian build, không nói mốc 1k hay 10k/tháng, không nói số người trả tiền đầu tiên. Pat nói có "một nội dung đưa hàng trăm khách trả tiền miễn phí qua một đêm" (`00:48`) nhưng video không giải thích nội dung đó là gì.
- Gus đoán churn thấp (`11:13`) nhưng không có số liệu; phần đó là suy đoán của host.
- Lợi thế khó sao chép: founder đang làm IT admin và hiểu Intune (`05:30`); video không nói thêm về thời gian làm nghề.
