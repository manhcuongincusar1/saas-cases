---
schema: 2
video_id: jZ1W85VdIBk
channel: superwall
title: "How I Built the #1 App on The App Store (Twice)"
date: 2025-12-06
url: https://www.youtube.com/watch?v=jZ1W85VdIBk
transcript: superwall/youtube-transcript/superwall/how-i-built-the-1-app-on-the-app-store-twice/transcript.md
kind: founder_case
speakers:
  - {name: Roger Chen, role: founder}
  - {name: Joseph Choi, role: host}
bias: "Superwall (công cụ paywall) tài trợ kênh; host Joseph Choi bán Consumer Club; founder đang bán Bro và Lobby. Số liệu (DAU, view) là founder tự nói trong podcast, không có dashboard."
analyzed: 2026-11-15
cases:
  - id: bro
    depth: full
    product: "Bro: AI companion nằm trên màn hình khoá, nổi phía trên ứng dụng nhắn tin"
    what: "Trợ lý AI dạng cửa sổ nổi (giống FaceTime nhỏ) phía trên nhắn tin, hẹn hò; app hit #1 App Store Mỹ"
    type: [ios-app]
    customer: "Người nhắn tin (đặc biệt chat với crush, dating app); video không nói trả tiền thế nào"
    founder:
      who: Roger Chen
      base: null
      technical: null
      team: "có co-founder Leo (làm mockup bằng Protopie)"
      background: "Từng làm Lobby (app hang out online); học ở Chicago (theo video)"
    revenue: null
    pricing: null
    idea_origin: [adjacent_expansion]
    scale_channels: [paid_tiktok, ugc_creators, tiktok_organic]
    community_at_discovery: null
    demand_signal:
      kind: content_views
      level: 2
      what: "Video mockup (app chưa xong) trên tài khoản thương hiệu TikTok: 7,9 triệu view; nội dung chính là ý tưởng sản phẩm"
      q: "This was a 7. 9 million views."
      ts: "00:05:29"
    prior_failures: null
    unfair_advantage:
      - {value: cofounder, what: "Có co-founder Leo làm mockup", q: "So this one is made by my co-founder Leo.", ts: "00:00:21"}
      - {value: prior_success, what: "Lobby (công ty trước) đạt 500k DAU và #1 App Store ở 5 nước", q: "Lobby, reached 500,000 daily active users", ts: "00:00:00"}
      - {value: domain_expertise, what: "Làm sản phẩm social lâu năm", q: "I feel like we've been working on social products for a long time", ts: "00:40:21"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: paid_tiktok, what: "Mua quảng cáo TikTok để test format và giao diện trước khi có app", q: "All he did was buy Tik Tok ads, test formats", ts: "00:01:40"}
      - {channel: ugc_creators, what: "Sau khi test, mở rộng ý tưởng với 50 creators TikTok", q: "Then he scaled the concept with 50 creators on Tik Tok", ts: "00:01:40"}
      - {channel: tiktok_organic, what: "Founder nói app lên hạng vì TikTok (video demo và video mockup)", q: "it was a lot of Tik Tok honestly", ts: "00:03:25"}
    build: null
  - id: lobby
    depth: full
    product: "Lobby: phòng chờ để bạn bè hang out online, có hoạt động nền (YouTube, SoundCloud, game)"
    what: "App video call ngẫu nhiên kiểu phòng chờ ký túc xá; có nút chụp ảnh nhóm (boomerang) và trò 'một phút' để gọi nhanh"
    type: [mobile-app]
    customer: "Bạn bè muốn hang out online một cách tự nhiên, không cần hẹn"
    founder:
      who: Roger Chen
      base: null
      technical: null
      team: "co-founder (video không nói rõ cho Lobby)"
      background: "Làm nhiều năm về social product; học ở Chicago (theo video)"
    revenue: null
    pricing: null
    idea_origin: [own_pain]
    scale_channels: [word_of_mouth]
    community_at_discovery:
      value: "Chính founder dùng video call với bạn, cảm giác như họp hội nghị chứ không phải hang out"
      insider: true
      q: "it always feels less like a hangout and more like a conference call"
      ts: "00:16:39"
    demand_signal: null
    prior_failures:
      count: 1
      what: "Gần một năm không tăng trưởng chất lượng; retention kém trước khi bùng nổ ở Israel"
      q: "we actually like struggled with it for a while"
      ts: "00:20:01"
    unfair_advantage:
      - {value: domain_expertise, what: "Làm sản phẩm social lâu năm", q: "I feel like we've been working on social products for a long time", ts: "00:40:21"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: word_of_mouth, what: "Lobby bùng nổ ở Israel năm 2022 (video không nói 10 người đầu tiên đến từ đâu)", q: "lobby just suddenly went viral in Israel", ts: "00:20:13"}
    build: null
steps:
  - stage: find-idea
    ts: "00:01:10"
    case: bro
    tactic: s9-niche-narrowing
    tactic_note: "Mở sang kịch bản kề bên: đặt AI companion vào các app người ta đã dùng, không nằm trong hộp đen"
    what: "Từ Lobby, ý tưởng mở rộng: đặt AI companion vào các app đang dùng (nhắn tin, dating, camera roll)."
  - stage: find-idea
    ts: "00:03:56"
    case: bro
    tactic: s9-niche-narrowing
    tactic_note: "Thu hẹp từ tầm nhìn lớn xuống một kịch bản cụ thể: nhắn tin trước, rồi dating app"
    what: "Tầm nhìn 'companion luôn ở bên bạn' quá rộng; chọn một kịch bản cụ thể là nhắn tin, rồi mới tới dating app."
  - stage: validate
    ts: "00:05:40"
    case: bro
    tactic: s8-content-demand-test
    tactic_note: "Video mockup (không phải app thật) đăng TikTok trước khi build xong để đo nhu cầu"
    what: "Đăng video mockup do co-founder làm trên tài khoản thương hiệu; một video đạt 7,9 triệu view trước khi có app."
  - stage: validate
    ts: "00:08:51"
    case: bro
    tactic: s8-content-demand-test
    tactic_note: "Có chi tiền quảng cáo trả phí để test trước khi có app"
    what: "Mua quảng cáo cho video đầu tiên để có phản hồi nhanh về format và giao diện trước khi có app."
  - stage: validate
    ts: "00:06:02"
    case: bro
    tactic: other
    tactic_note: "Prototype bằng Protopie (mockup bấm được, quay video), dùng trước khi làm app thật"
    what: "Làm mockup bằng Protopie, dùng trước với nhau mỗi ngày để tìm flow không hợp lý; giảm công kỹ thuật không cần thiết."
  - stage: grow
    ts: "00:04:31"
    case: bro
    tactic: g3-organic-content-formats
    tactic_note: "Format hook và demo: mở bằng người thật đang gặp tình huống, rồi demo app; sản xuất hàng loạt"
    what: "Chọn format hook bằng một tình huống có người thật, rồi demo app; sản xuất hàng loạt video, vài video outlier đạt 2–3 triệu view."
  - stage: grow
    ts: "00:12:11"
    case: bro
    tactic: g3-organic-content-formats
    tactic_note: "Dồn sức vào một format thắng (bong bóng bro nổi trên text)"
    what: "Chọn format 'bro nổi trên màn hình' làm trọng tâm và dồn toàn bộ vào format đó."
  - stage: grow
    ts: "00:34:01"
    case: bro
    tactic: g7-creator-ops
    tactic_note: "Tìm creator qua hashtag (ví dụ relationship), email để họ đăng; số creator giảm dần"
    threshold: "~50 creator lúc đỉnh, còn 10–20"
    what: "Tìm creator TikTok qua hashtag rồi email; lúc đỉnh có khoảng 50 creator, sau đó nhiều người ngừng đăng, còn khoảng 10–20."
  - stage: grow
    ts: "00:23:05"
    case: lobby
    tactic: g10-referral-viral-loop
    tactic_note: "Tính năng chụp ảnh nhóm (boomerang): đếm ngược, đăng story; nút sáng lên mỗi 5–10 phút để nhắc chụp"
    what: "Thêm tính năng chụp ảnh nhóm lúc đang video call; ảnh boomerang được đăng story, người chưa vào tò mò và quay lại."
  - stage: grow
    ts: "00:22:07"
    case: lobby
    tactic: g10-referral-viral-loop
    tactic_note: "Vòng mời bạn bè trong app; không dựa vào content marketing"
    what: "Làm các tính năng mời và chia sẻ ngay trong sản phẩm để bạn bè mời nhau; content marketing không giải được vấn đề mật độ."
  - stage: grow
    ts: "00:20:51"
    case: lobby
    tactic: g8-funnel-measurement
    tactic_note: "Đo tỉ lệ người có 5 bạn trong ngày đầu, so theo thị trường"
    threshold: "Israel ~60% so với ~20% nơi khác"
    what: "Đo tỉ lệ người có 5 bạn trong ngày đầu; Israel ~60%, nơi khác ~20%; từ đó quyết đầu tư vào mật độ mạng."
  - stage: grow
    ts: "00:23:49"
    case: lobby
    tactic: other
    tactic_note: "Lan sang quốc gia mới qua nhóm người dùng (trường quốc tế ở Cairo) sau khi đã seed ban đầu"
    what: "Lan từ Anh sang Ý, Đức, rồi Ai Cập và Ả Rập Xê Út qua nhóm người dùng; video nói có seed ban đầu nhưng không nêu cách seed."
  - stage: retain
    ts: "00:27:24"
    case: lobby
    tactic: g5-retention
    tactic_note: "Thanh thông báo ngẫu nhiên giờ đêm mời trò chuyện một phút với bạn bè"
    what: "Thanh thông báo ngẫu nhiên mời gọi một phút trò chuyện với bạn bè, để bạn bè có mặt cùng lúc."
quotes:
  - {ts: "00:01:10", who: Roger Chen, stage: find-idea, theme: [], text: "the insight is basically AI companions should not live in a black box. They should live with you in the apps you already use.", vi: "Insight là AI companion không nên nằm trong hộp đen; nó nên sống cùng bạn trong các app bạn đã dùng."}
  - {ts: "00:03:56", who: Roger Chen, stage: find-idea, theme: [clarity], text: "we still need to find a wedge like a concrete wedge like a concrete scenario in people's lives.", vi: "Vẫn cần tìm một điểm vào cụ thể, một kịch bản cụ thể trong đời sống người dùng."}
  - {ts: "00:07:01", who: Roger Chen, stage: build, theme: [], text: "So every time you you try that like you get some new insight. It's like hey like this flow doesn't work like it's too long.", vi: "Mỗi lần thử mockup là có thêm một insight; flow nào quá dài thì lộ ra ngay."}
  - {ts: "00:10:04", who: Roger Chen, stage: validate, theme: [action-over-research], text: "in the beginning like ads are really the fastest the fastest way to get feedback and you know", vi: "Ở giai đoạn đầu, quảng cáo là cách nhanh nhất để có phản hồi."}
  - {ts: "00:10:04", who: Roger Chen, stage: validate, theme: [action-over-research], text: "like that's the most dreadful period because you're you're just in your head you know you have no feedback and you can easily, you know, go on the wrong path.", vi: "Giai đoạn giữa ý tưởng và ra mắt là lúc đáng sợ nhất: không có phản hồi, dễ đi sai hướng."}
  - {ts: "00:14:37", who: Roger Chen, stage: mindset, theme: [], text: "So we want our product to augment your social relationships instead of like displacing them.", vi: "Sản phẩm nên bổ sung cho quan hệ xã hội của bạn, không thay thế chúng."}
  - {ts: "00:18:02", who: Roger Chen, stage: find-idea, theme: [], text: "the insight behind lobby is really that like people are going to hand out online, but it's got to be spontaneous and chill.", vi: "Insight của Lobby: người ta muốn hang out online, nhưng phải tự nhiên và thoải mái."}
  - {ts: "00:20:51", who: Roger Chen, stage: grow, theme: [persistence], text: "we know that the answer is really really to double down whatever it takes um to get our density up.", vi: "Chúng tôi biết phải dồn hết sức để tăng mật độ mạng lưới."}
  - {ts: "00:22:07", who: Roger Chen, stage: grow, theme: [], text: "this is not something that's solvable through content marketing", vi: "Vấn đề này không giải được bằng content marketing."}
  - {ts: "00:25:40", who: Roger Chen, stage: grow, theme: [], text: "it has to be a shared experience.", vi: "Phải là trải nghiệm chung: mọi người biết ảnh sắp được chụp và cùng hào hứng."}
  - {ts: "00:29:48", who: Roger Chen, stage: mindset, theme: [], text: "instead of using AI to create content we want to use AI to create context", vi: "Thay vì dùng AI để tạo nội dung, dùng AI để tạo bối cảnh cho người ta nói chuyện."}
  - {ts: "00:34:01", who: Roger Chen, stage: grow, theme: [], text: "this process took way way longer than I thought.", vi: "Quá trình làm việc với creator lâu hơn tôi nghĩ nhiều."}
  - {ts: "00:34:47", who: Roger Chen, stage: grow, theme: [persistence], text: "with content right like it's really hard to predict these things like there are not like rules they're not so you just have to try everything", vi: "Với nội dung không có luật lệ; phải thử mọi thứ cho tới khi có video bùng nổ."}
  - {ts: "00:38:22", who: Roger Chen, stage: mindset, theme: [passion-fuel], text: "I personally did not feel that much passion about it so it's pretty hard to keep tweaking the details.", vi: "Cá nhân tôi không đam mê ý tưởng đó nên rất khó tiếp tục chỉnh chi tiết."}
  - {ts: "00:39:36", who: Roger Chen, stage: mindset, theme: [passion-fuel], text: "I think like the best kind of social experiences provide a kind of like um relaxed joyful experience where you just like connect with other people.", vi: "Trải nghiệm social tốt nhất là thoải mái, vui, và giúp người ta kết nối với nhau."}
rules:
  - {ts: "00:08:32", who: Joseph Choi, stage: build, theme: [], text: "I haven't seen that many people do this strategy before proto just prototyping it before you even make the app.", vi: "Tôi chưa thấy nhiều người làm chiến lược này: prototype trước khi làm app.", evidence: opinion}
  - {ts: "00:09:32", who: Joseph Choi, stage: validate, theme: [action-over-research], text: "I feel like ads are one of the best ways to iterate in the beginning.", vi: "Tôi nghĩ quảng cáo là một trong những cách tốt nhất để lặp lại ý tưởng ở giai đoạn đầu.", evidence: opinion}
  - {ts: "00:11:00", who: Joseph Choi, stage: validate, theme: [action-over-research], text: "I feel like just the ads ads as validation is actually really really smart.", vi: "Dùng quảng cáo để kiểm chứng ý tưởng là rất thông minh.", evidence: opinion}
numbers:
  - {ts: "00:00:00", metric: "người dùng hằng ngày của Lobby (founder nói)", value: 500000, unit: count, evidence: claimed}
  - {ts: "00:05:29", metric: "view video mockup của Bro trên tài khoản thương hiệu", value: 7900000, unit: count, evidence: claimed}
  - {ts: "00:05:12", metric: "video outlier của Bro (2–3 triệu view)", value: 2500000, unit: count, evidence: claimed}
  - {ts: "00:20:51", metric: "tỉ lệ người có 5 bạn ngày đầu (Israel; nơi khác khoảng 20%)", value: 0.6, unit: ratio, evidence: claimed}
  - {ts: "00:20:51", metric: "retention ngày 90 của Lobby ở Israel", value: "25–30%", unit: ratio, evidence: claimed}
frameworks: [content-before-product, product-as-main-character]
idea_patterns: [adjacent-platform-expansion]
---

## Một câu

Roger Chen (từng làm Lobby) thử Bro bằng mockup và quảng cáo TikTok trước khi có app; một video mockup đạt 7,9 triệu view; trước đó Lobby đạt 500k DAU nhờ vòng mời bạn bè và chụp ảnh nhóm.

## Bài học cho tôi

- Test ý tưởng bằng mockup và quảng cáo nhỏ trước khi viết code; founder và host đều nói quảng cáo là cách có phản hồi nhanh nhất lúc đầu (`"00:09:32"`, `"00:10:04"`).
- Với app cần người dùng mời nhau, đo tỉ lệ người có 5 bạn ngày đầu rồi thiết kế tính năng mời (`"00:20:51"`, `"00:22:07"`).

## Đừng tin vội

- Số liệu (500k DAU, 7,9 triệu view, retention 25–30%) là founder nói trong podcast; không có doanh thu nào được nêu cho Bro hay Lobby.
- Lobby không tăng trưởng gần một năm; bước ngoặt là Israel với tỉ lệ người có 5 bạn ngày đầu ~60% so với ~20% nơi khác. Đây là điều kiện thị trường khó lặp lại; video không giải thích vì sao Israel khác.
- Podcast do Superwall (paywall) tài trợ và host bán Consumer Club; founder đang bán Bro, nên người xem cần tách phần ca ngợi sản phẩm.
- Video không nói chi phí quảng cáo, thời gian từ ý tưởng đến app, hay 10 người dùng đầu tiên của Lobby. Transcript ghi host là "Joseph Choy", tôi ghi "Joseph Choi" theo brief.
