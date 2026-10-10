---
id: uvIcGuN2iO8
slug: erly-pushup-alarm
product: Erly
founder: Jake Glacer
tagline: Đồng hồ báo thức phải chống đẩy mới tắt được — AI kiểm tra bằng camera
revenue_usd_month: 50000
revenue_basis: doanh thu 28 ngày gần nhất (founder show dashboard)
model: mobile-app-subscription
category: productivity-habit
audience: B2C — người trẻ khó dậy sớm, sinh viên
started: 2025-12 (launch)
time_to_first_sale: 3 tuần sau video influencer đầu tiên ($1.000)
time_to_scale: 4 tháng → $50K/tháng
team_size: 1 (nay có thêm người hỗ trợ)
funding: bootstrapped
main_channel: influencer marketing (day-in-the-life content) có bảo đảm lượt xem
tech_stack: [Claude Code, Firebase, Superwall, OpenAI, Mixpanel, Grow, SideShift, Instantly, Cal, Agree]
key_metrics:
  downloads_2026: 200.000+
  downloads_30d: 50.000+
  pricing: $29,99/năm hoặc $9,99/tháng, có free trial
  build_time: 19 ngày tới App Store (chưa có tính năng báo thức)
  influencer_cpm: $2-3 (trả theo bảo đảm lượt xem)
  deal: 2-4 video/tháng + cam kết lượt xem
replicability_vn: 4
difficulty: 2
video_url: https://www.youtube.com/watch?v=uvIcGuN2iO8
published: 2026-07-05
views: 309900
tags: [mobile-app, influencer-marketing, api-window, simple-idea, viral-mechanic, ship-fast, marketing-first, power-law, native-content]
---

# Erly — $50K/tháng từ chiếc báo thức bắt bạn chống đẩy

> **Tóm tắt 30 giây:** Jake, 24 tuổi, học kế toán, có CPA, làm ở Big Four hơn một năm. Anh khó dậy sớm nên **nhắn bạn mỗi tối** hứa sẽ gửi video chống đẩy lúc 6h sáng hôm sau để tự ràng buộc mình. Anh biến đúng thói quen đó thành app: **Erly — báo thức chỉ tắt khi bạn chống đẩy thật**, camera AI kiểm tra. **19 ngày** từ commit đầu tới App Store. Launch cuối 2025, **4 tháng sau đạt $50K/tháng**, 200.000+ lượt tải. Anh nói thẳng: *"Build không quan trọng lắm. Marketing mới là thứ quan trọng."*

![](screenshots/03_01m52s_usd-50-000.jpg)

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu 28 ngày gần nhất | **hơn $50.000** |
| Lượt tải 30 ngày | **hơn 50.000** |
| Lượt tải trong 2026 | **200.000+** |
| Giá | **$29,99/năm** hoặc **$9,99/tháng** (có free trial) |
| Thời gian build tới App Store | **19 ngày** |
| Nhân sự | 1 (nay có hỗ trợ) |

**Dòng thời gian:**
```
19 ngày   : từ commit đầu → live App Store (CHƯA có tính năng báo thức)
+19 ngày  : tính năng báo thức lên sóng
+7 ngày   : video influencer đầu tiên → thấy có người mua → ĐÃ VALIDATE
+3 tuần   : $1.000 doanh thu đầu tiên
Tháng 3   : $30.000/tháng
Tháng 4   : $50.000/tháng
```

---

## 2. Ý tưởng đến từ đâu — thói quen tự chế ⭐

Anh khó dậy sớm, nên mỗi tối **nhắn tin cho bạn**: *"mai 6h sáng tao sẽ gửi mày video tao chống đẩy."* Việc đó ràng buộc anh, và **nó hiệu quả**.

MVP ban đầu **hoàn toàn không có báo thức** — chỉ là app ghi nhận cam kết dậy sớm.

### Bước ngoặt: cửa sổ API ⭐⭐

Anh nhận ra app chưa đủ viral, nên **dành trọn một ngày đi bộ và suy nghĩ**, viết ra các hướng đi, rồi chọn thêm tính năng báo thức.

**Thời điểm là tất cả:** ngay trước khi **iOS 26** ra mắt với **AlarmKit API** — lần đầu tiên app bên thứ ba nối được vào **hệ thống báo thức gốc của iPhone**.

> **Trước đó, mọi app báo thức đều "hơi giả" và không đáng tin** — chúng dùng âm thanh trong app và các cách lách. Với app báo thức, **độ tin cậy là tất cả**. AlarmKit xoá bỏ điểm yếu đó.

Pat gọi tên chính xác: **anh đã ship sẵn phiên bản đầu — chỉ vì thấy nó hay ho — rồi một thay đổi nền tảng biến nó thành business.**

**Producer đúc kết thành nguồn ý tưởng dùng được ngay:**

> **Hãy theo dõi các thay đổi API mà Apple hoặc các nền tảng khác mở ra. Mỗi lần có năng lực mới, một loạt app sẽ ra đời — nhưng cửa sổ thời gian rất ngắn.**

Ví dụ họ nêu: API camera mới, widget lập trình được, screen time lập trình được (→ cả loạt app chặn màn hình).

> **Đây là nguồn ý tưởng đáng tin cậy nhất và ít cạnh tranh nhất trong toàn bộ knowledge base.** Xem thêm [Chart Detector AI](../2026-07-23_i-make-50k-per-month-working-5-hours-a-week/case.md) (ChatGPT mở upload ảnh). Việc cần làm: **đọc release notes WWDC và changelog API của OpenAI/Anthropic mỗi kỳ.**

![](screenshots/06_04m15s_ch-finding-the-idea.jpg)

---

## 3. Bộ khung chọn ý tưởng của Jake ⭐

> **"Giải một vấn đề ĐAU theo cách ĐƠN GIẢN, và nó phải TỰ THÂN VIRAL. Nếu bản thân ý tưởng chưa viral, hãy thêm một yếu tố mới lạ để làm nó viral."**

Ba tiêu chí, cùng lý do:

| Tiêu chí | Vì sao |
|---|---|
| **Đau** | Đau thì người ta **trả tiền** |
| **Đơn giản** | Đơn giản thì **dễ thể hiện giá trị trong nội dung rất nhanh** |
| **Tự thân viral** | Có yếu tố khiến người xem phải dừng lại |

**Cách nhận biết một vấn đề đủ đau:**

> **Nếu nó chạy qua đầu bạn ít nhất một lần mỗi ngày, đó gần như chắc chắn là vấn đề rất đau — và bạn đang chủ động tìm cách giải, kể cả khi bạn không nhận ra.**

Anh dẫn chứng: hồi đại học, anh và bạn cùng phòng **nói về chuyện đi ngủ sớm/dậy sớm mỗi tối, không ngày nào không nhắc.**

**Phép thử sau khi có sản phẩm:** mỗi lần anh kể về app, người ta luôn nói *"tôi cần cái này"* hoặc *"tôi không cần nhưng bạn tôi / người yêu tôi cần"*. **Lần nào cũng vậy.**

> **Phép thử này dùng ngay được:** mô tả ý tưởng cho 10 người. Nếu không ai nói "tôi cần" hoặc "người X cần", vấn đề chưa đủ đau.

---

## 4. Triết lý: marketing là mọi thứ ⭐⭐

Đây là thông điệp trung tâm của case:

> **"Build không quan trọng lắm. Cái thật sự quan trọng là marketing. Nên tôi ưu tiên nó hơn mọi thứ."**

**Bộ khung của anh:** ship nhanh, validate nhanh nhất có thể. Anh **biết** mình build được sản phẩm — thứ anh **không biết** là mình có kéo được view hay không. **Cái chưa biết mới là chỗ cần test trước.**

> **"Có quá nhiều người build được app, và với AI thì quá dễ. Nhưng không có mấy người biết marketing, biết cách kéo view. Và nếu không ai biết app của bạn tồn tại, thì nó không tồn tại."**

**Lời khuyên cuối cùng của anh, gọn trong một câu:** *tập trung vào top of funnel, và chỉ top of funnel.*

---

## 5. Playbook influencer marketing ⭐⭐

Đây là **hướng dẫn influencer marketing chi tiết nhất** trên kênh — bổ sung cho playbook paid ads của [Chart Detector AI](../2026-07-23_i-make-50k-per-month-working-5-hours-a-week/case.md).

### Cách tìm và chọn influencer

Anh tìm trên TikTok và Instagram, **gửi rất nhiều DM**. Anh thừa nhận **khởi đầu rất khó, tỉ lệ phản hồi cực thấp**.

**Tiêu chí lựa chọn — điểm mấu chốt:** tìm người đang làm nội dung **"day in the life"** hoặc lifestyle, nơi app **lồng vào được một cách tự nhiên**.

> **Vì sao tiêu chí này quyết định tất cả:**
>
> **"Rất nhiều khi influencer marketing trông quá lộ là quảng cáo. Lúc đó influencer đòi nhiều tiền hơn và cần lý do thuyết phục hơn để nhường một chỗ trên trang của họ. Nhưng nếu bạn tìm được người ĐANG SẴN làm loại nội dung mà app của bạn khớp hoàn hảo vào — như cảnh báo thức trong video day-in-the-life — thì họ sẵn sàng lồng nó vào hơn nhiều."**

**Đây là lời chào hàng thắng:** họ **cứ tiếp tục làm đúng video họ vẫn làm** — chỉ khác là **được trả tiền**.

### Video mẫu chuyển đổi tốt

Format: *POV cuộc sống sinh viên* → thức dậy → chuông reo → chống đẩy → app phân tích → dấu tích xanh, báo thức tắt.

Anh gọi đó là **win-win-win**:
- **Influencer** vẫn làm video của họ và được trả tiền
- **Anh** có lượt tải
- **Người xem** nhận được giải pháp cho vấn đề của họ mà **không có cảm giác đang xem quảng cáo**

**Và cơ chế chuyển đổi thật nằm ở bình luận:** gần như video nào thể hiện tốt cũng có bình luận hỏi *"app tên gì vậy?"* → họ trả lời bên dưới. Trên Instagram, anh **ghim bình luận đó lên đầu**.

### Cấu trúc hợp đồng ⭐

| Yếu tố | Chi tiết |
|---|---|
| **Khối lượng** | **2-4 video/tháng** |
| **Điều khoản quan trọng nhất** | **Bảo đảm lượt xem (view guarantee)** — trả tiền theo lượt xem thực nhận |
| **Giá** | khoảng **$2-3 CPM** |
| **Mức rủi ro** | **Thấp** — chốt trần chi phí, thấy kết quả trong ~1 ngày |

> **"Bảo đảm lượt xem" là chi tiết đáng giá nhất phần này.** Nó chuyển rủi ro từ anh sang influencer. Không có nó, anh trả tiền cho một canh bạc.

**Phân phối theo quy luật luỹ thừa:** phần lớn video chỉ **tàm tạm**. Thỉnh thoảng mới có một video **1 triệu, 2 triệu, 5 triệu view** — và **tiền thật nằm ở đó**.

> **Hệ quả về vốn:** phải chi cho đủ nhiều video để "trúng" được cái lớn. Vài video đầu gần như chắc chắn lỗ.

### Đo lường — chấp nhận sự mù mờ

Anh nói thẳng: **đo lường influencer marketing cực kỳ khó.**

**Cách anh làm — giữ thật đơn giản:**
- Theo dõi **lượt xem** và **quan sát các đợt tăng vọt**
- Lưu dữ liệu lịch sử; khi thấy **vọt view trùng với vọt chuyển đổi**, khá chắc là do video đó
- Coi cả hệ thống như một **hộp đen**: *bỏ vào $5.000, lấy ra $10.000 → chạy được*

> **"Rốt cuộc bạn sẽ lỗ tiền ở một số creator cụ thể, và bạn sẽ không biết là ai. Chuyện đó là không tránh khỏi."**

> **Đây là sự trung thực hiếm thấy.** Đối lập trực tiếp với [Lazy Method](../2026-08-12_the-lazy-method-how-i-build-10k-month-apps/case.md) — Will bỏ hẳn UGC vì **không đo được attribution**. Hai founder, hai lựa chọn ngược nhau trên cùng một vấn đề. **Jake chấp nhận mù mờ để đổi lấy nội dung rẻ và tự nhiên; Will trả giá cao hơn để lấy số liệu sạch.** Anh chọn phe nào tuỳ vào việc anh chịu được sự mơ hồ đến đâu.

![](screenshots/09_09m09s_usd-50-000.jpg)

---

## 6. Tech stack — đầy đủ nhất trên kênh

**Sản phẩm:**

| Công cụ | Vai trò |
|---|---|
| **Claude Code** | Viết code (anh gọi là công cụ tốt nhất) |
| **Firebase** | Database, auth, cloud function |
| **Superwall** | Paywall + subscription |
| **OpenAI** | AI API |
| **Mixpanel** | Analytics trong app |

**Marketing & vận hành — phần ít ai chia sẻ:**

| Công cụ | Vai trò |
|---|---|
| **Grow** | Theo dõi và thanh toán cho influencer |
| **SideShift** | Tìm nguồn, theo dõi, trả tiền UGC creator |
| **Instantly** | Gửi email hàng loạt để tiếp cận influencer |
| **Cal** | Đặt lịch họp |
| **Agree** | Hợp đồng |
| **Google Sheets** | Chạy gần như mọi thứ |
| **QuickBooks** | Kế toán |
| **1Password** | Quản lý mật khẩu |

> Đáng chú ý: **SideShift** cũng chính là công cụ được nhắc tới ở [AngelMatch](../2026-08-23_i-make-32k-month-from-3-simple-boring-websites/case.md) như một database influencer. Hệ sinh thái công cụ quản lý creator đang hình thành rõ nét.

---

## 7. Áp dụng cho tôi (indie hacker VN)

**Đây là một trong những case cân bằng nhất để sao chép:** ý tưởng đơn giản, build nhanh, vốn vừa phải, và có playbook rõ ràng.

**Sao chép được ngay:**
- ✅ **Bộ lọc 3 tiêu chí**: đau + đơn giản + tự thân viral
- ✅ **Phép thử "chạy qua đầu mỗi ngày"** để nhận diện vấn đề đủ đau
- ✅ **Phép thử 10 người**: có ai nói *"tôi cần"* hoặc *"bạn tôi cần"* không
- ✅ **Theo dõi thay đổi API** (WWDC, changelog OpenAI/Anthropic) làm nguồn ý tưởng
- ✅ **Ship trong 3 tuần**, kể cả thiếu tính năng chính
- ✅ **Chọn influencer đang SẴN làm nội dung mà app lồng vào tự nhiên** — không phải người có nhiều follower nhất
- ✅ **Bắt buộc có điều khoản bảo đảm lượt xem** trong hợp đồng
- ✅ **Ghim bình luận trả lời "app tên gì"**

**Vì sao hợp với thị trường VN:**
- Influencer/KOC Việt Nam có CPM rẻ hơn nhiều so với $2-3
- Nội dung "một ngày của tôi" cực phổ biến trên TikTok Việt
- Không cần vốn lớn như paid ads — bắt đầu được với vài triệu đồng
- Ngách thói quen (dậy sớm, tập thể dục, học tập) mang tính phổ quát

**Rào cản thật:**
- ⚠️ **Quy luật luỹ thừa nghĩa là phải chi đủ nhiều** trước khi trúng video lớn. Dự trù lỗ ở giai đoạn đầu.
- ⚠️ **Không đo được chính xác** — phải chấp nhận. Nếu anh cần số liệu sạch, chọn con đường paid ads của [Chart Detector AI](../2026-07-23_i-make-50k-per-month-working-5-hours-a-week/case.md).
- ⚠️ **Tỉ lệ phản hồi DM rất thấp.** Đây là công việc chân tay, gửi hàng trăm tin.
- ⚠️ **Cửa sổ API đóng nhanh.** Khi AlarmKit mở, cả loạt app báo thức ra đời cùng lúc. Phải nhanh.
- ⚠️ ARPU: $29,99/năm khó bán ở VN → cân nhắc làm bản tiếng Anh nhắm quốc tế, hoặc định giá lại theo tháng.

**Ý tưởng biến thể theo đúng công thức "nhiệm vụ để tắt báo thức":** giải toán, quét mã QR ở phòng bếp, đi đủ số bước, chụp ảnh bàn làm việc đã dọn, đọc to một câu. Cơ chế giống hệt, nhiệm vụ khác nhau — và **mỗi nhiệm vụ là một ngách nội dung riêng.**

---

## Nguồn

- Video: [This Insanely Simple App Makes $50K/Month](https://www.youtube.com/watch?v=uvIcGuN2iO8) — Starter Story, 05/07/2026, 19:16, 309K views
- Sản phẩm: [Erly](https://erly.co/)
- Transcript: [`_raw/transcripts/uvIcGuN2iO8.md`](transcript.md) · Ảnh: [`screenshots/uvIcGuN2iO8/`](screenshots/)
