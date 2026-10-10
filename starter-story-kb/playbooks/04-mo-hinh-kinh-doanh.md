# Playbook 4 — CHỌN MÔ HÌNH KINH DOANH

> Ba playbook trước trả lời *xây gì*, *có ai cần không*, *bán thế nào*.
> Playbook này trả lời câu hỏi đến trước tất cả: **loại doanh nghiệp nào hợp với hoàn cảnh của tôi.**
>
> Toàn bộ số liệu dưới đây tính từ 180 case trong kho, truy vấn trực tiếp từ `data/cases.csv`.
> Cột "khả thi VN" và "độ khó" là đánh giá của tôi trên thang 1–5 khi viết từng case.

## 1. Bức tranh toàn cảnh

| Nhóm mô hình | Số case | Doanh thu trung vị/tháng | Khả thi VN | Độ khó |
|---|---:|---:|---:|---:|
| SaaS / micro-SaaS | **72** | 38.500 USD | 3,7 | 3,2 |
| App di động | **43** | 30.000 USD | 3,7 | 2,9 |
| Dịch vụ đóng gói / agency | 12 | **158.000 USD** | 3,3 | 3,4 |
| Nội dung / media | 10 | 83.000 USD | **2,8** | 3,4 |
| Danh mục nhiều doanh nghiệp | 5 | 72.000 USD | 3,0 | 3,2 |
| Sản phẩm số / tri thức | 3 | 125.500 USD | **4,0** | **2,3** |
| Thương mại điện tử | 2 | rất cao | **2,0** | **4,5** |

**Ba điều bảng này nói ra ngay:**

**a) Doanh thu trung vị của dịch vụ đóng gói cao gấp bốn lần SaaS — nhưng đừng đọc vội.**
Agency có biên lợi nhuận **30–35%** ([StoryArb](../videos/2023-11-02_the-multipreneur-hes-building-a-10m-portfolio-of-inc/case.md)),
trong khi micro-SaaS thường **85–99%**. Quy về lợi nhuận: 158.000 × 32% ≈ **50.000 USD**,
so với 38.500 × 90% ≈ **35.000 USD**. Vẫn cao hơn, nhưng là 1,4 lần chứ không phải 4 lần —
và bạn phải quản lý người.

Ngoại lệ quan trọng: [DesignJoy](../videos/2023-05-17_i-make-1-3m-year-with-one-skill/case.md)
làm dịch vụ đóng gói **một mình**, chi phí 176 USD/tháng, biên gần như 100%. Đây là ô tốt nhất
trong toàn bộ bảng — nhưng nó đòi hỏi một kỹ năng bạn làm **nhanh**, không chỉ làm được.

**b) Sản phẩm số/tri thức có tỷ lệ giá trị trên độ khó tốt nhất** — khả thi VN cao nhất (4,0),
độ khó thấp nhất (2,3), doanh thu trung vị 125.500 USD. Nhưng mẫu chỉ có 3 case, và cả ba
đều **bán kinh nghiệm đã tích luỹ nhiều năm** — [Thomas Frank](../videos/2024-04-18_i-made-2-5m-selling-a-digital-product/case.md)
có 3 triệu subscriber trước khi bán template đầu tiên. Mô hình này **kiếm tiền từ khán giả đã có**,
nó không phải cách xây khán giả.

**c) Thương mại điện tử có khả thi VN thấp nhất (2,0) và khó nhất (4,5).**
Vốn tồn kho, chuỗi cung ứng, kho vận, đổi trả — và [Tabs Chocolate hết hàng nhiều tháng hơn số tháng có hàng](../videos/2023-06-07_i-make-11m-year-selling-one-product/case.md)
dù doanh thu triệu đô. Nút thắt là **vốn lưu động**, không phải marketing.

## 2. Câu hỏi quyết định: chi phí biên của bạn tăng theo cái gì?

Đây là câu hỏi phân loại quan trọng nhất, và nó quyết định mọi thứ phía sau: giá, kênh, tốc độ,
và cả việc bạn có ngủ được không.

| Chi phí biên tăng theo | Ví dụ trong kho | Biên | Hệ quả |
|---|---|---:|---|
| **Không tăng theo gì cả** | [Cursor Directory](../videos/2025-11-16_my-website-makes-35k-month-built-in-3-hours/case.md), [template Notion](../videos/2024-04-18_i-made-2-5m-selling-a-digital-product/case.md) | 99% | bán thêm không tốn gì — freemium an toàn |
| **Số job/lượt gọi** | [Data Fetcher](../videos/2025-08-13_how-i-built-it-23k-month-micro-saas/case.md) hosting 2.500 USD | 85% | giá phải gắn với hạn mức dùng |
| **Token AI** | các app AI trong kho | 70–75% | **freemium là tự sát** — user free ngốn tiền thật |
| **Máy chủ render** | [ScreenshotOne](../videos/2024-11-22_how-i-built-it-12k-month-micro-saas/case.md) 3–4K USD | **40–60%** | cần vốn lưu động, MRR không phải thu nhập |
| **Giờ người** | agency, dịch vụ có nhân viên | 30–35% | mỗi khách mới cần thêm người |
| **Tiền quảng cáo** | [Letterly](../videos/2025-11-24_how-he-makes-250k-per-month-from-a-simple-app-letter/case.md) 200K/250K | **~6%** | tắt tiền là tắt khách |
| **Hàng tồn kho** | thương mại điện tử | thay đổi | doanh thu triệu đô, dòng tiền tự do ≈ 0 |

**Cách dùng bảng này:** trước khi chọn mô hình, hãy trả lời *khi tôi có thêm một khách hàng,
tôi tốn thêm bao nhiêu?* Nếu bạn không trả lời được con số đó, **bạn chưa được phép định giá**.

Đây là lý do [ScreenshotOne công bố biên 40–60%](../videos/2024-11-22_how-i-built-it-12k-month-micro-saas/case.md)
đáng tin hơn phần lớn case khoe 90% — vì founder biết chính xác mỗi ảnh chụp tốn bao nhiêu.

## 3. Bảng chọn theo hoàn cảnh của bạn

| Hoàn cảnh của bạn | Mô hình hợp nhất | Vì sao | Case tham chiếu |
|---|---|---|---|
| Biết code, không có khán giả, không có vốn | **Micro-SaaS trên marketplace** | marketplace là kênh phân phối miễn phí; khả thi VN cao nhất (4,4) | [Data Fetcher](../videos/2025-08-13_how-i-built-it-23k-month-micro-saas/case.md), [NotionForms](../videos/2024-11-07_how-i-built-it-37k-month-notion-app/case.md) |
| Có một kỹ năng làm **nhanh**, không có vốn | **Dịch vụ đóng gói một mình** | thu tiền từ tuần đầu, chi phí gần bằng 0 | [DesignJoy](../videos/2023-05-17_i-make-1-3m-year-with-one-skill/case.md) |
| Có chuyên môn ngành, kiên nhẫn nhiều năm | **Nội dung + sản phẩm số** | biên cao nhất, nhưng chậm nhất | [Swim University](../videos/2024-05-04_i-turned-one-website-into-1m-year/case.md) |
| Biết code, chịu được 12% tỷ lệ thắng | **Danh mục app di động** | độ khó thấp nhất (2,9), thử được nhiều lần | [HabitKit](../videos/2025-06-21_how-i-built-it-15k-month-mobile-app/case.md) |
| Có vốn, muốn bỏ qua rủi ro nhu cầu | **Mua doanh nghiệp đang chạy** | không phải hỏi *có ai trả tiền không* | [FE International](../videos/2023-04-17_zero-to-1-1b-from-flipping-websites/case.md) |
| Đang đi làm, không muốn nghỉ | **SEO / affiliate ngách mới** | tích luỹ được khi ngủ, không cần có mặt | [Fin vs Fin](../videos/2024-03-30_i-make-1m-year-with-one-website/case.md) |

## 4. Kênh phân phối — số liệu và hai phát hiện ngược đời

| Kênh chính | Số case | Doanh thu trung vị | Khả thi VN |
|---|---:|---:|---:|
| SEO / ASO (tìm kiếm) | **46** | 35.000 USD | 3,7 |
| Xây audience (X / LinkedIn) | 33 | 52.000 USD | **3,2** |
| Video ngắn organic | 23 | 43.500 USD | 3,5 |
| Cộng đồng (Reddit / Discord) | 9 | 22.500 USD | 3,7 |
| Quảng cáo trả phí | 8 | 35.500 USD | 3,6 |
| **YouTube** | **8** | **130.000 USD** | 3,4 |
| **Marketplace nền tảng** | **5** | 23.000 USD | **4,4** |
| Email chủ động | 3 | 22.000 USD | 4,0 |

**Phát hiện 1 — YouTube có doanh thu trung vị cao gấp ba lần mọi kênh khác, nhưng chỉ 8 case dùng.**

Vì sao? Vì nó **đắt về công sức nhất**: cần quay, dựng, xuất hiện trước camera. Chính rào cản đó
giữ cạnh tranh thấp. Và cơ chế thì rất mạnh — [FollowBuddy](../videos/2026-03-19_i-make-17k-month-with-one-strategy/case.md)
cho thấy YouTube Search mang lại người xem **có ý định mua**, khác hẳn video ngắn vốn mang lại
người xem **giết thời gian**. Nhớ [phép tính của Jure: 200 triệu view TikTok = 300.000 USD](../videos/2025-04-12_i-make-60k-month-with-4-apps/case.md),
tức 0,0015 USD một view.

**Phát hiện 2 — Marketplace nền tảng có điểm khả thi VN cao nhất (4,4) nhưng doanh thu thấp nhất.**

Đây là **đường vào an toàn nhất cho người Việt**: không cần audience, không cần tiếng Anh nói,
không cần vốn. Đổi lại trần thấp và rủi ro nền tảng. Với người chưa có gì, 23.000 USD/tháng
là một điểm khởi đầu rất tốt — và bạn học được toàn bộ quy trình trong lúc kiếm tiền.

**Điều kiện then chốt:** bạn phải vào **sớm**, khi nền tảng vừa mở API hoặc vừa mở marketplace.
Đây là biến số quyết định trong cả [Data Fetcher](../videos/2025-08-13_how-i-built-it-23k-month-micro-saas/case.md)
lẫn [NotionForms](../videos/2024-11-07_how-i-built-it-37k-month-notion-app/case.md).

## 5. Cách định giá doanh nghiệp bạn đang xây

Từ [người đã bán hơn 1 tỷ USD doanh nghiệp](../videos/2023-04-17_zero-to-1-1b-from-flipping-websites/case.md):

> Doanh nghiệp nhỏ được định giá theo **bội số LỢI NHUẬN, không phải doanh thu**.
> Khoảng thông thường: **4–10 lần lợi nhuận năm.**

Hiểu lầm "bội số doanh thu" tồn tại vì với doanh nghiệp một người, doanh thu và lợi nhuận gần bằng nhau.

**Ba điều kiện để nằm ở nửa trên của khoảng đó:**
1. Khách hàng **định kỳ hoặc quay lại**
2. Đang **tăng trưởng**
3. Ở trong lĩnh vực **còn tồn tại lâu dài**

**Áp dụng ngược để chọn mô hình:** nếu bạn muốn xây thứ bán được, hãy tránh mô hình phụ thuộc
hoàn toàn vào cá nhân bạn. DesignJoy có biên gần 100% nhưng **không có Brett thì không có doanh nghiệp** —
bội số của nó sẽ nằm ở đáy, hoặc không bán được. Ngược lại, [một SaaS biên 40% nhưng có khách thuê bao](../videos/2024-11-22_how-i-built-it-12k-month-micro-saas/case.md)
lại ở vùng thuận lợi hơn khi bán.

## 6. Ba cái bẫy lặp lại nhiều nhất trong 180 case

**Bẫy 1 — Nhầm doanh thu với lợi nhuận.**
[Letterly công bố 250.000 USD/tháng](../videos/2025-11-24_how-he-makes-250k-per-month-from-a-simple-app-letter/case.md);
cộng chi phí chính anh nêu (quảng cáo 200K + lương 30K + AI 5K) còn lại **khoảng 15.000 USD**.
Quy tắc: **con số nào không kèm biên lợi nhuận thì coi như chưa biết gì.**

**Bẫy 2 — Nhầm sự chú ý với nhu cầu.**

| Case | Sự chú ý | Tiền |
|---|---|---|
| [PuffCount](../videos/2025-09-20_the-1m-mobile-app-playbook/case.md) | 11,6 triệu view | gần 0 lượt cài |
| [BulkMockup](../videos/2026-02-11_how-i-built-a-12k-month-micro-saas/case.md) | 12.000 view | 213 USD tổng |
| SuperMeme | 1,5 triệu người dùng | 400 khách trả tiền |

Và cùng founder đó, app Questgen chỉ 150.000 người dùng nhưng **chuyển đổi gấp năm lần** —
vì khách dùng nó **để làm việc**, không phải để giải trí.

**Bẫy 3 — Nhầm một cú lớn với dòng tiền bền.**
[Pat Walls ký hợp đồng tài trợ 112.000 USD ở tháng thứ 8, nhưng hết 365 ngày vẫn chỉ 3.500 USD/tháng](../videos/2024-10-30_the-day-i-hit-reset-on-my-life/case.md).
Một khoản lớn không phải run-rate.

## 7. Việc làm trong tuần này

1. **Trả lời câu hỏi mục 2:** khi tôi có thêm một khách, tôi tốn thêm bao nhiêu? Viết ra con số.
2. **Chọn một ô trong bảng mục 3** khớp với hoàn cảnh thật của bạn — vốn, kỹ năng, thời gian, khán giả.
3. **Kiểm tra kênh:** mô hình bạn chọn có kênh phân phối nào trong bảng mục 4 mà bạn tiếp cận được
   không cần tiếng Anh nói và không cần vốn? Nếu không có, đổi mô hình.
4. **Tính thử bội số:** nếu doanh nghiệp này chạy được 12 tháng, nó bán được bao nhiêu?
   Nếu câu trả lời là *"không bán được vì phụ thuộc tôi"*, hãy quyết định có chấp nhận điều đó không.

## Nguồn

Toàn bộ số liệu truy vấn từ `data/cases.csv` (180 case). Mỗi con số trong bảng đều dẫn về case gốc
có transcript đầy đủ, ảnh chụp màn hình, và mục cảnh báo thiên kiến nguồn riêng.

Xem thêm: [Playbook 1 — Tìm ý tưởng](01-tim-y-tuong.md) · [Playbook 2 — Validate](02-validate.md) · [Playbook 3 — Go-to-market](03-go-to-market.md)
