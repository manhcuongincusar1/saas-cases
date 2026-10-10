# Playbook 1 — TÌM Ý TƯỞNG

> Đúc kết từ các case đã phân tích trong [`videos/`](../videos/README.md). Mỗi phương pháp đều dẫn tới case cụ thể để xem chi tiết.

---

## Nguyên tắc bao trùm

Sau khi đọc hàng chục case, có đúng **một mẫu hình lặp lại nhiều nhất**, và nó ngược với trực giác của phần lớn dân kỹ thuật:

> **Gần như không ai thành công nhờ nghĩ ra ý tưởng mới. Họ thành công nhờ nhìn thấy thứ đã tồn tại — rồi đứng ở vị trí đúng để phục vụ nó.**

Và một hệ quả quan trọng nữa:

> **Ý tưởng tốt gần như luôn đến từ nhóm người mà chính bạn thuộc về.**
>
> [Gaurabh](../videos/2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30-day/case.md) **thất bại** 30 ngày đầu vì nhắm YouTube creator — nhóm anh không thuộc về, không có quan hệ, không xin nổi một cuộc gọi. Anh **thành công** khi đổi sang chuyên gia muốn xây thương hiệu cá nhân — đúng chính là anh.
>
> [Matt (Live Tourney)](../videos/2026-07-15_i-quit-my-job-at-meta-to-build-a-30k-month-saas/case.md) nói thẳng vế ngược: rất nhiều người cố build cho nha sĩ, nhưng họ không phải nha sĩ, không biết gì về nha sĩ — ba tháng sau việc trở nên khó và họ bỏ cuộc.

**Bộ lọc số 0, hỏi trước mọi thứ khác:** *Tôi có thuộc về nhóm khách hàng này không? Tôi có nói chuyện được với 10 người trong nhóm này ngay tuần này không?*

---

## 9 nguồn ý tưởng, xếp theo độ tin cậy

### 1. Vấn đề bạn gặp TRONG LÚC làm việc khác ⭐⭐⭐

Đây là nguồn xuất hiện nhiều nhất trong toàn bộ knowledge base.

| Case | Đang làm gì | Vấn đề đụng phải → business |
|---|---|---|
| [Fastlane](../videos/2026-08-30_the-insanely-obvious-secret-behind-this-69k-month-sa/case.md) | Build app | Không biết marketing → công cụ làm content |
| [AngelMatch](../videos/2026-08-23_i-make-32k-month-from-3-simple-boring-websites/case.md) | Gọi vốn cho startup fintech | Dựng danh sách nhà đầu tư quá khổ → database bán $32K/tháng |
| [Live Tourney](../videos/2026-07-15_i-quit-my-job-at-meta-to-build-a-30k-month-saas/case.md) | Chơi giải golf | Sân chấm điểm bằng giấy → SaaS $350K ARR |
| [Erly](../videos/2026-07-05_this-insanely-simple-app-makes-50k-month/case.md) | Cố dậy sớm | Tự chế thói quen nhắn bạn → app $50K/tháng |

**Cách khai thác:** khi bạn tắc ở đâu đó, đừng chỉ bực. Hỏi: **bao nhiêu người khác cũng đang tắc đúng chỗ này?**

> Ở AngelMatch có chi tiết đáng chú ý: **business đầu (app fintech) thất bại, nhưng công cụ tự chế để cứu nó lại thành công.**

### 2. Bảng tính bạn đang dùng ⭐⭐⭐

Nguồn có tỉ lệ hành động cao nhất, và **làm được ngay trong 30 phút**.

[Jack (Profit AI)](../videos/2026-06-24_i-turned-this-spreadsheet-into-a-30k-month-micro-saa/case.md) làm tư vấn nhiều năm, công việc chính là dựng bảng tính cho khách. Anh tải bảng tính xuống CSV, đưa vào AI, bảo *"build cái này"* → **$30K MRR app + $40K MRR dịch vụ**.

**Bài tập làm hôm nay:**
1. Mở Google Drive, liệt kê **20 bảng tính** dùng gần nhất
2. Với mỗi cái hỏi: *ai khác cũng phải làm việc này bằng tay?*
3. Chọn cái **tốn thời gian nhất** và **nhiều người cũng cần**
4. Tải CSV → đưa vào Claude Code → *"build cái này"*

> **Vì sao nguồn này mạnh: ý tưởng đã được validate sẵn** — bạn đã dùng nó cho công việc thật, có người đã trả tiền cho kết quả của nó.
>
> **Và hào bảo vệ không phải code — mà là chuyên môn ngành.** AI dựng được giao diện; chỉ bạn mới biết công thức nào đúng.

### 3. Thay đổi API — cửa sổ ngắn, cạnh tranh gần 0 ⭐⭐⭐

| Case | API mở ra gì | Kết quả |
|---|---|---|
| [Chart Detector AI](../videos/2026-07-23_i-make-50k-per-month-working-5-hours-a-week/case.md) | ChatGPT cho upload ảnh | Bot Telegram → app $56K/tháng |
| [Erly](../videos/2026-07-05_this-insanely-simple-app-makes-50k-month/case.md) | iOS 26 **AlarmKit** — lần đầu app bên thứ ba nối được vào báo thức gốc | App báo thức đáng tin → $50K/tháng |

Producer của kênh đúc kết thành nguồn ý tưởng dùng được ngay:

> **Theo dõi các thay đổi API mà Apple hoặc nền tảng khác mở ra. Mỗi lần có năng lực mới, một loạt app sẽ ra đời — nhưng cửa sổ rất ngắn.**

Ví dụ họ nêu: API camera mới, widget lập trình được, screen time lập trình được (→ cả loạt app chặn màn hình).

**Việc cần làm định kỳ:** đọc release notes WWDC, changelog API của OpenAI/Anthropic, thông báo nền tảng. **Đây là nguồn ý tưởng ít người khai thác nhất.**

### 4. Marketplace mua bán app — ý tưởng đã có giá thị trường ⭐⭐

[Michael (Go Tall)](../videos/2026-07-19_this-stupidly-simple-app-makes-100k-month/case.md) vào **acquire.com** không phải để mua, mà để **đọc ý tưởng đã có doanh thu**. Thấy một app đoán chiều cao rao bán $20.000 → tín hiệu: có người trả tiền thật cho việc này. Anh không mua, anh tự build → **$100K/tháng**.

**Nơi để đọc:** acquire.com, Flippa, MicroAcquire, Indie Hackers. **Miễn phí, không cần mua gì.**

### 5. Bình luận trên mạng xã hội ⭐⭐⭐

Nguồn xuất hiện độc lập ở **bốn case khác nhau** — đây là mẫu hình mạnh nhất.

| Case | Tín hiệu tìm thấy trong bình luận |
|---|---|
| [Go Tall](../videos/2026-07-19_this-stupidly-simple-app-makes-100k-month/case.md) | Dưới mọi video về chiều cao, người ta **tự khai** tuổi, chiều cao bố mẹ — không ai yêu cầu |
| [Tone Adapt](../videos/2026-06-14_the-first-app-i-ever-built-makes-25k-month/case.md) | Người chơi guitar than đúng vấn đề anh gặp, không có giải pháp |
| [Stella](../videos/2026-07-12_she-built-this-340k-month-app-in-60-days/case.md) | *"Ước gì có cái này"*, *"tôi đang vật lộn với chuyện này"* |
| [Flame](../videos/2026-06-21_i-built-a-10k-month-app-with-this-one-system/case.md) | Bình luận **hỏi mua sản phẩm** = có ý định mua (chữ C trong VSC) |

> **Insight sắc nhất, từ Go Tall: hành vi tự khai dữ liệu trong bình luận = nhu cầu chưa được phục vụ.** Khi người lạ tự nguyện đưa bạn input mà không ai yêu cầu, **họ đang xin bạn output**.

Lời khuyên của Pat cho ai hỏi "nên build app gì":
> **"Đừng build app. Đi làm nội dung đi. Rồi bạn sẽ tự tìm ra ý tưởng."**

### 6. Bản địa hoá thứ đã thành công ở nơi khác ⭐⭐⭐

Với founder ngoài Mỹ, đây là **chiến lược có tỉ lệ ăn cao nhất**.

[Tomer (CalBuddy)](../videos/2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) nghe podcast về Cal AI ($1M+/tháng ở Mỹ) và click ngay: **app đã tồn tại không quan trọng, nếu ở thị trường của tôi chưa ai biết đến nó.** Bản tiếng Hebrew cho Israel → **$81K/tháng trong 12 tháng**.

**Điều kiện bắt buộc anh nêu:**
> **Nếu bản địa hoá cho thị trường nhỏ, ngách phải RẤT LỚN.** Thị trường đã nhỏ thì không được chọn thêm vertical hẹp.

Pat xác nhận: **nhiều thị trường quốc gia vẫn còn bỏ trống**, và nhiều founder chạy ads ở thị trường ngoài Mỹ trước vì chỉ số tốt hơn.

### 7. Đối thủ tồn tại nhưng "quá đắt, quá phức tạp" ⭐⭐

Công thức B2B đáng tin cậy nhất, và ít người dùng nhất.

| Case | Đối thủ | Vì sao khách không dùng |
|---|---|---|
| [Live Tourney](../videos/2026-07-15_i-quit-my-job-at-meta-to-build-a-30k-month-saas/case.md) | Golf Genius | *"Quá phức tạp và quá đắt"* |
| [Profit AI](../videos/2026-06-24_i-turned-this-spreadsheet-into-a-30k-month-micro-saa/case.md) | Scenario planner của Deloitte | Tính phí hàng chục nghìn đô, hoàn toàn không tiếp cận được |
| [Flame](../videos/2026-06-21_i-built-a-10k-month-app-with-this-one-system/case.md) | Trị liệu tâm lý cặp đôi | 80% cặp đôi cần cải thiện nhưng **không trả $200/buổi** |

> **Đừng tìm thị trường CHƯA có phần mềm. Hãy tìm thị trường ĐÃ có phần mềm nhưng không ai chịu dùng nó.** Sự tồn tại của đối thủ chứng minh nhu cầu; việc họ bị từ chối chỉ ra khoảng trống.

**Câu hỏi để hỏi bất kỳ doanh nghiệp nhỏ nào:** *"Có phần mềm cho việc này chứ? Sao anh không dùng?"* Câu trả lời **"quá đắt"** hoặc **"quá rắc rối"** chính là bản mô tả sản phẩm của bạn.

### 8. Sở thích của chính bạn — vấn đề "bé xíu" ⭐⭐

[Kian (Tone Adapt)](../videos/2026-06-14_the-first-app-i-ever-built-makes-25k-month/case.md), 21 tuổi, chơi guitar mỗi ngày hơn một năm:

> **"Nếu bạn có một vấn đề bé xíu, thì ngoài kia có ít nhất hàng nghìn, nếu không phải hàng chục nghìn người đang có đúng vấn đề đó."**

**Cách soi một sở thích:** trong bất kỳ sở thích nào cũng có điểm đau bé xíu — chưa có giải pháp, hoặc quy trình quá chậm, hoặc kết quả không chính xác, hoặc bất tiện.

**Lợi thế:** bạn **chính là** khách hàng của mình → không cần nghiên cứu thị trường.

Christian ([3AK](../videos/2026-06-28_how-we-built-this-20k-month-ai-app/case.md)) nói cùng ý theo cách khác:
> **"Lấy thứ anh đã làm hằng ngày và biến nó thành thứ kiếm ra tiền."**

### 9. Nhóm khách bị bỏ quên vì người build không thuộc nhóm đó ⭐⭐

[Sarah (Stella)](../videos/2026-07-12_she-built-this-340k-month-app-in-60-days/case.md) chỉ ra: có cả loạt app **không được thiết kế để giải quyết vấn đề của phụ nữ, vì chúng do đàn ông thiết kế**. Cô cho rằng phần lớn đàn ông sẽ **không bao giờ nghĩ tới** việc build app manifesting.

Producer thừa nhận thẳng: khán giả kênh **93-94% là nam**, và ngách manifesting/tarot/tử vi **hoàn toàn nằm ngoài tầm nhìn của anh** — mà đó là cơ hội lớn.

> **Bộ lọc: chỗ lệch giữa "ai đang build sản phẩm" và "ai đang cần sản phẩm" chính là khoảng trống thị trường.**

---

## Bộ lọc: ý tưởng này có đáng làm không

Gộp từ nhiều case, xếp theo thứ tự nên hỏi:

| # | Câu hỏi | Nguồn | Trượt thì sao |
|---|---|---|---|
| **0** | **Tôi có thuộc về nhóm khách này không?** | Gaurabh, Matt | Rủi ro rất cao — cân nhắc lại |
| **1** | **Giải thích được bằng MỘT ảnh chụp màn hình không?** | [Will Baker](../videos/2026-08-12_the-lazy-method-how-i-build-10k-month-apps/case.md) | Sẽ chết trên feed |
| **2** | Nó có **đau** không? Có **đơn giản** không? Có **tự thân viral** không? | [Jake (Erly)](../videos/2026-07-05_this-insanely-simple-app-makes-50k-month/case.md) | Đau → trả tiền. Đơn giản → dễ làm nội dung |
| **3** | Vấn đề này có **chạy qua đầu tôi ít nhất một lần mỗi ngày** không? | Jake | Chưa đủ đau |
| **4** | Kể cho 10 người — có ai nói **"tôi cần"** hoặc **"bạn tôi cần"** không? | Jake | Chưa đủ đau |
| **5** | Nó chạm được mấy tầng **tháp Maslow**? | [Michael (Go Tall)](../videos/2026-07-19_this-stupidly-simple-app-makes-100k-month/case.md) | Càng nhiều tầng càng dễ bán |
| **6** | Chạy được **khung VSC** không? | [On (Flame)](../videos/2026-06-21_i-built-a-10k-month-app-with-this-one-system/case.md) | Xem [playbook validate](02-validate.md) |
| **7** | Nếu là **directory/database**: người mua có phải **doanh nghiệp** không? | [Rashid](../videos/2026-08-23_i-make-32k-month-from-3-simple-boring-websites/case.md) | B2C directory gần như không sống được |

---

## Ba điều cần bỏ khỏi đầu

**1. "Ý tưởng này có người làm rồi" không phải lý do dừng lại.**
> Michael (Go Tall): *"Vẫn còn app đếm calo kiếm $30K/tháng trong khi đã có Cal AI."*
>
> Will Baker: **designer không phát minh ý tưởng mới — designer lấy thứ đang chạy rồi làm nó tốt hơn.**
>
> Gus nhận xét về CalBuddy: App Store có hàng nghìn app đếm calo, anh đã dùng cả chục cái mà **không hề nghĩ chúng là bản sao của nhau**.

**2. Ý tưởng "kém sang" thường là ý tưởng tốt.**
> Michael: *"Có những viên ngọc chỉ xuất hiện khi bạn sẵn sàng vứt bỏ cái tôi."* Anh kể khi nói mình làm app đoán chiều cao, người ta chỉ đáp *"ừ, chúc may mắn"*.

**3. Ý tưởng không phải phần khó.**
Mọi founder trên kênh, khi được hỏi bí quyết, đều trả lời cùng một thứ: **phân phối**. Xem [playbook 03](03-go-to-market.md).

---

## Ngoại lệ cần biết

[Sarah (Stella)](../videos/2026-07-12_she-built-this-340k-month-app-in-60-days/case.md) nói **ngược lại** với tất cả những điều trên: cô cho rằng mảng app có quá nhiều copy-paste, và điều làm Stella thành công là **app kiểu này chưa hề tồn tại** — cô **phát minh** ra nó.

**Cách hoà giải:** Sarah có **4 triệu follower**. Cô đủ sức **tự tạo nhu cầu** cho thứ chưa ai biết. Người không có phân phối thì **không nên** đánh cược vào ý tưởng chưa được xác nhận.

> **Chiến lược phải khớp với tài sản bạn đang có.**
> - Có khán giả → làm được thứ mới, tự tạo nhu cầu
> - Không có khán giả → **chọn thứ đã được chứng minh**, để thị trường validate hộ

---

## Việc làm trong tuần này

1. **30 phút:** mở Google Drive, liệt kê 20 bảng tính gần nhất → nguồn #2
2. **30 phút:** liệt kê mọi sở thích/cộng đồng bạn thuộc về → nguồn #8, #9
3. **1 giờ:** vào acquire.com đọc 30 listing app nhỏ → nguồn #4
4. **1 giờ:** vào TikTok/Reddit ngách của bạn, **đọc bình luận**, ghi lại mọi câu than phiền và mọi lần người ta tự khai dữ liệu → nguồn #5
5. **30 phút:** liệt kê app đang kiếm $100K+/tháng ở Mỹ, kiểm tra bản tiếng Việt trên App Store → nguồn #6
6. Chạy 3-5 ý tưởng tốt nhất qua **bộ lọc 8 câu** ở trên

→ Tiếp theo: [Playbook 2 — Validate](02-validate.md)
