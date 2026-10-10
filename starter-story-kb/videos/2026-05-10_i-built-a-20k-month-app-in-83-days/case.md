---
id: r4R_Hlw7sbo
slug: once-commitment-metric
product: Once
founder: Brian Shin (+ bạn gái, đồng sáng lập)
tagline: Máy ảnh dùng một lần dạng số cho sự kiện — ảnh chỉ hiện ra sau, như phim chụp thật
revenue_usd_month: 22000
revenue_basis: doanh thu tháng hiện tại; đạt $20K/tháng trong 83 ngày kể từ launch
model: b2c-usage-based
category: social-events
audience: B2C — người tổ chức đám cưới, sinh nhật, sự kiện công ty
started: 2025-12 (launch)
time_to_first_sale: validate TRƯỚC khi viết dòng code nào
time_to_scale: 83 ngày → $20K/tháng
team_size: 2
funding: bootstrapped
main_channel: cold outreach thủ công qua hashtag Instagram + mạng lưới cá nhân
tech_stack: [Claude Code, Conductor, Figma, Supabase, Vercel]
key_metrics:
  weekly_active_users: 10.000-12.000
  events_february: hơn 300
  events_march: ~700
  pricing: theo số khách mời — 10 khách $2; 150 khách $50
  cold_outreach: 250-300 người nhắn → 15 phản hồi → 12 sự kiện chốt
replicability_vn: 5
difficulty: 2
video_url: https://www.youtube.com/watch?v=r4R_Hlw7sbo
published: 2026-05-10
views: 287001
tags: [validation, commitment-metric, pre-validation, cold-outreach, mom-test, b2c, usage-based-pricing, design-craft, ship-fast, no-ai-design]
---

# Once — "commitment metric": validate TRƯỚC khi viết dòng code đầu tiên

> **Tóm tắt 30 giây:** Brian từng đồng sáng lập một startup B2B có vốn đầu tư mạo hiểm, 50 người, nặng về bán hàng. Lần này anh muốn **toàn quyền kiểm soát**, nên cùng bạn gái làm **Once** — máy ảnh dùng một lần dạng số cho sự kiện: khách quét mã tham gia, chụp ảnh, và **ảnh chỉ hiện ra vào thời điểm bạn đặt** — mô phỏng đúng cảm giác chờ tráng phim. **$20K/tháng trong 83 ngày.** Nhưng điều đáng học nhất không phải app — mà là cách anh **validate trước khi viết một dòng code**, bằng thứ anh gọi là **commitment metric**.

![](screenshots/03_02m23s_usd-22-000.jpg)

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu tháng | **~$22.000** |
| Thời gian đạt $20K/tháng | **83 ngày** |
| Người dùng hoạt động tuần | **10.000-12.000** |
| Sự kiện tháng 2 | **hơn 300** |
| Sự kiện tháng 3 | **~700** |

**Định giá theo mức sử dụng — rất hợp lý:**

| Quy mô | Giá |
|---|---|
| Sinh nhật nhỏ 10 người | **$2** |
| Đám cưới 150 người | **$50** |

> **Càng nhiều khách mời → gói càng cao.** Giá gắn thẳng với giá trị nhận được, và mức khởi điểm $2 gần như không có rào cản tâm lý.

---

## 2. Ý tưởng — từ một thói quen du lịch

Anh và bạn gái đi **7-8 nước trong một năm**, và mỗi thành phố họ đều **mang theo một máy ảnh dùng một lần**.

> Máy ảnh dùng một lần là **sản phẩm rất đơn giản, nhưng kỳ diệu ở chỗ nó có RẤT NHIỀU GIỚI HẠN**: không xem được ảnh ngay, số kiểu chụp có hạn. **Chính những giới hạn đó khiến trải nghiệm trở nên thật hơn.**
>
> Ý tưởng: **tại sao không làm một trải nghiệm số tái tạo đúng cảm giác đó?**

> **Bài học thiết kế đáng chú ý: GIỚI HẠN chính là tính năng.** Ngược hoàn toàn với bản năng thông thường (thêm tính năng, bỏ ràng buộc). Ở đây, sự khan hiếm và chờ đợi mới là thứ tạo ra cảm xúc — và tạo ra lý do để chia sẻ.

---

## 3. Cách validate — trước khi có code ⭐⭐⭐

Đây là đóng góp lớn nhất của case, và Pat nói anh **chưa từng thấy ai làm theo cách này**.

### Phần 1 — Vét sạch mạng lưới cá nhân

> Anh mở **ba tab: X, LinkedIn, và Instagram/Facebook**. Đi qua **từng người** trong danh sách bạn bè và xem ai có thể phù hợp — **khoanh tròn mọi người sắp có sự kiện**.

**Kết quả: 4 người bạn đồng ý thử** — một tiệc Halloween, một sinh nhật, một đám cưới, một sự kiện networking.

### Phần 2 — Ra ngoài vòng tròn thân quen ⭐

> Vì Once dùng được ở tiệc, sự kiện, đám cưới — anh **tìm trên Instagram theo hashtag** (#wedding, #birthdayparty). Anh lập danh sách **250-300 người** trên nhiều nền tảng.
>
> Anh viết **một tin nhắn lạnh rất đơn giản, tối đa 2-3 câu**, đủ để gây chú ý và chào ý tưởng.

**Kết quả — con số rất đáng nhớ:**

| Số người nhắn | Phản hồi | Sự kiện chốt |
|---|---|---|
| **250-300** | **~15** | **~12 sự kiện trong một tháng** |

> **Tỉ lệ ~5% phản hồi và ~4% chốt.** Đây là dữ liệu thật để anh đặt kỳ vọng: muốn 12 khách đầu tiên, hãy chuẩn bị nhắn 250 người.

Đó là lúc họ quyết định: **thứ này có tiềm năng thị trường — làm tới.**

### Bản MVP đầu: một web app, và nó hỏng liên tục

Bản đầu mất **1-2 tuần**, là **web app** chỉ có tính năng cốt lõi. Bạn anh có tiệc Halloween sắp tới → họ **in mã mời ra giấy** để mọi người tham gia chụp ảnh.

> **Nó hỏng nhiều lần trong sự kiện** — nhưng họ đã validate được điều cốt lõi: **người ta thích chụp ảnh của nhau vào một album chung, theo trải nghiệm mô phỏng máy ảnh dùng một lần.**
>
> **"Nó không cần hoàn hảo. Nó chỉ cần đủ hoàn hảo để kiểm chứng đúng thứ chúng tôi muốn kiểm chứng."**

Sau khi validate, họ **vứt bỏ hoàn toàn bản đầu tiên**.

---

## 4. Playbook 5 bước "commitment metric" ⭐⭐⭐

### Bước 1 — Định nghĩa chỉ số cam kết

**Cam kết có hai chiều:**

| Chiều | Nội dung |
|---|---|
| **Cam kết của chính anh** | Đặt **một ngày cụ thể** và **một con số cụ thể** (khách hàng, hoặc chỉ số khác) anh muốn thấy trong khoảng thời gian đó. Ít nhất anh biết mình đang dành một **số ngày hữu hạn** để validate. |
| **Cam kết của người dùng** | **KHÔNG nhất thiết phải là thanh toán.** |

> **Đây là phần tinh tế nhất.** Với Once, chỉ số cam kết là **người tổ chức sự kiện dùng sản phẩm trong sự kiện của họ**.
>
> **"Tuỳ ngành dọc, tuỳ sản phẩm, phải có một chỉ số nào đó thật sự đại diện cho VIỆC SỬ DỤNG."**

### Bước 2 — Vét sạch mạng lưới cá nhân

Mở hết mọi tài khoản mạng xã hội, tìm ai liên quan tới chân dung khách hàng lý tưởng.

**Và cảnh báo bắt buộc — The Mom Test:**
> Nếu anh validate sản phẩm với **mẹ mình**, bà sẽ rất hào hứng với bất cứ thứ gì anh làm. **Đó không phải cách validate.**
>
> **"Hãy thành thật với chính mình, để chắc chắn rằng anh đang VALIDATE sản phẩm chứ không phải đang đi TÌM SỰ ĐỘNG VIÊN cho nó."**

> Cùng nguyên tắc với [Fastlane](../2026-08-30_the-insanely-obvious-secret-behind-this-69k-month-sa/case.md) — xem [playbook validate](../../playbooks/02-validate.md).

### Bước 3 — Dựng mockup nhanh

> **Đừng dành quá 2-3 ngày cho việc này.** Lên Figma hoặc dùng công cụ AI. **Dù nó tệ đến đâu**, chỉ cần tìm ra thứ đơn giản nhất có thể đưa cho người dùng xem.

### Bước 4 — Đi tới nơi người dùng đang sống ⭐

> Bắt đầu từ số 0. Lên **Reddit** và học mọi ngóc ngách của Reddit, nếu Reddit là nơi cần đến. Hoặc TikTok. Hoặc YouTube.
>
> **Vì kênh này không chỉ dùng để validate — nếu validate thành công, nó sẽ là KÊNH MARKETING CHÍNH của anh về sau.**

**Và câu đắt nhất của case:**
> **"Điều tôi vẫn nói với bạn bè và các founder khác là: nếu anh chưa từng bị BAN khỏi các nền tảng đó ít nhất HAI LẦN, thì anh chưa thử đủ."**

### Bước 5 — Đặt con số đủ để tự tin

> Với họ, mục tiêu rất đơn giản: **trước khi viết một dòng code, cần 10 sự kiện có NGÀY THẬT, có CAM KẾT THẬT rằng họ sẽ dùng sản phẩm.**
>
> Việc cam kết dùng nó trong một sự kiện **có bạn bè, gia đình, người thân ở đó** — họ cho rằng đó đã là một cam kết đủ lớn, **gần như tương đương với việc trả tiền.**

> **Đây là insight cốt lõi: tìm ra hành động nào TỐN KÉM VỀ MẶT XÃ HỘI đối với khách hàng.** Đặt uy tín của mình vào trước mặt bạn bè và gia đình là một cam kết thật — đôi khi mạnh hơn cả việc trả vài đô.

![](screenshots/08_08m42s_ch-validation-playbook.jpg)

---

## 5. Quan điểm gây tranh cãi: KHÔNG dùng AI cho thiết kế ⭐

> **"Có thể đây là quan điểm gây tranh cãi, nhưng sau khi validate bằng web app, chúng tôi VỨT BỎ phiên bản đầu tiên."**
>
> **"Tôi tin app tiêu dùng về bản chất là một NGHỀ THỦ CÔNG. Tôi dùng rất nhiều AI cho dev, cho tài chính, cho mọi thứ — nhưng cho THIẾT KẾ thì chúng tôi không bao giờ dùng AI. Vì thiết kế đòi hỏi GU. Và càng có chính kiến rõ ràng thì thiết kế ra càng tốt."**

Pat đồng tình: với app B2C, anh muốn nó **có cảm giác** — đây không chỉ là tiện ích, mà là niềm vui và sự sáng tạo.

> **Cùng kết luận với [Cat on Chair](../2026-07-26_this-simple-app-makes-18k-month/case.md)** — hào bảo vệ là **cảm giác thủ công**, thứ AI chưa làm được. Hai case độc lập, cùng một quan điểm.

**Tech stack:** Figma (thiết kế) · **Claude Code** (anh nói *"tôi sống trong Claude Code"*) · **Conductor** — công cụ chạy **nhiều instance Claude Code song song trên các work tree khác nhau** · Supabase (database + backend) · Vercel (phần web).

---

## 6. Lời khuyên cuối

> **"Điều quan trọng nhất là NGỪNG SUY NGHĨ QUÁ NHIỀU và cứ launch."**
>
> Anh từng là người nghĩ quá nhiều: *làm marketing thế nào? bán hàng thế nào?* — nhưng nhận ra **đó không phải những thứ quan trọng nhất khi đi từ 0 tới 1**.
>
> **"Thay vào đó, hãy dành thời gian đó để nói chuyện với nhiều người dùng hơn, và xây bản đầu tiên trong một hai tuần là tối đa, rồi launch. Vì mọi giả định và phỏng đoán của anh có thể thành vô nghĩa ngay khi launch. Anh có thể đang giải một vấn đề HOÀN TOÀN KHÁC so với điều anh nghĩ ban đầu."**

---

## 7. Nhận xét của producer — điểm đáng suy nghĩ nhất ⭐

Producer thú nhận rất thật:

> Anh **rùng mình** khi nghĩ tới việc nhắn tin cho một người ngẫu nhiên anh quen 10 năm trước để hỏi *"tôi vừa làm cái này, anh thấy sao?"*

**Và Pat đưa ra phân tích quan trọng nhất của cả video:**

> **Ngày trước, khi build còn KHÓ, anh BUỘC PHẢI hỏi người ta trước rồi mới quyết định build. Đó là cách tự nhiên — vì anh không build nổi.**
>
> **Bây giờ, các công cụ AI trở thành một cái NẠNG: "ồ, mình có ý tưởng hay" — và thay vì đi nói chuyện với người ta, mình chỉ việc build nó.** Rồi anh build xong, nó chạy, nó ngon. **Và rồi anh không biết làm gì tiếp. Anh sợ. Nó trông không đẹp như anh muốn.** Thế là anh mất động lực làm đúng cái việc cực kỳ quan trọng kia — chia sẻ nó với những người lạ mà anh chưa nói chuyện suốt 10 năm.

> **"Đây mới là phần đáng sợ. Trong một thế giới mà ai cũng build được mọi thứ trong một giờ, ĐÂY chính là nước sốt bí mật: đi ra ngoài và đặt chỉ số cam kết của anh — 'tôi cần 10 người nói rằng họ sẽ dùng thứ này trước khi tôi làm xong nó'."**

---

## 8. Áp dụng cho tôi (indie hacker VN)

**Đây là playbook validate tốt nhất trong knowledge base cho sản phẩm B2C, và chi phí bằng 0.**

**Làm ngay tuần này:**

| Bước | Việc | Thời gian |
|---|---|---|
| **1** | Định nghĩa **chỉ số cam kết**: ngày cụ thể + con số cụ thể. Chọn hành động **tốn kém về mặt xã hội** với khách, không nhất thiết là tiền | 30 phút |
| **2** | Mở X + LinkedIn + Facebook, **đi qua từng người trong danh sách bạn**, khoanh ai phù hợp | 2 giờ |
| **3** | Dựng mockup — **tối đa 2-3 ngày**, dù xấu | 2-3 ngày |
| **4** | **Tìm 250-300 người lạ** qua hashtag/group, nhắn tin **2-3 câu** | 1 tuần |
| **5** | Đạt con số cam kết → **mới bắt đầu build** | |

**Kỳ vọng thực tế theo dữ liệu của anh:** nhắn **250-300** → phản hồi **~15** → chốt **~12**.

**Vì sao rất hợp với VN:**
- ✅ **Chi phí bằng 0** — chỉ tốn thời gian
- ✅ **Hashtag Instagram và group Facebook Việt Nam** rất dễ tìm người tổ chức sự kiện, cưới hỏi, sinh nhật
- ✅ **Định giá theo mức dùng từ $2** — mô hình giá này hợp với thị trường nhạy cảm về giá như VN
- ✅ **Ngách sự kiện/cưới hỏi ở VN rất lớn** và chưa có sản phẩm dạng này bằng tiếng Việt
- ✅ Đội 2 người

**Rào cản thật:**
- ⚠️ **Cold outreach là việc khó về mặt tâm lý** — producer thừa nhận thẳng. Đây là rào cản thật, không phải kỹ thuật.
- ⚠️ **Có thể bị ban tài khoản** — anh coi đó là dấu hiệu đã thử đủ, nhưng cần chuẩn bị tài khoản dự phòng
- ⚠️ **Cần gu thẩm mỹ thật** nếu theo triết lý "không dùng AI cho thiết kế". Không có người có gu thì phần này không sao chép được.
- ⚠️ **83 ngày là rất mới** — chưa chứng minh được độ bền hay retention
- ⚠️ Mô hình theo sự kiện có tính **mùa vụ** (mùa cưới) — doanh thu không đều

---

## Nguồn

- Video: [I Built a $20K/Month App in 83 Days](https://www.youtube.com/watch?v=r4R_Hlw7sbo) — Starter Story, 10/05/2026, 16:14, 287K views
- Sản phẩm: Once
- [`transcript.md`](transcript.md) · [`screenshots/`](screenshots/)
