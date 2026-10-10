---
id: P4QodeA_lQ0
slug: snag-benji-system
product: Snag
founder: Benjamin "Benji" Chen (20 tuổi, NYU) — cùng team 10X Studio
tagline: App tìm đồ miễn phí quanh bạn — sản phẩm thứ 45, và là cái đầu tiên anh dồn toàn lực
revenue_usd_month: 30000
revenue_basis: MRR trên Superwall; tổng thu $80.000+ sau 4 tháng
model: mobile-app-subscription
category: deals-marketplace
audience: B2C — người muốn tìm đồ miễn phí quanh khu vực
started: 2026-01 (launch, ~4 tháng trước khi quay)
time_to_first_sale: không nêu
time_to_scale: 4 tháng → $30K MRR
team_size: nhóm nhỏ (10X Studio)
funding: bootstrapped
main_channel: UGC ở quy mô lớn → chuyển creative thắng sang Meta Ads
tech_stack: [Cursor, Claude Code Max, Superwall, Mixpanel, Supabase, Figma, Loops, GoDaddy]
key_metrics:
  users: 100.000+ đã xác thực
  conversions: 9.000
  total_proceeds: 80.000+
  ratings: 3.300 đánh giá App Store
  build_time: 4-5 giờ/app (chưa tính backend)
  ugc_hit_rate: phỏng vấn 100 creator → 9-10 người dùng được
  ugc_threshold: video >50.000 view mới đem chạy ads
  revenue_per_views: 100.000 view ≈ $1.000-2.000
replicability_vn: 4
difficulty: 3
video_url: https://www.youtube.com/watch?v=P4QodeA_lQ0
published: 2026-05-31
views: 220189
tags: [mobile-app, ugc-at-scale, paid-ads, meta-ads, system, shiny-object-syndrome, reverse-engineer-marketing, playbook, superwall, roas]
---

# Snag — $30K/tháng sau 45 app, và hệ thống đằng sau

> **Tóm tắt 30 giây:** Benji, 20 tuổi, sinh viên NYU, đã build **hơn 45 app trong một năm**. Anh thừa nhận thẳng lý do: **hội chứng vật thể sáng bóng** — app đầu (Pillar) lên 11.000 người dùng gần như không tốn chi phí thu hút, rồi anh bỏ; app thứ hai cũng vậy; rồi 43 cái nữa. Cuối cùng anh **khoá lại và dồn toàn lực vào một sản phẩm**: **Snag** — app tìm đồ miễn phí quanh khu vực. **4 tháng: $30K MRR**, 100.000+ người dùng, $80.000 tổng thu. Giá trị của case này không phải app — mà là **hệ thống lặp lại được**.

![](screenshots/02_01m40s_usd-80-000.jpg)

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| MRR | **$30.000** |
| Tổng thu | **hơn $80.000** |
| Người dùng đã xác thực | **hơn 100.000** |
| Lượt chuyển đổi | **9.000** |
| Đánh giá App Store | **3.300** — anh nhấn mạnh đây là **social proof rất quan trọng** khi quảng bá app tiêu dùng |
| Thời gian | **4 tháng** |
| Gói | tuần / tháng / năm / mua một lần |

**Bối cảnh cá nhân:** lớn lên ở châu Á, học rất giỏi (GPA 4.0), **bán công ty truyền thông đầu tiên với giá sáu chữ số**, từng làm ở Quốc hội Mỹ, quỹ đầu tư, nghiên cứu định lượng — rồi mới chuyển sang làm sản phẩm phần mềm.

---

## 2. Quy trình build 4-5 tiếng ⭐

Điểm khiến case này khác biệt: **anh đảo ngược thứ tự thông thường.**

> **"Thứ có đòn bẩy cao nhất anh có thể làm là tìm được một ý tưởng tốt. NÊN ANH BẮT ĐẦU TỪ MARKETING."**

**Quy trình đúng thứ tự anh làm:**

| Bước | Việc |
|---|---|
| **1** | **Đảo ngược từ tuyên bố giá trị** mà anh muốn thể hiện trong app |
| **2** | Hỏi: **app trông như thế nào thì thu hút được người dùng trong 3 GIÂY?** |
| **3** | Vào **Figma** — wireframe, thiết kế |
| **4** | Đưa thiết kế vào **Claude Code** trong IDE, code ra |

**Tổng: 4-5 tiếng** cho một app tử tế (chưa tính backend).

> **Đây là đảo ngược quan trọng nhất của case:** phần lớn người build hỏi *"tôi làm được gì?"* rồi mới nghĩ cách bán. Benji hỏi *"tôi bán được gì trong 3 giây?"* rồi mới build đúng thứ đó.
>
> Cùng tinh thần với bộ lọc **"giải thích được bằng một ảnh chụp màn hình"** của [Will Baker](../2026-08-12_the-lazy-method-how-i-build-10k-month-apps/case.md).

**Tech stack:** Cursor (IDE) · Claude Code Max (viết gần như toàn bộ) · Supabase (backend) · Superwall (A/B test paywall) · Mixpanel (đo onboarding có đủ tốt không) · Loops (email kéo lại người đã huỷ) · Figma · GoDaddy · tài khoản Apple Developer.

---

## 3. Cách tìm ý tưởng

**Ba nguồn anh dùng:**
1. **YouTube và Twitter** — thấy người ta kiếm tiền từ đủ loại ý tưởng khác nhau, từ đó phát hiện điểm đau **chưa được phục vụ** và **có tác động tới chính anh**
2. **Sensor Tower** — tra thẳng những app đang kiếm nhiều tiền
3. **Sao chép app đó và làm tốt hơn 10%**

**Ví dụ anh tự đưa ra, và nó rất thuyết phục:**
> Sau khi anh ra mắt **Height GPT**, có khoảng **20 app sao chép** xuất hiện. **Nhưng tất cả đều đang kiếm hàng trăm nghìn đô** — vì chúng có **giao diện tốt hơn, marketing tốt hơn, phễu tốt hơn**.

> **"Ý tưởng không đáng giá bao nhiêu nếu anh không đưa được sản phẩm tới người dùng cuối theo một cách TỐT HƠN."**

Pat chốt lại rất chuẩn: **ý tưởng vô giá trị, nhưng đồng thời cũng là tất cả.**

---

## 4. Hệ thống UGC → Paid Ads ⭐⭐⭐

Đây là phần giá trị nhất, và là **quy trình vận hành chi tiết nhất về UGC trong toàn bộ knowledge base**.

### Giai đoạn 1 — Tuyển và lọc creator

| Bước | Chi tiết |
|---|---|
| Tiếp cận | Liên hệ **rất nhiều creator** |
| **Lọc** | **Phỏng vấn từng người** để xem họ có **tố chất viral** bên trong không |
| **Tỉ lệ đạt** | **~10%** — cứ **100 creator phỏng vấn thì được 9-10 người dùng được** |
| Hợp đồng | **Retainer hằng tháng + cấu trúc CPM** |

> **Con số 10% là dữ liệu quý.** Nó cho biết đây là **công việc vận hành thật**: muốn có 10 creator tốt, phải phỏng vấn 100 người. Đây là chỗ hầu hết mọi người bỏ cuộc.

### Giai đoạn 2 — Ngưỡng để chuyển sang ads

> **Nếu video của họ đạt trên 50.000 view, đó là video tốt — đem chạy trên Meta Ads.**

**Kinh tế đơn vị anh chia sẻ:**
> **Cứ 100.000 view, họ thu được khoảng $1.000-2.000 trực tiếp từ lợi nhuận subscription.**

Ví dụ thật: một video **soft-sell** (bán mềm, không lộ quảng cáo) đạt **240.000 view**.

### Giai đoạn 3 — Chạy và scale ads

| Bước | Chi tiết |
|---|---|
| **Test** | Chi **~$50/ngày** để test một creative đáng giữ hay không |
| **Tín hiệu tốt** | **ROAS > 1** hoặc **CTR rất cao** |
| **Scale** | Tăng dần: **$50 → $100 → $200 → $300** |
| **Ví dụ thật** | Một quảng cáo họ đổ tổng **~$3.000** trước khi ROAS chuyển âm |

**Cảnh báo quan trọng anh nêu — hiệu suất giảm dần:**
> **Meta Ads KHÔNG phải cấu trúc tăng trưởng tuyến tính.** Nếu anh có biên lợi nhuận 10% khi chi $100/ngày, **không có nghĩa** chi $200 thì được 20% — vì **hiệu suất biên giảm dần**. Phải theo dõi ads có bị **fatigue** không, và **liên tục bơm thêm creative mới** để test.

> **"Số lượng creative rất quan trọng khi chạy paid ads — để anh có nhiều vé số hơn."**

> **Ẩn dụ "vé số" xuất hiện độc lập ở cả [Lazy Method](../2026-08-12_the-lazy-method-how-i-build-10k-month-apps/case.md).** Hai founder, cùng một cách hiểu về ads.

**Vì sao chuyển từ UGC sang ads:** Pat chỉ ra — làm việc với UGC creator **về lâu dài rất mệt** (tuyển lại, người bỏ đi, quản lý). Chuyển sang paid ads khi nó bắt đầu chạy là **khôn ngoan**.

![](screenshots/08_08m11s_metric.jpg)

---

## 5. Playbook 4 bước nếu bắt đầu lại từ đầu ⭐

Anh nhấn mạnh: **cách này đã hiệu quả ngay từ app ĐẦU TIÊN, khi anh còn là sinh viên không có tiền** — nên nó áp dụng được cho tất cả mọi người.

### Bước 1 — Tìm ý tưởng scale được (đòn bẩy cao nhất)

> **"Một sản phẩm tốt thì không cần nhiều marketing. Người ta chuyển đổi ở tỉ lệ cao hơn, và người ta không muốn huỷ subscription vì sản phẩm mang lại quá nhiều giá trị."**

**Ví dụ với Snag — tuyên bố giá trị cực đơn giản:**
> Trả vài đô mỗi tháng → **được tiếp cận những món đồ trị giá hàng trăm đô**. Đó là lý do tỉ lệ chuyển đổi rất cao.

Pat đồng tình và bổ sung một bộ lọc dùng ngay được:
> **App yêu thích của anh là app giúp anh KIẾM thêm tiền hoặc TIẾT KIỆM tiền.** Tuyên bố giá trị rất đơn giản, và anh sẵn sàng trả.

### Bước 2 — Build

Mở IDE, dùng Claude Code. Anh nói thẳng: khi mới bắt đầu, **rất có thể anh chỉ đang làm app một-mục-đích, kiểu wrapper quanh một API — và điều đó hoàn toàn ổn**. Chỉ cần dùng API cho đúng, app chạy được, và **có cơ chế xác thực người dùng để được App Store duyệt**.

### Bước 3 — Phân phối

> **Nếu không có tiền thuê UGC creator hay influencer, hãy TỰ QUAY.** Anh đã tự quay **hàng nghìn video** cho các app trước. Rồi tìm một editor dựng video ở quy mô lớn, mua gói, chạy chúng thành paid ads.

> **"Kỹ năng lớn nhất hiện nay là khả năng tạo nội dung và biết cách kéo view, kéo tương tác trong cái thế giới thuật toán TikTok mà chúng ta đang sống."**

### Bước 4 — Lặp trên sản phẩm

Làm sản phẩm tốt hơn → **LTV cao hơn, CAC thấp hơn**.
> **"Kinh doanh rốt cuộc là sự trao đổi giá trị. Họ đưa anh tiền, anh đưa họ giá trị."**

---

## 6. Về hội chứng vật thể sáng bóng

Anh không giấu: app đầu (**Pillar**, tự cải thiện bản thân) lên **11.000 người dùng với CAC gần bằng 0** — và anh **dừng vì shiny object syndrome**. App thứ hai (**Height GPT**) cũng vậy. Rồi 43 sản phẩm nữa.

**Bước ngoặt: quyết định khoá lại và dồn vào MỘT sản phẩm** có thể scale theo thời gian, cùng những người giỏi.

> **Đây là bằng chứng ngược cho chính bài học của [Gaurabh](../2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30-day/case.md)** (72 app, $0). Cả hai đều mắc cùng một bệnh; điểm khác là Benji **chọn dừng và dồn lực**, và đó là lúc doanh thu xuất hiện.
>
> **Bài học: số app anh build không quan trọng. Số app anh CHỌN Ở LẠI mới quan trọng.**

**Lời khuyên cuối của anh — về việc chọn môi trường:**
> **"Hãy tự tạo ra may mắn của mình và gặp đúng người."** Anh học được rất nhiều trong vài tháng nhờ gặp Blake Anderson (xem [case Cal AI](../2026-08-16_i-spent-24-hours-with-ios-millionaires/case.md)). Làm việc với người giỏi khiến anh **muốn tự nâng mình lên cho kịp nhịp**.
>
> Anh nói rõ: **không phải networking vô nghĩa** — mà là cứ tiếp tục làm, lặp lại, học từ sai lầm, tới lúc anh đủ sức làm việc cùng người giỏi.

---

## 7. Cảnh báo thiên kiến nguồn

- **Mâu thuẫn lớn nhất nằm ngay trong lời Benji, cách nhau 7 phút.** Ở phút 02:39 anh nói: *"tôi đã BÁN công ty truyền thông đầu tiên với giá SÁU CHỮ SỐ"*, rồi làm ở Quốc hội, quỹ đầu tư, nghiên cứu định lượng. Ở phút 09:53 anh nói: *"cách này đã hiệu quả với cả app đầu tiên của tôi, và lúc đó tôi KHÔNG CÓ TIỀN vì còn là sinh viên — nên nó áp dụng được cho tất cả mọi người."* **Một người vừa bán công ty sáu chữ số không phải "không có tiền", và playbook này không "áp dụng cho tất cả mọi người".**
- **Đoạn tài trợ ở 04:14–04:50 vừa là quảng cáo vừa là phễu bán hàng của chính kênh.** Nội dung là *"iOS Bootcamp miễn phí"* của **Starter Story Build**, nhưng link đi qua `clickhubspot.com`. Được nhắc lại lần nữa ở 13:42 với lời hứa *"chúng tôi sẽ giúp bạn nghĩ ý tưởng, build nó, và đưa lên App Store"*. Nhà tài trợ **không liên quan tới Snag**.
- **Không có ảnh chụp nào cho phần tốn tiền nhất.** Anh có bật Superwall (MRR $30K, 100.000 user, 9.000 conversion, $80K tổng thu) — nhưng **toàn bộ số liệu ads là lời kể miệng**: ROAS, $50/ngày, $3.000/creative, "100.000 view ra $1.000-2.000". Không một màn hình Meta Ads Manager nào. Đây chính là những con số quyết định mô hình có lãi hay không.
- **Kinh tế đơn vị ẩn sau con số đẹp:** 9.000 lượt chuyển đổi tạo ra $80.000, tức **khoảng $8,9 mỗi lượt chuyển đổi** — rất thấp, gợi ý phần lớn khách mua **gói tuần**. Anh dùng **Loops để email kéo lại người đã huỷ**, tức churn là vấn đề thật — nhưng **không một con số churn nào được nêu**, cũng không có tỉ lệ hoàn tiền, chi phí ads tổng, hay phần Apple cắt.
- **Nguồn dữ liệu của Snag — thứ khiến app tồn tại — không được hỏi một câu nào.** App "tìm đồ miễn phí quanh bạn" phải lấy dữ liệu từ đâu đó (nhóm cho tặng, Marketplace, Craigslist...). Video không nêu, và cũng không ai hỏi về rủi ro điều khoản dịch vụ hay tính bền của nguồn đó.
- **Thiên kiến sống sót được đóng gói thành phương pháp.** 45 app trong một năm, **43 cái không được nhắc tên và gần như không tạo doanh thu**. Video dùng con số 45 làm bằng chứng quy trình hiệu quả, nhưng nó cũng là bằng chứng cho tỉ lệ trúng rất thấp. Chính anh gọi 43 cái đó là hệ quả của "hội chứng vật thể sáng bóng".
- **Bối cảnh bị làm mờ:** anh làm trong **10X Studio (có team, có nguồn lực)** chứ không solo, và anh nói thẳng mình học được rất nhiều nhờ **gặp Blake Anderson** (Cal AI). Đây là quyền tiếp cận một mạng lưới rất hẹp, không phải thứ mua được.
- **Chính Pat thừa nhận điểm yếu của kênh** ở phút 06:32: *"đây là điều mọi người sẽ nói trong phần bình luận — Starter Story, các anh không nói đủ về marketing."*

## 8. Áp dụng cho tôi (indie hacker VN)

**Sao chép được ngay:**
- ✅ **Đảo ngược quy trình: bắt đầu từ marketing, không từ tính năng.** Hỏi *"app trông thế nào để hút người dùng trong 3 giây?"* trước khi mở IDE.
- ✅ **Bộ lọc tuyên bố giá trị:** app **giúp kiếm tiền** hoặc **giúp tiết kiệm tiền** có tỉ lệ chuyển đổi cao nhất
- ✅ **Ngưỡng UGC: chỉ đem video >50.000 view sang chạy ads.** Đừng đốt tiền cho creative chưa được chứng minh organic.
- ✅ **Test ads $50/ngày, ROAS > 1 mới scale** — $50 → $100 → $200 → $300
- ✅ **Hiểu hiệu suất biên giảm dần** — gấp đôi ngân sách không gấp đôi lợi nhuận
- ✅ **Chưa có tiền thì TỰ QUAY.** Benji đã tự quay hàng nghìn video.
- ✅ **Sensor Tower** để tra app đang kiếm tiền, rồi làm tốt hơn 10%

**Lợi thế cho VN:**
- ✅ Tự quay video là con đường vốn 0 đồng — hoàn toàn khả thi
- ✅ Chi phí thuê editor ở VN rẻ → dựng video ở quy mô lớn dễ hơn
- ✅ Tỉ lệ lọc creator 10% dễ đạt hơn vì thị trường KOC Việt rất đông

**Rào cản thật:**
- ⚠️ **Snag phụ thuộc dữ liệu đồ miễn phí theo khu vực** — mô hình này khó bê nguyên sang VN; hãy lấy **hệ thống**, không lấy **ý tưởng**
- ⚠️ **Phỏng vấn 100 creator để chọn 10** là khối lượng vận hành lớn, cần người
- ⚠️ **Cần vốn cho giai đoạn ads** — $3.000 cho một creative trước khi ROAS âm
- ⚠️ Anh làm trong **10X Studio** (có team, có nguồn lực) — không phải solo
- ⚠️ Anh có nền tảng đặc biệt (đã bán một công ty sáu chữ số trước đó)

**Khi KHÔNG nên dùng mô hình này:**

- **Khi anh không có ít nhất $3.000-5.000 sẵn sàng đốt vào creative KHÔNG sinh lời.** Benji đổ **$3.000 vào MỘT quảng cáo** trước khi ROAS chuyển âm, và chính anh gọi mỗi creative là "một vé số" — nghĩa là phải mua nhiều vé. Cộng thêm retainer hằng tháng cho creator, đây là mô hình cần vốn lưu động, không phải mô hình $0.
- **Khi giá trị sản phẩm của anh không hiện ra trong 3 giây trên màn hình điện thoại.** Toàn bộ quy trình đảo ngược của anh bắt đầu từ câu hỏi *"app trông thế nào để hút người dùng trong 3 giây?"*. Snag qua được vì lời hứa là "trả vài đô, nhận đồ trị giá hàng trăm đô". Một công cụ B2B, một dashboard, một API — không có 3 giây nào để bán, và nên đi đường của [Savvy Nomad](../2026-05-21_i-make-1-7m-year-in-the-most-boring-niche-imaginable/case.md) (giá trị định lượng, bán ít) thay vì đường UGC.
- **Khi sản phẩm của anh phụ thuộc vào một nguồn dữ liệu bên thứ ba mà anh không kiểm soát.** Snag sống nhờ luồng đồ miễn phí theo khu vực — nguồn đó không được nêu trong video, và ở Việt Nam không có bản tương đương. **Hãy lấy hệ thống UGC → ads, đừng lấy ý tưởng.** Nếu anh định đi đường creator dài hạn, mô hình đào tạo của [Nicole](../2026-05-17_my-two-apps-make-150k-month-each/case.md) (tạo ra creator giỏi) có đòn bẩy cao hơn cách lọc 100 lấy 10 của Benji.

---

## Nguồn

- Video: [I Built A $30K/Month App: Here's My Exact Process](https://www.youtube.com/watch?v=P4QodeA_lQ0) — Starter Story, 31/05/2026, 14:13, 220K views
- Sản phẩm: Snag (10X Studio)
- [`transcript.md`](transcript.md) · [`screenshots/`](screenshots/)
