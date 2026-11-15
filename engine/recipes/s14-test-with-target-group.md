---
id: s14-test-with-target-group
strategy: S14
title: "Đưa bản chưa hoàn thiện cho đúng nhóm khách tại một nơi hoặc dịp có sẵn (sự kiện, câu lạc bộ, nhóm cộng đồng, nhóm bạn)"
label: manual                  # gặp, đăng, chia sẻ màn hình bằng tay; agent chỉ giúp soạn bài và ghi kết quả
time: "2–4 giờ chuẩn bị; 1 dịp hoặc 3–7 ngày trong nhóm"
cost: "$0"
evidence: corpus
signal_level_when_pass: 4      # xếp theo cách của công thức này: dùng thật hoặc cam kết có ngày cụ thể ≈ mức 4 (tự khai bằng hành động). VALIDATE.md không có hàng riêng cho việc này; trả tiền thì đi s7 (mức 8)
tools: []
status: draft
---

## Dùng khi
Mình có một bản chạy được dù xấu và có đường vào một nhóm đúng khách (câu lạc bộ, server Discord, subreddit ngách, người theo dõi trên X, nhóm bạn đúng nhóm). Chưa có bản nào thì quay lại `s8-content-demand-test` hoặc `s7-preorder-buy-button`. Host Pat Walls nói test kiểu này khó nhưng đỡ mất thời gian build sai thứ (về Once). Công thức này **chưa hoàn thiện**: kho có 10 case nhưng mỗi case là một kiểu nhóm khác nhau (xem Thực tế), nên chưa có quy trình nào được lặp lại ở nhiều founder.

## Đầu vào
Một bản dùng thử (web xấu, TestFlight, một tính năng, mockup) và một nhóm cụ thể mà mình vào được trong ≤1 tuần.

## Các bước
1. **[manual] Chọn một nhóm có sẵn, gọi tên được.** Kho có ba kiểu: *dịp có sẵn* (Once: tiệc Halloween của bạn; Social Wizard: buổi homecoming với bạn học cấp ba), *cộng đồng ngách trực tuyến* (Algrow: server Discord; StageTimer: một subreddit ngách; Creator Buddy: khoảng 150 người theo dõi trên X), *người quen có chuyên môn* (CutCoach: câu lạc bộ đấu vật; Neurogum: đồng nghiệp ở Hulu; Oceans: bạn bè và người quen). Việc cụ thể ≤15 phút: viết tên nhóm, cách vào, ai là người đúng khách trong đó.
2. **[manual] Đặt mốc cam kết trước khi đưa bản thử.** Brian Shin (Once) đặt mốc trước khi viết dòng code: 10 sự kiện có ngày cụ thể đang dùng app, và nói tín hiệu cam kết của khách không nhất thiết là tiền. Đây là mốc của một founder, không phải của kho. Tự ghi mốc của mình vào một dòng, kèm ngày.
3. **[manual] Đưa bản chưa hoàn thiện và ngồi xem.** Once: bản web xấu, hay lỗi, in mã mời cho khách; Creator Buddy: gặp từng người, xem họ bấm vào đâu và gặp lỗi ở đâu; Algrow: chia sẻ màn hình dùng Algrow vài ngày liên tiếp trong voice chat, người trong server hỏi và Sam trả lời (Sam nói chỉ cần cái mình giải quyết chạy được thì ship gì cũng được); StageTimer: đăng bản free của một tính năng lên subreddit ngách, không ghi giá.
4. **[manual] Ghi hành vi, không ghi lời khen.** Ghi: ai dùng, ai quay lại, ai xin thêm, ai cam kết ngày. CutCoach đưa MVP cho câu lạc bộ đấu vật beta test, không ai dùng vì bản đầu bắt huấn luyện viên nhập kế hoạch; anh đổi concept. Bản thử bị bỏ cũng là dữ liệu.
5. **[manual] Hỏi một câu 'mua không'.** Oceans chào bạn bè và người quen với giá giảm thay vì chờ mọi thứ hoàn chỉnh (Ian Myers: thước đo của anh là ngày mai gọi một người, họ có mua không). Nếu nhóm dùng thật, đề nghị trả tiền ngay bằng `s7-preorder-buy-button`.
6. **[manual] Ghi kết quả** theo thang 0–8 của `VALIDATE.md` và quyết định.

## Đầu ra
Mỗi nhóm một dòng: nhóm (tên) · cách vào · bản đã đưa · số người dùng thật / quay lại / cam kết ngày · lời khen (đếm riêng, không tính) · mức tín hiệu 0–8 · việc làm tiếp.

## Ngưỡng qua
Ngưỡng cho từng mức nằm ở `VALIDATE.md`, không chép lại. Điều kiện riêng của công thức này: QUA khi số người đúng khách **dùng thật hoặc cam kết ngày cụ thể** đạt mốc mình đã ghi ở bước 2 (đề xuất, chưa có số của kho; Once chọn 10 sự kiện); lời khen không tính.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 11 step trong 10 video |
| Case (video, case) có step này | 10, trong đó 10 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 0/11 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 4/10 |
| Case full không nêu existing_audience | 9/10 |
| Case full video không kể bằng chứng nhu cầu trước launch | 3/10 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 8.0 tháng (6.0–24.0), n=7 |
| Kênh scale trả tiền / thuần organic / không nêu | 3 / 6 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s14-test-with-target-group.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Bằng chứng founder còn ít: 10 case full, 11 step, không có step nào chỉ do host mô tả. Theo trường nhu cầu của kho: không nêu 4, bạn bè khen 2, tự kể nỗi đau 2, trả tiền 1, build trước 1. Trong 10 case, 7 là người trong cuộc, 2 tự ghi không phải, 1 không nêu. Số tháng tới mức doanh thu hiện tại có n=7, không dùng để kết luận tốc độ.

## Bằng chứng từ kho
Mọi câu dưới đây là của founder hoặc host; câu của Pat Walls và Gus là host.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Brian Shin (founder) · `2026-05-10_i-built-a-20k-month-app-in-83-days` · 08:51 | "And the commitment metric of the client to signal validation doesn't always need to be payment." | founder nói (Once): tín hiệu cam kết của khách không nhất thiết là tiền |
| Pat Walls (host/expert) · `2026-05-10_i-built-a-20k-month-app-in-83-days` · 11:12 | "It sounds hard, but it will save you so much time not building the wrong thing." | lời của host: khó nhưng đỡ mất thời gian build sai thứ |
| Gus (host/expert) · `2026-05-10_i-built-a-20k-month-app-in-83-days` · 14:53 | "Instead of talking to people, I'm just going to build it." | bẫy (host): thay vì nói chuyện với người, mình chọn build luôn |
| Kelechi (founder) · `2025-10-28_my-2-apps-made-1-5m` · 02:52 | "this was probably the first time that my high school friends cared about anything I was working on" | founder kể (Social Wizard): bạn học ở buổi homecoming lần đầu quan tâm; đây là tín hiệu mức bạn bè, chưa phải khách trả tiền |
| Sam Adeniyi (founder) · `2026-01-14_i-built-a-14k-month-saas-using-discord` · 08:34 | "I think the main thing you have to do first is build maybe a bit of rapport in the community." | founder khuyên (Algrow): xây quan hệ trong cộng đồng trước khi đưa ra |
| Sam Adeniyi (founder) · `2026-01-14_i-built-a-14k-month-saas-using-discord` · 05:12 | "So as long as what you're trying to solve works I think you can ship anything." | founder nói (Algrow): chỉ cần cái mình giải quyết chạy được thì ship gì cũng được |
| Pat Walls (host/expert) · `2025-06-25_this-app-makes-25-000-month` · 13:47 | "I really like how he used Reddit to validate his idea cuz you don't need an audience" | lời của host về StageTimer: dùng subreddit để validate vì không cần audience |
| Lucas (founder) · `2025-06-25_this-app-makes-25-000-month` · 01:20 | "And the reason is I'm building something for people that I don't know." | founder kể (StageTimer): lý do anh phải thử là đang làm cho người mình không quen |
| Lucas (founder) · `2025-06-25_this-app-makes-25-000-month` · 02:55 | "it took me 224 days to actually get my first dollar. And that's totally okay." | bẫy về thời gian (StageTimer): mất 224 ngày mới có đô la đầu tiên |
| Ian Myers (founder) · `2025-03-08_i-quit-my-job-accidentally-built-a-10m-business` · 09:14 | "for me it was all about if I make this business can I call someone tomorrow and they'll buy it from me" | founder nói (Oceans): thước đo của anh là ngày mai gọi một người có mua không |
| Connor (founder) · `2025-12-17_this-23-yr-old-genius-makes-1myear-with-no-code-` · 00:11:39 | "I actually kind of went through a list of like maybe five ideas of different apps and I made some like Figma mock-ups for them." | founder kể (Payout): năm mockup Figma cho năm ý tưởng, để influencer chọn ý hợp khán giả của anh ta |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Lời khen của bạn bè là mức 1, vô nghĩa theo thang của `VALIDATE.md`.** Kelechi (Social Wizard) kể lần đầu bạn học cấp ba quan tâm tới việc anh làm; đó là phản ứng chứ chưa phải cam kết. 2 trong 10 case (Social Wizard, Once) được kho ghi là 'bạn bè khen'. Riêng Once, founder đặt mốc là cam kết có ngày cụ thể của người tổ chức sự kiện và coi đó là gần như tương đương một khoản thanh toán; ranh giới giữa 'khen' và 'cam kết có ngày' là lằn ranh công thức này dựa vào.
- **Nhóm 'có sẵn' không đồng nghĩa nhóm trả tiền.** Oceans chào bạn bè và người quen với giá giảm, ba khách đầu không lãi. Neurogum phát mẫu cho đồng nghiệp ở Hulu để nghe phản hồi: đó là người quen đáng tin, không phải khách mua. `VALIDATE.md` cổng 2.6 hỏi nhóm tiếp cận được có phải nhóm trả tiền không.
- **Dễ chọn build thay vì gặp người.** Gus nhận xét về Once: thay vì nói chuyện với người, mình chọn build luôn; công cụ AI làm việc đó dễ hơn.
- **Test tốt có thể giết bản đầu.** CutCoach: câu lạc bộ đấu vật không dùng, nên anh đổi concept và thiết kế lại. Đừng đọc đó là thất bại của công thức.
- **Mất thời gian dù chọn đúng nhóm.** Lucas (StageTimer) mất 224 ngày mới có đô la đầu tiên dù đã dùng Reddit để hỏi, và đang làm cho người anh không quen (bảng trên).
- **Không phải mọi thử nghiệm ở đây là đo nhu cầu của khách.** Payout (Connor) làm 5 mockup Figma cho influencer chọn ý hợp khán giả: đó là chọn ý, không phải khách thật dùng thử.
- **Con số trả tiền của Wrestle AI nằm ở app mẹ.** Fight AI đăng cùng bạn bè, khoảng $1.000 lãi ròng (transcript ghi lỗi, kho đọc là $1.000); app mẹ đã build xong, không phải trước build, và không phải bản của Wrestle AI.
- **Kho chỉ chứa người thắng.** 10 founder full lên được kênh. Người đưa bản thử cho nhóm rồi bị bỏ lơ và dừng lại không có mặt, nên 'dùng thật' ở đây là mẫu của người thắng.

## Quyết định
- **QUA** nếu số người đúng khách dùng thật hoặc cam kết ngày cụ thể đạt mốc đã ghi, và không chỉ là người quen khen: mức 4. Sang `s7-preorder-buy-button` để lên mức 8, hoặc `VALIDATE.md` cổng 4.
- **DỪNG** nếu cả nhóm không ai dùng lại hoặc cam kết, và lý do (như CutCoach) không sửa được bằng một lần đổi bản.
- **TEST THÊM** nếu có người dùng nhưng chưa đủ mốc: trong 7 ngày (đề xuất, chưa có số của kho) đưa bản sửa cho đúng những người đã dùng, rồi hỏi một câu 'mua không'.

## Cho solo founder bán global (từ VN)
- **Chép được:** các nhóm trực tuyến (Discord, subreddit, người theo dõi trên X): Algrow, StageTimer, Creator Buddy đều làm từ xa. StageTimer dùng Reddit và Pat Walls nhận xét là không cần audience.
- **Rào cản thật:** (a) kiểu 'dịp có sẵn' (tiệc, homecoming, câu lạc bộ ở thực địa) cần có mặt ở nơi đó, nên solo ở VN khó chép vì khách mục tiêu ở US. (b) Vào được một nhóm cộng đồng US cần xây quan hệ trước (Sam, Algrow: cần chút rapport trong cộng đồng), không nên vào chỉ để quảng cáo. (c) Người đứng ngoài ngách: trong 10 case, 7 là người trong cuộc, 2 tự ghi không phải, 1 không nêu (hai nhóm sau không gộp); bằng chứng cho người ngoài rất ít.
- **KHÔNG nên làm** nếu nhóm chỉ là bạn bè, gia đình hoặc người không thuộc nhóm trả tiền (kết quả là mức 1), hoặc nếu bản thử cần có mặt tại sự kiện ở nơi mình không ở.
