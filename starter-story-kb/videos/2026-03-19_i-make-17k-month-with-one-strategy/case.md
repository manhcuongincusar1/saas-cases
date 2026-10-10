---
id: 4KfFB-dh71Y
slug: followbuddy-youtube-search-seo
product: FollowBuddy
founder: Ben
tagline: App tìm người unfollow Instagram — $0 quảng cáo, toàn bộ khách đến từ YouTube SEARCH (không phải YouTube "audience")
revenue_usd_month: 17000
revenue_basis: doanh thu 28 ngày gần nhất ~$17.4K; founder nói tròn "20K/tháng" trong cùng video — tôi lấy con số 28 ngày vì nó khớp tiêu đề và có ảnh dashboard
model: micro-saas-subscription
category: social-media-tools
audience: B2C — người dùng Instagram muốn biết ai đã unfollow mình
started: ~2024 (ấp ủ ý tưởng từ 4 năm trước đó)
time_to_first_sale: không nêu; sản phẩm ra mắt sau khi thuê dev ngoài
time_to_scale: ~2 năm từ lúc bắt đầu build tới $17K/tháng
team_size: 2 (founder + 1 dev toàn thời gian)
funding: bootstrapped
main_channel: YouTube Search (SEO video), $0 ads
tech_stack: [React, MongoDB, AWS, SendGrid, RevenueCat, Keywords Everywhere]
key_metrics:
  users: 82.000 tài khoản
  paying_users: 3.128 (2.752 subscription đang hoạt động)
  trials_active: 484
  ad_spend: 0
  yearly_price: 50 USD/năm (gói được đẩy mạnh nhất; còn có gói tuần và tháng)
  channel_views: 40.000 view/28 ngày trên kênh thương hiệu, chủ yếu từ search
  hero_video: 25.000 view sau 7 tháng — quay trong 20 phút
replicability_vn: 5
difficulty: 2
video_url: https://www.youtube.com/watch?v=4KfFB-dh71Y
published: 2026-03-19
views: 53250
---

# FollowBuddy — $17K/tháng bằng một chiến lược lặp đi lặp lại

> **Tóm tắt 30 giây:** Ben làm marketing agency 7 năm, phát hiện hàng loạt người theo dõi anh bị Instagram khoá tài khoản vì dùng app "xem ai unfollow". Anh tìm ra cách làm việc đó **hợp lệ** (dùng tính năng export dữ liệu chính thức của Instagram), ấp ủ ý tưởng **4 năm** vì không đủ tiền thuê dev, cuối cùng build và giờ thu $17K/tháng với **$0 tiền quảng cáo**. Toàn bộ khách đến từ **YouTube Search** — không phải xây kênh, không phải viral, mà là làm đi làm lại cùng một loại video nhắm đúng từ khoá có ý định mua.

![Chiến lược](screenshots/01_00m15s_ch-i-dare-you-to-try-this-strategy.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | ~$17.4K trong 28 ngày (founder nói tròn "20K/tháng") |
| Người dùng | 82.000 |
| Khách trả tiền | 3.128 (2.752 subscription hoạt động) |
| Đang dùng thử | 484 |
| Chi quảng cáo | **$0** |
| Giá | $50/năm (gói chính), có thêm gói tuần/tháng |
| View kênh thương hiệu | 40.000/28 ngày, gần như toàn bộ từ search |

![$0 quảng cáo](screenshots/02_00m52s_usd-0.jpg)

**Lưu ý về số liệu:** trong video có vài con số đọc rời rạc ("14,000 new customers", "1742"). Tôi chỉ giữ những con số có ảnh dashboard xác nhận và nhất quán với nhau. Con số "20K/tháng" founder nói có thể gộp sản phẩm khác hoặc làm tròn lên.

## 2. Nguồn gốc ý tưởng: 4 năm nằm chờ vì thiếu tiền ⭐⭐⭐

Đây là phần đáng giá nhất và ít người nói ra:

1. Ben làm nội dung dạy người ta tăng follower trên Instagram.
2. Người xem bắt đầu coi anh là "bộ phận hỗ trợ Instagram" cá nhân, hỏi anh mọi thứ.
3. Cách đây 3-4 năm, câu hỏi dồn về **một chủ đề duy nhất**: tài khoản của họ bị khoá/bị ban.
4. Điều tra ra: tất cả đều dùng app "xem ai unfollow" — loại app **vi phạm điều khoản Instagram**.
5. Anh tự hỏi: *có cách nào làm việc này mà an toàn không?* Nhóm anh tìm ra cách — dùng chính tính năng **export dữ liệu** mà Instagram cho phép.
6. Anh làm video về cách đó → **hơn 1 triệu view**. Phương pháp này lan rộng đến mức được đặt tên: *compare lists method*.
7. Trớ trêu: anh vô tình xây doanh nghiệp cho người khác — đẩy cả triệu lượt truy cập sang một công cụ sắp xếp danh sách ngẫu nhiên trên mạng. *"He owes me a coffee."*

> **Rồi anh chờ 4 năm.** Không phải vì lười, mà vì **không đủ tiền thuê lập trình viên**. Mỗi năm anh lên Upwork hỏi bạn bè dev: *"Cái này build hết bao nhiêu?"* Đến 2 năm trước, giá xuống đủ thấp — anh mới bấm nút làm.

![Tìm ra ý tưởng](screenshots/04_02m48s_ch-finding-the-business-idea.jpg)

**Vì sao điều này quan trọng với bạn:** rào cản của Ben suốt 4 năm **không phải ý tưởng, không phải phân phối, mà là chi phí build**. Đó chính là rào cản mà AI coding vừa phá sập. Ben nói thẳng: sản phẩm này ra đời trước khi có Cursor/Claude Code.

## 3. Playbook YouTube Search — 4 bước ⭐⭐⭐

Ben lặp lại quy trình này **7 năm liền**, cho mọi sản phẩm anh làm và mọi công ty anh tư vấn.

![Playbook](screenshots/07_06m42s_ch-the-youtube-search-playbook.jpg)

### Bước 1 — Vẽ "thang nhận thức" (awareness ladder) rồi mới tìm từ khoá

Sai lầm lớn nhất trong SaaS: ám ảnh **kiếm khách** mà không dành thời gian nghĩ **khách là ai và họ đang đau gì**.

Thang nhận thức, từ dưới lên:
1. *Chưa biết mình có nhu cầu* ← Ben **bỏ qua** tầng này
2. Biết mình có nhu cầu
3. Biết có một số giải pháp
4. Biết các giải pháp cụ thể
5. Biết lợi ích
6. Sẵn sàng mua

Với mỗi tầng, hỏi: người ở tầng này sẽ hỏi câu gì? Ben trước đây làm trong đầu, giờ dùng ChatGPT để bung ra.

Rồi câu hỏi then chốt: **họ gõ câu đó NHƯ THẾ NÀO?** Nhiều người đoán đúng ý nhưng sai chữ. Dùng **Keywords Everywhere** (hoặc VidIQ) gõ thẳng vào thanh tìm kiếm YouTube để xem lượng tìm thật/tháng.

Chọn 10-20 từ khoá, ưu tiên theo **ý định mua**, không theo lượt tìm.

### Bước 2 — Kiểm tra đối thủ, rồi quay

Với mỗi từ khoá, xem cái gì đang xếp hạng:
- **Không có video liên quan?** Quay ngay hôm nay. *"Kể cả video dở, bạn vẫn có thể lên số 1."*
- **Có đối thủ?** Tìm cách làm tốt hơn. Ben nêu ví dụ cụ thể: nếu video đang top dài 12 phút mà thằng đó lảm nhảm hết 8 phút, anh quay bản **4 phút** — cho người xem nhiều giá trị hơn trên mỗi phút → YouTube nhận tín hiệu tốt hơn → đẩy anh lên nhanh hơn.

> *"Nếu bạn làm SEO đúng, bạn sẽ vào top 3-5 gần như mọi lần, kể cả với kênh hoàn toàn mới."*

### Bước 3 — Đóng gói

- **Tiêu đề:** đưa từ khoá chính lên đầu, nhưng **viết cho người đọc**. Sai lầm phổ biến nhất là viết quá máy móc cho thuật toán. *"Bạn phải nói với máy tính và với con người cùng lúc."*
- **Mở đầu video:** xác nhận ngay người xem đã đến đúng chỗ — lặp lại chính câu họ vừa tìm. Rồi vào việc luôn.
- **Trong video:** trung thực, nói cả **điểm yếu** của sản phẩm. Ben khẳng định điều này **làm tăng tỉ lệ chuyển đổi**.
- **Kết:** nếu đây chưa phải video "sẵn sàng mua", dẫn họ sang video ở tầng tiếp theo của thang nhận thức.
- **Mô tả:** không chỉ dán link app. Hai câu đầu của mô tả **hiện ngay trong kết quả tìm kiếm** — đó là bất động sản miễn phí để tăng tỉ lệ click.
- **Tags:** liệt kê mọi cách diễn đạt của cùng một vấn đề. *"unfollow app instagram", "instagram unfollow app", "instagram unfollow app comparison"...* Càng cụ thể, YouTube càng tin bạn thật sự hiểu vấn đề này.

### Bước 4 — Theo dõi và xếp gạch

Làm đi làm lại **biến thể** của cùng từ khoá cho tới khi lên hạng.

> **Điểm khác biệt then chốt so với Google:** trên Google gần như không thể chiếm nhiều vị trí cho cùng một truy vấn. **Trên YouTube thì được** — nhất là khi bạn chạy nhiều kênh. Mục tiêu: ai gõ biến thể nào của vấn đề đó cũng thấy mặt bạn.

![Cách kiếm khách](screenshots/05_04m20s_ch-how-he-gets-customers.jpg)

## 4. Con số chứng minh: video 20 phút, sống 7 tháng ⭐⭐

Video *"best Instagram unfollower tracker apps"*:
- **25.000 view**, đăng 7 tháng trước
- Quay hết **20 phút**
- Vẫn kéo người xem mới **mỗi 48 giờ** — toàn người đang có vấn đề ngay lúc đó
- Xếp **số 1** cho "unfollower app Instagram" và "best Instagram unfollower tracker"

Vì sao chuyển đổi cao: khách của Ben **đã từng bị lừa bởi các app khác**. Video cho anh cơ hội giải thích vì sao sản phẩm anh khác — điều mà một quảng cáo không làm được.

> **Nguyên tắc:** search traffic là traffic **ý định cao**. *"Tôi không phải thuyết phục ai cả. Họ tự thuyết phục mình rồi. Họ chỉ đang đi tìm giải pháp và tôi muốn là người đưa nó cho họ."*

## 5. Mâu thuẫn với các case khác — và cách hoà giải ⭐⭐

Ben nói thẳng: **"xây audience là lãng phí thời gian"**. Điều này va vào nhiều case khác trong kho:

| Quan điểm | Ai nói | Đúng khi nào |
|---|---|---|
| Xây audience là lãng phí; chỉ cần bám **ý định tìm kiếm** | Ben (case này) | Sản phẩm giải một vấn đề **người ta chủ động đi tìm**, có từ khoá rõ ràng |
| YouTube là **bảo hiểm** cho doanh nghiệp | [Jacky Chow](../2026-03-22_i-make-250k-month-from-13-businesses-after-losing-ev/case.md) | Bạn có nhiều sản phẩm và cần một kênh sở hữu để tung ra bất cứ cái gì |
| Personal brand là động cơ chính | [Marc Lou](../2026-04-26_how-i-work-77k-month-solopreneur/case.md) | Bạn bán cho chính cộng đồng bạn thuộc về (indie hacker bán cho indie hacker) |

**Hoà giải:** cả ba đều dùng YouTube nhưng ở hai chế độ khác nhau. Ben chạy **YouTube như công cụ tìm kiếm** — video không cần hay, không cần mặt đẹp, chỉ cần đúng từ khoá; nó hoạt động ngay cả khi kênh có 0 người đăng ký. Marc Lou và Jacky chạy **YouTube như đài phát** — cần sức hút cá nhân, cần thời gian, nhưng đổi lại tung sản phẩm mới nào cũng có sẵn khán giả.

Nếu bạn ngại lên hình hoặc tiếng Anh chưa tốt: **chế độ của Ben là chế độ dành cho bạn**. Không cần sáng tạo, không cần personality.

Ben cũng đập lại phản biện "anh làm được vì anh đã có kênh sẵn":

> *"Tôi sẽ nói đó là suy nghĩ ngu ngốc. Ngu ngốc vì tôi xây toàn bộ kênh của mình bằng đúng những việc tôi đang nói với bạn. Tôi chỉ có những thứ đó **vì** tôi đã làm điều tôi đang nói. Đó là niềm tin tự giới hạn — và nó chính là thứ đang chặn tất cả những người sẽ cạnh tranh với bạn."*

![Không có kinh nghiệm thì sao](screenshots/09_12m34s_ch-what-if-i-don-t-have-experience.jpg)

## 6. Sản phẩm hoạt động thế nào

Cực kỳ đơn giản — và đó là điểm mạnh:
1. Người dùng vào Instagram, dùng tính năng **export dữ liệu chính thức** để lấy danh sách follower/following.
2. Upload file đó lên FollowBuddy.
3. Bấm "generate results" → so sánh với lần kiểm tra trước.
4. Ra danh sách: ai unfollow, ai không follow lại. Click vào là sang thẳng Instagram.

Ben demo: 319 người unfollow, 264 người không follow lại. *"Bạn sẽ thấy vài thông tin làm bạn đau lòng."*

**Không đụng vào API Instagram, không vi phạm điều khoản.** Toàn bộ giá trị nằm ở chỗ: làm được việc mà các app khác làm, nhưng **không làm người dùng bị khoá tài khoản**.

![Cách hoạt động](screenshots/10_13m12s_ch-how-followbuddy-works.jpg)

## 7. Tech stack

| Hạng mục | Công cụ |
|---|---|
| Frontend | React |
| Database | MongoDB |
| Cloud | AWS |
| Email | SendGrid |
| Thanh toán | **RevenueCat** (~1% trên mỗi giao dịch) |
| Nghiên cứu từ khoá | Keywords Everywhere |

Ben **không phải lập trình viên**. Anh thuê một dev toàn thời gian.

## 8. Lời khuyên về việc không biết code

> *"Hợp tác với người giỏi nhất có thể là con đường đúng. Cho người ta phần chia trong cuộc chơi."*

Cách Ben làm: hứa với dev rằng **sau khi build xong sẽ có việc làm toàn thời gian** — đó là thứ hấp dẫn anh ta. Cách khác: chia doanh thu.

Điểm anh nhấn mạnh cho thời AI:

> *"Với AI, khoảng cách giữa một người tạm ổn và một người xuất sắc đang giãn ra từng ngày. Tôi sẽ làm mọi thứ có thể để làm việc với người xuất sắc, kể cả khi điều đó nghĩa là tôi mang về ít hơn dự tính. Tôi đã trả giá cho việc không nghĩ như vậy — mất khoảng một năm thời gian và rất nhiều tiền."*

Lời khuyên cuối: *"Đừng phức tạp hoá. Nếu bạn có dù chỉ một chút ý tưởng, hãy đi thử. Bạn không cần sáng tạo — bạn chỉ đang đi tới nơi người ta đã ở sẵn và xuất hiện đúng lúc họ đang tìm cách giải quyết vấn đề."*

## 9. Áp dụng cho tôi (indie hacker VN)

**Sao chép được ngay — đây là case dễ áp dụng nhất trong kho tính tới giờ:**

- **Không cần tiền quảng cáo.** $0. Rào cản vốn gần như bằng không.
- **Không cần lên hình đẹp, không cần giọng hay.** Video của Ben là màn hình + giọng nói. Video 20 phút quay xong vẫn ăn 25.000 view.
- **Không cần tiếng Anh hoàn hảo** nếu bạn nhắm **từ khoá tiếng Việt** — thị trường VN gần như trống về YouTube SEO cho công cụ phần mềm.
- **Quy trình có thể lặp một cách máy móc.** Đây là loại công việc bạn giao được cho chính mình vào 2 tiếng buổi tối.

**Cách tôi sẽ bắt đầu tuần này:**
1. Cài Keywords Everywhere, gõ 20 truy vấn quanh vấn đề tôi định giải.
2. Với mỗi truy vấn, xem top YouTube. Đánh dấu cái nào **không có video liên quan** — đó là ô trống.
3. Quay 3 video ngắn (dưới 5 phút), mỗi video một từ khoá, bằng Loom hoặc OBS.
4. Đo sau 30 ngày. Nếu có view từ search → nhân lên.

**Rào cản thật, không tô hồng:**

- **Rủi ro nền tảng ở mức cao.** Toàn bộ sản phẩm sống nhờ tính năng export dữ liệu của Instagram. Meta đổi hoặc bỏ tính năng đó → sản phẩm chết trong một đêm. Đây là cùng loại rủi ro đã xoá sổ mảng content của [Jacky Chow](../2026-03-22_i-make-250k-month-from-13-businesses-after-losing-ev/case.md). Nếu làm mô hình này, hãy coi doanh thu là **tiền thuê**, không phải tài sản — và tái đầu tư sang thứ bạn sở hữu.
- **ARPU $50/năm là thấp.** Cần vài nghìn khách trả tiền mới ra tiền thật. Với thị trường VN, giá này còn phải giảm nữa → cân nhắc nhắm khách quốc tế ngay từ đầu.
- **YouTube SEO có độ trễ.** Video của Ben cần vài tháng để lên hạng. Đây không phải kênh cho người cần doanh thu trong 30 ngày — khác hẳn [Google Ads của Journable](../2026-03-25_i-built-a-100k-month-android-app/case.md) hay [lifetime deal của Floga](../2026-03-29_my-app-made-120k-in-24-hours/case.md).
- **Cửa sổ này sẽ đóng.** Producer Gus nói thẳng: YouTube search đang rẻ vì *"người ta lười quay video, họ thà để AI viết bài SEO"*. Khi điều đó thay đổi, lợi thế mất. Ước tính của họ: còn vài năm.

**Khi nào KHÔNG dùng mô hình này:** khi sản phẩm của bạn giải một vấn đề **người ta chưa biết mình có**. Ben bỏ hẳn tầng "chưa nhận thức" của thang — không ai gõ tìm thứ họ chưa biết là vấn đề. Sản phẩm loại đó cần quảng cáo hoặc nội dung lan truyền, không phải SEO.

## Nguồn

- Video: <https://www.youtube.com/watch?v=4KfFB-dh71Y> (18:00, đăng 19/03/2026, 53.250 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
