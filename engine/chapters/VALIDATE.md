# Chương 2 — Validate: thực tế trước, công thức sau

> Số đếm lấy từ `kb/data/kb.duckdb` (209 video 2025+; 186 case full). Câu truy vấn: `engine/chapters/validate.sql` (các truy vấn riêng của từng công thức nằm ở `engine/recipes/<id>.extra.sql`).
> Ngưỡng và thang điểm của chương này **không viết lại**: xem `VALIDATE.md` ở gốc dự án (4 cổng, thang tín hiệu 0–8).
> Hai điều phải đọc cùng mọi con số dưới đây: (1) **kho chỉ chứa người thắng**, nên không có số người làm y hệt mà thất bại; (2) **"không nêu" không có nghĩa "không có"**, vì video không kể hết.
> Một điều thứ ba cho riêng chương này: 186 là số cặp (video, case); 175 sản phẩm khác nhau, vì một sản phẩm có thể xuất hiện ở nhiều video (Payout ba video, Cardstock và Curiosity Quench hai video mỗi cái).

## Thực tế: founder trong kho validate bằng cách nào, và video kể được bao nhiêu

### 1. "101/186 không có bằng chứng nhu cầu trước launch" nghĩa là video không kể, không phải founder không validate

Trường nhu cầu của kho (`demand_kind`) chỉ ghi loại bằng chứng *mà video kể* về trước lần ra mắt công khai đầu tiên. Trên 186 case full:

| Loại bằng chứng (`demand_kind`) | Mức theo thang 0–8 | Số case |
|---|---|---|
| Video không nêu | — | **101** |
| Tự kể nỗi đau hoặc waitlist miễn phí (`self_reported_pain_or_free_waitlist`) | 4 | 26 |
| Build trước rồi mới chờ (`built_first`) | 0 | 23 |
| View nội dung (`content_views`) | 2 | 10 |
| Có người trả tiền (`paid`) | 8 | 10 |
| App tương tự đang bán có doanh thu (`similar_product_revenue`) | 3 | 7 |
| Bạn bè khen (`friends_praise`) | 1 | 5 |
| Comment hỏi mua (`buy_intent_comments`) | 5 | 2 |
| Phỏng vấn lặp lại (`repeated_interviews`) | 6 | 1 |
| Người lạ chủ động xin (`inbound_requests`) | 7 | 1 |

Đọc đúng con số này cần thêm ba điều:
- **Host ít hỏi chuyện validate.** Theo `kb/QUESTIONS.md` (đo trên tiêu đề chương của 171 video Starter Story và 42 video Superwall có chương, xếp nhóm bằng từ khoá nên chỉ là ước lượng; mẫu này không trùng 209 video của kho): câu hỏi "How did you validate the idea?" có ở khoảng **18%** số tập Starter Story và **7%** số tập Superwall, trong khi câu hỏi về build có ở 78% và 55%. Video không kể validate một phần vì host không hỏi.
- **Một phần "không nêu" thực ra có kể việc.** Trước lượt sửa kb ngày 16/11, 18 case không nêu có step ở chặng validate. Sau khi điền `demand_signal` cho 4 case có câu nguyên văn đỡ được và tín hiệu đến trước lần ra mắt đầu tiên (Sheets Resume, Tech Lockdown, Stoppr, NeuroGum), còn 14 case có step validate mà trường nhu cầu để trống (ví dụ Floga và Make Logo AI: tiền đến ngay lúc ra mắt, không phải trước đó). Trường nhu cầu vẫn có thể đếm thiếu; số 101 là cận trên của 'video không kể'.
- **Khi có nêu, đa số ở mức thấp.** 85 case có nêu loại bằng chứng; chỉ 14 (mức 5 trở lên: comment hỏi mua 2, phỏng vấn lặp 1, người lạ xin 1, trả tiền 10) tức 14/85, và 26 trong số 85 chỉ là tự kể nỗi đau hoặc waitlist miễn phí (mức 4).

Kết luận được: video trong kho phần lớn không kể bằng chứng nhu cầu. Kết luận *không* được: "founder trong kho không validate", hay "validate không cần thiết".

### 2. "Build trước rồi chờ": 23 case, ghi nhận (không phải lời khuyên)

23 case full mà video kể là build xong rồi mới đi tìm hoặc chờ người dùng. Ghi nhận những gì kho có:

- **Kho chỉ chứa người thắng.** 23 founder này lên được kênh. Người build trước rồi không ai dùng và bỏ cuộc thì không có mặt, nên không thể suy ra "build trước ổn".
- **Đây là điều video kể, không chắc là điều đã xảy ra.** Hai sản phẩm trong 23 case có video khác kể validate: Curiosity Quench (video kia nói đăng TikTok 60 giây về ý tưởng khi chưa build, 15 người comment xin) và CardStock (video kia nói đăng bài lên subreddit thẻ bóng chày trước khi build, 10–15 người trả lời muốn dùng). Mỗi video chỉ kể một phần câu chuyện.
- **Cái giá được kể ra.** NGL: build khoảng một tháng, rồi gần 6 tháng không ai dùng (câu nguyên văn: "We built the app in about a month, but then it was like 6 months of nobody using it."). Vault Air: đưa app ra mà không biết có ai dùng không, tháng đầu kiếm $66. Savewise: đăng Product Hunt, Hacker News và Indie Hackers, bounce 95–96%; gửi 300–400 tin cho influencer, chỉ một người trả lời. Visualizee: bản V1 mất khoảng 5 tháng ngoài giờ rồi mới nghe người dùng nói quá khó. Live Tourney: bắt đầu khoảng 4 năm trước làm cho giải của chính mình.
- **Thời gian build rất khác nhau.** Theo trường `build_time`: nhiều case build ngắn (Yaphone và GeoSports trong một cuối tuần; App Alchemy, Halo AI, Vault Air, Bank Statement Converter từ một đến vài tuần; NGL và CutCoach khoảng một tháng) và vài case build nhiều tháng (Vugola khoảng 4, Visualizee khoảng 5, CardStock khoảng 6, Maxed AI khoảng 6, AbMax 2 tháng cho bản Lovable đầu tiên, rồi bỏ và rebuild).

**`prior_failures` của chính 23 case này.** 9/23 case có `prior_failures_count` > 0 (tổng 12 lần); 13/23 có mô tả `prior_failures_what`. Để so: trên cả 186 case full là 78/186 (42%) và 106/186 (57%); 9/23 là 39% và 13/23 là 57%, tức **không khác phần còn lại**. Đọc phần mô tả:
- Có số lần ghi rõ: Savewise 2 (đăng Product Hunt, HN, IH, và 300–400 tin influencer), CutCoach 2 (các app trước không ra tiền vì không làm marketing), Money AI 2 (một app làm 2 năm không ai quan tâm, cùng các side project khác), Payout 1 (video về vụ class action nhiều view nhưng ít đăng ký), Voicy 1 (Meet Waves đạt 5K MRR nhưng không bùng nổ vì không làm marketing), Links 1 (Visual vật lộn tìm market fit), AbMax 1 (bản Lovable đầu tiên tự thấy không thể release), Visualizee 1 (V1 quá khó dùng, trước đó hai năm dậm chân ở khoảng $100/tháng), Maxed AI 1 (Dish Rate bị bỏ vì ngại chi phí dev).
- Có mô tả nhưng không đếm: Yaphone (các dự án freelance trước đó xấu, không người dùng), Curiosity Quench (3 năm thử nhiều business), NGL (6 tháng đầu rất khó, đổi thiết kế và tên), Halo AI (18 tháng ra nhiều sản phẩm thất bại).
- Nhận xét: trong các mô tả này, lý do chính founder nêu là không làm marketing/phân phối hoặc sản phẩm khó dùng; chỉ vài case (Yaphone, Money AI, NGL) nói thẳng là không có người dùng. 10 trong 23 case không có mô tả thất bại trước (`không nêu`, không phải "không có").

### 3. Dữ liệu không đỡ được câu "validate thì đi nhanh hơn"

Tháng tới mức doanh thu *hiện tại* của case full, theo nhóm bằng chứng nhu cầu (chỉ tính case có số tháng):

| Nhóm | Trung vị (p25–p75) | n |
|---|---|---|
| Build trước (`built_first`) | 6,5 tháng (5,3–28,5) | 18 |
| Có bằng chứng từ mức 3 trở lên | 12,0 tháng (6,0–30,0) | 29 |
| Không nêu | 10,0 tháng (6,0–23,0) | 51 |
| Mức 1–2 (bạn bè khen, view) | 8,0 tháng (4,0–18,0) | 9 |

Theo từng loại: tự kể nỗi đau hoặc waitlist miễn phí 24,0 tháng (n=17); trả tiền 12,0 tháng (n=5).

**Thẳng thắn: dữ liệu này không đỡ được câu "validate thì nhanh hơn", và cũng không đỡ được câu ngược lại ("build trước thì nhanh hơn").**
- Nếu đọc thô, nhóm `built_first` có trung vị thấp nhất và nhóm có bằng chứng từ mức 3 trở lên cao hơn gần gấp đôi. Đó là điều dữ liệu cho thấy, nhưng không nên đọc là nguyên nhân.
- Khoảng giữa p25–p75 chồng gần như hoàn toàn giữa các nhóm; `built_first` đến 28,5 tháng ở p75.
- "Mức doanh thu hiện tại" khác nhau giữa các case (không phải cùng một mốc như $1k MRR), và mốc đo là lúc quay video; một sản phẩm mới ra tự nhiên có số tháng ngắn.
- n nhỏ (9 đến 51), và kho chỉ chứa người thắng; các nhóm không được kiểm soát theo ngách, vốn hay audience.
- **0 case ở mọi nhóm đạt mức hiện tại trong 1 tháng trở xuống.** Từ 3 tháng trở xuống: `built_first` 2/18, mức từ 3 trở lên 5/29, không nêu 5/51, mức 1–2 2/9. Đây là thời gian tới mức doanh thu hiện tại (thường rất lớn hơn $1k), không phải mốc $1k MRR; kho không ghi mốc $1k, và có 3 case tự khai chạm $10k MRR sau khoảng 1 tháng, cả 3 đều có đường tới audience có sẵn (xem mục "Tốc độ" ở `FIND.md`), nên không kết luận gì về tốc độ theo nhóm validate.

Nên coi lý do để validate là việc *tránh mất công build sai* và *chọn đúng nhóm khách*, một lập luận mỗi người tự cân; số tháng của kho không đỡ được nó.

## Công thức trong chương

| Công thức | Case (full / tổng) | Ghi chú | Trạng thái |
|---|---|---|---|
| `s8-content-demand-test` | 26 / 28 | 8 step chỉ host (trên 41); chủ yếu đo view và waitlist miễn phí, chỉ 6/26 case đạt mức 5 trở lên | đã viết |
| `s10-customer-interviews` | 17 / 17 | hai nhánh: trước launch (9 case full) và sau launch (4 case full); chỉ 1 case ghi mức 6 | đã viết |
| `s7-preorder-buy-button` | 11 / 12 | kể cả dịch vụ làm tay bán trước (4 case); nối cổng 3 và mức 8 | đã viết |
| `s14-test-with-target-group` | 10 / 10 | bằng chứng founder còn ít: mỗi case một kiểu nhóm; bản chưa hoàn thiện | đã viết |
| `s4-tiktok-comment-mining` (chương 1) | 11 / 13 | cổng 2.5 (comment hỏi mua); 10 step không gắn case | đã viết (chương FIND) |

## Tín hiệu nhu cầu: thang 0–8 và 10 case `paid`

Thang 0–8 và mức 5 là ngưỡng tối thiểu để build nằm ở cổng 3 của `VALIDATE.md`; chương này không chép lại. Chỉ nêu những gì kho cho thấy ở mức cao nhất của thang. **Theo `kb/SCHEMA.md`, `demand_signal` chỉ tính tín hiệu đến trước lần ra mắt công khai đầu tiên, không nhất thiết trước khi build.** Vì vậy "10 case `paid`" không có nghĩa là 10 case thu tiền trước khi viết code. Đọc từng case (video, số tiền, mốc):

| Sản phẩm | Tiền | Thời điểm so với build và launch | Tiền đến từ |
|---|---|---|---|
| Setter AI | một khách trả $500 qua Stripe | **trước khi có sản phẩm** (landing page giả cùng demo AI giả); kho ghi là đặt cọc hoàn lại 100% | một khách B2B |
| Subscribr | khoảng $20k trong 2–3 ngày | **trước khi build xong**: pre-sale 50 suất lifetime, cam kết giao trong 60 ngày và hoàn tiền bất kỳ lúc nào trước khi giao | email list hơn 1.000 người dựng trước |
| BulkMockup | $300 | **trước khi có plugin**: khách freelance trả cho kết quả của một script (1.800 mockup trong khoảng 30 phút) | một khách freelance |
| Sheets Resume | vài trăm đô mỗi lần review CV, rồi giá lên $300 và $400 | **trước khi có app**: review CV làm tay cùng một đồng nghiệp cũ; app AI ra sau, ngày 26/8 | người tìm việc, qua bài Reddit nổi tiếng của founder |
| Sway AI | khoảng $15 mỗi lần | **trước khi có app**: review hồ sơ hẹn hò làm tay qua DM Instagram | follower của co-founder |
| Runafy | $5, hơn 90 người | **trước khi app tồn tại**: landing hai câu có nút Stripe; waitlist khoảng 2.000 | copy format reels đã chạy, đăng khoảng 50 video |
| Wrestle AI | khoảng $1.000 lãi ròng (transcript ghi lỗi 'a,000') | **sau build, và là của app mẹ Fight AI**: đăng cùng bạn bè sau khi build xong bản đầu cho chính mình. Pre-order '8K tuần đầu' của Wrestle AI không rõ là lượt hay tiền, nên không dùng | bạn bè của founder |
| Fastlane | khoảng 16k ARR từ bản beta trả phí | **sau khi build beta, trước launch công khai (23/3)**: beta đưa cho waitlist khoảng 2.000 người vào tháng 12 | người trong waitlist |
| Audio Pen | thông báo Stripe từ beta tester (số tiền không nêu) | **trong buổi build 12 giờ**: waitlist miễn phí mở ở giờ thứ 10, người đăng ký tự trả khi bản beta còn thô, không ai được yêu cầu trả | người theo dõi trên X và cộng đồng build-in-public |
| Excel Exercises | $50, vài đơn nữa sau vài tuần | **sau khi có một bản đang chạy trên mạng nhưng còn dở**: chưa quảng bá, chưa nói với ai; người lạ tự vào trả | người lạ tự tìm tới, không quảng bá |

Đọc bảng:
- **Chỉ 6/10 là tiền đến trước khi có sản phẩm** (Setter AI, Subscribr, BulkMockup, Sheets Resume, Sway AI, Runafy). 4/10 là tiền đến khi đã có một bản thô hoặc dở đang chạy (Wrestle AI qua app mẹ, Fastlane, Audio Pen, Excel Exercises). Cả 10 khớp chữ của mức 8 ("có người trả tiền dù sản phẩm còn thô") nhưng chỉ 6 đạt điều cổng 3 muốn (không viết code trước khi có tín hiệu).
- **Sản phẩm được trả tiền thường là việc làm tay hoặc bản rất mỏng**: script chạy một lần, review bằng tay, landing hai câu, demo giả.
- **Mỗi case dựa vào một nguồn tiếp cận có sẵn**: email list (Subscribr), follower (Sway AI, Audio Pen), waitlist 2.000 (Runafy, Fastlane), một tên miền cũ đã được Google index (Setter AI). Solo không audience không có cùng nền; xem `s7-preorder-buy-button`.
- **Số khách nhỏ ở vài case**: Setter AI và BulkMockup mỗi case một khách; Excel Exercises một đơn $50 rồi vài đơn. Mức 8 chữ nghĩa nhưng một người chưa phải thị trường.
- **Tiền hoàn lại được hay không đổi nghĩa tín hiệu.** Setter AI (đặt cọc hoàn lại 100%) và Subscribr (hoàn bất kỳ lúc nào trước khi giao) là tiền có thể rút lại; Floga bán lifetime không hoàn tiền nhưng trường nhu cầu của kho để trống.
- **Trường nhu cầu đếm thiếu `paid`.** Floga (500–600 người mua lifetime khi app còn dở) và Make Logo AI (đơn đầu tiên qua form, chưa có backend) có thu tiền ngay lúc ra mắt trong step nhưng demand_kind để trống vì tiền đến cùng lúc với lần ra mắt đầu tiên; Sheets Resume đã được điền `paid` ở lượt sửa 16/11.
- **Kho chỉ chứa người thắng.** 10/186 case full là `paid` nhưng đó là mẫu của người đã thành công; không có số người thu tiền trước và không ai trả.

Gợi ý chọn công thức: có người để gửi bài hoặc email mà chưa có ý định thu tiền thì chạy `s8-content-demand-test` (kỳ vọng mức 4, tối đa mức 5); muốn mức 8 thì `s7-preorder-buy-button`; muốn hiểu vì sao người ta trả hay không thì `s10-customer-interviews`; có sẵn một nhóm để đưa bản dở thì `s14-test-with-target-group`.
