---
schema: 2
video_id: _9agAuKOOPg
channel: superwall
title: "The Secrets of Consumer Club: Insights from Joseph Choi - Superwall Podcast"
date: 2025-04-04
url: https://www.youtube.com/watch?v=_9agAuKOOPg
transcript: superwall/youtube-transcript/superwall/the-secrets-of-consumer-club-insights-from-joseph-choi-superwall-podcast/transcript.md
kind: expert_talk
speakers: [{name: Joseph Choi, role: expert}, {name: Taylor Fox, role: host}]
bias: "Video thuộc kênh Superwall (công cụ paywall), và Superwall đang quảng bá sản phẩm web-to-app của họ. Joseph điều hành cộng đồng Consumer Club (Discord) và hay giới thiệu công cụ phân tích TikTok do chính ông build. Các ví dụ app và số liệu là nghe kể."
analyzed: 2026-11-15
cases:
  - id: cal-ai
    depth: mention
    product: "Cal AI (app đếm calo bằng ảnh chụp đồ ăn)"
    what: "Chỉ hiện app 1–2 giây, không nhắc tên; phần giữ chân là theo dõi calo hằng ngày"
    type: [mobile-app]
    revenue: {amount: 2000000, unit: usd, basis: monthly, note: "Joseph nói 'last time I saw', nghe được, chưa kiểm", q: "they're they're making $2 million a month", ts: "00:42:50", evidence: claimed}
  - id: focus-tree
    depth: mention
    product: "Focus Tree (app cây ảo giúp tập trung)"
    what: "Founder Laurent (thành viên Consumer Club) dùng creator sinh viên, flash màn hình app vài giây; chuyển đổi xảy ra ở comment"
    type: [mobile-app]
  - id: tollan
    depth: mention
    product: "Tollan (app AI companion dạng nhân vật hoạt hình)"
    what: "Ra mắt vài tuần trước, lên top 1–2 App Store; Joseph nói ai cũng có thể làm bản tương tự bằng model voice mới"
    type: [mobile-app]
  - id: oasis
    depth: mention
    product: "Oasis (từ app nước sang app sức khoẻ)"
    what: "Founder Cormac làm talking head xanh trước nền màn hình app; mở rộng từ chất lượng nước sang không khí và thanh protein; có thể là một người"
    type: [mobile-app]
  - id: ngl
    depth: mention
    product: "NGL (app hỏi đáp kiểu questionnaire)"
    what: "Seeding tài khoản theo tên từng trường cấp 3, follow cả trường, rồi đăng cùng lúc"
    type: [mobile-app]
  - id: tabs-chocolate
    depth: mention
    product: "Tabs Chocolate (thương hiệu e-com, không phải app)"
    what: "Thuê thiếu niên nói về sản phẩm trên tài khoản mới 0 follower, không ads; từ 0 lên 10 triệu trong 1 năm (video không nêu đơn vị tiền)"
    type: [ecom-brand]
steps:
  - stage: find-idea
    ts: "00:11:12"
    what: "Lướt TikTok mỗi ngày, lưu video vào thư mục bookmark theo format, rồi tự hỏi vì sao nó làm mình có cảm xúc."
    tactic: s4-tiktok-comment-mining
    tactic_note: "Phân loại theo format (talking head, slideshow, B-roll chữ...) chứ không theo app"
  - stage: find-idea
    ts: "00:24:29"
    what: "Tìm từ khoá ngách (ADHD, journaling, quan hệ...), lọc video đang chạy tốt, so view với median của chính tài khoản để loại video chỉ nhờ follower."
    tactic: s4-tiktok-comment-mining
    tool: "công cụ tự build của Joseph (lọc TikTok theo từ khoá và view so với median tài khoản)"
  - stage: validate
    ts: "00:29:08"
    what: "Copy video đang chạy tốt, thuê creator quay bản sửa nhẹ để đo nhu cầu trước khi launch."
    tactic: s8-content-demand-test
    tactic_note: "Nhái video đã có view rồi chỉ sửa một phần để gắn sản phẩm; đo view trước khi build hoặc thuê influencer đắt"
  - stage: grow
    ts: "00:58:52"
    what: "Đăng video đầu tiên trên tài khoản TikTok mới: nói thẳng trước điện thoại, gần như không chỉnh sửa, đạt 50.000 view."
    tactic: g3-organic-content-formats
    tactic_note: "Quay bằng điện thoại, nói tự nhiên; hook đủ tốt"
  - stage: grow
    ts: "00:20:26"
    what: "Trả lời comment bằng video reply để hiện cho đúng người đã tương tác, rồi đưa CTA ngày hôm sau."
    tactic: g3-organic-content-formats
    tactic_note: "Video reply dùng như retargeting đối với người đã xem video gốc"
  - stage: grow
    ts: "00:17:28"
    case: cal-ai
    what: "Cal AI chỉ hiện app 1–2 giây, không nhắc tên; người xem tự vào App Store hoặc hỏi trong comment."
    tactic: g3-organic-content-formats
    tactic_note: "CTA mềm, không link; app chỉ xuất hiện trên màn hình"
  - stage: grow
    ts: "00:17:45"
    case: focus-tree
    what: "Creator sinh viên flash màn hình app vài giây; chuyển đổi xảy ra khi creator trả lời comment hỏi tên app."
    tactic: g3-organic-content-formats
    tactic_note: "Nội dung study setup làm nền; comment là nơi chuyển đổi"
  - stage: grow
    ts: "01:08:15"
    case: oasis
    what: "Talking head xanh trước nền màn hình app; mở rộng dần từ nước sang chất lượng không khí và thanh protein."
    tactic: g3-organic-content-formats
    tactic_note: "Mở rộng mảng nội dung kề sau khi đã có domain authority và view"
  - stage: grow
    ts: "00:36:15"
    what: "Một founder (kể qua tweet của Alex) có 5 tài khoản mỗi điện thoại, đăng 3 bài mỗi ngày mỗi tài khoản; mua iPhone và SIM Mỹ cho creator, huấn luyện warm-up tài khoản."
    tactic: g7-creator-ops
    tactic_note: "Nghe kể (tweet của Alex), không phải trải nghiệm của Joseph; creator làm việc theo lịch đăng"
  - stage: grow
    ts: "00:05:57"
    case: tabs-chocolate
    what: "Thuê nhiều thiếu niên nói về sản phẩm trên tài khoản mới không follower, không chạy ads."
    tactic: g7-creator-ops
    tactic_note: "Ví dụ e-com, không phải app"
  - stage: launch
    ts: "00:39:51"
    case: ngl
    what: "Follow hàng loạt tài khoản theo tên từng trường cấp 3 để học sinh follow lại, rồi đăng bài đầu cho cả trường thấy cùng lúc mở app."
    tactic: other
    tactic_note: "Seeding audience bằng tài khoản theo trường (kiểu alumni); không phải g1 vì không dùng group/DM"
quotes: []
rules:
  - {ts: "00:04:19", who: Joseph Choi, stage: find-idea, theme: [], text: "It's really just like start with the market. Like understand what does the market want?", vi: "Thực ra là bắt đầu từ thị trường: hiểu thị trường muốn gì.", evidence: opinion}
  - {ts: "00:22:39", who: Joseph Choi, stage: find-idea, theme: [], text: "a lot of times it actually starts with the um reverse engineering like what would make a good viral moment on TikTok and then building that as a feature into your product.", vi: "Nhiều khi bắt đầu bằng cách đảo ngược: khoảnh khắc nào trên TikTok sẽ viral, rồi làm nó thành tính năng của sản phẩm.", evidence: opinion}
  - {ts: "00:45:53", who: Joseph Choi, stage: find-idea, theme: [], text: "I've heard people refer to it as like start with a channel.", vi: "Người ta gọi đó là bắt đầu từ kênh.", evidence: opinion}
  - {ts: "00:46:14", who: Joseph Choi, stage: find-idea, theme: [builder-trap], text: "if you don't know what it's going to look like, then you start with a product and then you you build it", vi: "Nếu không biết nội dung sẽ trông thế nào, bạn bắt đầu bằng sản phẩm, build xong rồi mới nghĩ tới nội dung.", evidence: opinion}
  - {ts: "00:29:08", who: Joseph Choi, stage: validate, theme: [sell-before-build], text: "and to validate your market first before maybe maybe even before launching", vi: "Dùng nội dung để kiểm chứng thị trường trước khi launch, thậm chí trước khi thuê influencer đắt.", evidence: opinion}
  - {ts: "00:17:02", who: Joseph Choi, stage: grow, theme: [], text: "So a lot of times the calls to actions are a lot softer.", vi: "Nên nhiều khi lời kêu gọi hành động nhẹ hơn nhiều.", evidence: opinion}
  - {ts: "00:20:26", who: Joseph Choi, stage: grow, theme: [right-audience], text: "it's almost like a Facebook retargeting campaign where you're targeting the same people that engaged with that original video with the video reply.", vi: "Gần giống chiến dịch retargeting trên Facebook: nhắm đúng những người đã tương tác với video gốc.", evidence: opinion}
  - {ts: "00:31:39", who: Joseph Choi, stage: grow, theme: [], text: "there should be some hypothesis behind why you're choosing this type of content.", vi: "Phải có giả thuyết về lý do chọn loại nội dung này.", evidence: opinion}
  - {ts: "00:57:25", who: Joseph Choi, stage: grow, theme: [], text: "Like people do want authentic content, whatever form that comes in", vi: "Người ta vẫn muốn nội dung thật, dù dưới hình thức nào.", evidence: opinion}
  - {ts: "00:59:22", who: Joseph Choi, stage: grow, theme: [ship-ugly], text: "as long as you know kind of the fundamentals of like here's a piece of content that you kind of think people will be interested in.", vi: "Miễn là nắm nền tảng: một nội dung bạn nghĩ người ta sẽ quan tâm.", evidence: opinion}
  - {ts: "01:18:23", who: Joseph Choi, stage: grow, theme: [], text: "So, I really think that you need like with underpriced distribution, you kind of have to understand it yourself.", vi: "Với kênh phân phối còn bị định giá thấp, founder phải tự hiểu nó trước đã; sau đó mới thuê người làm tiếp.", evidence: opinion}
  - {ts: "01:20:02", who: Joseph Choi, stage: grow, theme: [], text: "I would approach them with caution and just like I think there's certain experts and service providers and agencies that do do a good job", vi: "Tôi sẽ thận trọng với agency; có vài chuyên gia làm tốt nhưng vòng đời thường không quá 6 tháng.", evidence: opinion}
  - {ts: "01:26:43", who: Joseph Choi, stage: mindset, theme: [], text: "everyone can do it if you're smart and you just figure it out after a couple iterations", vi: "Ai thông minh và tự thử vài vòng thì đều làm được.", evidence: opinion}
  - {ts: "01:28:02", who: Joseph Choi, stage: mindset, theme: [revenue-first], text: "you might not get rich quick, but I think now more than ever by far is like a time where you can build something that is like ramen profitable", vi: "Không giàu nhanh, nhưng bây giờ là lúc dễ nhất để làm ra thứ đủ sống (ramen profitable).", evidence: opinion}
numbers:
  - {ts: "00:58:52", metric: "view video đầu của tài khoản TikTok mới (Joseph tự đăng)", value: 50000, unit: count, evidence: claimed}
  - {ts: "00:36:15", metric: "bài TikTok mỗi tài khoản mỗi ngày (quan niệm trong giới, kèm 5 tài khoản/điện thoại)", value: 3, unit: count, evidence: claimed}
  - {ts: "01:30:37", metric: "ngưỡng view để tiếp tục thử một ý (Joseph khuyên)", value: 5000, unit: count, evidence: opinion}
frameworks: [sell-before-build, start-with-channel, video-reply-retargeting]
idea_patterns: [snap-and-get-result, content-as-app]
---
## Một câu

Joseph Choi (Consumer Club) cho rằng phân phối quan trọng hơn sản phẩm: kiểm nhu cầu bằng nội dung TikTok trước khi build, tìm ý tưởng bằng cách xem khách đang xem gì, và dùng comment hay video reply để chốt.

## Bài học cho tôi

- Kiểm nhu cầu bằng nội dung trước khi build: nhái video đang chạy tốt trong ngách, sửa nhẹ, đo view (`00:29:08`).
- Dùng video reply để nhắm lại đúng những người đã tương tác với video gốc (`00:20:26`).

## Đừng tin vội

- Bias: video là kênh của Superwall, công cụ paywall đang quảng bá web-to-app của chính họ (khoảng `01:23:58`). Joseph hay giới thiệu công cụ TikTok do mình build.
- Các ví dụ (Cal AI ~2 triệu USD/tháng, Focus Tree, Tollan, Oasis, NGL) là nghe kể, Joseph dùng "last time I saw" và "I think"; không kiểm được.
- Survivor bias: chỉ kể case thắng. Joseph tự nói AI avatar có vấn đề đạo đức nhưng không đi sâu (`00:53:39`).
- Điều kiện riêng: TikTok 2025, slideshow và AI avatar đang lên; nhiều ví dụ dựa vào audience sẵn có hoặc mạng lưới của Consumer Club, không sao chép được.
- Video không nói: chi tiết build, cách có 10–100 người dùng đầu tiên, giá gói, tỷ lệ chuyển đổi, và số liệu của chính Joseph.
