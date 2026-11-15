---
id: s15-idea-filter-criteria
strategy: S15
title: "Lọc ý tưởng bằng bộ tiêu chí viết sẵn (bằng chứng founder còn ít)"
label: manual                  # tự viết tiêu chí và chấm tay; không có công cụ
time: "≤1 giờ cho một danh sách ứng viên"
cost: "$0"
evidence: corpus
signal_level_when_pass: 1      # QUA chỉ là ứng viên đã qua bộ lọc của chính mình; chưa có tín hiệu bên ngoài
tools: []
status: draft
---

> **Bằng chứng founder còn ít: 3 founder, 3 step, 1 case gắn doanh thu.** Đây là công thức mỏng; dùng như một danh sách tiêu chí để tham khảo, không như một phương pháp đã kiểm.

## Dùng khi
Mình đã có 3–10 ứng viên từ `s5-insider`, `s11-copy-or-localize-proven`, `s13-others-pain-or-inbound` hoặc nguồn khác và cần loại bớt trước khi chạy `VALIDATE.md`. Không dùng để tìm ý tưởng.

## Đầu vào
Danh sách ứng viên, mỗi dòng một câu mô tả; một bộ 3–6 tiêu chí do mình viết trước khi nhìn ứng viên (bước 1; con số 3–6 là đề xuất, chưa có số của kho: Erikas dùng 3, Nico dùng 4).

## Các tiêu chí từng founder dùng (theo mô tả step trong DB; câu truy vấn ở `engine/recipes/s15-idea-filter-criteria.extra.sql`)
| Founder | Tiêu chí | Ghi chú |
|---|---|---|
| Erikas (Kaching Bundles, app Shopify; video của host Pat Walls) | (1) làm xong trong vài tháng, không hơn; (2) thị trường rộng, hữu ích cho mọi cửa hàng Shopify; (3) ít cạnh tranh | step gắn case; anh nói thị trường rộng giúp marketing dễ hơn và tận dụng khách Shopify sẵn có của anh |
| Nico (17 app, bán 2 app; video của host Pat Walls) | (1) giá trị với người khác: họ có coi đây là vấn đề đáng giải hay chỉ là bất tiện nhỏ; (2) quy mô: đủ nhiều người muốn; (3) kỹ năng: mình tự làm được; (4) phân phối: có cách tiếp cận khách mà có lời | step không gắn case; mô tả chung cách anh lọc |
| Mike (3 SaaS, playbook) | một bộ lọc phủ định: không làm business phụ thuộc AI hoặc API mình không kiểm soát (rủi ro nền tảng); ý tưởng anh còn cân nhắc là công cụ documentation | step không gắn case; ở mốc khác anh còn khuyên chọn ý tưởng đã có người làm (bảng bằng chứng) |

Chồng lấn giữa ba người: "thị trường đủ rộng" có ở Erikas và Nico (2/3); "dễ làm/mình làm được" ở Erikas (về thời gian build) và Nico (về kỹ năng), hai nghĩa gần nhau nhưng không giống; "ít cạnh tranh", "rủi ro nền tảng", "đường tiếp cận khách" mỗi cái chỉ có một người. Không tiêu chí nào có cả 3.

## Các bước
1. **[manual] Viết tiêu chí trước khi nhìn ứng viên** (≤15 phút): chọn 3–6 từ bảng trên, ghi mỗi tiêu chí là câu hỏi có/không và bằng chứng nào sẽ trả lời nó (link, số).
2. **[manual] Chấm từng ứng viên** (≤15 phút): có/không cho mỗi tiêu chí, kèm bằng chứng. Nico hỏi người khác có coi đó là vấn đề đáng giải không: ở bước này chỉ dựa trên thứ đã nhìn thấy, đừng bịa số.
3. **[manual] Loại ứng viên vi phạm tiêu chí phủ định**, nếu mình chọn (kiểu Mike: phụ thuộc AI/API ngoài tầm kiểm soát).
4. **[manual] Đối chiếu hai tiêu chí đối lập về cạnh tranh.** Erikas lọc "ít cạnh tranh", còn Mike khuyên chọn ý tưởng đã có người làm; host còn nói Shopify là nền tảng đã trưởng thành. Kho không có luật chọn giữa hai hướng: ghi lựa chọn của mình và lý do; tiền ngay cạnh và độ đông của bản sao nằm ở `VALIDATE.md` cổng 1.1 và 2.9.
5. **Ghi ứng viên còn lại** vào `journey/ideas/` kèm bảng chấm, rồi chạy `VALIDATE.md` cổng 1.

## Đầu ra
Mỗi ứng viên một dòng: ý tưởng · bảng có/không theo tiêu chí · bằng chứng · còn hay loại · mức tín hiệu 0–8.

## Ngưỡng qua
Không có số của kho. Đề xuất, chưa có số của kho: ứng viên chỉ còn lại nếu qua mọi tiêu chí mình đã viết ở bước 1; ngưỡng tín hiệu thật nằm ở `VALIDATE.md`.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 3 step trong 3 video |
| Case (video, case) có step này | 1, trong đó 1 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 2/3 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 0/1 |
| Case full không nêu existing_audience | 1/1 |
| Case full video không kể bằng chứng nhu cầu trước launch | 0/1 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | — tháng (—–—), n=0 |
| Kênh scale trả tiền / thuần organic / không nêu | 0 / 1 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s15-idea-filter-criteria.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Ba step, ba video, ba founder khác nhau: hai người (Nico, Mike) nói cách họ lọc nói chung, một người (Erikas) gắn với một sản phẩm cụ thể (doanh thu tự ghi khoảng 400 nghìn USD MRR). Kho không có số người dùng bộ lọc mà vẫn thất bại; và không có số tiêu chí nào dự đoán thành công.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Các tiêu chí ở bảng trên lấy từ mô tả step của DB (các mốc 04:44 của Erikas, 04:26 của Nico, 10:15 của Mike), không phải câu trích nguyên văn.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Nico (founder) · `2025-03-31_i-locked-myself-in-a-room-made-17-apps-sold-2-fo` · 04:58 | "most of the successful ideas I had came to me like organically in a sense that I needed that for myself" | founder kể: bốn tiêu chí lọc của anh, nhưng ý thành công nhất của anh đến một cách tự nhiên từ nhu cầu của chính mình |
| Nico (founder) · `2025-03-31_i-locked-myself-in-a-room-made-17-apps-sold-2-fo` · 09:34 | "I didn't start ads right at the start so I first tried to validate the ID organically" | founder kể: sau khi lọc, anh kiểm ý tưởng bằng cách organic trước khi chạy quảng cáo |
| Erikas (founder) · `2025-04-19_my-apps-make-4-5m-year-with-0-marketing` · 02:54 | "So that's how I kind of knew that there is an opportunity for me to be in that ecosystem and to try to beat all of those solid developers." | founder kể (Kaching Bundles): lý do vào hệ sinh thái Shopify; anh còn nói muốn đánh bại các developer vững, nên 'ít cạnh tranh' không có nghĩa là không có đối thủ |
| Erikas (founder) · `2025-04-19_my-apps-make-4-5m-year-with-0-marketing` · 05:31 | "Before building it, I tried to validate it with basically talking to users." | founder kể: sau bộ lọc ba tiêu chí, anh kiểm bằng cách nói chuyện với người dùng trước khi build |
| Pat Walls (host/expert) · `2025-04-19_my-apps-make-4-5m-year-with-0-marketing` · 06:48 | "In other words, that means there's a good amount of competition on the platform." | lời của host: hệ sinh thái Shopify khá trưởng thành, nghĩa là có nhiều cạnh tranh trên nền tảng; đối chiếu với tiêu chí ít cạnh tranh của Erikas |
| Mike (founder) · `2025-11-02_i-built-3-saas-apps-to-200k-mrr-heres-my-exact-playb` · 06:02 | "pick an idea that's been done before. New ideas are risky." | lời khuyên của founder Mike (không phải một case): chọn ý tưởng đã có người làm; đối lập với tiêu chí ít cạnh tranh của Erikas |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Bằng chứng mỏng.** 3 founder; câu "tiêu chí này đúng" không có số đỡ. Kho chỉ chứa người thắng nên không có người lọc bằng đúng các tiêu chí này mà thất bại.
- **"Ít cạnh tranh" không đồng nghĩa không có đối thủ.** Erikas chọn tiêu chí này nhưng cũng nói muốn đánh bại các developer vững (bảng), và host mô tả Shopify là nền tảng đã khá trưởng thành.
- **Ý thành công nhất của Nico đến từ nhu cầu của chính anh** (bảng), nên bộ lọc của anh có thể chỉ giải thích sau khi chọn; kho không phân biệt được.
- **Bằng chứng nhu cầu của Kaching Bundles yếu hơn tên gọi.** Trong DB, "comment có ý định mua" thực ra là comment hỏi chỗ tải một app miễn phí, không phải hỏi mua.

## Quyết định
- **QUA** nếu ứng viên qua mọi tiêu chí đã viết ở bước 1. Sang `VALIDATE.md` cổng 1.
- **DỪNG** nếu vi phạm một tiêu chí phủ định, hoặc bằng chứng cho một tiêu chí là trống.
- **TEST THÊM** nếu chỉ thiếu một bằng chứng: bổ sung trong 3 ngày (đề xuất, chưa có số của kho).

## Cho solo founder bán global (từ VN)
- **Chép được:** cách viết tiêu chí trước rồi chấm sau; làm hoàn toàn từ xa. Hai tiêu chí về "mình tự làm được" và "đường tiếp cận khách mà có lời" đặc biệt hợp solo không audience.
- **Rào cản thật:** hai trong ba founder lọc dựa trên thứ họ đã có (khách Shopify sẵn có của Erikas; kỹ năng của Nico); solo mới phải tự viết lại tiêu chí theo thứ mình thật sự có, không chép nguyên.
- **KHÔNG nên làm** nếu danh sách ứng viên chưa có bằng chứng nào (chưa qua `s3`/`s4`/`s1`); khi đó bộ lọc chỉ lọc ý kiến của chính mình.
