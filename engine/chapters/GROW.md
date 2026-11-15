# Chương 3 — Grow: thực tế trước, công thức sau (phần 1: ra mắt, người dùng đầu, organic)

> Số đếm lấy từ `kb/data/kb.duckdb` (209 video 2025+; 186 case full). Câu truy vấn: `engine/chapters/grow.sql` (chạy: `duckdb kb/data/kb.duckdb < engine/chapters/grow.sql`).
> Hai điều phải đọc cùng mọi con số dưới đây: (1) **kho chỉ chứa người thắng**, nên không có số người làm y hệt mà thất bại; (2) **"không nêu" không có nghĩa "không có"**, vì video không kể hết.
> Công thức grow dùng nhãn khác chương 1–2: grow **không** chuyển ứng viên lên thang tín hiệu 0–8 của `VALIDATE.md`. Mỗi công thức ghi "cách đo thành công" (số người dùng theo kênh) ở mục Đầu ra, và `signal_level_when_pass` để `—`.

## Thực tế: founder trong kho có người dùng đầu tiên bằng cách nào

**Kênh người dùng đầu tiên** (bảng `first_users`, 186 case full; 143 case có ít nhất một dòng, 43 case video không nêu; một case có thể có nhiều kênh nên cột tổng lớn hơn 143):

| Kênh (`channel`) | Số case full |
|---|---|
| Nội dung của founder (`founder_led_content`) | 32 |
| Reddit (`reddit`) | 26 |
| TikTok organic (`tiktok_organic`) | 26 |
| Truyền miệng (`word_of_mouth`) | 19 |
| Chợ ứng dụng / nền tảng (`platform_marketplace`; gồm Product Hunt, Chrome Web Store, marketplace của Airtable, Shopify...) | 13 |
| Audience sẵn có (`own_audience`) | 12 |
| SEO (`seo`) | 12 |
| Influencer trả tiền / hợp tác (`influencer_paid` 9, `influencer_partner` 9) | 9 / 9 |
| YouTube của founder (`youtube_founder`) | 8 |
| Creator UGC (`ugc_creators`) | 8 |
| Tìm kiếm trong App Store (`app_store_search`) | 7 |
| Instagram Reels (`instagram_reels`) | 6 |
| Hợp đồng B2B (`b2b_deals`) | 5 |
| Nhóm Facebook (`facebook_groups`) | 3 |
| Quảng cáo trả tiền (`paid_meta` 3, `paid_tiktok` 3, `paid_apple_search` 1, `paid_google` 1, `paid_unspecified` 1) | 9 lượt trong 5 loại (một case có thể xuất hiện ở nhiều loại) |
| AppSumo | 1 |

Đọc bảng: kênh người dùng **đầu tiên** của founder trong kho chủ yếu là kênh không tốn tiền (nội dung của chính mình, Reddit, TikTok, truyền miệng). Reddit là kênh lặp lại nhiều nhất ở cấp "tìm người dùng đầu" trong tactic `g1-first-10-users` (22 case full). Điều này **không** chứng minh Reddit hay TikTok tốt hơn kênh khác: đây là những kênh mà người thắng đã kể và chọn kể.

**Kênh scale: trả tiền hay organic** (`scale_channels`, 186 case full):

| Nhóm | Số case full | Tỉ lệ |
|---|---|---|
| Có ít nhất một kênh trả tiền (`paid_*` hoặc `influencer_paid`; có thể kèm kênh organic) | 64 | 34% |
| Chỉ kênh organic | 98 | 53% |
| Video không nêu | 24 | 13% |

Hơn một nửa chỉ nêu kênh organic; khoảng một phần ba có kênh trả tiền ở giai đoạn scale. Cách đọc: trả tiền thường đến **sau** khi đã có organic chạy được (xem `g6-paid-ads`, mục `tactic_note` ghi trước hay sau), và 24 case không nêu có thể thuộc nhóm nào cũng được.

**Tốc độ.** Hai phép đo khác nhau, đừng lẫn. (1) Trong 107 case full có số tháng tới **mức doanh thu hiện tại** (thường hàng chục nghìn USD/tháng, không phải $1k), trung vị 12 tháng (p25 = 5, p75 = 24); 14 case từ 3 tháng trở xuống; 0 case từ 1 tháng trở xuống. (2) Mốc **$10k MRR** có số tháng ở 10 case (founder tự khai, tính từ lúc ra mắt hoặc từ lúc bắt đầu, video không thống nhất): 3 case nói khoảng 1 tháng (Launch Fast, SiteGPT, 3AK Track), 3 case khoảng 3 tháng, còn lại 4, 6, 8, 12 tháng. **Cả 3 case khoảng 1 tháng đều có đường tới audience có sẵn:** Launch Fast đổi equity lấy audience của một đối tác (kênh người dùng đầu: `influencer_partner`), SiteGPT có `existing_audience` và `prior_success` (founder đã bán SaaS trước, có khách cũ), 3AK Track có `existing_audience` (hàng trăm nghìn follower). Đừng đọc thành "3/10 làm được trong 1 tháng": với solo không audience, kho không có case nào đạt mốc này từ số không (câu truy vấn: `engine/chapters/speed.sql`). Mốc **$1k MRR** không có case nào ghi số tháng (`to_1k_mrr` trống cả 186 case), và mốc doanh thu đầu tiên chỉ có 7 case (1–24 tháng). Vậy kho không có số đo trực tiếp cho "$1k MRR trong 1 tháng"; nó chỉ có vài ca tự khai chạm $10k MRR sau khoảng 1 tháng, toàn người thắng và tính mốc không đồng nhất. Đừng hứa tốc độ; đo tín hiệu (mức 5–8 của `VALIDATE.md`) thay vì MRR trong tháng đầu. (Cũng đứng ở đầu `COOKBOOK.md`.)

**Hai câu cảnh báo.**
1. **Kho chỉ chứa người thắng.** Mọi tactic dưới đây được đếm trên founder đã thành công đủ để lên kênh. Số người dùng cùng kênh mà không ra gì không có trong kho, nên số case chỉ cho biết "đã có người làm và kể", không cho biết xác suất.
2. **"Không nêu" ≠ "không có".** 43/186 case không có dòng nào về người dùng đầu tiên; 24/186 không nêu kênh scale. Một kênh vắng mặt trong bảng có thể vẫn được dùng.

## Thứ tự việc phải làm (KHÔNG xếp theo số bằng chứng)

Thứ tự theo việc cần làm trước/sau của một sản phẩm mới. Số case ở cột giữa chỉ để biết bằng chứng dày hay mỏng; tactic có nhiều case (`g4`, `g3`) không có nghĩa phải làm trước.

| Bước | Công thức | Case (full / tổng) | Ghi chú | Trạng thái |
|---|---|---|---|---|
| 1. Ra mắt | `g1-first-10-users` | 52 / 54 | 22 case full có Reddit trong `first_users`; 3 step không gắn case | đã viết |
| 1. Ra mắt | `g9-launch-platforms` | 27 / 28 | lifetime deal, AppSumo, Product Hunt/HN, marketplace; 4 step không gắn case | đã viết |
| 1. Ra mắt (nếu B2B) | `g12-outbound-b2b` | 5 / 5 | tactic mới, mỏng; thay cho g1 khi khách là doanh nghiệp; 1 step không gắn case | đã viết |
| 1. Ra mắt (trang đích) | `g11-positioning-messaging` | 6 / 6 | tactic mới, mỏng; làm cùng lúc với g1/g9 vì mọi kênh đều dẫn về trang này; 1 step không gắn case | đã viết |
| 2. Organic | `g2-aso-seo-organic` | 34 / 38 | ASO (app có sẵn) và SEO (web); chậm, trả sau; 6 step không gắn case | đã viết |
| 2. Organic | `g3-organic-content-formats` | 107 / 135 | đăng gì; lớn nhất chương nhưng 46 step không gắn case | đã viết |
| 2. Organic | `g10-referral-viral-loop` | 7 / 8 | mỏng; vòng mời bạn trong sản phẩm | đã viết |
| 2. Organic (cơ hội) | `g14-press-pr` | 4 / 4 | tactic mới, rất mỏng; không lên kế hoạch được, ghi nhận khi có cơ hội | đã viết |
| 3. Thu tiền, đo | `g4-pricing-paywall` | 120 / 136 | nhiều case nhất vì gần như ai cũng kể giá; 19 step không gắn case | đã viết |
| 3. Thu tiền, đo | `g8-funnel-measurement` | 26 / 30 | đo phễu và CAC/LTV; 4 step không gắn case | đã viết |
| 4. Giữ chân | `g5-retention` | 24 / 25 | 4 step không gắn case | đã viết |
| 5. Tốn tiền, tuỳ chọn | `g7-creator-ops` | 68 / 88 | làm việc với creator/UGC/clipper; 38 step không gắn case | đã viết |
| 5. Tốn tiền, tuỳ chọn | `g6-paid-ads` | 53 / 61 | 19 step không gắn case | đã viết |

Ghi chú về chỗ đặt:
- **g12** nằm ở bước 1 vì với khách là doanh nghiệp, outbound thay cho group/DM của g1; chỉ có 5 case full, chưa đủ để coi là chuẩn.
- **g11** nằm ở bước 1 nhưng có thể làm lại bất cứ lúc nào: 6 case full, gồm đổi định vị khi đã có khách, viết landing riêng cho một ICP, thí nghiệm trang đưa tới "magic moment". Bằng chứng mỏng.
- **g14** (báo chí, TV): trong 4 case full, ba case báo chí đến sau một sự kiện hoặc vì sản phẩm mới lạ (NeuroGum sau crowdfunding, YourMove, Flame), một case founder gửi email lạnh cho nhà báo (Rootd). Chưa đủ để lên lịch.
- **g7 và g6** đặt cuối vì tốn tiền hoặc tốn người và là lựa chọn: kho cho thấy 64/186 case full có kênh trả tiền khi scale, 98/186 chỉ organic.
- Công thức viết sau (g3, g4, g5, g6, g7, g8, g11, g12, g14) do phiên khác viết; bảng này chỉ giữ chỗ.

## Công thức đã viết trong phần 1

| Công thức | Dùng khi | Trạng thái |
|---|---|---|
| `g1-first-10-users` | chưa có người dùng nào | đã viết |
| `g9-launch-platforms` | sản phẩm ra được một ngày launch hoặc có nền tảng sẵn người dùng | đã viết |
| `g2-aso-seo-organic` | sản phẩm đã có, cần được tìm thấy mà không trả tiền | đã viết |
| `g10-referral-viral-loop` | sản phẩm có tính xã hội sẵn; mỏng | đã viết |
