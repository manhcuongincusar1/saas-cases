---
id: xWnqY2Mav4s
slug: cardstock-scanemon
product: CardStock + Scanemon
founder: Kyle Fowler
tagline: Quét thẻ bài bằng camera → nhận diện và định giá; một app cho thẻ thể thao, một cho Pokémon
revenue_usd_month: 92000
revenue_basis: CardStock ~$75K MRR + Scanemon ~$17K MRR (founder show dashboard); anh nói tổng "$120K/tháng" và $1,5M/năm
model: mobile-app-subscription
category: hobby-collectibles
audience: B2C — người sưu tầm thẻ thể thao và thẻ Pokémon
started: 2019 (CardStock), 2025 (Scanemon)
time_to_first_sale: ngay sau khi đăng bài cập nhật lên Reddit
time_to_scale: CardStock 6 năm; Scanemon 1 năm
team_size: 5
funding: bootstrapped
main_channel: TikTok slideshow (tự làm + phân phối qua creator)
tech_stack: [Swift, SwiftUI, Core Data, AWS EC2, RevenueCat, Cursor, Codex, Claude, Supabase, Railway]
key_metrics:
  cardstock: 15.000 subscription hoạt động · ~13.000 lượt tải/tháng
  scanemon: 3.400 subscription · ~16.000 khách mới/tháng (nhiều hơn CardStock)
  mvp_time: CardStock ~6 tháng · Scanemon MVP trong MỘT NGÀY bằng Cursor agent
replicability_vn: 4
difficulty: 2
video_url: https://www.youtube.com/watch?v=xWnqY2Mav4s
published: 2026-06-07
views: 77624
tags: [mobile-app, hobby-niche, scratch-own-itch, collectibles, tiktok-slideshow, second-app, ai-coding, camera-scanning, reddit-launch]
---

# CardStock & Scanemon — $1,5M/năm từ hai app quét thẻ bài

> **Tóm tắt 30 giây:** Kyle Fowler sưu tầm thẻ bài từ nhỏ. Anh muốn số hoá bộ sưu tập của mình, lên App Store tìm — **không có app nào làm việc đó**. Anh tự build **CardStock** (quét thẻ thể thao bằng camera → nhận diện và định giá) năm 2019. Từ ba người trong tầng hầm kiếm vài trăm đô, nay **5 người đi khắp thế giới, $1,5 triệu/năm**. Năm 2025 anh làm lại đúng công thức cho thẻ Pokémon — **Scanemon** — MVP dựng **trong một ngày** bằng AI, và nay app mới này **kéo nhiều khách mới hơn cả app gốc**.

![](screenshots/02_01m42s_ch-app-businesses-breakdown.jpg)

---

## 1. Con số

| App | MRR | Người dùng | Ghi chú |
|---|---|---|---|
| **CardStock** (thẻ thể thao) | **~$75.000** | **15.000** subscription hoạt động · ~13.000 lượt tải/tháng | Ra mắt 2019 |
| **Scanemon** (thẻ Pokémon) | **~$17.000** | **3.400** subscription · **~16.000 khách mới/tháng** | Ra mắt 2025 |

> **Chi tiết đáng chú ý nhất: Scanemon mới một năm nhưng kéo NHIỀU khách mới hơn CardStock đã chạy 6 năm.** Điều này cho thấy: khi đã có công thức, **app thứ hai đi nhanh hơn hẳn app đầu** — và chọn đúng ngách quan trọng hơn thâm niên.

Đội: **5 người**, làm việc từ khắp nơi trên thế giới.

---

## 2. Ý tưởng — đơn giản đến mức dễ bỏ qua

Anh sưu tầm thẻ từ bé. Anh muốn **lập danh mục và sắp xếp** bộ sưu tập, rồi nhận ra: **dù sắp xếp kỹ đến đâu, khi không có bộ sưu tập bên cạnh thì anh không biết thẻ nào là thẻ nào.**

Suy nghĩ tiếp theo: *chắc số hoá được và đưa lên điện thoại. Chắc phải có app cho việc này.*

> **Anh lên App Store — và không có app nào.** Nên anh tự build.

**Toàn bộ quy trình validate chỉ có vậy.** Không phỏng vấn, không khung, không nghiên cứu thị trường.

> **Đây là dạng "giải vấn đề của chính mình" thuần khiết nhất trong knowledge base.** Cùng cơ chế với [Tone Adapt](../2026-06-14_the-first-app-i-ever-built-makes-25k-month/case.md) (chơi guitar) và [Erly](../2026-07-05_this-insanely-simple-app-makes-50k-month/case.md) (cố dậy sớm).

**Và quan điểm của anh về rủi ro — rất đáng ngẫm:**

> **"Dù có kiếm được tiền hay không sau khi làm tất cả các bước đó, nếu anh giải được vấn đề cho chính mình thì khả năng cao người khác cũng có vấn đề đó. Họ có trả tiền không? Tôi không biết. Nhưng dù sao, nếu anh build một app cho thứ anh đam mê và giải được một vấn đề, anh đã thắng rồi — vì anh đã giải xong vấn đề của mình."**

> **Đây là cách đóng khung rủi ro rất lành mạnh**, và là lý do kiểu founder này trụ được lâu: kết quả tệ nhất vẫn là một công cụ họ thật sự dùng.

---

## 3. Quy trình 4 bước tìm app triệu đô ⭐

| Bước | Nội dung |
|---|---|
| **1. Tìm vấn đề hoặc cơ hội** | Tạo một note trong điện thoại để ghi ý tưởng. **"Nếu anh không thấy vấn đề nào trong đời mình, không thấy mình đang làm việc gì chậm chạp lặp đi lặp lại — thì anh đang KHÔNG CHÚ Ý."** |
| **2. Xác định giải pháp** | **Phiên bản giải quyết vấn đề một cách TỐI THIỂU nhất.** Cách nhanh nhất là gì? |
| **3. Build** | **"Phần lớn mọi người đang đánh giá quá cao độ khó của việc làm app. AI khiến người ta nhận ra nó thực sự dễ."** |
| **4. Kiếm tiền** | **Superwall** hoặc **RevenueCat**. Anh nói gần như chắc chắn AI tự tích hợp được — *"AI còn điều khiển được cả trình duyệt"* |

> **Câu ở bước 1 là câu đắt nhất case này:** không có ý tưởng không phải vì không có vấn đề — mà vì **không để ý**. Việc cần làm là mở một note và bắt đầu ghi.

---

## 4. Khác biệt giữa 2019 và 2025 — bằng chứng AI đã đổi cuộc chơi ⭐

| | **CardStock (2019)** | **Scanemon (2025)** |
|---|---|---|
| Cách build | Swift + SwiftUI + Core Data, **chủ yếu tra Stack Overflow** | **Để agent của Cursor sinh gần như toàn bộ** |
| Thời gian tới MVP | **~6 tháng** (có 3 tháng gián đoạn giữa chừng) | **MỘT NGÀY** |
| Kết quả | *"nó làm cực kỳ tốt"* | |

> **Sáu tháng xuống một ngày.** Đây là so sánh trực tiếp thuyết phục nhất trên kênh về việc rào cản kỹ thuật đã sập.

**Cách ra mắt CardStock:** build xong, **đăng một bài cập nhật lên Reddit** → có lượt tải gần như ngay lập tức.

**Về đội ngũ ban đầu — chi tiết dễ thương và đáng học:** khi bắt đầu chỉ có mình anh. Anh thấy bạn bè sắp phải đi làm những công việc chán ngắt, nên **rủ họ vào và chia doanh thu ba phần** — dù lúc đó **gần như không có doanh thu** và **họ không biết code mấy**. Anh dạy họ. Ba năm sau, đội đó vẫn ở cùng nhau.

---

## 5. Tech stack

**Sản phẩm:** Swift + SwiftUI + Core Data · **AWS EC2** cho database thẻ · **RevenueCat** cho subscription.

**Công cụ hằng ngày:** Codex (qua ChatGPT), Cursor, Claude, Notion, Slack, Framer (website), Supabase, Railway, Code Rabbit, WhisperFlow, Granola.

---

## 6. Marketing: TikTok slideshow ⭐

> **"Chúng tôi cực kỳ thành công với TikTok slideshow. Nó rất đơn giản, rất dễ lặp lại. Anh nghĩ ra một format, tìm ra cái gì chuyển đổi, tìm ra cái gì kéo view, rồi tìm điểm cân bằng giữa hai thứ đó để đẩy lượt tải."**

**Về đo lường — nhận xét sắc:**
> **"Rất khó quy công, NHƯNG nếu đó là thứ duy nhất anh đang làm thì lại rất dễ quy công."**

> Cùng nguyên lý "một kênh duy nhất = attribution sạch" của [Go Tall](../2026-07-19_this-stupidly-simple-app-makes-100k-month/case.md).

**Công cụ anh nêu tên: Noise** — nền tảng phân phối TikTok slideshow tới creator. Creator nhận một **template**, đăng lên, và **anh trả tiền theo số view họ đạt được**.

> **Trả theo view — lại đúng điều khoản "view guarantee" mà [Erly](../2026-07-05_this-insanely-simple-app-makes-50k-month/case.md) coi là quan trọng nhất.** Hai case độc lập, cùng một cấu trúc hợp đồng. Đây là chuẩn mực nên áp dụng.

**Cách khởi động khi chưa có tiền:** tự đăng TikTok trên tài khoản của mình, hoặc lập vài tài khoản, xem có đủ view không — **đó cũng là một cách validate**, đặc biệt nếu anh có nhiều thời gian hơn tiền.

---

## 7. Lời khuyên cuối

> **"Người ta thường rất sẵn lòng giúp đỡ và chia sẻ thông tin. Người làm được điều gì đó rất thành công thì rất thích nói về việc họ đã thành công thế nào. Đừng lo mình làm phiền người ta — họ sẽ tự báo nếu thấy phiền."**

---

## 8. Nhận định của host — cửa sổ thời gian ⭐

Pat đưa ra một nhận định về thời điểm, đáng ghi lại:

> **Xây business quanh sở thích của mình — ngay lúc này là một cửa sổ ngắn.** Vài năm trước rất khó làm. Và trong tương lai khi mọi thứ tự động hoá hết, không rõ còn khả thi không. Nhưng **AI đang cho phép anh thấy một vấn đề trong đời sống hằng ngày, ship nó trong vài giờ, rồi test ngay ngoài thị trường.**

Producer nhận xét về phong cách của Kyle, và điều này cũng là một bài học:
> Anh **không nghĩ quá nhiều**. Không phân tích quá kỹ. *"Tôi thích mấy tấm thẻ này. Việc này vui với tôi. Nên tôi làm."* Cách tiếp cận đó **rất dễ tiếp cận** — ai cũng có thể tự hỏi *mình thích cái gì, và mình build được gì từ đó.*

---

## 9. Cảnh báo thiên kiến nguồn

- **Con số trên tiêu đề không cộng ra được từ hai app.** Kyle nói CardStock *"khoảng 75K MRR"* và Scanemon *"17K MRR"* — **tổng là $92K**, không phải **$120K** như tiêu đề, và **$92K × 12 = $1,1 triệu**, không phải **$1,5 triệu/năm** như anh tự nói ở phút 01:02. Chênh lệch khoảng 30% và **không ai trong video đối chiếu lại**.
- **Không có dashboard doanh thu nào được chiếu.** Pat yêu cầu rõ ràng: *"anh bật dashboard doanh thu lên được không, tôi muốn cho khán giả thấy cái này là thật"* — nhưng Kyle chỉ **đọc số bằng miệng**, với ngôn ngữ rào đón: *"khoảng 15.000 subscription và LÊN TỚI khoảng 75K MRR"*. Bộ ảnh chụp của video cũng không có màn hình RevenueCat hay App Store Connect nào. **Toàn bộ con số của case này là lời tự khai.**
- **Một con số tự mâu thuẫn không ai hỏi lại:** Scanemon được nói là có **3.400 subscription đang hoạt động** nhưng **16.000 khách mới MỖI THÁNG**. Nếu mỗi tháng có 16.000 khách mới mà tổng đang hoạt động chỉ 3.400, thì hoặc **churn ở mức thảm hoạ**, hoặc "khách mới" thực ra là **lượt tải miễn phí** chứ không phải người trả tiền. Video trình bày con số này như một thành tích (*"nhiều hơn cả CardStock"*) mà không giải thích.
- **Đoạn tài trợ HubSpot ở 03:58–04:43** — *"million-dollar problems database"* / *"Steal 90+ Business Ideas"* qua link `clickhubspot.com`, nhắc lại ở 14:21. **Không liên quan tới Kyle**; đây là lead magnet của kênh. Mô tả video còn viết sai chính con số của mình: *"$120,00K per month"*.
- **Pat tự đưa ra một khẳng định không đúng ở 11:44:** *"những người như anh không nhất thiết phải lên đây chia sẻ... anh cũng chẳng được lợi gì nhiều từ việc này."* Thực tế Kyle nhận **77.000 lượt xem quảng bá miễn phí**, cộng link LinkedIn và cả hai app trong phần mô tả. Đây là cách kênh tự khoác cho mình vai trò trung lập.
- **Chi phí bị hứa rồi bỏ qua.** Chương 06:05 tên là *"Tech stack AND COSTS"* nhưng **không một con số chi phí nào xuất hiện**: server AWS EC2, dữ liệu giá thẻ, tiền trả creator qua Noise, lương 5 người. Không có churn, không có CAC, không có lợi nhuận — và không có phần Apple cắt 15-30%.
- **Tài sản thật của business không được giải thích.** Giá trị của app nằm ở **database định giá và dữ liệu giao dịch gần nhất** — nguồn dữ liệu đó ở đâu ra, tốn bao nhiêu, có được phép dùng không, hoàn toàn không được hỏi. Đây là phần khó sao chép nhất và cũng là phần bị bỏ trắng.
- **Bối cảnh bị làm mờ:** Kyle **được bố mẹ cho đi trại lập trình từ nhỏ**, đã học một khoá phát triển iOS và **đã tự làm một game iOS trước đó**. "Anh chàng bình thường" trong mô tả video thực ra là một lập trình viên có nền từ tuổi thiếu niên. Và **CardStock mất 6 năm** — con số $1,5 triệu/năm là kết quả của 6 năm cộng một đội 5 người, không phải của quy trình 4 bước.

## 10. Áp dụng cho tôi (indie hacker VN)

**Sao chép được:**
- ✅ **Mở note trong điện thoại, ghi mọi việc lặp đi lặp lại chậm chạp** anh gặp mỗi ngày — bước 1 của Kyle, làm được ngay
- ✅ **Lên App Store tìm thử.** Nếu **không có app nào** cho vấn đề anh gặp → tín hiệu mạnh
- ✅ **Bản MVP tối thiểu nhất** giải được vấn đề, không hơn
- ✅ **TikTok slideshow** — dạng nội dung rẻ nhất, dễ lặp lại nhất
- ✅ **Trả creator theo view**, không trả theo bài
- ✅ **Khi công thức chạy, làm lại nó cho ngách kế bên** — CardStock → Scanemon

**Bài học chiến lược quan trọng nhất: app thứ hai.**
Thay vì tìm ý tưởng hoàn toàn mới, anh **lấy đúng cơ chế (quét bằng camera → nhận diện → định giá) và đổi sang một cộng đồng sưu tầm khác.** App thứ hai mất **một ngày** để dựng MVP và đang tăng nhanh hơn app đầu.

**Ngách sưu tầm/định giá ở VN đáng soi (cùng cơ chế):** tem, tiền xu, đồng hồ cũ, giày sneaker, cây cảnh/bonsai, đồ chơi mô hình, sách cũ, thẻ bài. **Mỗi ngách một app, cùng một khuôn.**

**Rào cản thật:**
- ⚠️ **Cần database định giá.** Đây mới là phần khó thật, không phải code. CardStock cần server riêng cho database thẻ và dữ liệu giao dịch gần nhất. **Không có dữ liệu giá thì app vô dụng.**
- ⚠️ **Nhận diện ảnh cần độ chính xác cao** — người sưu tầm sẽ bỏ ngay nếu quét sai
- ⚠️ **Thị trường sưu tầm ở VN nhỏ và ARPU thấp** → nếu làm, nên nhắm thị trường quốc tế bằng tiếng Anh
- ⚠️ **CardStock mất 6 năm** để tới mức này. Scanemon nhanh hơn vì đã có sẵn công thức, đội ngũ và kênh phân phối — **không phải vì ngách dễ hơn.**

**Khi KHÔNG nên dùng mô hình này:**

- **Khi ngách sở thích của anh KHÔNG có một luồng dữ liệu giá công khai, cập nhật liên tục.** Cả hai app đều bán đúng một thứ: *"tấm thẻ này đáng bao nhiêu, và gần đây nó được bán bao nhiêu"*. Không có dữ liệu giao dịch gần nhất thì app chỉ còn là một cuốn album ảnh. Với tem, đồng hồ cũ hay bonsai ở VN, **hãy trả lời câu "dữ liệu giá đến từ đâu" TRƯỚC khi viết dòng code đầu tiên** — đó mới là sản phẩm.
- **Khi anh không thật sự thuộc cộng đồng đó.** Toàn bộ quy trình validate của Kyle chỉ là *"tôi có vấn đề này và App Store không có app nào"*. Lợi thế duy nhất của mô hình là **anh biết người sưu tầm cần gì mà người ngoài không biết**. Nếu anh chọn ngách chỉ vì thấy nó ra tiền, anh mất lợi thế đó và phải thắng bằng marketing — lúc ấy playbook UGC của [Benji](../2026-05-31_i-built-a-30k-month-app-heres-my-exact-process/case.md) hay [Nicole](../2026-05-17_my-two-apps-make-150k-month-each/case.md) mới là thứ anh cần, không phải case này.
- **Khi anh cần kết quả trong vòng 12 tháng.** CardStock mất **6 năm** để tới mức hiện tại. Scanemon dựng MVP trong một ngày nhưng nó thừa hưởng **đội 5 người, database thẻ, kênh TikTok và 6 năm uy tín** đã có sẵn. Nếu anh cần dòng tiền sớm, đây là mô hình sai — nó là mô hình tích luỹ, không phải mô hình bật nhanh.

---

## Nguồn

- Video: [I Built Two Apps That Make $120K/Month](https://www.youtube.com/watch?v=xWnqY2Mav4s) — Starter Story, 07/06/2026, 14:50, 77K views
- Sản phẩm: CardStock · Scanemon
- [`transcript.md`](transcript.md) · [`screenshots/`](screenshots/)
