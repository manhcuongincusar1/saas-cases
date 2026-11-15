---
id: pwvnH9S4j60
slug: excel-exercises
product: Excel Exercises
founder: Jake — cựu nhân viên tài chính, tự học code, build site như side project 5-6 năm trước rồi nghỉ việc làm full-time 2 năm trước
tagline: Web app dạy Excel bằng bài tập tương tác (không dùng video), hard paywall sau vài bài miễn phí — site "chán nhất internet" thu $30-35K/tháng gần như tự chạy
revenue_usd_month: 30000
revenue_basis: Doanh thu 4 tuần gần nhất "a little over $30,000" đọc từ Stripe, founder nói đang kiếm "$30 to $35,000 a month". Là doanh thu gộp (gồm gói tháng và năm), chưa trừ phí Stripe và ad spend; không phải MRR thuần. Khớp với tiêu đề "$30K/Month".
model: b2c-saas-subscription
category: edtech — học Excel (hàm và phím tắt) qua bài tập mô phỏng
audience: B2C là chính (người học Excel để đi làm, đổi việc, tránh lộ điểm yếu) cộng thêm đơn mua cho nhóm từ công ty và trường đại học
started: build khoảng 5-6 năm trước (tính tới 10/2026) như side project buổi tối và cuối tuần
time_to_first_sale: không nêu thời gian chính xác; lần đầu có người trả $50 khi site còn xấu và chưa quảng bá gì
time_to_scale: bản chạy được đầu tiên mất nhiều tháng; từ lúc full-time (2 năm trước) tăng khoảng 5 lần tới $30-35K/tháng
team_size: 1 (solo, founder luôn nói "I")
funding: bootstrapped
main_channel: SEO với trang landing dài 1.500-2.000 chữ, sau đó thêm paid ads và đơn mua cho team
tech_stack: [HTML, CSS, vanilla JavaScript, Claude, Google Cloud Platform, Google Analytics, SendGrid, Stripe]
key_metrics:
  revenue_last_4_weeks_usd: 30000
  visitors_last_4_weeks: 50000
  active_paying_subscribers: 2500
  growth_since_full_time_x: 5
  ltv_cac_ratio_avg: 3
  gcp_bill_usd_month_max: 100
  sendgrid_usd_month: 35
  first_sale_usd: 50
difficulty: 3
video_url: https://www.youtube.com/watch?v=pwvnH9S4j60
published: 2026-10-28
views: 215329
tags: [saas, seo, hard-paywall, boring-business, solo-founder, bootstrapped, scratch-own-itch, side-project, paid-ads, subscription]
---

# Excel Exercises — website học Excel "chán nhất internet" thu $30K/tháng

> **Tóm tắt 30 giây:** Jake làm tài chính, bị bắt xem một chuỗi video training Excel dài lê thê tới mức buồn ngủ, rồi nghĩ ra "Duolingo but for Excel". Anh tự học code, build site dạy hàm và phím tắt Excel bằng bài tập mô phỏng ngay trên trình duyệt, đưa lên internet khi còn xấu và chưa nói với ai — vài tuần sau có người trả $50 và vài đơn lẻ tẻ nữa, đó là validation. Mô hình freemium với hard paywall sau vài bài miễn phí. Tăng trưởng đến từ SEO (nhồi 1.500-2.000 chữ vào chính trang chủ, trái lời khuyên "guru"), sau đó paid ads và đơn mua cho team/trường đại học. Số hiện tại: 4 tuần gần nhất hơn $30K doanh thu, ~50.000 visitor, ~2.500 subscriber đang trả phí, chi phí hạ tầng dưới $100/tháng cộng $35 SendGrid. Bài học mạnh nhất không phải ý tưởng mà là kỷ luật phân tích: tách unit economics theo gói tháng và gói năm, phát hiện gói tháng gần như hoà vốn, nhân đôi giá gói tháng — và tăng trưởng bùng lên.

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu 4 tuần gần nhất | **hơn $30.000** |
| Mức founder nói là hiện tại | **$30.000-35.000/tháng** |
| Visitor trong 4 tuần | **~50.000** |
| Subscriber đang trả phí | **~2.500** |
| Tăng trưởng từ lúc full-time | **~5 lần** (2 năm) |
| Tỷ lệ LTV/CAC trung bình (trước khi tách segment) | **~3 : 1** |
| Hạ tầng (GCP) | **dưới $100/tháng** |
| Email marketing (SendGrid) | **$35/tháng** |
| Nhân sự | **1 (solo)** |

[02:28](https://www.youtube.com/watch?v=pwvnH9S4j60&t=148s) là đoạn founder đọc số từ dashboard.

**Về con số:** "$30K" là doanh thu 4 tuần (hơi ít hơn một tháng lịch), lấy từ Stripe, gộp cả khách trả theo tháng và theo năm. Video không nói rõ phần doanh thu năm nào bị dồn vào kỳ này nên không tách được MRR thật. Phép chia thô $30.000 / 2.500 subscriber ≈ $12 mỗi subscriber mỗi 4 tuần chỉ là suy luận của người viết, không phải số founder nêu. Biên lợi nhuận không được nói trực tiếp, nhưng chi phí cố định cực thấp nên phần lớn chi phí thật nằm ở ad spend — con số này video không đưa.

---

## 2. Sản phẩm giải quyết vấn đề gì

Excel Exercises dạy **hàm và phím tắt Excel bằng bài tập và mô phỏng hands-on**, thay vì video ([01:24](https://www.youtube.com/watch?v=pwvnH9S4j60&t=84s)). Người dùng gõ công thức vào một bảng trông và hành xử như Excel/Google Sheets; nếu sai (ví dụ quên dấu nháy quanh điều kiện) hệ thống giải thích và cho thử lại, đúng thì được điểm và đi tiếp ([10:11](https://www.youtube.com/watch?v=pwvnH9S4j60&t=611s)). Có dashboard bài học, leaderboard, và một số project thực tế tải file dữ liệu về làm theo.

Người dùng điển hình theo founder: sinh viên mới ra trường tìm việc đầu tiên, người đổi việc, và cả người "exaggerated their abilities a little bit" ở công việc mới rồi cần học bù. Nỗi đau là **kỹ năng được yêu cầu trên CV/ở chỗ làm nhưng học bằng video thì không nhớ** — đây là điểm sản phẩm khác với kho nội dung miễn phí quanh đó.

Video không nói về đối thủ cụ thể, nên không biết Excel Exercises hơn họ ở đâu ngoài hình thức học.

---

## 3. Ý tưởng đến từ đâu

Ý tưởng là **nỗi đau của chính founder**. Jake làm tài chính; mọi nhân viên mới ở công ty đều phải học một khoá Excel online gồm chuỗi video dài. Anh buồn ngủ, mất tập trung, không nhớ gì. Về sau thấy một bài học Duolingo, anh nảy ra "Duolingo but for Excel" ([04:23](https://www.youtube.com/watch?v=pwvnH9S4j60&t=263s)).

Bối cảnh kỹ thuật: học tài chính ở đại học, không có nền tảng công nghệ, tự học code bằng YouTube và Stack Overflow, từng làm một app iPhone cho vui. Excel Exercises là **web project đầu tiên** của anh. Điều này ngược với hình dung "dev giỏi build SaaS" — nhưng cũng đúng với mục 7: code ban đầu phần lớn là copy-paste từ Stack Overflow, và sản phẩm lúc đầu rất thô.

---

## 4. Cách validate

Đây là một trong những validation "ngược đời" nhất trong kho case:

- Anh **đưa site lên internet từ rất sớm, không có môi trường dev/production tách biệt**, chưa nói với ai, chưa quảng bá ([04:56](https://www.youtube.com/watch?v=pwvnH9S4j60&t=296s)).
- Một ngày anh nhận thông báo có người trả **$50**. Anh nghĩ là nhầm lẫn "cuz it looks scary… It looks like Russian hackers are going to steal your identity".
- Vài tuần sau có thêm vài đơn lẻ tẻ — "that was the validation that I needed". Diễn giải của anh: họ tin vào ý tưởng đến mức sẵn sàng trả tiền dù thực thi lúc đó rất kém.

Điểm đáng nói: tín hiệu này chỉ có ý nghĩa vì đã có người **trả tiền** (hard paywall), không phải chỉ đăng ký hay like. Nhưng cũng cần nhớ: video không cho biết lượng traffic lúc đó, nên "vài đơn" có thể phản ánh ý định tìm kiếm Excel (nhu cầu có sẵn) hơn là sức hút của riêng sản phẩm. Đó là suy luận của người viết.

Lời khuyên của anh cho người khác ([09:03](https://www.youtube.com/watch?v=pwvnH9S4j60&t=543s)): chọn vấn đề bạn hiểu sâu, và đưa sản phẩm ra càng sớm càng tốt.

---

## 5. Go-to-market ⭐ — SEO nhồi chữ ở trang chủ, rồi paid ads và deal cho team

### 0 → $10K/tháng: SEO ([07:07](https://www.youtube.com/watch?v=pwvnH9S4j60&t=427s))

- Anh nói có đăng lên Reddit vài lần, nhưng tăng trưởng thật đến từ **SEO**.
- Có viết blog về các hàm Excel, nhưng điều kéo traffic lại là **trang landing dài khoảng 1.500-2.000 chữ**: giới thiệu sản phẩm là gì, học Excel kiểu này ra sao, vì sao tốt hơn xem video. Chính trang này được index và "got me the most traffic, and it was also the highest intent traffic".
- Anh tự mô tả đó là cách "vomiting a bunch of words onto as many pages as I could for a really, really long time". "Online marketing gurus" bảo đừng để nhiều chữ như vậy trên trang chủ, nhưng anh giữ vì thấy "this is where all my sales are coming from".

Đây là **data-driven, không theo tài liệu**: nhìn nguồn doanh thu rồi giữ thứ đang bán được.

### $10K → $30K/tháng: paid ads và đơn mua cho team ([07:57](https://www.youtube.com/watch?v=pwvnH9S4j60&t=477s))

- **Paid advertising** là bước ngoặt tăng trưởng và cũng đổi cách anh nghĩ về business: khi traffic miễn phí và chi phí thấp thì mỗi subscription gần như lãi thuần; khi trả tiền mua user thì phải tính CAC và lợi nhuận kỳ vọng. Video không nói kênh quảng cáo cụ thể, ngân sách hay CPA.
- **Đơn mua cho trường đại học và doanh nghiệp**: kiểu product-led growth — người dùng thử, thích, về công ty nói với sếp, sếp liên hệ hỏi mua cho "like 50 people" ([08:30](https://www.youtube.com/watch?v=pwvnH9S4j60&t=510s)). Không có số liệu về tỷ trọng doanh thu từ nhóm này hay mức giá team.

### Phân tích unit economics theo segment ([11:20](https://www.youtube.com/watch?v=pwvnH9S4j60&t=680s))

Stripe chỉ cho một số LTV gộp cho mọi gói. Jake thấy tỷ lệ LTV/CAC trung bình ~3:1 là ổn nhưng tăng trưởng chậm hơn kỳ vọng, nên xuất toàn bộ payment ra spreadsheet và tách **gói tháng** với **gói năm**. Kết quả: gói năm lãi tốt, gói tháng "barely turning a profit" với thời gian hoàn vốn khoảng 4-5 tháng. Anh **nhân đôi giá gói tháng, giữ nguyên giá gói năm**, và "that's when growth really it off" (ASR bỏ mất một chữ, ý là tăng trưởng bùng lên). Video không cho giá cụ thể trước và sau.

---

## 6. Mô hình kiếm tiền & giá

- **Freemium với hard paywall**: vài bài học miễn phí đầu để người dùng hiểu sản phẩm khác video ra sao, rồi chặn ([02:12](https://www.youtube.com/watch?v=pwvnH9S4j60&t=132s)). Founder giải thích bài miễn phí là cần thiết vì nhiều người chưa từng dùng kiểu học này.
- Có gói **tháng** và gói **năm**, cộng đơn mua cho team/trường. Giá cụ thể: **video không nêu**, chỉ biết lần đầu có người trả $50 và gói tháng đã được nhân đôi.
- Founder nói hệ thống "all automated", có thể đi nghỉ mà site tự chạy.

Điểm đáng học: với sản phẩm có vòng đời người dùng ngắn (học xong thì rời), annual plan là nơi có lãi thật; gói tháng chủ yếu để hạ rào cản vào. Đây là diễn giải từ số liệu founder nêu, không phải câu anh nói.

---

## 7. Tech stack & chi phí

| Hạng mục | Công cụ |
|---|---|
| Front-end | HTML, CSS, vanilla JavaScript — phần lớn copy từ Stack Overflow 6 năm trước, nay thêm code do Claude viết |
| Hosting | Google Cloud Platform, hoá đơn thường dưới **$100/tháng** |
| Analytics | Google Analytics (free) |
| Email marketing | SendGrid, **$35/tháng** (chi phí định kỳ duy nhất ngoài hosting) |
| Thanh toán | Stripe (phí theo phần trăm cộng số cent cố định) |

Thử thách kỹ thuật lớn nhất lúc đầu: **bảng phải trông và hành xử như spreadsheet thật**, nếu không người học bực bội ([06:01](https://www.youtube.com/watch?v=pwvnH9S4j60&t=361s)). Chính founder cũng nói anh không biết Claude đang viết gì — nghĩa là phần codebase đang được duy trì phần lớn bằng AI, và video không cho biết chất lượng/độ ổn định của nó. Host nhắc "Python and CodeX" nhưng đó là lời host, không phải stack của Jake.

---

## 8. Bài học & trích dẫn

- **Sản phẩm chán + intent cao + chi phí gần bằng 0 = lợi nhuận.** Host kết luận: "You hit a paywall and that's it."
- **Chỉ số trung bình che mất sự thật.** LTV gộp của Stripe 3:1 nghe ổn, nhưng tách theo segment thì gói tháng gần hoà vốn.
- **Ra mắt khi còn xấu.** Có thể có hiệu ứng sống sót: ta chỉ nghe câu chuyện của sản phẩm đã sống, còn bao nhiêu site xấu không ai trả tiền thì không biết.
- **Lợi thế thời gian:** 5-6 năm tích luỹ SEO, nội dung và domain. Người mới bắt đầu hôm nay không có.

> **"I woke up one day and had a notification that someone had paid me $50."**

> **"What I ended up doing was doubling my monthly price and keeping my annual price the same."**

> **"If you're not embarrassed by the first iteration, then you've waited too long."**

> **"Stripe gives you one LTV metric for all of your subscriptions for all time."**

**Góc nhìn tỉnh táo:** video nhấn mạnh "very little effort" và "simplest" nhưng chính lời kể cho thấy 5-6 năm, nhiều tháng cho bản đầu, và từ $10K lên $30K phải có paid ads với phân tích bài bản. Con số $30K cũng là mức hiện tại sau nhiều năm — không phải kết quả của thời gian ngắn. Video không nói về churn, tỷ lệ chuyển đổi free → paid, hay đối thủ.

---

## 9. Áp dụng cho tôi (indie hacker ở VN, bán global)

**Sao chép được gì:**
- **Cơ chế "học bằng làm" thay cho video** ở một kỹ năng nghề nghiệp có giá trị tiền bạc: bài tập có phản hồi tức thì, điểm, tiến độ. Hard paywall sau vài bài miễn phí để người dùng thấy khác biệt.
- **Trang landing dài, nhiều chữ, hướng vào intent mua** (so sánh "vì sao tốt hơn cách cũ") thay vì chỉ một trang tối giản — và quyết định giữ hay bỏ dựa vào nguồn doanh thu thật.
- **Tách unit economics theo từng gói giá** trước khi đốt thêm ads; tăng giá gói tháng để đẩy khách sang annual.
- **Product-led growth sang team**: người dùng cá nhân mang sản phẩm về công ty, sếp hỏi mua nhiều seat.
- **Ra mắt sớm khi còn thô**, để người lạ trả tiền xác nhận.

**Rào cản thật:**
- **SEO không còn dễ như 5-6 năm trước.** Founder hưởng lợi từ việc vào sớm; hôm nay "học Excel" có rất nhiều nội dung miễn phí và công cụ AI trả lời trực tiếp. Video không bàn về cạnh tranh nên đây là nhận định của người viết.
- **Làm cho bảng tương tác "hành xử như Excel thật"** là kỹ thuật khó thật, không phải HTML đơn giản; chấm công thức đúng/sai cho hàng trăm hàm cần nhiều test.
- **Vốn cho paid ads** để tăng từ $10K lên $30K: video không cho ngân sách hay CPA, nên không đánh giá được rủi ro.
- **Thanh toán và pháp nhân:** bán subscription và đơn cho công ty/trường cần Stripe hoặc merchant of record, và hoá đơn cho khách doanh nghiệp. Đây là điều cần chuẩn bị sớm khi bán global từ VN (nhận định của người viết, chưa nêu chi tiết pháp lý).
- **Mô hình "tự động" chỉ đúng ở giai đoạn cuối.** Giai đoạn đầu cần nhiều năm nội dung và index.

**Biến thể đáng thử ở thị trường trả cao:**
- **Cùng cơ chế cho kỹ năng công cụ có người trả tiền và có kỳ thi hoặc phỏng vấn:** ví dụ SQL, Power BI, Google Sheets nâng cao, kế toán/finance modeling cho nhân viên và sinh viên Mỹ/UK/Canada/Úc. Giá cỡ vài chục USD/năm cho cá nhân (ước tính của người viết). Có cửa vì người dùng có động cơ nghề nghiệp rõ và chấp nhận trả tiền cho việc "không bị lộ".
- **Bán team license cho phòng ban tài chính/vận hành**: tập trung biến người dùng cá nhân thành đơn 20-100 seat, đúng cơ chế founder nói. Giá/seat cỡ vài chục tới vài trăm USD/năm là giả định để kiểm chứng.
- **Chỉ thử bước SEO landing page dài trước** (không cần build đủ nghìn bài tập): làm 15-30 bài, trang landing dài bằng intent mua, xem bao nhiêu người trả để xác nhận cầu trước khi đầu tư engine mô phỏng.

**Khi nào KHÔNG nên làm:**
- Khi bạn muốn tăng trưởng nhanh trong vài tháng: case này mất nhiều năm và hưởng lợi từ thời điểm SEO.
- Khi chủ đề đã bị miễn phí hoá hoàn toàn hoặc AI trả lời tốt hơn bài tập của bạn.
- Khi bạn không thể kiên trì với một nội dung đơn điệu: đây là "sản phẩm chán", thắng nhờ kiên trì chứ không nhờ ý tưởng.
- Khi bạn ngại phân tích số liệu theo từng segment giá, vì đó là chỗ tạo ra đòn bẩy thật của case này.

---

## Nguồn

- Video: [I Make $30K/Month From the Most Boring Website on the Internet](https://www.youtube.com/watch?v=pwvnH9S4j60) — Starter Story, 28/10/2026, 13:07, 215K views
- Transcript: [`transcript.md`](transcript.md)
