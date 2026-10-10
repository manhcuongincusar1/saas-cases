---
id: d8PdJJcEtE0
slug: profit-ai-spreadsheet
product: Profit AI
founder: Jack
tagline: Biến bảng tính đã dùng cho khách hàng suốt nhiều năm thành app Shopify
revenue_usd_month: 70000
revenue_basis: $30K MRR phần app + gần $40K MRR phần dịch vụ; tổng $147.000 kể từ khi launch 12/2025
model: b2b-saas-subscription
category: ecommerce-analytics
audience: B2B — chủ shop Shopify, agency thương mại điện tử
started: 2025-12 (Shopify duyệt đúng ngày Giáng sinh)
time_to_first_sale: vài tuần đầu không có khách, chỉ beta tester dùng miễn phí
time_to_scale: ~5 tháng → $70K MRR tổng
team_size: nhỏ
funding: bootstrapped
main_channel: truyền miệng (CHƯA hard-launch marketing)
tech_stack: [Claude Code, Codex, Framer, Instantly, Google Sheets]
opex_usd_month: 200
key_metrics:
  users: 122 (phần lớn dùng free)
  paying: 38-39
  installs_vs_uninstalls: 47 cài / 43 gỡ (churn cao)
  pricing: từng $5.000/tháng, hạ xuống $800/tháng; gói free có 30 ngày dùng thử bản trả phí
  build_time: 3,5-4 tháng
replicability_vn: 5
difficulty: 3
video_url: https://www.youtube.com/watch?v=d8PdJJcEtE0
published: 2026-06-24
views: 43685
tags: [micro-saas, spreadsheet-to-app, b2b, shopify, ecommerce-tools, consultant-to-saas, non-developer, ai-coding, pricing-experiment, churn-warning]
---

# Profit AI — biến một bảng tính thành micro-SaaS $70K/tháng

> **Tóm tắt 30 giây:** Jack làm tư vấn cho agency và thương hiệu thương mại điện tử nhiều năm. Công việc chính của anh là **dựng bảng tính** giúp founder và team marketing ra quyết định tốt hơn. Một ngày anh nghĩ: **sao không biến chính cái bảng tính này thành app?** Anh **không biết code** — anh tải bảng tính xuống dạng CSV, đưa vào Cursor và bảo *"build cái này"*. Ra mắt trên Shopify tháng 12/2025. Năm tháng sau: **$30K MRR từ app + gần $40K MRR từ dịch vụ**, tổng **$147.000** kể từ khi launch — và **chưa hề chạy marketing chính thức**.

![](screenshots/02_00m51s_usd-147-000.jpg)

---

## 1. Con số — kèm cảnh báo trung thực

| Chỉ số | Giá trị |
|---|---|
| MRR phần app | **$30.000** |
| MRR phần dịch vụ | **~$40.000** |
| Tổng doanh thu từ khi launch | **$147.000** |
| Người dùng | **122** (phần lớn dùng free) |
| Khách trả tiền | **38-39** |
| Chi phí công cụ | **~$200/tháng** |
| Thời gian build | **3,5-4 tháng** |

> ⚠️ **Anh tự nêu điểm yếu, và đây là dữ liệu quý:** **47 lượt cài / 43 lượt gỡ**. Anh nói thẳng: *"chúng tôi đang churn gần bằng số khách mang về."* Pat cũng ghi nhận churn **chưa lý tưởng**, nhưng đây là app rất mới.
>
> **Bài học:** đây là case tăng trưởng nhanh **chưa được chứng minh về độ bền**. Đọc nó như một playbook tìm ý tưởng, không phải bằng chứng về một business ổn định.

**Chi tiết đáng chú ý: doanh thu dịch vụ ($40K) LỚN HƠN doanh thu app ($30K).** Đây là mẫu hình dịch vụ-cộng-phần mềm — dịch vụ nuôi dòng tiền trong lúc phần mềm còn non.

---

## 2. Ý tưởng: bảng tính chính là danh sách ý tưởng ⭐⭐

**Đây là insight trung tâm, và nó dùng được ngay cho bất kỳ ai.**

Bối cảnh: Jack ra mắt thương hiệu thương mại điện tử đầu tiên năm 2016 (bán phần mềm và sample pack cho nhà sản xuất nhạc). Biên lợi nhuận rất cao vì là business phần mềm. Anh đi từ sinh viên túng thiếu thành có nhiều tiền hơn mức biết tiêu.

Sau đó anh chuyển sang tư vấn cho các agency. Triết lý của anh:

> **"Quyết định tốt đến từ thông tin."**

Anh dựng những bảng tính **dễ tiếp cận** giúp founder và team marketing ra quyết định tốt hơn. Và anh mô tả rất thẳng:

> **"Bảng tính là công việc khổ sai, và dữ liệu thì ngốn thời gian."**

Chính chỗ khổ sai đó là sản phẩm.

**Pat đúc kết thành công thức:**

> **Tìm những việc lặp đi lặp lại, nhàm chán — rồi biến chúng thành sản phẩm đơn giản.**

**Và producer đưa ra hành động cụ thể nhất trong toàn bộ knowledge base:**

> **Mở Claude Code ngay bây giờ. Kết nối tài khoản Google Drive. Nhìn 20 bảng tính gần nhất trong tài khoản của anh. Bảo nó build một cái thành app.**

> **Đây là bài tập tôi khuyến nghị anh làm ngay hôm nay.** Nếu anh đã đi làm, đã tư vấn, đã vận hành bất cứ thứ gì — **những bảng tính anh đang dùng chính là danh sách ý tưởng đã được validate**, vì anh đã dùng chúng cho công việc thật.

**Pat kể trải nghiệm riêng:** anh có một bảng tính theo dõi tài sản/ngân sách cá nhân dùng nhiều năm, đưa vào Claude Code và **build xong trong một ngày**.

![](screenshots/07_05m33s_ch-the-spreadsheet.jpg)

---

## 3. Bảng tính đó có gì

Anh mở ra cho xem, và nó cho thấy đúng loại giá trị mà một bảng tính tốt mang lại:

- **Trang P&L** — dễ đọc, số to, màu rõ, tháng tốt nhất được tô đậm dần bằng định dạng có điều kiện
- Nơi ghi **chi phí cố định** và **chi phí biến đổi**, giá vốn
- **LTV** — để biết nên trả nhiều hay ít hơn để có một khách hàng
- **Máy tính ROAS** — anh nói đây là chỉ số **hay bị hiểu sai**
- **Công cụ phân tích quảng cáo**
- **Scenario planner**

Anh so sánh rất sắc:

> Nếu nhìn một scenario planner thật — loại **Deloitte** làm và tính phí **hàng chục nghìn đô** — nó phức tạp và hoàn toàn không tiếp cận được. Còn thứ anh làm là **biến những thứ cực kỳ phức tạp thành đơn giản nhất có thể.**

> **Đây chính là định vị sản phẩm:** không phải làm thứ chưa ai làm — mà làm thứ **đã tồn tại nhưng chỉ giới doanh nghiệp lớn với ngân sách khổng lồ mới tiếp cận được**, rồi mở nó cho phần còn lại.
>
> **Cùng công thức với [Live Tourney](../2026-07-15_i-quit-my-job-at-meta-to-build-a-30k-month-saas/case.md)** — đối thủ tồn tại nhưng "quá đắt và quá phức tạp".

---

## 4. Cách biến bảng tính thành app — quy trình cụ thể

Trước đó anh từng nhờ một developer quen làm giúp và **bị từ chối**. Rồi làn sóng code bằng AI tới, và anh **đổ hàng trăm giờ vào Codex** để tự học.

**Quy trình thật, đơn giản đến mức khó tin:**

1. **Tải bảng tính xuống dạng CSV**
2. **Đưa vào Cursor**
3. **Bảo nó: "build cái này"**
4. **Xác định mọi chỗ AI làm sai** → nói lại: *"chỗ này phải sửa, công thức đúng là thế này"*

Mất **3,5-4 tháng**. Anh nói ngày nay việc này **dễ hơn nhiều**.

> **Bước 4 mới là chỗ giá trị của anh nằm.** AI dựng được giao diện; **chỉ anh mới biết công thức nào đúng**, vì anh đã dùng nó với khách hàng thật nhiều năm. **Chuyên môn ngành là hào bảo vệ, không phải kỹ năng code.**

---

## 5. Bài học định giá ⭐

Đây là dữ liệu thật hiếm gặp:

| Giá | Kết quả |
|---|---|
| **$5.000/tháng** | Chỉ vài người mua — đều là doanh nghiệp anh **đã làm việc cùng từ trước** |
| **$800/tháng** | Mức hiện tại |

> **Bài học: giá quá cao thì chỉ bán được cho quan hệ sẵn có, không bán được cho thị trường.** Nếu mọi khách hàng của anh đều là người anh đã quen, anh **chưa** có sản phẩm — anh đang làm dịch vụ.

**Về gói free — quan điểm ngược dòng:**

> Anh biết nhiều người chê gói free, nhưng anh **muốn tất cả mọi người dùng app**. Nên gói free của anh còn kèm **30 ngày dùng thử toàn bộ bản trả phí**.

⚠️ Lưu ý: chiến lược này có thể liên quan tới con số churn cao. Nhiều người dùng free + dùng thử rộng rãi = nhiều người thử rồi bỏ.

---

## 6. Tech stack — ~$200/tháng

| Công cụ | Vai trò | Chi phí |
|---|---|---|
| **Claude Code** (gói Max) | Phát triển chính | ~$200/tháng |
| **Codex** (trong terminal) | Bổ trợ | được giảm 100% |
| **Framer** | Website | — |
| **Instantly** | Email marketing | — |
| **Google Sheets** | Vẫn dùng | miễn phí |

**Sản phẩm có một phần là "Claude wrapper"** — anh nói thẳng: Claude + skills + connector, chạy qua Profit AI, cho phép **triển khai thẳng từ Slack**. Khách nhắn Slack bot (thực chất là Claude) để đẩy dữ liệu đi đâu tuỳ ý.

> **Đây là mẫu hình sản phẩm 2026 đáng chú ý:** giá trị không nằm ở mô hình AI — nó nằm ở **pipeline dữ liệu và connector**. Ai cũng gọi được Claude; không phải ai cũng nối được vào dữ liệu Shopify, ads và kế toán của khách hàng.

---

## 7. Cơ hội trong mảng công cụ thương mại điện tử ⭐

Pat khẳng định rất mạnh:

> **"Tôi mê mảng công cụ thương mại điện tử. Nó không giống mảng công cụ cho creator — chỗ đó đầy AI wrapper. Công cụ thương mại điện tử là một trong những mảng bị đánh giá thấp nhất hiện nay."**

**Bằng chứng anh đưa ra:**
- Một khách mời từ ~1 năm trước (Eric Kos) làm **plugin Shopify**, khi phỏng vấn đang ở **$200.000/tháng** — nay đã vượt **$1 triệu/tháng**
- Một khách mời sắp lên sóng chỉ làm **báo cáo cho Klaviyo** — một công cụ duy nhất trong hệ sinh thái ecommerce — và đang làm **$1 triệu/năm**

**Nguồn ý tưởng Jack chỉ ra:** mỗi doanh nghiệp có nhu cầu dữ liệu **rất riêng**. Một agency ở Miami vừa ký với anh có **cả triệu lẻ một** trường hợp cần dữ liệu khác nhau.

> **Kết luận: "đưa dữ liệu tốt hơn vào tay chủ doanh nghiệp" là một mỏ ý tưởng gần như vô tận.** Mỗi công cụ trong hệ sinh thái Shopify/ecommerce (Klaviyo, ads, tồn kho, vận chuyển, hoàn hàng, đánh giá) đều có thể là một micro-SaaS báo cáo riêng.

![](screenshots/10_08m33s_ch-business-ideas.jpg)

---

## 8. Lời khuyên cuối

> **"Đừng nhắm tới sự lười biếng. Nếu mục tiêu của anh là kiếm thật nhiều tiền mà không làm gì, anh sẽ bị thay thế rất nhanh. Thị trường này chạy nhanh và nó thích nhanh."**

> **"Cứ hỏi Claude xem nó làm được không. Tôi liên tục ngạc nhiên về việc nó làm được bao nhiêu chỉ từ một prompt — miễn là nó được kết nối với mọi thứ."**

> ⚠️ Lưu ý sự đối lập với [Lazy Method](../2026-08-12_the-lazy-method-how-i-build-10k-month-apps/case.md) — Will xây cả triết lý trên việc "lười tối đa". Jack thì bác bỏ thẳng. **Cách hoà giải:** Will lười ở khâu **vận hành** (thuê ads làm thay), nhưng rất kỷ luật ở khâu **chọn ý tưởng và tối ưu phễu**. Không ai lười ở phần quan trọng.

---

## 9. Cảnh báo thiên kiến nguồn

- **Hơn một nửa doanh thu KHÔNG phải từ app.** Tiêu đề bán câu chuyện *"biến bảng tính thành micro-SaaS $30K/tháng"*, nhưng Jack nói rõ: **$30K MRR cho app và gần $40K MRR cho DỊCH VỤ**. Phần dịch vụ chính là công việc tư vấn anh đã làm nhiều năm trước khi có app. **Con số "$70K/tháng" trộn một business phần mềm mới với một business tư vấn cũ** — và phần lớn hơn là phần cũ.
- **Các con số trên dashboard không khớp nhau.** Anh chiếu bảng điều khiển Shopify: **47 lượt cài / 43 lượt gỡ**, **$147.000 tổng thu tới nay**, **122 người dùng**, **38-39 khách trả tiền**. Nhưng 47 lượt cài không thể sinh ra 122 người dùng, và $147.000 kể từ tháng 12 chỉ tương đương **khoảng 2 tháng** ở mức MRR gộp $70K mà anh khai. **Không ai đối chiếu lại các con số này trong video.**
- **Toàn bộ khách hàng đến từ mạng lưới cũ — và chính anh nói ra.** Beta tester là *"một nhóm brand mà TÔI QUEN"*; ở mức $5.000/tháng *"chỉ có vài người mua, đều là doanh nghiệp CHÚNG TÔI ĐÃ LÀM VIỆC CÙNG"*; agency ở Miami cũng là quan hệ. Và anh thừa nhận: *"phần lớn tăng trưởng đến từ truyền miệng. Chúng tôi CHƯA hard-launch marketing gì cả."* **Nghĩa là case này chưa chứng minh được BẤT KỲ kênh thu hút khách nào có thể lặp lại.** Đây là lỗ hổng lớn nhất nếu anh không có sẵn mạng lưới tương đương.
- **Đoạn tài trợ HubSpot ở 04:38–05:10** — *"MicroSaaS Ideas Database"* qua `clickhubspot.com`, nhắc lại ở 12:02. Đáng chú ý: **mô tả video ghi "190+ ý tưởng" nhưng lời quảng cáo trong video nói "hơn 100 ý tưởng"** — cùng một tài liệu, hai con số. Nhà tài trợ **không liên quan tới Profit AI**.
- **Bối cảnh bị làm mờ:** Jack ra mắt thương hiệu thương mại điện tử đầu tiên năm 2016 và theo lời anh, đi *"từ sinh viên túng thiếu thành có nhiều tiền hơn mức biết tiêu"* rất nhanh. Anh đã tư vấn cho agency nhiều năm. Anh cũng **không phải người ngoại đạo với code** — anh nói mình *"đổ hàng trăm giờ vào Codex"* để học. Nhãn "không biết code" trong video là đúng về mặt kỹ thuật nhưng gây hiểu lầm về công sức thật.
- **Con số dùng để hype cả danh mục là tin nghe lại.** Pat nói một khách mời cũ (Eric Kos) *"vừa vượt $1 triệu/tháng"* và một khách sắp lên sóng làm *"$1 triệu/năm chỉ với báo cáo Klaviyo"* — cả hai đều **không có bằng chứng nào trong video này**, và chúng được dùng để chứng minh rằng mảng công cụ ecommerce là "mỏ vàng".
- **Thiếu số liệu quan trọng:** tỉ lệ churn thật theo tháng (chỉ có con số cài/gỡ luỹ kế), CAC, chi phí thực hiện phần dịch vụ $40K (đây là tiền đổi bằng giờ người, không phải biên phần mềm), và tỉ lệ chuyển đổi sau 30 ngày dùng thử.
- **Điểm cộng đáng ghi nhận:** Jack là một trong số ít khách mời **tự nêu điểm yếu** — anh chủ động nói *"chúng tôi đang churn gần bằng số khách mang về"* và kể thẳng thất bại định giá $5.000. Mức trung thực này cao hơn mặt bằng của kênh.

## 10. Áp dụng cho tôi (indie hacker VN)

**Đây là case có con đường hành động rõ ràng nhất cho người đã đi làm.**

**Làm ngay hôm nay — bài tập 30 phút:**
1. Mở Google Drive, liệt kê **20 bảng tính** anh dùng gần nhất
2. Với mỗi cái, hỏi: *ai khác cũng phải làm việc này bằng tay?*
3. Chọn cái **tốn nhiều thời gian nhất** và **nhiều người khác cũng cần**
4. Tải xuống CSV → đưa vào Claude Code → *"build cái này"*
5. Sửa những chỗ AI hiểu sai công thức — **đây là phần chỉ anh làm được**

**Vì sao mô hình này rất hợp:**
- ✅ **Ý tưởng đã được validate sẵn** — anh đã dùng bảng tính đó cho việc thật
- ✅ **Chuyên môn ngành là hào bảo vệ**, không cần giỏi code
- ✅ **Chi phí $200/tháng**
- ✅ **B2B trả bằng USD** — né hoàn toàn vấn đề ARPU thấp ở VN
- ✅ **Marketplace Shopify là kênh phân phối sẵn có** — không cần tự kéo traffic từ đầu
- ✅ Có thể **giữ mảng dịch vụ** nuôi dòng tiền trong lúc phần mềm còn non

**Ngách đáng soi cho người Việt:** bất kỳ bảng tính nào anh (hoặc bạn bè làm agency/ecommerce/kế toán/logistics) đang dùng hằng ngày. Cụ thể: báo cáo hiệu quả quảng cáo, tính giá vốn và lợi nhuận theo SKU, quản lý tồn kho nhiều kênh, đối soát COD, tính lương theo ca.

**Rào cản thật:**
- ⚠️ **Churn cao** (47 cài / 43 gỡ) — mô hình này chưa chứng minh giữ chân được khách
- ⚠️ **Phải có chuyên môn ngành thật.** Không có bảng tính từ công việc thật thì không có case này.
- ⚠️ **Định giá khó** — anh phải hạ từ $5.000 xuống $800
- ⚠️ Marketplace Shopify có luật riêng, tỉ lệ ăn chia, và rủi ro bị chính Shopify làm luôn tính năng đó
- ⚠️ **3,5-4 tháng build** dù có AI — đừng kỳ vọng vài tuần

**Khi KHÔNG nên dùng mô hình này:**

- **Khi anh không có sẵn một mạng lưới khách hàng để bán vòng đầu.** Mọi khách hàng đầu tiên của Jack đều là quan hệ có sẵn từ nghề tư vấn, và anh thừa nhận **chưa chạy marketing lần nào**. Case này cho anh cách TÌM ý tưởng, **không cho anh cách BÁN**. Nếu anh xuất phát từ con số 0 về quan hệ, hãy ghép nó với một kênh đã chứng minh được — ví dụ directory đối tác của [Hero Analytics](../2026-06-10_i-built-a-1m-saas-in-a-hidden-niche/case.md) hoặc SEO "alternative to X" của [Shipper](../2026-05-28_i-built-a-micro-version-of-a-1b-saas-now-i-make-50k/case.md).
- **Khi bảng tính của anh chỉ chứa DỮ LIỆU chứ không chứa CÔNG THỨC.** Giá trị của Jack nằm ở bước 4: phát hiện chỗ AI tính sai và nói *"công thức đúng phải là thế này"*. Đó là logic nghiệp vụ tích luỹ nhiều năm. Một bảng tính chỉ để lưu danh sách thì AI dựng lại được trong 10 phút và **không ai trả $800/tháng cho nó**.
- **Khi anh cần một sản phẩm giữ chân khách lâu dài, không phải một công cụ tra cứu.** 43 gỡ trên 47 cài là dữ liệu thật, và nó phù hợp với bản chất sản phẩm báo cáo: người ta xem vài lần, hiểu ra điều cần hiểu, rồi gỡ. Cộng thêm gói free kèm 30 ngày dùng thử toàn phần — [Shipper](../2026-05-28_i-built-a-micro-version-of-a-1b-saas-now-i-make-50k/case.md) chọn ngược lại (0 khách miễn phí) chính vì lý do này. **Điều kiện phân định: chi phí phục vụ một người dùng free của anh có gần bằng 0 không? Nếu không, gói free là gánh nặng.**

---

## Nguồn

- Video: [I Turned This Spreadsheet Into a $30K/Month Micro-SaaS](https://www.youtube.com/watch?v=d8PdJJcEtE0) — Starter Story, 24/06/2026, 12:24, 43K views
- Sản phẩm: Profit AI (Shopify app)
- Transcript: [`_raw/transcripts/d8PdJJcEtE0.md`](transcript.md) · Ảnh: [`screenshots/d8PdJJcEtE0/`](screenshots/)
