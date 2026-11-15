---
id: g14-press-pr
strategy: G14
title: "Báo chí, TV, PR miễn phí: nhận khi cơ hội đến, và gửi email lạnh cho nhà báo viết đúng đề tài"
label: manual                  # gửi email và theo dõi bằng tay; agent chỉ giúp lập danh sách nhà báo
time: "2 giờ dựng danh sách nhà báo và một bản pitch; gửi đều 2 tuần"
cost: "$0 (kho không nêu chi phí)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

> **Bằng chứng founder còn ít:** 4 case (đều full) và 1 step của host, từ 4 video. Kho không cho biết có bao nhiêu email đã gửi hay bao nhiêu nhà báo trả lời. Đọc như "ai đã được đưa tin và vì sao", không như quy trình.

## Dùng khi
Sản phẩm có điều mới lạ (công nghệ vừa ra, câu chuyện founder, chiến dịch gây quỹ) và mình muốn thêm một nguồn lượt vào miễn phí. PR **không thay** kênh phân phối đều (`g3`, `g2`), và kho không cho thấy nó lên lịch được. Nếu mục tiêu là người dùng trả tiền ngay, dùng `g1` hoặc `g9`.

## Đầu vào
Một câu "điều gì mới ở sản phẩm này mà nhà báo muốn kể", tên của founder (Ania ở Rootd nói đặt tên thật vào câu chuyện thì khán giả đồng cảm hơn), và 10 bài báo gần đây về cùng đề tài (số 10 là đề xuất, chưa có số của kho).

## Các bước
1. **[chrome] Lập danh sách ≥10 nhà báo đã viết về đề tài của mình (số 10 là đề xuất, chưa có số của kho)** (Rootd tìm người viết về sức khoẻ tâm thần, đọc rồi tìm email hoặc nhắn qua LinkedIn). Mỗi dòng: tên, bài đã viết, email.
2. **[manual] Viết một pitch ngắn** nói câu chuyện thật (founder nói về lý do làm), không nói tính năng. Rootd gửi cho nhà báo và phần lớn không ai trả lời, nhưng vài lần được đăng bài lớn (Cosmopolitan, Women's Health, Time theo lời founder).
3. **[manual] Gửi 2–3 email mỗi ngày trong 2 tuần,** ghi ai đã đọc hay trả lời. Số lượng này là đề xuất, chưa có số của kho (Rootd nói "a ton of work" nhưng không nêu số).
4. **[manual] Đón cơ hội đến sau một sự kiện.** NeuroGum được Time viết rồi được mời lên Dr. Oz sau chiến dịch crowdfunding; YourMove AI được báo lớn (WSJ, Washington Post, Fox Business) đưa tin vì sản phẩm AI mới lạ lúc đó, lượng khách từ PR ít nhưng cho domain authority; Flame bản đầu được TechCrunch đưa tin. Khi nhà báo hỏi, trả lời trong ngày.
5. **[manual] Gắn số đo:** link riêng hoặc mã riêng cho mỗi bài để biết lượt vào thật, vì YourMove nói lượng khách từ PR ít.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng "bài báo hoặc lần lên TV": mỗi dòng gồm ngày, nơi đăng, lượt vào, người dùng đăng ký và người trả tiền (nếu đo được), và có thêm quan hệ nào không.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 2 tuần, ≥1 nhà báo trả lời; sau 8 tuần, ≥1 bài đăng ở nơi có đúng khách của mình. PR là cơ hội, nên không có ngưỡng "phải qua". Nếu mục tiêu là xác nhận người trả tiền, quay về `VALIDATE.md` (cổng 1–4, thang 0–8).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 5 step trong 4 video |
| Case (video, case) có step này | 4, trong đó 4 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/5 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 2/4 |
| Case full không nêu existing_audience | 4/4 |
| Case full video không kể bằng chứng nhu cầu trước launch | 2/4 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 51.0 tháng (40.5–61.5), n=2 |
| Kênh scale trả tiền / thuần organic / không nêu | 1 / 3 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g14-press-pr.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Ba trong bốn case báo chí đến **sau một sự kiện hoặc vì sản phẩm mới lạ** (NeuroGum sau crowdfunding, YourMove, Flame); một case duy nhất là founder chủ động gửi email lạnh (Rootd, cũng có mặt ở `g12-outbound-b2b`). Trong 4 case: 3 insider và 1 outsider (Flame), không có case "không nêu" (câu truy vấn: `engine/recipes/g14-press-pr.extra.sql`). Cả 4 video là kênh có bán chương trình hoặc quảng bá (Starter Story, Superwall); chuyện NeuroGum do chính founder kể nhiều năm sau (survivor bias). Số tháng tới mức doanh thu hiện tại chỉ có ở 2/4 case.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Kho không có câu nguyên văn nói về cách gửi email cho nhà báo; phần đó nằm ở mô tả step (đã dẫn ở trên). Bảng chỉ giữ câu nói về điều kiện và hạn chế của PR.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Dmitri (YourMove AI) (founder) · `2026-01-04_he-had-nothing-until-he-built-a-stupid-simple-30` · 00:12:23 | "This was before most people had been exposed to AI, so most people that saw the product like were super excited about it." | founder kể: ra mắt trước khi hầu hết người dùng biết AI nên ai thấy sản phẩm cũng hào hứng (bối cảnh báo chí đưa tin) |
| Dmitri (YourMove AI) (founder) · `2026-01-04_he-had-nothing-until-he-built-a-stupid-simple-30` · 00:11:46 | "the honest answer um with this particular company is I I got lucky" | founder kể: tự nhận tăng trưởng của công ty này một phần là may mắn |
| An (Flame) (founder) · `2026-02-16_full-app-growth-guide-2026-how-to-make-viral-con` · 00:19:52 | "We had product conviction. We did not have distribution conviction." | founder kể: nhìn lại thì có niềm tin vào sản phẩm nhưng không có niềm tin vào phân phối (Flame bản đầu lên TechCrunch rồi retention ngày 30 chỉ 0,8% theo lời An) |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 4 founder được đưa tin và đủ thành công để lên kênh; không có số người gửi pitch mà không nhận được gì. Rootd tự nói phần lớn không trả lời.
- **Báo chí không thay phân phối.** Flame bản đầu được TechCrunch đưa tin và tăng trưởng organic mạnh trong tháng đầu, rồi retention ngày 30 chỉ 0,8% theo lời An; founder tự nói sau đó thiếu "distribution conviction" (câu ở bảng). Lượng khách từ PR của YourMove ít.
- **Một phần là may.** Dmitri (YourMove) tự nói tăng trưởng của công ty một phần là may mắn (câu ở bảng), và nói báo chí đến khi AI còn mới (câu ở bảng): điều kiện thời điểm không lặp lại được.
- **Một quan hệ có thể giúp ngoài PR.** Theo kho, lần lộ diện của NeuroGum trên Shark Tank (2019, không chốt được deal) mở đường cho quan hệ, và sau đó một nhà đầu tư của chương trình giúp họ trong vụ kiện nhãn hiệu (step và lợi thế ghi trong kho, do host kể lại): giá trị của việc lộ diện nằm ở quan hệ, không chỉ lượt vào.

## Quyết định
- **QUA** (để giữ làm một kênh phụ) nếu sau 8 tuần có ≥1 bài đăng ở nơi có đúng khách và lượt vào đo được (đề xuất, chưa có số của kho).
- **DỪNG** nếu gửi tới ≥30 nhà báo đúng đề tài mà 0 người trả lời (đề xuất, chưa có số của kho): đề tài không đủ mới hoặc pitch nói tính năng; dồn thời gian vào `g3` hoặc `g2`.
- **TEST THÊM** nếu có trả lời nhưng chưa đăng: thêm một góc "câu chuyện thật của founder", gửi lại cho 10 nhà báo khác trong 14 ngày.

## Cho solo founder bán global (từ VN)
- **Chép được:** gửi email cho nhà báo viết đúng đề tài, làm hoàn toàn từ xa; cá nhân hoá bằng câu chuyện thật. Gắn link riêng để đo.
- **Rào cản thật:** (1) nhà báo Mỹ/EU đọc ra ngay email dịch vụng; (2) câu chuyện "founder ở nước ngoài" có thể là điểm lạ, nhưng kho không có case nào kể như vậy; (3) TV và Shark Tank là sự kiện ở Mỹ, không lên kế hoạch được từ xa; (4) kho cho thấy báo chí thường đến sau một sự kiện, nên có sự kiện (ra mắt, gây quỹ, số liệu) mới có thứ để pitch.
- **KHÔNG nên làm** nếu sản phẩm chưa có gì mới để kể, hoặc nếu mục tiêu của tuần này là có người dùng trả tiền (đi `g1`, `g9`, `g3`); và đừng dồn thời gian chờ PR thay cho kênh đều.
