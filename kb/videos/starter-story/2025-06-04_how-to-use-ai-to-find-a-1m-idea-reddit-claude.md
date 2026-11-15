---
schema: 2
video_id: L_FY6aW9cJ4
channel: starter-story
title: "How to Use AI to Find a $1M Idea [Reddit, Claude]"
date: 2025-06-04
url: https://www.youtube.com/watch?v=L_FY6aW9cJ4
transcript: starter-story-kb/videos/2025-06-04_how-to-use-ai-to-find-a-1m-idea-reddit-claude/transcript.md
kind: expert_talk
speakers: [{name: Steph France, role: expert}, {name: Pat Walls, role: host}]
bias: "Steph France là marketer làm framework và tải prompt miễn phí qua link trong mô tả (phễu); Starter Story Build (chương trình trả phí) được quảng bá cuối video (23:28). Ví dụ landing page là bản demo, không có sản phẩm thật."
analyzed: 2026-11-15
cases: []
steps:
  - stage: find-idea
    ts: "02:05"
    what: "Chọn một thị trường trong ba thị trường lớn (sức khoẻ, tài chính, quan hệ) có điểm mình biết hoặc quan tâm, rồi dùng prompt 'market idea expander' để đào tới ngách con."
    tactic: s9-niche-narrowing
    tactic_note: "Chọn ngách trong ba thị trường người ta vốn chi tiền, rồi mở rộng ngách con bằng prompt"
  - stage: validate
    ts: "05:15"
    what: "Kiểm nhu cầu: dùng Google và tiện ích Keyword Everywhere để xem lượng tìm kiếm và từ khoá liên quan; sau đó Google Trends để xem xu hướng ổn định hay tăng."
    tactic: s2-google-trends-volume
    tool: "Google, Keyword Everywhere, Google Trends"
  - stage: find-idea
    ts: "09:13"
    what: "Tìm nơi người ta than vấn đề: dùng truy vấn nâng cao trên Google để lấy thread Reddit, đọc và chọn thread đúng subreddit, rồi copy vào tài liệu."
    tactic: s3-reddit-pain-mining
    tool: "Google (truy vấn nâng cao), Reddit"
  - stage: find-idea
    ts: "13:00"
    what: "Đưa các thread đã copy vào Claude: prompt đầu tiên tách các nỗi đau, nhóm theo chủ đề, kèm trích dẫn của người nói."
    tactic: other
    tool: "Claude"
    tactic_note: "Dùng AI tách pain point từ thread Reddit đã thu thập"
  - stage: find-idea
    ts: "15:05"
    what: "Đưa các nỗi đau vào prompt 'market gap generator' để sinh ba ý tưởng sản phẩm theo khung khác biệt; chọn một ý tưởng."
    tactic: other
    tool: "Claude"
    tactic_note: "Sinh ý tưởng từ pain point qua prompt khung khác biệt (market gap)"
  - stage: validate
    ts: "18:48"
    what: "Dùng prompt tạo landing page đưa vào Lovable; trong khoảng một giờ có landing page với tiêu đề, tính năng, FAQ và form."
    tactic: s8-content-demand-test
    tool: "Claude, Lovable"
    tactic_note: "Landing page trước khi build xong, để đo nhu cầu"
  - stage: validate
    ts: "21:27"
    what: "Đề xuất (chưa làm trong video): đặt popup hỏi vài câu và hỏi có muốn được báo khi app ra mắt; khi waitlist đạt khoảng 100 người thì mới build."
    tactic: other
    tactic_note: "Quiz trên trang chờ kèm waitlist; build khi đủ khoảng 100 người (đề xuất, chưa thấy kết quả)"
quotes: []
rules:
  - {ts: "02:20", who: Steph France, stage: find-idea, theme: [revenue-first], text: "So you are already reducing the risk.", vi: "Như vậy bạn đã giảm rủi ro, vì đây là thị trường người ta chắc chắn sẵn sàng chi tiền.", evidence: opinion}
  - {ts: "04:59", who: Steph France, stage: find-idea, theme: [], text: "if you don't have any then just pick one that sounds good.", vi: "Nếu không có lợi thế nào thì cứ chọn một thị trường nghe hấp dẫn.", evidence: opinion}
  - {ts: "21:27", who: Steph France, stage: validate, theme: [], text: "And if it's a lot of time investment and if your time is reduced then I would always go by validating again.", vi: "Nếu việc build tốn nhiều thời gian và thời gian của bạn có hạn, hãy luôn kiểm chứng lại trước.", evidence: opinion}
numbers:
  - {ts: "00:15", metric: "thời gian toàn bộ quy trình (video nói 45 phút, sáu công cụ, năm prompt)", value: 45, unit: minutes, evidence: claimed}
  - {ts: "07:34", metric: "lượt tìm 'co-parenting' (đọc từ công cụ Keyword Everywhere; không rõ khu vực/thời gian)", value: 40000, unit: count, evidence: claimed}
  - {ts: "22:08", metric: "ngưỡng waitlist trước khi build (đề xuất của Steph)", value: 100, unit: count, evidence: opinion}
frameworks: []
idea_patterns: [niche-down-proven-category]
---
## Một câu

Gold Mining framework của Steph France: sáu công cụ, năm prompt, khoảng 45 phút đi từ chọn ngách trong ba thị trường lớn, kiểm nhu cầu bằng Google Trends, gom nỗi đau từ Reddit, sinh ý tưởng bằng AI đến landing page. Chỉ là demo, chưa có sản phẩm thật hay doanh thu.

## Bài học cho tôi

- Bắt đầu từ ba thị trường người ta vốn chi tiền, rồi đào ngách con trước khi kiểm nhu cầu (`02:20`).
- Trước khi build, đưa trang chờ có quiz và waitlist ra; video gợi ý build khi đủ khoảng 100 người, nhưng chưa có kết quả thật (`21:27`).

## Đừng tin vội

- Đây là demo: landing page "co-parenting" trong video không có khách, không có doanh thu và chưa qua thử nghiệm với người thật.
- Steph là marketer làm framework và tải prompt qua link (phễu); Starter Story Build được quảng bá cuối video (`23:28`).
- Con số 40.000 lượt tìm và các số ước lượng từ công cụ không nói rõ khu vực, thời gian, hay độ tin cậy.
- Ngách quan hệ/nuôi con là nhạy cảm và cần hiểu sâu; cách tìm ý tưởng này không tự cho biết người dùng có trả tiền hay không.
- Video không nói có ai đã dùng framework này để ra sản phẩm có doanh thu.
