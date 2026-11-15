---
id: s12-timing-shift
strategy: S12
title: "Bắt một thay đổi vừa xảy ra (API, AI mới, sự kiện, trend) và làm ngay trên nó"
label: manual                  # đọc changelog, X, App Store bằng tay; agent hỗ trợ liệt kê
time: "1–2 giờ để lập bảng thay đổi; ship MVP ≤2 tuần"
cost: "$0 để tìm; chi phí build tuỳ thay đổi"
evidence: corpus
signal_level_when_pass: 1      # ra ứng viên; tín hiệu nhu cầu phải lấy tiếp ở chương VALIDATE
tools: []
status: draft
---

## Dùng khi
Mình không phải người trong ngách nào (nhánh B của `s5-insider`) và ship được nhanh. Thay đổi *vừa xảy ra* tạo khoảng trống chưa ai lấp, và người đi đầu thường chỉ cần ra mắt, chưa cần hơn người. Cửa sổ ngắn: kho có cả ví dụ thắng và ví dụ đóng cửa nhanh.

## Đầu vào
Một "bảng thay đổi 30 ngày": mỗi dòng là một thay đổi (API/tính năng nền tảng mới, khả năng AI mới, sự kiện, trend mạng xã hội, làn sóng cộng đồng).

## Các bước
1. **[manual] Lập bảng thay đổi.** Nguồn founder trong kho thật sự đi qua: changelog/API của nền tảng (iOS: AlarmKit; Instagram mở link; Notion ra API; Airtable mở marketplace; Gemini API), tính năng AI mới (upload ảnh của ChatGPT; Suno), sự kiện (Skype đóng; drama Product Hunt), trend trên TikTok/X (peptide; "ngày trong giấc mơ" nhờ ChatGPT). Mỗi dòng ghi ngày thay đổi.
2. **[manual] Đếm ai đã làm.** Tìm trên App Store/Product Hunt/X xem bao nhiêu sản phẩm đã ra trên thay đổi đó trong 30–60 ngày. Host Gus nói sau một thay đổi API thường có cả loạt app ra; số này cho biết mình còn trong cửa sổ hay không.
3. **[manual] Gắn một nỗi đau cụ thể, không gắn "công nghệ mới".** Câu hỏi của Ramsri (Question): việc thủ công nào đang có người trả tiền mà công nghệ mới giờ làm được? Denis (Yaphone) dùng nhu cầu có sẵn của người đang dùng Skype. Dòng nào chỉ có "thật thú vị" mà không có ai bực thì bỏ.
4. **[manual] Chọn một dòng làm được MVP trong ≤2 tuần.** Magic Music làm trong khoảng 4 ngày sau khi Suno ra; Yaphone dựng prototype trong một cuối tuần. Dài hơn thì cửa sổ có thể đã đóng.
5. **[manual] Kiểm đường organic và nhóm trả tiền.** Có từ khoá tìm kiếm cụ thể hoặc định dạng video đi kèm thay đổi đó không (`VALIDATE.md` cổng 1.3)? Nhóm trả tiền có phải nhóm tiếp cận được không?
6. **Ghi ứng viên** vào `journey/ideas/`: thay đổi, ngày, số người đã làm (bước 2), nỗi đau (bước 3), thời gian MVP.

## Đầu ra
Mỗi ứng viên một dòng: thay đổi + ngày · nỗi đau · ai trả tiền · số sản phẩm đã ra · thời gian MVP · đường organic · mức tín hiệu 0–8.

## Ngưỡng qua
Ngưỡng cho từng tín hiệu nằm ở `VALIDATE.md`. Riêng công thức này: ứng viên chỉ được vào chương VALIDATE khi có cả (a) một nỗi đau cụ thể và (b) MVP ≤2 tuần.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
Trong 34 step: 18 nhắc AI mới (ChatGPT, Gemini, Suno…) và 10 nhắc API/tính năng nền tảng/sự kiện cụ thể (đếm bằng từ khoá trên mô tả step, hai con số chồng lấn; câu truy vấn ở `engine/recipes/s12-timing-shift.extra.sql`). Theo năm video: 20 step ở video 2025, 14 ở 2026.

<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 34 step trong 32 video |
| Case (video, case) có step này | 32, trong đó 29 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/34 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 16/29 |
| Case full không nêu existing_audience | 25/29 |
| Case full video không kể bằng chứng nhu cầu trước launch | 15/29 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 13.5 tháng (6.3–30.0), n=16 |
| Kênh scale trả tiền / thuần organic / không nêu | 11 / 16 / 2 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s12-timing-shift.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Dom (founder) · `2025-10-21_i-made-1m-flipping-apps` · 06:50 | "the main difference between the projects is based on the trend you were running and the moment so basically the timing you know that's the main difference" | luật: khác biệt giữa các dự án là trend và thời điểm |
| Denis Yurchak (founder) · `2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month` · 08:02 | "It's a validated market which was first validated with the tweet by Peter levels I saw and then by sales I got from my Reddit post" | ví dụ: Skype đóng cửa; thị trường được kiểm bởi tweet kêu gọi rồi bởi doanh số từ một bài Reddit |
| Yasser (founder) · `2025-07-02_how-i-built-a-1m-business-in-117-days` · 01:35 | "I didn't do any validation or anything. I just like said if I don't do this someone else will." | ví dụ: làm ngay làn sóng ChatGPT, không validate; lý do 'nếu mình không làm người khác sẽ làm' |
| Yasser (founder) · `2025-07-02_how-i-built-a-1m-business-in-117-days` · 11:23 | "I was too worried that because everyone was saying it's like a chat GPT rapper. It's not going to work." | bẫy: ai cũng bảo chỉ là bản bọc ChatGPT sẽ không chạy |
| Gus (host/expert) · `2026-07-05_this-insanely-simple-app-makes-50k-month` · 16:46 | "look at changes to APIs that Apple or other platforms enable. Usually, there's a slew of apps that will get released when there is a new change in the API." | cách soi (host): theo dõi thay đổi API của Apple/nền tảng, sau đó có cả loạt app ra mắt |
| Pat Walls (host/expert) · `2025-08-23_how-i-finally-built-a-10k-month-saas-30-failures` · 05:15 | "reasons why businesses sometimes don't work or why projects fail is timing." | mặt trái (host): thời điểm cũng là lý do dự án chết |
| Nevo (founder) · `2026-07-30_how-postiz-went-from-17k-to-143k-month-in-4-mont` · 07:35 | "you should build before and then wait for the trend to happen" | biến thể: xây trước rồi chờ trend tới (Postiz) |
| Dan Kwon (founder) · `2025-10-26_he-made-22m-from-building-simple-apps-heres-how-` · 00:19:35 | "pretty much every product or project I've worked on has stemmed from some sort of momentum wave and an existing cult." | mẫu hình: sản phẩm nào cũng đi theo một làn sóng có sẵn cộng đồng |
| An (founder) · `2026-02-16_full-app-growth-guide-2026-how-to-make-viral-con` · 00:14:00 | "I did one big mistake though, Joseph, in this which you'll agree with. I focus on the product too much." | bẫy: ra sớm theo làn sóng nhưng sản phẩm yếu thì retention thấp (Flame AI) |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Đi sớm chưa chắc thắng.** Dmitri (yourmove-ai) làm trên Davinci-2, trước ChatGPT khi gần như chưa ai làm, nhưng theo kho là chưa chiếm được nhiều thị phần. Flame AI (câu nguyên văn ở bảng) retention thấp dù đi sớm.
- **Cửa sổ có thể đóng khi mình vào.** Host Pat nói timing là lý do dự án chết (bảng); Yasser nghe "chỉ là bản bọc ChatGPT" từ mọi người.
- **Không có validate nghĩa là không biết có nhu cầu hay không.** Yasser "didn't do any validation". Thành công của anh là mẫu từ kho người thắng. Kho không chứa người làm giống anh mà không thành.
- **Kho chỉ chứa người thắng.** 29 case full dùng s12 và lên được kênh; số người bắt đúng thay đổi mà không ra gì thì vắng mặt.
- **Phần lớn là AI/API; sẽ cũ nhanh.** Danh sách thay đổi ở bước 1 hết hạn theo tuần; công thức là *cách soi*, không phải menu.

## Quyết định
- **QUA** nếu có (a) nỗi đau cụ thể, (b) MVP ≤2 tuần (ngưỡng đề xuất, chưa có số của kho; lấy từ Magic Music ~4 ngày và Yaphone một cuối tuần), (c) số sản phẩm đã ra ở bước 2 không áp đảo (≥10 sản phẩm cùng việc trong 30 ngày là áp đảo, ngưỡng đề xuất, chưa có số của kho). QUA chỉ đưa ứng viên tới mức tín hiệu 1 (có ứng viên, chưa có bằng chứng bên ngoài); tín hiệu thật lấy ở `VALIDATE.md` cổng 1 và 2.
- **DỪNG** nếu chỉ có "công nghệ mới" không có nỗi đau, hoặc MVP cần >1 tháng, hoặc đã có sản phẩm làm đúng việc với doanh thu rõ.
- **TEST THÊM** nếu thiếu số ở bước 2: tìm trong 3 ngày; hoặc chạy `s8-content-demand-test` trên đúng nỗi đau đó.

## Cho solo founder bán global (từ VN)
- **Chép được:** bảng thay đổi 30 ngày và bước 2–4. Toàn bộ làm từ xa, không cần vùng, và đa phần chạy bằng code nhanh (hợp solo dev).
- **Rào cản thật:** cạnh tranh về tốc độ với founder ở US nghe tin sớm hơn hoặc có audience để ra mắt. Kho: nhiều case đi cùng một audience có sẵn hoặc cộng đồng đã ở đó (Dan Kwon: "momentum wave and an existing cult"). Solo không audience nên ghép với một kênh organic ngay từ bước 5.
- **KHÔNG nên làm** khi thay đổi cần giấy phép hoặc tuân thủ mà mình không thể có từ VN (thanh toán, y tế, tài chính), hoặc khi cả bảng thay đổi chỉ là "AI cho vui/hype" (`VALIDATE.md` cổng 1.4).
