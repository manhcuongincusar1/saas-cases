---
id: s4-tiktok-comment-mining
strategy: S4
title: "Soi TikTok/Instagram/YouTube trong ngách và đọc comment để thấy nhu cầu"
label: chrome                  # mở app/web video và đọc comment bằng tay hoặc Chrome; chưa có công cụ tự động đáng tin
time: "1–2 giờ cho 10 video; lượt kỹ có thể mất vài ngày"
cost: "$0"
evidence: corpus
signal_level_when_pass: 4–5    # QUA đòi cổng 2.3 và 2.5 của VALIDATE.md: 4 nếu chỉ có comment tự khai hoặc hỏi cách làm, 5 nếu có comment hỏi app/mua; đều chưa phải người mua của mình
tools: []
status: draft
---

## Dùng khi
Mình có một ngách hoặc một ý tưởng và cần thấy ngay người ta có nói về vấn đề đó không, bằng video thật và comment thật. Chọn `s3-reddit-pain-mining` nếu ngách hay ngồi ở diễn đàn hơn là video; chọn `s8-content-demand-test` nếu muốn thử bằng nội dung của chính mình.

## Đầu vào
Một từ khoá ngách (ví dụ "debloat", "quit vaping") hoặc một ý tưởng đã có một câu mô tả.

## Hai nhánh (phân loại tay của người viết theo mô tả step; câu truy vấn ở `engine/recipes/s4-tiktok-comment-mining.extra.sql`)
| Nhánh | Là gì | Số case (founder) | Ví dụ trong kho |
|---|---|---|---|
| X. Soi trend/format viral để chọn ý tưởng | xem video nổi trong ngách rồi chọn chủ đề hoặc format | 6 (6) | Flame (khung V, S, C), Natural Write, Payout (video thứ hai), Vugola, Puff Count, Copia |
| Y. Đọc comment để tìm hoặc xác nhận nhu cầu | người xem hỏi gì, xin gì, kể gì | 7 (7) | Go Tall, DBLI, GlowUp, Stella (comment dưới nội dung của chính mình), Payout, Stoppr, BulkMockup (comment YouTube) |

Payout đếm ở cả hai nhánh vì hai video khác nhau cùng một founder (DB ghi tên hai cách), nên 12 founder khác nhau cho 13 case. Cách chia là của người viết; Flame vừa soi video vừa đọc comment hỏi tên app nên ranh giới mờ.

## Các bước
1. **[chrome] Lọc video** (≤15 phút): tìm từ khoá ngách trên TikTok, sắp theo lượt thích mọi thời gian; ghi 10 video vào bảng (link, hook, view, số follower của tài khoản; con số 10 là đề xuất, chưa có số của kho). Puff Count làm đúng kiểu này: lướt 7 ngày và ghi từng video vào spreadsheet (link, hook, storyline, CTA).
2. **[chrome] Kiểm "viral thật" và "làm số lượng được"**: làm theo `VALIDATE.md` cổng 2.3 (V) và 2.4 (S); đừng chép ngưỡng ở đây. Flame là founder duy nhất trong nhánh này kể dùng khung VSC (V, S, C) khi chọn.
3. **[chrome] Đọc comment dưới 3–5 video lớn** (≤15 phút một lượt) và đếm bốn loại: hỏi tên app, hỏi cách giải, kể nỗi đau, cười/trêu. Cách đọc và ngưỡng của chữ C nằm ở `VALIDATE.md` cổng 2.5. Việc làm: dán bảng (video, loại comment, số lượng, một comment nguyên văn) vào ghi chú của ứng viên. Founder trong kho: Go Tall đọc comment người xem tự kể chiều cao; DBLI thấy người ta hỏi làm sao để hết phồng; GlowUp tìm thứ người ta xin (look, sản phẩm).
4. **[chrome] Đọc comment dưới nội dung của chính mình**, nếu đã có: Stella đọc những câu kiểu "ước gì có cái này" dưới video của chính founder. Nếu chưa có nội dung nào thì dùng biến thể của BulkMockup: tìm video YouTube trong ngách ít view nhưng nhiều comment (comment là nỗi đau chưa được giải) và liệt kê các phản đối.
5. **[manual] Đảo ngược** (host): hỏi khoảnh khắc nào làm video viral rồi biến nó thành tính năng. Chỉ có host nói; không founder nào kể đã làm.
6. **Ghi ứng viên** vào `journey/ideas/` kèm bảng bước 3 và link các video. Kết quả của bước 2–3 là tín hiệu mức 2–5 trong thang của `VALIDATE.md`.

## Đầu ra
Mỗi ứng viên một dòng: ngách/ý tưởng · 10 video (link) · bảng comment bước 3 · V, S, C đạt hay không (cổng 2.3, 2.4, 2.5) · mức tín hiệu 0–8.

## Ngưỡng qua
Ngưỡng nằm ở `VALIDATE.md` cổng 2.3 (V), 2.4 (S), 2.5 (C); không chép lại ở đây. Công thức này chỉ cho biết: chữ C (video có ra đơn không, đọc comment) là thứ host nhấn mạnh nhất; một video nhiều view chưa chứng minh gì (xem bảng bằng chứng).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 23 step trong 19 video |
| Case (video, case) có step này | 13, trong đó 13 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 10/23 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 9/13 |
| Case full không nêu existing_audience | 12/13 |
| Case full video không kể bằng chứng nhu cầu trước launch | 6/13 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 5.0 tháng (3.0–5.0), n=5 |
| Kênh scale trả tiền / thuần organic / không nêu | 5 / 8 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s4-tiktok-comment-mining.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
**10/23 step là lời host/expert, không phải việc founder đã làm** (6 video, người nói chính là Joseph Choi và khách của anh). 13 case founder (12 người) có 13 step, 11 ở giai đoạn tìm ý tưởng và 2 ở giai đoạn kiểm. 7/13 case không nêu loại bằng chứng nhu cầu nào; còn lại: lượt xem nội dung 3, trả tiền 1, build trước 1, tự khai hoặc danh sách chờ miễn phí 1. Nhóm outsider 5, insider 5, không nêu 3. Tháng tới mức hiện tại n=5, không đủ để đọc.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Louis (founder) · `2025-12-17_my-mobile-app-made-800k-in-365-days` · 03:54 | "by looking at comment section, you really just feel what people are wanting and you just try to come in and solve whatever they're asking for" | founder kể (GlowUp): đọc phần comment để thấy người ta muốn gì rồi làm đúng thứ họ xin |
| Pat Walls (host/expert) · `2026-07-12_she-built-this-340k-month-app-in-60-days` · 14:04 | "Don't build an app. Go build content. Then you can find your app idea once you do that." | lời khuyên của host (nói về Stella): làm nội dung trước, ý tưởng app xuất hiện sau |
| Pat Walls (host/expert) · `2025-09-06_our-simple-app-made-100k-in-90-days` · 02:39 | "I think that's really cool kind of finding an idea from a growth first strategy" | lời của host (Natural Write): tìm ý tưởng theo hướng tăng trưởng trước |
| David Attias (founder) · `2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-break` · 05:02 | "So, I validated by keyword research and by content research on TikTok and Instagram" | founder kể (Stoppr): kiểm bằng nghiên cứu từ khoá và nội dung trên TikTok, Instagram |
| Joseph Choi (host/expert) · `2026-10-11_start-1m-app-from-scratch` · 00:05:30 | "There's no point in having a video with 10 million views if it's not reaching the right audience, increasing downloads, and bringing in more revenue." | lời khuyên của host (Joseph Choi): video triệu view không đáng nếu không tới đúng người, không tăng tải và doanh thu; nối với cổng 2.5 của VALIDATE.md |
| Joseph Choi (host/expert) · `2026-10-11_start-1m-app-from-scratch` · 00:02:16 | "If I can't come up with any video that makes the app interesting to the right people, I would just scrap the entire idea and keep working on the idea itself." | lời khuyên của host: không nghĩ ra video làm app hấp dẫn đúng người thì bỏ ý tưởng |
| Yannis (host/expert) · `2026-05-21_the-new-short-form-strategy-dominating-for-app-g` · 00:53:39 | "Like I wouldn't build my app without trying to go viral first with a high converting format, right?" | lời khuyên của expert Yannis: không build app trước khi thử viral với một format chuyển đổi cao |
| Joseph Choi (host/expert) · `2025-04-04_the-secrets-of-consumer-club-insights-from-josep` · 00:22:39 | "a lot of times it actually starts with the um reverse engineering like what would make a good viral moment on TikTok and then building that as a feature into your product." | lời khuyên của host: bắt đầu từ việc đảo ngược khoảnh khắc viral rồi làm nó thành tính năng |
| Pat Walls hoặc Gus (host/expert) · `2026-07-19_this-stupidly-simple-app-makes-100k-month` · 08:14 | "Often, a lot of times when we build startups, we build something and then we get no DMs." | lời của host (nói về Go Tall): founder nhận được DM của người quan tâm chiều cao; nhiều startup build xong không có DM nào |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Công thức này chủ yếu là lời host/expert.** 10/23 step không gắn case; phần "đọc comment xem ai hỏi tên app" và khung V, S, C đến từ host (Joseph Choi) và expert, còn 13 case founder phần lớn chỉ kể "tôi lướt TikTok/đọc comment rồi chọn", ít ai kể có đếm hay có ngưỡng. Chữ C của `VALIDATE.md` là luật của dự án, không phải việc đa số founder trong kho làm.
- **Video nhiều view chưa phải nhu cầu.** Host nói video 10 triệu view không đáng nếu không tới đúng người và không tăng tải (bảng). Đây cũng là lý do bước 3 không thể bỏ.
- **Tìm tín hiệu ở nơi dễ thấy nhất thì ai cũng thấy.** 13 case đều lên được kênh; trend viral nên nhiều người cùng thấy và cùng làm (xem số bản sao ở `VALIDATE.md` cổng 2.9). Natural Write đi theo chủ đề đang hot; kho không cho biết có bao nhiêu người cùng làm mà thất bại.
- **Có thể là bắt trend, không phải nhu cầu bền.** 4/6 case nhánh X ghi nguồn ý tưởng có chép/theo trend (Natural Write, Copia, Vugola, Payout); xem `s12-timing-shift` về cửa sổ ngắn.
- **Kho chỉ chứa người thắng.** 13 case full dùng s4 và lên được kênh; số người đọc comment xong rồi không có đơn thì vắng mặt. "Không nêu" ≠ "không có": 7/13 không kể loại bằng chứng nhu cầu.

## Quyết định
- **QUA** nếu V, S, C đều đạt ở `VALIDATE.md` cổng 2.3–2.5 và nhóm comment hỏi/kể khớp nhóm mình tiếp cận được. Sang cổng 2.6 trở đi.
- **DỪNG** nếu video nhiều view nhưng comment chủ yếu trêu/cười, hoặc nhóm comment không phải nhóm trả tiền.
- **TEST THÊM** nếu thiếu số: đọc thêm 3–5 video khác trong 3 ngày (đề xuất, chưa có số của kho), hoặc chạy `s8-content-demand-test` với nội dung của chính mình.

## Cho solo founder bán global (từ VN)
- **Chép được:** bước 1–3, làm hoàn toàn từ xa, không cần audience, không tốn tiền. Đây là cách rẻ nhất trong kho để thấy tín hiệu bằng chứng công khai.
- **Rào cản thật:** (1) chỉ dùng được cho nhóm khách ở nền tảng video; nhóm B2B/chuyên nghiệp ngồi ở nơi khác (Reddit, LinkedIn, diễn đàn). (2) Thuật toán TikTok thấy từ VN có thể hiển thị khác với feed US; cần đặt vùng/ngôn ngữ phù hợp (suy luận của người viết, không phải từ kho). (3) Chưa có công cụ tự động đáng tin trong kho; việc đọc comment phải làm tay.
- **KHÔNG nên làm** nếu nhóm khách không xem video về vấn đề đó, hoặc nếu cả ngách chỉ có video giải trí và không ai hỏi gì trong comment (đúng tình huống host cảnh báo ở bước 3).
