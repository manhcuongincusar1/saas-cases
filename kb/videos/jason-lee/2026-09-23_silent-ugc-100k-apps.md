---
schema: 2
video_id: qGIWJBw1dyU
channel: jason-lee
title: "How these $100K/mo apps actually get users (New Strategy)"
date: 2026-09-23
url: https://www.youtube.com/watch?v=qGIWJBw1dyU
transcript: youtube-other/jasonleefinance/2026-09-23_how-these-100kmo-apps-actually-get-users-new-strategy/transcript.md
kind: expert_talk
speakers:
  - {name: Jason Lee, role: expert}
bias: "Arcads AI tài trợ video; link Arcads trong mô tả là link riêng của Jason (go.heyjasonlee.com/arcads) và toàn bộ cách làm chạy trên Arcads, nên con số 83 cent/video cũng là lời quảng bá gói $88. 'Skill' miễn phí là mồi thu lead (thebreadcrumb.co). Doanh thu ba app ($100–300K/tháng) Jason nói miệng, không nêu nguồn. Jason không đưa ra kết quả nào của chính các video AI ông tạo."
analyzed: 2026-11-15
cases:
  - id: gym-app-lipa
    depth: mention
    product: "App gym/fitness; auto-caption ghi tên không nhất quán: Lipa, Lifa, Lifter, Lyft, lifta (chưa xác định được app nào)"
    what: "App tập gym; quảng bá bằng video TikTok không lời, rồi chạy lại chính video đó làm quảng cáo Meta"
    revenue: {amount: 300000, unit: usd, basis: monthly, note: "Jason nói miệng, không nêu nguồn", q: "They are making $300,000 a month with this app.", ts: "00:01:57", evidence: claimed}
    scale_channels: [tiktok_organic, paid_meta]
  - id: swerve-ai-chat
    depth: mention
    product: "Swerve AI Chat"
    what: "App tiêu dùng (chat AI); quảng bá bằng video không lời, hook là dòng chữ"
    revenue: {amount: 100000, unit: usd, basis: monthly, note: "Jason nói miệng, không nêu nguồn", q: "This is also another consumer app that's doing 100K per month.", ts: "00:02:27", evidence: claimed}
    scale_channels: [tiktok_organic]
  - id: couple-joy
    depth: mention
    product: "Couple Joy"
    what: "App cho cặp đôi; có hẳn một kênh lập riêng để quảng bá app, video không lời rồi tới demo app"
    revenue: {amount: 200000, unit: usd, basis: monthly, note: "Jason nói miệng, không nêu nguồn", q: "Couple Joy, making 200K per month.", ts: "00:02:27", evidence: claimed}
    scale_channels: [tiktok_organic]
steps:
  - stage: grow
    ts: "00:02:06"
    case: gym-app-lipa
    what: "Format 'silent UGC': người trong video không nói, dòng chữ đè trên hình làm hook ('Three years in the gym. And now I find this'), nửa sau chiếu app. Video ví dụ được nói là 4 triệu view."
    tactic: g3-organic-content-formats
    tactic_note: "video không lời, hook bằng chữ, app ở cảnh hai"
  - stage: grow
    ts: "00:02:43"
    case: couple-joy
    what: "Lập hẳn một kênh chỉ để quảng bá một app; mọi video cùng một kiểu: hook chữ rồi demo app, không lời."
    tactic: g3-organic-content-formats
    tactic_note: "tài khoản riêng cho một app, một format lặp lại"
  - stage: grow
    ts: "00:03:43"
    what: "Cách làm bằng AI Jason trình diễn: lấy một video TikTok viral làm mẫu, cho Claude Code điều phối và Arcads (Seedance 2.5, Nano Banana) tạo lại video với nhân vật AI của mình; cảnh hai là đoạn quay màn hình app, quay một lần rồi dùng lại cho mọi video."
    tactic: g3-organic-content-formats
    tool: "Claude Code, Arcads (Seedance 2.5, Nano Banana)"
    cost: "khoảng $0,83/video theo gói Arcads $88/tháng; kênh 30 video khoảng $24"
    tactic_note: "nhân bản video viral bằng AI thay cho thuê creator; Jason không cho thấy kết quả phân phối"
  - stage: grow
    ts: "00:04:26"
    what: "Làm cả một tài khoản TikTok với cùng một nhân vật, mỗi video một hook chữ khác nhau, để thử hook nào chạy rồi mới tính scale bằng paid ads."
    tactic: g3-organic-content-formats
    tactic_note: "thử nhiều hook trên một nhân vật cố định"
  - stage: grow
    ts: "00:12:22"
    what: "Soi format trước khi làm: gõ tên app đối thủ vào TikTok để xem các video top đang quảng bá nó; hoặc tìm cụm hook chung ('I can't believe', 'I just found out', 'no one told me') rồi xem video nào đang quảng bá app."
    tactic: g3-organic-content-formats
    tool: "tìm kiếm TikTok"
    tactic_note: "soi format đang chạy của app khác"
  - stage: grow
    ts: "00:13:42"
    case: gym-app-lipa
    what: "Đăng organic trước để biết video nào có view, rồi đổ tiền quảng cáo sau đúng video đó. Jason chỉ ra app gym làm vậy: cùng một video không lời trên TikTok xuất hiện trong Meta Ads Library."
    tactic: g6-paid-ads
    tool: "Meta Ads Library"
    tactic_note: "sau organic: lấy video organic đã thắng làm quảng cáo"
quotes: []
rules:
  - ts: "00:00:00"
    who: Jason Lee
    stage: mindset
    theme: [builder-trap]
    text: "It's getting a lot easier and easier to build software. But if you can't get people to pay for it, what is the point?"
    vi: "Làm phần mềm ngày càng dễ. Nhưng không khiến người ta trả tiền được thì làm để làm gì?"
    evidence: opinion
  - ts: "00:01:25"
    who: Jason Lee
    stage: grow
    theme: []
    text: "Do these videos convert views into paying customers for our app? So, I did some research and the answer is not really. I mean, they could work if you're selling physical products, but definitely not for apps."
    vi: "Video UGC có diễn viên AI (loại có lời) có biến view thành khách trả tiền cho app không? Jason nói ông đã tìm hiểu và câu trả lời là không hẳn: có thể được với hàng vật lý, không được với app."
    evidence: opinion
  - ts: "00:03:20"
    who: Jason Lee
    stage: grow
    theme: []
    text: "if you were to create a video like this, I find that sometimes it still looks like AI. The expression is kind of exaggerated and sometimes the voice is not natural."
    vi: "Video AI có lời đôi khi vẫn lộ là AI: biểu cảm hơi quá, giọng đôi khi không tự nhiên."
    evidence: opinion
  - ts: "00:06:01"
    who: Jason Lee
    stage: grow
    theme: []
    text: "what matters here is actually the first scene which is the model and the hook. That is the thing that's going to drive engagement and then you don't want to show your app until the end."
    vi: "Thứ quyết định là cảnh đầu: nhân vật và hook. Nó kéo tương tác; app thì để tới cuối mới cho thấy."
    evidence: opinion
  - ts: "00:12:11"
    who: Jason Lee
    stage: grow
    theme: [right-audience]
    text: "this silent UGC format works best for consumer apps."
    vi: "Format silent UGC hợp nhất với app tiêu dùng."
    evidence: opinion
  - ts: "00:12:22"
    who: Jason Lee
    stage: grow
    theme: [right-audience]
    text: "I don't see this format used a lot for B2B apps."
    vi: "Tôi không thấy format này được dùng nhiều cho app B2B."
    evidence: opinion
  - ts: "00:13:17"
    who: Jason Lee
    stage: grow
    theme: []
    text: "you want to make sure that you warm up your Tik Tok account if you're starting with a fresh one."
    vi: "Tài khoản TikTok mới thì phải 'làm ấm' trước khi đăng nhiều video."
    evidence: opinion
  - ts: "00:13:42"
    who: Jason Lee
    stage: grow
    theme: []
    text: "It is not the only way because a lot of these apps are also running ads, but this is a good way to start if you're starting from zero."
    vi: "Đây không phải cách duy nhất vì nhiều app trong số này cũng chạy quảng cáo, nhưng là cách tốt để bắt đầu từ số 0."
    evidence: opinion
  - ts: "00:13:42"
    who: Jason Lee
    stage: grow
    theme: []
    text: "you will start to collect data and see what videos are getting views and then you can take those videos and put an ad spend behind them and get even more traffic"
    vi: "Làm organic trước sẽ có dữ liệu video nào có view, rồi lấy đúng các video đó chạy quảng cáo để có thêm traffic."
    evidence: opinion
numbers:
  - {ts: "00:01:57", metric: "view của một video silent UGC quảng bá app gym", value: 4000000, unit: views, evidence: claimed}
  - {ts: "00:11:30", metric: "view cao nhất trên một tài khoản mẫu (Jason nêu 300.000 và 1,3 triệu)", value: 1300000, unit: views, evidence: claimed}
  - {ts: "00:14:18", metric: "credit Arcads cho một video Seedance 2.5", value: 75, unit: count, evidence: claimed}
  - {ts: "00:14:18", metric: "credit của gói Arcads $88/tháng", value: 8000, unit: count, evidence: claimed}
  - {ts: "00:14:45", metric: "chi phí mỗi video AI (gói $88 chia 106 video)", value: 0.83, unit: usd, evidence: claimed}
  - {ts: "00:14:45", metric: "chi phí một kênh 30 video", value: 24, unit: usd, evidence: claimed}
frameworks: [organic-find-format-then-paid-scale]
idea_patterns: []
---

## Một câu

Jason Lee (video do Arcads tài trợ) giới thiệu "silent UGC": video không lời, dòng chữ làm hook rồi chiếu app, và cách dùng Claude Code cùng Arcads nhân bản video TikTok viral với giá khoảng 83 cent mỗi video.

## Bài học cho tôi

- Trong format này, cảnh đầu (nhân vật và hook chữ) là thứ kéo tương tác, app chỉ xuất hiện ở cuối; đoạn quay app làm một lần rồi dùng lại (`00:06:01`).
- Thứ tự Jason khuyên trùng với lựa chọn organic: đăng organic để biết video nào có view, rồi mới đổ tiền quảng cáo sau video thắng (`00:13:42`).

## Đừng tin vội

- Video được Arcads tài trợ và dùng link riêng của Jason. Con số 83 cent/video là phép chia trên bảng giá Arcads, cũng là lời quảng bá gói.
- Doanh thu ba app là lời Jason, không nêu nguồn. Tên app gym bị auto-caption ghi năm kiểu (Lipa, Lifa, Lifter, Lyft, lifta), nên chưa xác định được app nào để kiểm.
- Jason không cho thấy kết quả nào của các video AI do ông tạo: không view, không lượt cài, không doanh thu. Bằng chứng "format chạy" là video của app khác, không rõ do người thật hay AI quay. Chính ông nói video UGC AI có lời "not really" ra khách cho app (`00:01:25`), và phần "research" đó không được trình bày.
- View chưa phải tiền: các video 4 triệu và 1,3 triệu view không kèm số lượt cài hay số người trả (`VALIDATE.md`: đếm tiền, không đếm view).
- Video không nói tới các rủi ro của chính cách làm: nhân bản video của người khác và dùng ảnh một người "found randomly on Google" làm nhân vật (`00:05:39`) là dùng nội dung và hình ảnh của người khác khi chưa xin phép; TikTok có thể khoá tài khoản (video chỉ nhắc warm-up); lời chứng thực do nhân vật AI không có thật nói ra có thể vướng quy định về testimonial giả ở Mỹ. Ba điểm này là ghi chú của tôi, chưa kiểm chi tiết.
- Rào cản khi làm từ VN mà video không nhắc: tài khoản TikTok đăng từ VN thường bị phân phối cho người xem ở VN (`VALIDATE.md`).
