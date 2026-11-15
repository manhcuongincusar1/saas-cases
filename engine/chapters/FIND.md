# Chương 1 — Tìm ý tưởng: thực tế trước, công thức sau

> Số đếm lấy từ `kb/data/kb.duckdb` (kb.duckdb: 210 video, trong đó 209 từ Starter Story + Superwall và 1 video ngoài hai kênh; 186 case full). Câu truy vấn: `engine/chapters/find.sql`.
> Hai điều phải đọc cùng mọi con số dưới đây: (1) **kho chỉ chứa người thắng**, nên không có số người làm y hệt mà thất bại; (2) **"không nêu" không có nghĩa "không có"**, vì video không kể hết.

## Thực tế: founder trong kho tìm ý tưởng bằng cách nào

**Ý tưởng đến từ đâu** (186 case full, một case có thể có nhiều nguồn; 22 case video không nêu):

| Nguồn ý tưởng (`idea_origin`) | Số case |
|---|---|
| Nỗi đau của chính mình (`own_pain`) | 77 |
| Nghề, chuyên môn (`domain_expertise`) | 46 |
| Thay đổi/thời điểm mới (`timing_trigger`) | 37 |
| Chép/theo trend (`trend_copy`) | 21 |
| Đam mê (`passion_skin`) | 14 |
| Soi doanh thu để chọn (`revenue_scouting`) | 12 |
| Mở rộng sang ngách kề (`adjacent_expansion`) | 12 |
| Tín hiệu từ audience (`audience_signal`) | 11 |
| Khách/người dùng xin (`user_request`) | 9 |
| Thu hẹp ngách (`niche_down`) | 7 |

**Cách tìm bằng công cụ gần như vắng.** Chỉ 19/186 case full có step dùng soi doanh thu, từ khoá/xu hướng tìm kiếm, review đối thủ hoặc chợ thuê người (s1, s2, s3-reviews, s6); 34/186 nếu tính cả đọc Reddit và comment TikTok. Ở chiều ngược lại, s5-insider xuất hiện ở 88 case full, s12 ở 28, s11 ở 27. Điều này **không** chứng minh công cụ vô dụng: có thể video không kể bước tìm, hoặc đó là việc host/expert nói chứ founder không làm (xem cột "chỉ host" trong từng công thức). Nó chỉ cho thấy đây không phải cách phần đông founder trong kho đã đi.

**Founder có phải người trong cuộc không** (`community_at_discovery.insider`): 117 case là người trong cuộc (63%), 22 tự ghi là đứng ngoài (12%), 47 video không nêu (25%). Ba nhóm này **không được gộp**: 47 case kia chỉ là video không kể, chưa chắc là người ngoài.

Tactic dùng ở step tìm ý tưởng (find-idea), số case full trong từng nhóm (một case có thể dùng nhiều tactic):

| Tactic | Người trong cuộc (117) | Không nêu (47) | Đứng ngoài (22) |
|---|---|---|---|
| s5-insider | 81 | 6 | 1 |
| s12-timing-shift | 16 | 4 | 8 |
| s11-copy-or-localize-proven | 15 | 7 | 5 |
| s13-others-pain-or-inbound | 4 | 1 | 6 |
| s4-tiktok-comment-mining | 5 | 2 | 4 |
| s9-niche-narrowing | 8 | 6 | 3 |
| s1-revenue-spy | 6 | 3 | 3 |

Riêng 22 case đứng ngoài, nguồn ý tưởng ghi nhận là: `timing_trigger` 6, `trend_copy` 4, `revenue_scouting` 3, `own_pain` 2, `adjacent_expansion` 2, `niche_down` 2, còn lại mỗi nguồn 1. Cỡ mẫu nhỏ (22), chỉ để định hướng. Với người đứng ngoài hầu hết ngách (đúng tình huống của solo bán global từ VN), đây là nhóm bằng chứng gần mình nhất, nhưng vẫn chỉ là 22 case của người thắng.

**Tốc độ.** Hai phép đo khác nhau, đừng lẫn. (1) Trong 107 case full có số tháng tới **mức doanh thu hiện tại** (thường hàng chục nghìn USD/tháng, không phải $1k), trung vị 12 tháng (p25 = 5, p75 = 24); 14 case từ 3 tháng trở xuống; 0 case từ 1 tháng trở xuống. (2) Mốc **$10k MRR** có số tháng ở 10 case (founder tự khai, tính từ lúc ra mắt hoặc từ lúc bắt đầu, video không thống nhất): 3 case nói khoảng 1 tháng (Launch Fast, SiteGPT, 3AK Track), 3 case khoảng 3 tháng, còn lại 4, 6, 8, 12 tháng. **Cả 3 case khoảng 1 tháng đều có đường tới audience có sẵn:** Launch Fast đổi equity lấy audience của một đối tác (kênh người dùng đầu: `influencer_partner`), SiteGPT có `existing_audience` và `prior_success` (founder đã bán SaaS trước, có khách cũ), 3AK Track có `existing_audience` (hàng trăm nghìn follower). Đừng đọc thành "3/10 làm được trong 1 tháng": với solo không audience, kho không có case nào đạt mốc này từ số không (câu truy vấn: `engine/chapters/speed.sql`). Mốc **$1k MRR** không có case nào ghi số tháng (`to_1k_mrr` trống cả 186 case), và mốc doanh thu đầu tiên chỉ có 7 case (1–24 tháng). Vậy kho không có số đo trực tiếp cho "$1k MRR trong 1 tháng"; nó chỉ có vài ca tự khai chạm $10k MRR sau khoảng 1 tháng, toàn người thắng và tính mốc không đồng nhất. Đừng hứa tốc độ; đo tín hiệu (mức 5–8 của `VALIDATE.md`) thay vì MRR trong tháng đầu. (Cũng đứng ở đầu `COOKBOOK.md`.)

## Công thức trong chương

| Công thức | Case (full / tổng) | Ghi chú | Trạng thái |
|---|---|---|---|
| `s5-insider` | 88 / 92 | lớn nhất; có Nhánh B khi mình không phải người trong cuộc | đã viết |
| `s12-timing-shift` | 28 / 32 | phần lớn là AI/API mới, hết hạn nhanh | đã viết |
| `s11-copy-or-localize-proven` | 27 / 29 | | đã viết |
| `s9-niche-narrowing` | 17 / 20 | 9 step không gắn case | đã viết |
| `s13-others-pain-or-inbound` | 11 / 12 | | đã viết |
| `s4-tiktok-comment-mining` | 11 / 13 | 10 step không gắn case | đã viết |
| `s1-revenue-spy` | 12 / 13 | 7 step không gắn case; công thức viết trước, đã cập nhật số | đã cập nhật |
| `s3-reddit-pain-mining` | 5 / 8 | | đã viết |
| `s15-idea-filter-criteria` | 3 founder | tactic mới, mỏng | đã viết |
| `s3-competitor-reviews` | 4 / 4 | mỏng; công thức viết trước, đã cập nhật nhãn | đã cập nhật |
| `s2-google-trends-volume` | 3 / 4 | một trang mỏng | đã viết |
| `s2-aso-keyword-gap` | 1 / 1 | chủ yếu expert, 1 case founder; giữ vì không cần là người trong cuộc và không bị khoá vùng | đã cập nhật nhãn |
| `s6-upwork-demand` | 1 / 1 | chưa có founder nào xác nhận; không viết | — |
