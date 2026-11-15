---
id: s13-others-pain-or-inbound
strategy: S13
title: "Ý tưởng từ nỗi đau của người khác, hoặc từ một lời nhờ/lời mời đến tay"
label: manual                  # đọc hộp thư, DM, Reddit, comment bằng tay; agent chỉ giúp gom và đếm
time: "1–2 giờ cho một lượt gom; kiểm thêm 3 ngày"
cost: "$0"
evidence: corpus
signal_level_when_pass: 3      # QUA đòi nhiều người tả cùng nỗi đau và có người trả tiền cho thứ thay thế: mức 3-4 của thang (VALIDATE.md); ghi 3 vì chưa có comment hỏi mua
tools: []
status: draft
---

## Dùng khi
Mình không thuộc nhóm khách (nhánh B của `s5-insider`) nhưng có một nỗi đau nhìn thấy trực tiếp ở người khác, hoặc có một lời nhờ/lời mời nằm trong hộp thư của mình. Chọn `s5-insider` nếu mình chính là người đau; chọn `s11-copy-or-localize-proven` nếu thứ hấp dẫn là một sản phẩm đã chạy.

## Đầu vào
Nhánh A: 3–5 nỗi đau mình thật sự thấy hoặc được kể trong 30 ngày qua. Nhánh B: hộp thư, DM, comment, lời mời hợp tác 90 ngày gần nhất (khoảng thời gian là đề xuất, chưa có số của kho).

## Hai nhánh (phân loại tay của người viết theo mô tả step; câu truy vấn ở `engine/recipes/s13-others-pain-or-inbound.extra.sql`)
| Nhánh | Là gì | Số founder (case) | Ví dụ trong kho |
|---|---|---|---|
| A. Nỗi đau người khác quan sát hoặc được kể | bạn bè, người quen, một cảnh làm việc, một video thấy người khác gặp vấn đề | 5 (6) | Stagetimer (bạn ở studio dùng app Flash cũ), Parakeet Chat (bạn trong tù kể dịch vụ nhà tù đắt và tệ), DBLI (thấy người phồng mặt trên TikTok), Question.ai, Locked (hai video, cùng founder Evan) |
| B. Lời nhờ hoặc lời mời đến tay | người lạ xin giúp, tin nhắn, lời mời tài trợ, tweet viral, link ai đó gửi | 5 (6, gồm 1 case chỉ được nhắc) | Sheets Resume (người lạ xin xem CV trên Reddit), Payout (ý tưởng lấy từ lời mời tài trợ Casper đã từ chối), ScrapeCreators (follower gửi link tin rao bán), Fitted (sáu người bạn gửi một TikTok), Jungle (tweet viral), một bảng xếp hạng doanh thu xác minh (phản ứng với tweet của Peter Levels; chỉ được nhắc) |

Kho còn 1 step chỉ của host: một chủ e-commerce mang vấn đề đến một founder đã làm 5 năm một app không ai dùng.

## Các bước (Nhánh A: nỗi đau người khác)
1. **[manual] Ghi nỗi đau mình thấy** (≤15 phút): ai gặp, bao lâu một lần, họ đang dùng gì. Stagetimer: Lucas thấy bạn phải đứng dậy đi bấm nút ở phòng khác bằng app Flash cũ. Parakeet Chat: Jordan nghe người bạn trong tù kể về dịch vụ đắt và tệ.
2. **[manual] Đếm người khác tả cùng nỗi đau bằng chữ của họ**: chạy `s3-reddit-pain-mining` hoặc `s4-tiktok-comment-mining`. Host khen Lucas dùng Reddit để kiểm vì không cần audience (bảng).
3. **[manual] Hỏi "ai trả tiền và đang trả gì?"** Nhóm đó đang trả cho thứ thay thế nào (dịch vụ, app, người)? Nếu không có thì đây có thể là vitamin (`VALIDATE.md` cổng 1.2). Host nói về Locked: người ta trả tiền để giải quyết vấn đề, còn game thì chưa chắc.
4. **[manual] Đưa bản thô tới đúng nhóm đó, không phải bạn bè mình.** Jordan: kiểm ý tưởng và build MVP là một việc, đưa tới đúng người bị ảnh hưởng. Lucas nói thẳng là anh đang làm cho người anh không quen: bước này không thể bỏ.
5. **[manual] Gọi tên đường organic tới nhóm đó.** Parakeet Chat tăng trưởng bằng truyền miệng trong nhóm; không gọi được tên đường thì ghi là rủi ro.

## Các bước (Nhánh B: lời nhờ/lời mời đến tay)
1. **[manual] Gom** (≤15 phút): mở hộp thư, DM, comment 90 ngày gần nhất; gom mọi lời nhờ, câu hỏi lặp lại, lời mời, link người ta gửi. Casper duyệt 5 ý tưởng từ lời mời tài trợ đã từ chối; Colin để ý người lạ xin xem CV trên Reddit; Adrian nhận link tin rao bán từ một follower.
2. **[manual] Đếm người hỏi cùng một việc.** Một lời nhờ chưa phải nhu cầu. Sheets Resume: DB ghi Colin trả lời khoảng 20.000 câu hỏi về CV trên Reddit trong 6 năm.
3. **[manual] Làm thử không scale cho người hỏi.** Colin kể kiểm ý tưởng bằng cách làm cho người ta theo cách không bán hoặc không scale (bảng).
4. **[manual] Hỏi "người hỏi có phải nhóm trả tiền không?"** và gọi tên đường organic: ở nhánh B, đường này thường là chính kênh nhận lời nhờ (Reddit của Colin, kênh video của Casper).
5. **[manual] Kiểm xem lời nhờ của mình có đến nhờ audience hay không.** Trong 5 case full nhánh B, 3 nêu existing_audience (Payout, Sheets Resume, ScrapeCreators ở mức "một chút"); Fitted có co-founder với khoảng 50–60 nghìn follower. Solo chưa có hộp thư như vậy cần xem mục "Cho solo founder" bên dưới.

## Đầu ra
Mỗi ứng viên một dòng: nỗi đau hoặc lời nhờ (nhánh A/B) · số người tả cùng nỗi đau (link) · ai trả tiền và trả gì · đường organic · mức tín hiệu 0–8.

## Ngưỡng qua
Ngưỡng của từng tín hiệu nằm ở `VALIDATE.md` (cổng 1 và 2). Riêng công thức này: ứng viên vào chương VALIDATE khi có (a) ≥3 người khác tả cùng nỗi đau hoặc hỏi cùng một việc (đề xuất, chưa có số của kho), (b) có người đang trả tiền cho thứ thay thế, (c) đường organic gọi được tên.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 13 step trong 13 video |
| Case (video, case) có step này | 12, trong đó 11 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/13 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 5/11 |
| Case full không nêu existing_audience | 8/11 |
| Case full video không kể bằng chứng nhu cầu trước launch | 2/11 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 5.0 tháng (4.0–12.0), n=5 |
| Kênh scale trả tiền / thuần organic / không nêu | 7 / 4 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s13-others-pain-or-inbound.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Hai nhánh mỗi nhánh 5–6 case, nên chỉ là mô tả, không là xu hướng. Nhánh A: 5/6 case full tự ghi là outsider (đứng ngoài nhóm khách), 1 ghi insider (Locked ở một trong hai video; hai video của Locked ghi hai nhãn khác nhau). Nhánh B: 3 ghi insider, 1 ghi outsider (Scrape Creators, đã sửa 16/11 cho khớp), 1 không nêu; nhãn này không khớp định nghĩa "founder không thuộc nhóm khách", nên nhiều khả năng "insider" ở đó nghĩa là họ ở sẵn trong cộng đồng nơi lời nhờ đến (Reddit, creator, dev) chứ không phải trong nhóm khách. Tháng tới mức hiện tại quá ít (A: n=1; B: n=4, từ 2 đến 96 tháng), không đọc được. 10 founder khác nhau (Evan ở hai video, DB ghi tên hai cách), 11 case full.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Lucas (founder) · `2025-06-25_this-app-makes-25-000-month` · 01:20 | "And the reason is I'm building something for people that I don't know." | bẫy/hiện trạng (nhánh nỗi đau người khác): Stagetimer, founder tự nói đang làm cho những người anh không quen |
| Pat Walls (host/expert) · `2025-06-25_this-app-makes-25-000-month` · 13:47 | "I really like how he used Reddit to validate his idea cuz you don't need an audience" | lời khuyên của host: Lucas dùng Reddit để kiểm ý tưởng vì không cần có audience |
| Evan (founder) · `2026-06-07_the-14-year-old-who-built-a-14kmonth-ai-app` · 00:27:00 | "If you want to speed run to $10,000 a month, think of a problem that you or others face." | founder nói (nhánh nỗi đau người khác, Locked): nếu muốn chạy nhanh tới 10k/tháng thì nghĩ vấn đề mình hoặc người khác gặp |
| Joseph Choi (host/expert) · `2026-06-07_the-14-year-old-who-built-a-14kmonth-ai-app` · 00:26:35 | "Cuz people are willing to pay to solve problems, whereas something like this where it's like a game, it's not really solving a problem necessarily." | lời của host: người ta trả tiền để giải quyết vấn đề, còn app kiểu game thì chưa chắc giải quyết vấn đề (Locked) |
| Jordan (founder) · `2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of` · 05:38 | "So, in this step, validating the idea and building the MVP were the same thing. I had to build the MVP, get it in front of them in order validate it." | founder kể (Parakeet Chat, nỗi đau từ người quen trong tù): kiểm ý tưởng và build MVP là một việc, đưa tới đúng người đó |
| Jordan (founder) · `2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of` · 07:11 | "Accept that you must validate and you must be willing to let your idea die." | founder nói: chấp nhận phải kiểm và để ý tưởng chết |
| Jordan (founder) · `2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of` · 07:58 | "Lots of people who like these products want to talk about it. So, it's all word of mouth." | founder kể: tăng trưởng của Parakeet Chat là truyền miệng trong nhóm khách |
| Colin (founder) · `2025-01-22_how-i-built-it-20k-month-ai-app-as-a-non-technic` · 07:09 | "first validate the idea by doing it for people in a way that either isn't for sale or doesn't scale" | founder kể (Sheets Resume, lời nhờ từ người lạ trên Reddit): kiểm ý tưởng bằng cách làm cho người ta theo cách không bán hoặc không scale |
| Casper (founder) · `2026-03-15_the-stupid-simple-content-strategy-thats-making-` · 00:13:10 | "they're paying me to experiment on which ideas work well for them." | founder kể (Payout, lời mời tài trợ đến tay): các thương hiệu trả tiền để Casper thử ý tưởng nào hợp với họ |
| Casper (founder) · `2026-03-15_the-stupid-simple-content-strategy-thats-making-` · 00:05:20 | "I'm always like that towards ideas where it's like if it's low input on my end to build out, and it's very easy to just say yes" | founder kể (Payout): ý tưởng nào ít công build và dễ nói có thì Casper nhận |
| Julian Alvarez (founder) · `2025-11-02_this-ai-study-app-makes-100kmo-heres-how-no-code` · 00:03:17 | "We had like 3 months of runway and we needed something that would work right now basically." | founder kể (Jungle, ý từ tweet viral): chỉ còn ba tháng runway nên cần thứ chạy ngay |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Nhánh B chủ yếu chạy nhờ audience có sẵn.** Casper có khoảng 9 triệu follower trước khi có app (DB). Colin hỏi đáp CV trên Reddit nhiều năm. Một solo không có hộp thư như vậy khó có lời nhờ để gom; kho không có case nào tạo ra lời nhờ từ con số không.
- **Nhánh A: tin người quen không phải đo nhu cầu.** Lucas nói thẳng anh làm cho người anh không quen (bảng). 5/6 case nhánh A có kể một loại bằng chứng nhu cầu, nhưng loại đó là tự khai hoặc danh sách chờ miễn phí (3), đã build trước (1) hoặc lượt xem nội dung (1); không case nào kể có người trả tiền trước. Locked là game hoá (host hỏi game có giải quyết vấn đề không).
- **Một lời nhờ lẻ hoặc một tweet viral dễ thành ý tưởng "thú vị".** Jungle lấy ý từ tweet viral vì chỉ còn ba tháng runway (bảng); video không nêu họ kiểm trước. Trust the Mual là phản ứng với một tweet và chỉ được nhắc.
- **Kho chỉ chứa người thắng.** 11 case full, 10 founder; số người nghe một lời nhờ rồi build mà không ra gì vắng mặt. "Không nêu" ≠ "không có": 3/11 không kể bằng chứng nhu cầu.

## Quyết định
- **QUA** nếu có đủ (a)(b)(c) ở Ngưỡng qua. Sang `VALIDATE.md` cổng 1 và 2.
- **DỪNG** nếu chỉ có một người kể (một lời nhờ, một bạn) mà không ai khác tả, hoặc không ai trả tiền cho thứ thay thế.
- **TEST THÊM** nếu thiếu đúng một điều kiện: trong 7 ngày (đề xuất, chưa có số của kho) đăng 3 bài hỏi ở nơi nhóm khách ngồi hoặc tìm 2 sản phẩm thay thế có giá.

## Cho solo founder bán global (từ VN)
- **Chép được:** nhánh A bước 1–5, làm từ xa bằng Reddit, TikTok, review; không cần audience. Đây là nhánh hợp solo không audience.
- **Rào cản thật:** nhánh B phụ thuộc kênh nhận lời nhờ, mà solo mới thường không có; cách gần nhất trong kho là Colin giúp người lạ công khai trên Reddit trong nhiều năm, không nhanh. Nhóm khách global trả cao có thể khác văn hoá và ngôn ngữ so với bạn bè mình; nỗi đau "thấy ở bạn" ở VN chưa chắc là nỗi đau của nhóm khách US/EU.
- **KHÔNG nên làm** nhánh B khi không có hộp thư hoặc audience để lời nhờ đến (đừng giả lập), và không nên làm nhánh A nếu nỗi đau chỉ có ở nhóm mình không tiếp cận được bằng chữ hoặc video.
