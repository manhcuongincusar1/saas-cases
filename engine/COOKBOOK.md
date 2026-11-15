# Cookbook — mở trang này trước

> Cookbook cho solo founder bán **global** (US/UK/CA/AU/EU), thu USD/EUR, chọn **organic** hơn paid.
> Chưng cất từ **210 video** (Starter Story + Superwall 2025+, cộng một video ngoài) trong `kb/data/kb.duckdb`: 186 case founder kể kỹ. 29 công thức, 3 chương trả lời đúng 3 câu hỏi: **tìm ý tưởng thế nào, validate thế nào, grow thế nào.**
> Giai đoạn này **chỉ chưng cất**, chưa tìm ý tưởng. Giao thức chạy cho agent: `README.md`.

## Đọc trước: ba điều về bằng chứng

1. **Kho chỉ chứa người thắng.** Không có số người làm y hệt mà thất bại. Mọi tỉ lệ dưới đây là "trong số người đã lên kênh".
2. **"Không nêu" không có nghĩa "không có".** Video không kể hết; 54% case full (101/186) không kể bằng chứng nhu cầu trước launch, nhưng điều đó không có nghĩa họ không validate.
3. **Về tốc độ, đừng hứa gì.** Mục tiêu mặc định cũ là "$1k MRR trong 1 tháng". Kho **không đo mốc $1k** (không case nào ghi `to_1k_mrr`). Có hai phép đo gần nhất, và chúng khác nhau:
   - Thời gian tới **mức doanh thu hiện tại** (thường hàng chục nghìn USD/tháng): 107 case, trung vị **12 tháng** (p25 = 5, p75 = 24); 14 case từ 3 tháng trở xuống; 0 case từ 1 tháng trở xuống.
   - Mốc **$10k MRR**: 10 case có số tháng, founder tự khai, mốc tính không đồng nhất (từ lúc ra mắt hoặc từ lúc bắt đầu): 3 case khoảng 1 tháng, 3 case khoảng 3 tháng, còn lại 4, 6, 8, 12 tháng. **Cả 3 case khoảng 1 tháng đều có đường tới audience có sẵn:** Launch Fast đổi equity lấy audience của một đối tác (kênh người dùng đầu: `influencer_partner`), SiteGPT có `existing_audience` và `prior_success` (founder đã bán SaaS trước, có khách cũ), 3AK Track có `existing_audience` (hàng trăm nghìn follower). Đừng đọc thành "3/10 làm được trong 1 tháng": với solo không audience, kho không có case nào đạt mốc này từ số không (câu truy vấn: `engine/chapters/speed.sql`).
   Trong 1 tháng, thứ đo được là **tín hiệu nhu cầu** (mức 5–8 của `VALIDATE.md`), không phải MRR.

## Ba câu hỏi, trả lời ngắn từ kho

**1. Tìm ý tưởng** → `chapters/FIND.md`
- Phần đông founder tìm từ chính họ: nỗi đau riêng 77 case, nghề 46, thời điểm/thay đổi mới 37, chép trend 21 (186 case full). Chỉ 19/186 case (10%) có step dùng công cụ soi doanh thu, từ khoá hoặc review; 34/186 (18%) nếu tính cả Reddit và comment TikTok.
- 117 case là người trong cuộc, 22 tự ghi là đứng ngoài, 47 video không nêu. Với người đứng ngoài, lối đi nhiều nhất trong kho là bắt thay đổi mới (`s12`, 8 case), rồi nỗi đau người khác (`s13`, 6 case) và chép sản phẩm đã chạy (`s11`, 5 case).

**2. Validate** → `chapters/VALIDATE.md`
- 101/186 case không kể bằng chứng nhu cầu trước launch; trong 85 case có kể: tự kể nỗi đau/waitlist miễn phí 26, "build trước rồi chờ" 23, trả tiền 10, nội dung nhiều view 10, sản phẩm tương tự có doanh thu 7, bạn bè khen 5. Dữ liệu không đỡ được câu "validate thì nhanh hơn" (và cũng không đỡ câu ngược lại).
- 10 case "paid": chỉ 6 là tiền đến trước khi có sản phẩm.

**3. Grow** → `chapters/GROW.md`
- Người dùng đầu tiên chủ yếu đến từ kênh không tốn tiền: nội dung của founder 32 case, Reddit 26, TikTok organic 26, truyền miệng 19. Kênh scale: 98 case thuần organic, 64 có kênh trả tiền, 24 không nêu.
- Công thức grow xếp theo **thứ tự việc phải làm**, không theo số bằng chứng.

## Tình huống của tôi → chạy công thức nào

Giả định mặc định: solo, không audience, bán global từ VN, chọn organic.

| Tình huống | Chạy (theo thứ tự) |
|---|---|
| Đã ở trong một nghề/cộng đồng/nỗi đau hằng ngày | `s5-insider` → `s3-reddit-pain-mining` hoặc `s4-tiktok-comment-mining` để kiểm người khác cũng đau → chương VALIDATE |
| Đứng ngoài hầu hết ngách (thường là mình) | `s12-timing-shift` → `s13-others-pain-or-inbound` hoặc `s11-copy-or-localize-proven` → `s4`; ghép với người trong ngách là lối ít bằng chứng nhất (3 case, trong `s5` Nhánh B) |
| Muốn dùng công cụ tìm ngách (bằng chứng founder mỏng) | `s1-revenue-spy` → `s2-aso-keyword-gap` (chủ yếu lời expert, 1 case founder) → `s3-competitor-reviews` |
| Có vài ý tưởng, cần chọn | `s15-idea-filter-criteria` (3 founder), `s9-niche-narrowing` |
| Có một ứng viên, cần biết có nhu cầu không | `s8-content-demand-test`, `s10-customer-interviews`, `s14-test-with-target-group`; muốn tín hiệu mạnh nhất: `s7-preorder-buy-button` (mức 8) |
| Chưa có người dùng nào | `g1-first-10-users`, `g9-launch-platforms` (và `g12-outbound-b2b` nếu khách là doanh nghiệp) |
| Muốn được tìm thấy mà không trả tiền | `g2-aso-seo-organic`, `g3-organic-content-formats`, `g11-positioning-messaging` |
| Cần thu tiền và đo | `g4-pricing-paywall`, `g8-funnel-measurement` |
| Người dùng rời đi | `g5-retention` |
| Có format organic thắng, sẵn sàng tốn tiền (tuỳ chọn) | `g7-creator-ops`, `g6-paid-ads` |
| Cơ hội báo chí xuất hiện | `g14-press-pr` (không lên kế hoạch được) |

## Danh mục công thức (29)

**Chương 1 — Tìm ý tưởng** (`chapters/FIND.md`): `s5-insider`, `s12-timing-shift`, `s11-copy-or-localize-proven`, `s9-niche-narrowing`, `s13-others-pain-or-inbound`, `s4-tiktok-comment-mining`, `s1-revenue-spy`, `s3-reddit-pain-mining`, `s15-idea-filter-criteria`, `s3-competitor-reviews`, `s2-google-trends-volume`, `s2-aso-keyword-gap`. Không viết `s6-upwork-demand`: chưa có founder nào xác nhận (1 case, 1 step).

**Chương 2 — Validate** (`chapters/VALIDATE.md`; ngưỡng ở `../VALIDATE.md`): `s8-content-demand-test`, `s10-customer-interviews`, `s7-preorder-buy-button`, `s14-test-with-target-group`; kèm mục "Tín hiệu nhu cầu" theo thang 0–8.

**Chương 3 — Grow** (`chapters/GROW.md`): `g1-first-10-users`, `g9-launch-platforms`, `g2-aso-seo-organic`, `g3-organic-content-formats`, `g10-referral-viral-loop`, `g11-positioning-messaging`, `g4-pricing-paywall`, `g8-funnel-measurement`, `g5-retention`, `g12-outbound-b2b`, `g14-press-pr`, `g7-creator-ops`, `g6-paid-ads`.

Mỗi công thức có cùng khuôn: Dùng khi, Các bước, Ngưỡng qua, **Thực tế của công thức này** (bảng số tự sinh, có nhóm "giống user": case không nêu audience/vốn/network/thành công trước), Bằng chứng (nguyên văn, mốc giây, gắn nhãn host/expert hay founder), Bẫy, Quyết định **QUA · DỪNG · TEST THÊM**, và mục "Cho solo founder bán global". `signal_level_when_pass` khớp điều kiện QUA. Công thức dựa nhiều vào lời host/expert hoặc bằng chứng founder mỏng có nhãn ngay đầu.

## Quy ước và cách tái tạo số

- Số doanh thu trong video là founder tự khai trừ khi ghi `measured`. TrustMRR là số đã xác minh; Sensor Tower/AppMagic lệch 10–30 lần.
- Ví dụ trong công thức để **học cách làm**, không phải menu ngách để chọn. Ngưỡng không lấy từ kho đều ghi "đề xuất, chưa có số của kho".
- "Case" = một cặp (video, case); một founder kể hai sản phẩm đếm 2. 186 cặp case full ≈ 175 sản phẩm khác nhau.
- Dựng DB: `python3 -I kb/scripts/build.py`. Số của từng công thức: `python3 -I engine/scripts/build_recipe.py <id>` (câu truy vấn lưu cạnh công thức: `recipes/<id>.sql`, `.extra.sql`; trang chương: `chapters/*.sql`).
- Kiểm câu trích: `python3 -I engine/scripts/check_recipes.py` (mọi đoạn trích ≥30 ký tự phải nằm nguyên văn trong `evidence/`, sinh từ DB).
- Vocab: `kb/vocab.yaml`. Mục tìm ý tưởng bằng công cụ thật (`tools/`: `topgrossing.py`, `kw.py`, `autofill.py`, `reviews.py`) chỉ chạy ở giai đoạn sau, khi user cho phép.
