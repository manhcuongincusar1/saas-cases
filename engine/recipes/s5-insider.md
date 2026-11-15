---
id: s5-insider
strategy: S5
title: "Ý tưởng từ nỗi đau, nghề hoặc đam mê của chính mình (và nhánh khi mình không phải người trong cuộc)"
label: manual                  # không có bước nào chạy bằng máy: đây là phần của người, agent chỉ giúp liệt kê và kiểm
time: "2–3 giờ cho một lượt liệt kê và kiểm nhanh"
cost: "$0"
evidence: corpus
signal_level_when_pass: 3      # QUA đòi ≥3 người khác tả cùng nỗi đau (mức 4) và có người trả tiền cho thứ thay thế (mức 3): ghi 3, chưa phải mức 5 (comment hỏi mua)
tools: []
status: draft
---

## Dùng khi
Mình đã (hoặc có thể ngay) ở trong một nhóm khách: một nghề, một cộng đồng, một nỗi đau hằng ngày. Đây là cách founder trong kho nói họ tìm ý tưởng nhiều nhất. **Không dùng** khi mình đứng ngoài hầu hết ngách có tiền ở thị trường mình bán: sang **Nhánh B** bên dưới.

## Đầu vào
Ba danh sách tự viết, mỗi danh sách ≥5 dòng: (1) việc làm mình bực trong 30 ngày qua, (2) việc mình làm giỏi hơn người thường nhờ nghề hoặc kinh nghiệm, (3) nhóm/cộng đồng mình thật sự ở trong (không phải nhóm mình "thấy hay").

## Các bước (Nhánh A: mình là người trong cuộc)
1. **[manual] Liệt kê** theo ba danh sách. Mỗi dòng ghi: ai gặp việc này (mình + ai nữa), bao lâu một lần, hiện đang xử lý bằng gì.
2. **[manual] Lọc "người khác cũng đau":** với mỗi dòng còn lại, chạy `s3-reddit-pain-mining` hoặc `s4-tiktok-comment-mining` (mẫu dán ở các công thức đó). Cần thấy được người khác tả cùng nỗi đau bằng chữ của họ. Một người (là mình) chưa đủ.
3. **[manual] Hỏi "ai trả tiền?"** Có ai đang trả tiền cho giải pháp thay thế (app, dịch vụ, thuê người) không? Dùng `s1-revenue-spy` nếu là app. Sanskar (founder) tự dặn: nỗi đau phải có người trả tiền.
4. **[manual] Hỏi "đưa tới họ bằng đường nào, không tốn tiền?"** Founder Amazon-seller (Hassam) có nỗi đau và kiến thức ngách nhưng "zero audience means zero distribution". Nếu không nghĩ ra được đường organic (cộng đồng mình ở, một từ khoá, một định dạng video) thì ghi rõ là rủi ro.
5. **Ghi ứng viên** vào `journey/ideas/` (`status: inbox`) kèm: loại (nỗi đau / nghề / đam mê), bằng chứng ở bước 2–3, đường organic ở bước 4.

## Nhánh B: khi mình KHÔNG phải người trong cuộc
Đa số ngách US có tiền không phải của mình. Kho có 22 case full tự ghi là đứng ngoài nhóm khách (outsider); 47 case khác chỉ là video không nêu, không tính vào đây. Trong 22 case outsider, s5 vẫn xuất hiện 1 lần; phần còn lại đi bằng các lối dưới đây. Số bên cạnh là số case outsider có step tìm ý tưởng (find-idea) thuộc tactic đó (câu truy vấn: `engine/chapters/find.sql`, mục 8); một case có thể dùng nhiều lối:
1. **Bắt thay đổi mới** → `s12-timing-shift` (8 case).
2. **Nỗi đau của người khác** → `s13-others-pain-or-inbound` (6 case) và **chép/bản địa hoá một sản phẩm đã chạy** → `s11-copy-or-localize-proven` (5 case).
3. **Đọc comment TikTok/Instagram trong ngách** → `s4-tiktok-comment-mining` (4 case; kèm cảnh báo bằng chứng chủ yếu từ host ở công thức đó).
4. **Thu hẹp ngách** → `s9-niche-narrowing` (3 case) và **soi doanh thu** → `s1-revenue-spy` (3 case).
5. **Ghép với người trong cuộc** thay vì tự học ngách (chỉ 3 case: Wrestle AI có đồng sáng lập là influencer đấu vật, Clear 30 có đồng sáng lập là nhà tâm lý lâm sàng, Payout làm cùng một influencer). Payout tiếp cận qua một người quen chung. Việc làm cụ thể: viết danh sách 10 người đã ở sẵn trong ngách và có audience nhỏ, nhắn 3 người đầu với lời mời làm thử một bản. Ba case là rất ít; đây là lối ít bằng chứng nhất trong năm lối, đứng sau vì số, không phải vì nó tệ.

Thêm một lối đi lẻ chưa thành công thức: sống ở một nơi có nhóm bị bỏ sót (savvy-nomad: founder sống ở ngoài nước tự thấy người Mỹ là nhóm lớn nhất mà ít được phục vụ nhất; câu nguyên văn ở bảng bằng chứng). Chỉ một case.

## Đầu ra
Mỗi ứng viên một dòng: ý tưởng · loại (pain/nghề/đam mê, hay "nhánh B + cách ghép") · bằng chứng người khác đau (link) · ai trả tiền · đường organic · mức tín hiệu 0–8.

## Ngưỡng qua
Chỉ đưa vào `journey/ideas/` khi qua bước 2 (người khác cùng tả nỗi đau) VÀ bước 3 (có người đang trả tiền cho thứ thay thế). Ngưỡng chi tiết của từng tín hiệu nằm ở `VALIDATE.md` (cổng 1 và 2), không chép lại.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 94 step trong 90 video |
| Case (video, case) có step này | 92, trong đó 88 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 2/94 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 51/88 |
| Case full không nêu existing_audience | 72/88 |
| Case full video không kể bằng chứng nhu cầu trước launch | 44/88 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.0 tháng (5.0–30.0), n=53 |
| Kênh scale trả tiền / thuần organic / không nêu | 25 / 50 / 13 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s5-insider.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
Ghi chú: các câu **của host/expert** là lời khuyên, các câu **của founder** là việc họ kể. Hai loại được gắn nhãn rõ ở cột đầu.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| John (founder) · `2025-10-23_how-i-built-a-30k-month-mobile-app` · 02:39 | "For any developer, any idea you have has to be something that you a problem that you yourself have and if it works for you, there's a good chance it'll work for lots of other people." | nguyên tắc: ý tưởng là vấn đề chính mình có; chạy được với mình thì có khả năng chạy với nhiều người |
| Kian (founder) · `2026-06-14_the-first-app-i-ever-built-makes-25k-month` · 08:43 | "you understand and face the exact pain points that you're trying to solve without doing any market research." | lý do chọn: người trong cuộc hiểu và gặp đúng nỗi đau mà không cần nghiên cứu thị trường |
| Sebastian (founder) · `2025-06-21_how-i-built-it-15k-month-mobile-app` · 09:04 | "I will always be my first customer and so I always know exactly what's needed in the product" | lợi thế: founder là khách đầu tiên nên biết chính xác sản phẩm cần gì |
| Hassam (founder) · `2026-01-04_how-i-built-my-first-saas-without-an-audience-25` · 07:23 | "I felt like this project was successful over others because I had niche domain knowledge in the Amazon world." | kết quả: dự án thắng nhờ kiến thức ngách của chính founder (Amazon) |
| Hassam (founder) · `2026-01-04_how-i-built-my-first-saas-without-an-audience-25` · 03:44 | "But the thing is while I had this idea I also realized that I had zero audience and zero audience means zero distribution." | bẫy: nỗi đau riêng không tự sinh phân phối; founder vẫn không có audience |
| Thomas (founder) · `2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-th` · 05:30 | "Step one is to build in an area where you already have credibility." | bước 1 trong quy trình founder tự mô tả: làm ở lĩnh vực mình đã có uy tín |
| Thomas (founder) · `2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-th` · 05:45 | "Step two is to look for pain points instead of ideas." | bước 2 trong quy trình founder tự mô tả: tìm nỗi đau thay vì tìm ý tưởng |
| Paulius (founder) · `2025-05-24_i-built-an-app-with-cursor-made-30k-and-quit-my-` · 11:31 | "I think people underestimate the knowledge they already have." | nhắc kiểm kho tri thức sẵn có của chính mình trước khi đi tìm ngách mới |
| Sanskar (founder) · `2026-11-08_sanskar-30-micro-apps` · 08:28 | "Make sure whatever the problem you're solving there are people who can pay because this whole India hacking everything works only if there is revenue." | cổng sau s5: nỗi đau riêng phải có người sẵn lòng trả tiền (founder nói) |
| George (founder) · `2025-12-14_how-i-grew-my-mobile-app-to-17k-per-month` · 11:27 | "my co-founder is actually one of the biggest people in the wrestling influencing space" | nhánh không phải người trong cuộc: ghép với người đã ở trong ngách (đồng sáng lập là influencer đấu vật) |
| Asher (founder) · `2025-08-28_i-built-a-30kmo-app-that-helps-you-quit-smoking` · 00:02:00 | "Fred Munch, who's a clinical psychologist." | nhánh không phải người trong cuộc: đồng sáng lập là nhà tâm lý lâm sàng (Clear 30) |
| Connor (founder) · `2025-12-17_this-23-yr-old-genius-makes-1myear-with-no-code-` · 00:11:21 | "I reached out to Casper before I was friends with him and, you know, had a mutual connection." | nhánh không phải người trong cuộc: tiếp cận influencer qua người quen chung rồi làm app cùng (Payout) |
| Bo (founder) · `2026-05-21_i-make-1-7m-year-in-the-most-boring-niche-imagin` · 03:56 | "In that process, I kept seeing that Americans were the biggest, [music] most underserved group." | nhánh không phải người trong cuộc: tự thấy một nhóm bị bỏ sót khi đang sống ở ngoài nước |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Nỗi đau riêng không phải thị trường.** Mẫu hình hay gặp: founder bực một việc rồi build ngay, không kiểm người khác đau (bước 2). Trong kho, 46/88 case dùng s5 không kể bằng chứng nhu cầu nào trước launch. Có thể họ có mà video không kể, có thể họ không làm.
- **Kho chỉ chứa người thắng.** 88 founder dùng s5 và thành công đủ để lên kênh; số người dùng s5 mà thất bại không có trong kho.
- **Phân phối không đi kèm.** Hassam ở trên. Không audience là rủi ro kể cả khi mình hiểu ngách.
- **"Người trong cuộc" ở ngách nhỏ có thể nhỏ quá.** Xem cổng 1.5 `VALIDATE.md` (ngách siêu hẹp kẹt ~$10k/tháng).

## Quyết định
- **QUA** nếu ứng viên có ≥3 người khác tả cùng nỗi đau bằng chữ của họ (bước 2; ngưỡng "≥3" là đề xuất, chưa có số của kho), có người trả tiền cho cái thay thế (bước 3) và có một đường organic gọi được tên (bước 4). Khi đó ứng viên đạt mức tín hiệu 3 (có người trả tiền cho thứ tương tự) và 4 (người ta tự kể nỗi đau); sang `VALIDATE.md` cổng 1 để lấy mức 5 trở lên.
- **DỪNG** nếu chỉ có mình mình đau (bước 2 trắng) hoặc không ai trả tiền (bước 3 trắng).
- **TEST THÊM** nếu thiếu đúng một bước: trong 7 ngày làm bước thiếu (đăng 3 bài hỏi nỗi đau ở cộng đồng mình ở, hoặc tìm 2 sản phẩm thay thế có giá).

## Cho solo founder bán global (từ VN)
- **Chép được:** quy trình ba danh sách + bước 2–4. Không phụ thuộc vùng. Nhánh B bước 1 (ghép với người trong ngách) làm được từ xa qua DM/email/X.
- **Rào cản thật:** mình có thể không phải insider của ngách US trả cao (nhóm khách, ngôn ngữ, văn hoá). Đừng giả vờ. Trong kho, 117/186 case full là người trong cuộc và chỉ 22 tự ghi là đứng ngoài, nên s5 là con đường của số đông nhưng không nhất thiết là của mình. Với solo không audience, thanh kiểm "đường organic" (bước 4) quyết định hơn bước 1.
- **KHÔNG nên làm** nếu ngách nằm ở nơi mình không thể tiếp cận khách bằng chữ hoặc video (cần giọng bản xứ, cần có mặt, cần giấy phép) mà không có người trong ngách đi cùng.
