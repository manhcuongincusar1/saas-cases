---
id: s10-customer-interviews
strategy: S10
title: "Nói chuyện hoặc thu phản hồi có chủ đích với khách: trước launch để tìm nỗi đau, sau launch để biết nhóm trả tiền và việc cần sửa"
label: manual                  # gọi, nhắn DM, gửi email: việc của người; agent chỉ giúp lập danh sách và tổng hợp ghi chú
time: "3–5 giờ để tìm và hẹn người; mỗi cuộc 15–30 phút"
cost: "$0; Fastlane tặng thêm quyền truy cập sản phẩm để đổi lấy cuộc gọi"
evidence: corpus
signal_level_when_pass: 6      # nhánh trước launch: QUA khi cùng một nỗi đau lặp lại qua nhiều cuộc (mức 6). Nhánh sau launch không cho mức nào, chỉ cho nhóm khách và việc cần sửa
tools: []
status: draft
---

## Dùng khi
Mình đã có vài người đúng nhóm khách để hỏi (từ audience, email list, người đã comment hay người dùng đầu tiên) và muốn biết nỗi đau có lặp lại không, hay họ dùng sản phẩm vì lý do gì. Chưa có người nào để nói chuyện thì quay lại `s8-content-demand-test` hoặc `s7-preorder-buy-button` trước. Host nói một cuộc nói chuyện 15 phút đáng giá hơn 70 app tự build, và Pat Walls nói builder cần ra khỏi hang để nói chuyện với người dùng (câu ở bảng bằng chứng; đây là lời khuyên của host). Công thức có **hai nhánh**: *trước launch* (tìm nỗi đau, ngay cả khi chưa có sản phẩm) và *sau launch* (hỏi người dùng thật).

## Đầu vào
Danh sách 5–10 người đúng nhóm khách, mỗi người một cách tiếp cận (tweet, subreddit, email, người đã comment; xem bước 1).

## Các bước, nhánh trước launch (tìm nỗi đau)
1. **[manual] Tìm 5–10 người đúng nhóm khách và nhắn từng người** qua tweet, subreddit hoặc email (Tibo kể playbook của mình: người không liên quan thì phản hồi không có giá trị; step này không gắn case nên là lời của người kể playbook, không phải việc đã đo). Việc cụ thể ≤15 phút: lập bảng ba cột (tên, nhóm, cách tiếp cận) và nhắn 3 người đầu. CodeGuide nhắn từng người đã comment hoặc đăng ký để hỏi họ đang xử lý nỗi đau bằng cách nào; Audio Pen nhắn từng người đã phản hồi để hỏi họ dùng vào việc gì.
2. **[manual] Hỏi về việc đã xảy ra, không hỏi về ý tưởng.** Fastlane hỏi theo sách The Mom Test: lần gần nhất đã giải quyết vấn đề thế nào và tốn bao nhiêu tiền hay thời gian. Floga hỏi khách cũ của sản phẩm vật lý về vấn đề mà không nói lý do hỏi.
3. **[manual] Mở một cửa để hẹn mà không cần múi giờ.** Fastlane thêm nút 'Book a call' ngay trong giao diện, ai đặt lịch được thêm 7 ngày truy cập, kết quả khoảng 20 cuộc mỗi tuần. Runafy nhắn riêng khoảng 20 early adopter qua WhatsApp và dùng poll story Instagram.
4. **[manual] Ghi lại câu nguyên văn và đếm lặp.** Super Demo nói chuyện với hơn 100 founder B2B SaaS, rồi kết luận nỗi đau chung là ghét làm demo. Voicy (Kourosh) thấy 60–70% người gọi là dân gõ nhanh muốn tăng năng suất, còn 20–30% là người khuyết tật hoặc người cao tuổi dùng và không đòi cải tiến: nhóm sau mới là nhóm 'thuốc giảm đau'.
5. **[manual] Khi không có kênh để gửi link**, build MVP rồi đưa thẳng cho người trong nhóm: Parakeet Chat không thu email được vì nhà tù khép kín nên đưa MVP cho liên hệ bên trong dùng thử.

## Nhánh sau launch (hỏi người dùng thật)
Dùng các step mà kho đánh dấu 'sau launch': Gravl để app miễn phí rồi thu bug và yêu cầu tính năng của người dùng đầu; Push Scroll lập Discord 3–4 nghìn thành viên để lấy feedback và bỏ phiếu A/B; Rootd phát hành MVP còn nhiều lỗi rồi nghe vài trăm người dùng đầu; BulkMockup gửi email onboarding hỏi khách muốn hướng dẫn về gì. Tibo dặn nói chuyện với người dùng mỗi ngày; Pat Walls khen BulkMockup vì anh thật sự nói chuyện với khách; Ania Wysocka (Rootd) dặn nghe người dùng thật kỹ vì câu trả lời nằm ở họ. Việc làm trong ≤15 phút/lần: gửi một email hai câu (số 10 người là đề xuất, chưa có số của kho) cho 10 người dùng gần nhất ('bạn dùng cho việc gì?', 'điều gì làm bạn khó chịu nhất?') và gom câu trả lời vào một bảng.
- Nhánh này không cho mức tín hiệu nhu cầu: nó cho nhóm khách thật và việc cần sửa. Quyết định trả tiền đã xảy ra rồi.
- Có thêm 5 step không đánh dấu nhánh (Canary hỏi follower, Voicy gọi user, Flame hỏi các cặp đôi, Letterly hỏi vì sao dùng app thay vì ChatGPT, BulkMockup làm support call); đa số chắc ở sau khi có người dùng nhưng kho không ghi, nên không tính vào nhánh nào.

## Đầu ra
Bảng mỗi cuộc một dòng: ai · nhóm · việc họ làm hiện tại · tốn bao nhiêu · trích một câu nguyên văn · có lặp với cuộc khác không. Cuối bảng: nỗi đau lặp lại nhiều nhất và số người nói; mức 0–8; việc làm tiếp (`s7` thu tiền thử, `s8` kiểm bằng nội dung).

## Ngưỡng qua
Số cuộc cần có (cổng 3 và mức 6) nằm ở `VALIDATE.md`, không chép lại. Điều kiện riêng của công thức này: ít nhất 2 trong số người nói cùng nỗi đau kể được cách họ đang trả tiền hay tốn thời gian cho nó (đề xuất, chưa có số của kho).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 21 step trong 18 video |
| Case (video, case) có step này | 17, trong đó 17 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 2/21 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 9/17 |
| Case full không nêu existing_audience | 14/17 |
| Case full video không kể bằng chứng nhu cầu trước launch | 6/17 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 18.0 tháng (3.0–24.0), n=9 |
| Kênh scale trả tiền / thuần organic / không nêu | 5 / 11 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s10-customer-interviews.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Tách theo nhánh (`engine/recipes/s10-customer-interviews.extra.sql`): **nhánh trước launch** là các step ở chặng validate, 10 step ở 9 case full (CodeGuide, Subscribr, Attention Design, Fastlane, Floga, Parakeet Chat, Audio Pen, Super Demo, Runafy). **Nhánh sau launch** là step có ghi chú 'sau launch': 4 step ở 4 case full (Gravl, Push Scroll, Rootd, BulkMockup). 5 step ở 5 case không rõ trước hay sau. 2 step không gắn case (cùng một video, Tibo kể playbook). Theo trường nhu cầu của kho, 17 case full có s10 gồm: không nêu 6, trả tiền 5, build trước 2, tự kể nỗi đau 2, view nội dung 1 và **chỉ 1 case ghi mức 6** (Super Demo, phỏng vấn lặp lại). Tức là phần lớn founder có nói chuyện với khách nhưng không dùng nó làm bằng chứng nhu cầu duy nhất; trong 5 case 'trả tiền', 4 case có step s7 (xem công thức đó) và case còn lại là Fastlane với bản beta trả phí. Số tháng tới mức doanh thu hiện tại có n=9, không dùng để kết luận tốc độ (nhánh trước launch chỉ có n=5).

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Câu của Pat Walls và Gus là host.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Host ẩn danh (host/expert) · `2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30` · 02:41 | "The information that you will get from one single 15minute conversation is more valuable than the 70 apps that you could build." | lời khuyên của host: một cuộc nói chuyện 15 phút đáng giá hơn 70 app tự build |
| Gaurav (founder) · `2026-08-30_the-insanely-obvious-secret-behind-this-69k-mont` · 10:31 | "Try DMing people on Twitter, and get on a call with them, even if you have to pay them" | founder khuyên (Fastlane): nhắn người trên Twitter và gọi, kể cả phải trả tiền cho họ |
| Pat Walls (host/expert) · `2026-08-30_the-insanely-obvious-secret-behind-this-69k-mont` · 10:01 | "talking to customers isn't the solution, but it is the mechanism to figuring out where to market." | lời của host: nói chuyện với khách là cơ chế để biết nên bán ở đâu, không phải lời giải |
| Pat Walls (host/expert) · `2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-p` · 17:56 | "Personally, I think the playbook's amazing, but the biggest piece that he talked about is the need for builders to get out of their shell, to get out of their cave, and talk to people." | lời của host: builder cần ra khỏi hang và nói chuyện với người dùng |
| Tibo (founder) · `2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-p` · 17:09 | "Talk to your user every day and understand their core situation." | founder khuyên (nhánh sau launch): nói chuyện với người dùng mỗi ngày để hiểu tình huống cốt lõi của họ |
| Kourosh (founder) · `2026-10-14_app-for-dad-18k` · 10:43 | "I think dictation tools to you and me are vitamins. They make us a little bit better. But, to the people that I'm serving, it's a painkiller." | founder kể kết quả các cuộc gọi user (Voicy, sau khi đã có người dùng): với nhóm anh phục vụ công cụ đọc chính tả là thuốc giảm đau, với người khác chỉ là vitamin |
| Gus (host/expert) · `2026-10-14_app-for-dad-18k` · 14:50 | "And if you're watching this, well, you need to talk to people that you want to potentially use your product." | lời của host: cần nói chuyện với đúng người mình muốn họ dùng sản phẩm |
| Jordan (founder) · `2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of` · 05:38 | "So, in this step, validating the idea and building the MVP were the same thing. I had to build the MVP, get it in front of them in order validate it." | founder kể (Parakeet Chat): vì nhà tù khép kín, build MVP rồi đưa liên hệ bên trong dùng thử, validate và build là một |
| Jordan (founder) · `2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of` · 07:11 | "Accept that you must validate and you must be willing to let your idea die." | founder khuyên: chấp nhận ý tưởng có thể chết khi validate |
| Pat Walls (host/expert) · `2026-02-11_how-i-built-a-12k-month-micro-saas` · 10:54 | "What I think is really special about what you do is that you actually talk to customers." | lời của host về BulkMockup: điểm đặc biệt là anh thật sự nói chuyện với khách (nhánh sau launch) |
| Gil (founder) · `2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-br` · 08:57 | "step one is you have to build an audience because if you don't have an audience, you don't have anyone to sell to." | bẫy: không có audience thì không có ai để bán hay nói chuyện (Subscribr dựng email list trước) |
| Ania Wysocka (founder) · `2025-08-31_this-app-made-over-1m` · 13:10 | "I would suggest that you listen to users very closely. They will have the answers you need." | founder khuyên (Rootd, nhánh sau launch): nghe người dùng thật kỹ vì câu trả lời nằm ở họ |
| Joseph (founder) · `2026-03-11_how-this-250k-month-saas-got-its-first-100-users` · 04:14 | "People hated creating product demos. People hated the sound of their own voice and that's when I realized hey, there's something to run with here." | founder kể (Super Demo): sau khi nói chuyện với hơn 100 founder B2B SaaS, kết luận người ta ghét làm demo và ghét giọng mình |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Không có ai để gọi.** Attention Design (Garb) kể mình không có kết nối trong ngách content creation, mở được ít cuộc nói chuyện, ít insight, và kết quả cả đợt thử là một người mua với $99. Bước 1 là chỗ kẹt, không phải bước hỏi. Gil (bảng trên) dựng email list hơn 1.000 người *trước* khi nhắn từng người.
- **Cuộc gọi không đủ để thu tiền.** Fastlane và Voicy dùng cuộc gọi để biết nhóm nào nên nhắm và nên bán ở đâu; Pat nói cuộc gọi là cơ chế biết nên bán ở đâu, không phải lời giải (bảng trên). Video cho thấy doanh thu ban đầu của Fastlane là bản beta trả phí; kho không tách phần nào do cuộc gọi.
- **Hỏi sai nhóm thì nhiễu.** Gus nói cần nói chuyện với đúng người mình muốn họ dùng sản phẩm. Tibo: nếu người đó không liên quan thì phản hồi, dù khen hay chê, không có giá trị. Voicy thấy 60–70% người gọi là nhóm 'vitamin' và đòi cải tiến, khác hẳn nhóm 20–30% 'thuốc giảm đau'; nếu nghe theo số đông thì đi sai.
- **Nhánh sau launch hay bị gọi nhầm là validate.** Các step 'sau launch' xảy ra khi người dùng đã tồn tại; chúng giúp sửa và chọn nhóm, không chứng minh nhu cầu trước khi build.
- **Kho chỉ chứa người thắng.** 17 founder full dùng s10 và lên được kênh. Người nói chuyện với khách rồi bỏ ý tưởng không có mặt, nên 'cuộc gọi dẫn tới sản phẩm' là mẫu của người thắng, không phải xác suất.
- **Phần nhỏ là playbook, không phải việc đã làm** (2/21 step không gắn case, đều của Tibo). Phần còn lại là việc founder đã làm; cách hỏi 'Mom Test' là do Fastlane kể theo sách, không phải đo trên kho.

## Quyết định
- **QUA** (nhánh trước launch) nếu cùng một nỗi đau lặp lại qua đủ số cuộc theo `VALIDATE.md` cổng 3 và có người nói cách họ đang trả tiền hoặc tốn thời gian: mức 6. Chuyển `s7-preorder-buy-button` để lên mức 8.
- **DỪNG** nếu mỗi cuộc ra một nỗi đau khác nhau, hoặc người nói chuyện không thuộc nhóm sẽ trả tiền (`VALIDATE.md` cổng 2.6). Jordan (Parakeet Chat) dặn phải chấp nhận ý tưởng có thể chết khi validate.
- **TEST THÊM** nếu chưa tìm được đủ người: trong 7 ngày (đề xuất, chưa có số của kho) làm bước 1 (nhắn 10 người) hoặc chạy `s8-content-demand-test` để có người comment rồi nhắn lại.

## Cho solo founder bán global (từ VN)
- **Chép được:** bước 1–4, làm bằng DM hoặc email, không cần gọi video. CodeGuide và Audio Pen làm bằng nhắn tin; nút 'Book a call' kèm quà truy cập của Fastlane giải bài toán hẹn lịch; poll và nhắn riêng của Runafy cũng bất đồng bộ.
- **Rào cản thật:** (a) tiếng Anh nói và múi giờ (xem `VALIDATE.md` mục rào cản VN: đặt lịch qua DM hoặc Reddit, hoặc cho thêm quota để đổi lấy một cuộc gọi); (b) người đứng ngoài ngách khó tìm người để gọi: trong 17 case full có s10, 4 tự ghi không phải người trong cuộc, 1 không nêu, 12 là người trong cuộc (hai nhóm 'không phải' và 'không nêu' không gộp); Attention Design là ví dụ trong nhóm khó. (c) Người US phản hồi cho người lạ cần có lý do để trả lời.
- **KHÔNG nên làm** nếu chỉ định gọi bạn bè, người thân hoặc người không thuộc nhóm trả tiền (kết quả sẽ giống mức 1 của thang tín hiệu, vô nghĩa), hoặc khi chưa có danh sách người cụ thể mà chỉ có ý định 'sẽ phỏng vấn'.
