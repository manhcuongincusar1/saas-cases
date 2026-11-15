---
id: s3-reddit-pain-mining
strategy: S3
title: "Đọc Reddit, forum và Discord để tìm nỗi đau lặp lại bằng chữ của chính họ"
label: manual                  # Reddit chặn agent và Chrome tự động (VALIDATE.md mục 2.7): người mở tay, agent giúp ghi và đếm
time: "2–3 giờ cho 3–5 cộng đồng"
cost: "$0"
evidence: corpus
signal_level_when_pass: 4      # QUA đòi nhiều người tự tả cùng nỗi đau (mức 4 của thang VALIDATE.md); chưa phải mức 5 (comment hỏi mua)
tools: []
status: draft
---

## Dùng khi
Đã có một ngách hoặc một nghề (từ `s5`, `s12`, `s11`…) và cần biết nỗi đau của họ có lặp lại ngoài đầu mình không. Nếu ngách là chủ doanh nghiệp B2B thì xem bẫy đầu tiên bên dưới.

## Đầu vào
Một ngách + 3–5 nơi khách ngách hay hỏi giúp: subreddit, forum của chính nền tảng (Airtable), diễn đàn ý tưởng của hệ sinh thái (WooCommerce), server Discord ngách (tìm qua discboard.org).

## Các bước
1. **[manual] Chọn nơi.** Founder trong kho đọc ở: subreddit Hinge (Sway AI), subreddit Notion (Sync2Sheets), forum Airtable (Data Fetcher), diễn đàn ý tưởng WooCommerce (Barn2), Discord ngách (Algrow). Mở tay trên trình duyệt của mình.
2. **[manual] Đọc lặng lẽ, tìm bằng từ khoá của việc, không phải của sản phẩm.** Sync2Sheets vào subreddit Notion rồi tìm "sheets", "Google sheets", "excel", "CSV". Với Discord, đọc chat tìm câu hỏi lặp lại (Algrow đọc câu "how do I find a niche").
3. **[manual] Ghi mỗi thread vào một bảng:** link · câu nguyên văn người đó tả nỗi đau · số comment/upvote · họ đang xử lý bằng gì · họ có nhắc đã trả tiền cho thứ gì không. Mẫu dán: 5 dòng cho mỗi cộng đồng, ≤15 phút.
4. **[manual] Đếm lặp lại.** Cùng một nỗi đau trong ≥3 thread của ≥2 người khác nhau (ngưỡng đề xuất, chưa có số của kho).
5. **[manual] Giữ im lặng bán hàng.** Founder Bulkmockup chỉ trò chuyện khi thấy một nỗi đau lặp lại, không bán trong đó; founder Algrow dặn xây quan hệ với cộng đồng trước (câu ở bảng).
6. **Nối tiếp:** chạy `s3-competitor-reviews` trên giải pháp người ta đang dùng; hoặc chuyển ứng viên sang `VALIDATE.md` cổng 2 (2.7 "nỗi đau có được viết công khai không").

## Đầu ra
Bảng thread (bước 3) + một dòng ứng viên: nỗi đau · bao nhiêu người tả · giải pháp họ đang dùng · có ai trả tiền không · mức tín hiệu 0–8.

## Ngưỡng qua
Ngưỡng tín hiệu ở `VALIDATE.md` (cổng 2.7 và thang 0–8); không chép lại. Riêng công thức này: bước 4 đạt.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
8 case full, 10 step, 2 step chỉ do host/expert mô tả. Cả 8 case có bằng chứng nhu cầu được ghi, nhưng **6/8 là chính việc đọc cộng đồng được ghi thành bằng chứng** (mức 4, "người ta tự kể nỗi đau"), nên đây là hệ quả của cách ghi, không chứng minh Reddit tốt hơn kênh khác. Hai case khác là có người trả tiền trước build (Sway AI: người ta trả $15 để được góp ý hồ sơ; Bulkmockup: khách chuyển $300). Trung vị tháng tới doanh thu hiện tại là 27 tháng nhưng n=6 và khoảng rất rộng (p25 6, p75 57); không dùng để so tốc độ.

<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 10 step trong 10 video |
| Case (video, case) có step này | 8, trong đó 8 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 2/10 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 6/8 |
| Case full không nêu existing_audience | 8/8 |
| Case full video không kể bằng chứng nhu cầu trước launch | 0/8 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 27.0 tháng (6.0–57.0), n=6 |
| Kênh scale trả tiền / thuần organic / không nêu | 1 / 7 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s3-reddit-pain-mining.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Daniel (founder) · `2026-05-05_i-speedran-a-new-app-from-0-to-2myear-in-6-month` · 00:03:30 | "If you just look up like the Hinge Reddit and you see like what people are searching on there, you'll notice that people are just uploading pictures of themselves and their profile" | founder kể bước tìm: đọc subreddit Hinge, thấy người ta đăng ảnh hồ sơ xin góp ý (Sway AI) |
| Daniel (founder) · `2026-05-05_i-speedran-a-new-app-from-0-to-2myear-in-6-month` · 00:05:51 | "People were actually paying us before we built the app to get feedback on their profile" | founder kể kiểm trước build: người ta trả tiền để được góp ý hồ sơ khi chưa có app |
| Kian (founder) · `2026-06-14_the-first-app-i-ever-built-makes-25k-month` · 09:45 | "there are at least thousands if not tens of thousands of people out there with the exact same problem that you have." | founder kể kết luận sau khi hỏi guitarist trên Reddit và Instagram: nhiều người cùng một vấn đề |
| Joseph hoặc Timo (founder) · `2025-09-27_how-we-built-a-10k-mo-saas` · 04:54 | "I think the best pain point to find B2B ideas is not look around on Reddit or something because business owners, frankly, they don't really check Reddit." | giới hạn: ngách B2B chủ doanh nghiệp không ở Reddit (founder Setter AI nói) |
| Sam Adeniyi (founder) · `2026-01-14_i-built-a-14k-month-saas-using-discord` · 08:34 | "I think the main thing you have to do first is build maybe a bit of rapport in the community." | quy tắc ứng xử founder đặt ra: xây quan hệ với cộng đồng trước |
| Leandro (founder) · `2025-06-11_how-i-built-it-9k-month-micro-saas` · 14:18 | "Do not waste time building something that no one is going to be willing to pay for." | founder dặn: đừng build thứ không ai chịu trả tiền, sau khi thấy nhu cầu trong subreddit |
| Host (không nêu tên) (host/expert) · `2026-01-14_i-built-a-14k-month-saas-using-discord` · 14:29 | "go to small community, solve a really, really niche problem for a really, really niche customer." | lời khuyên của host: vào cộng đồng nhỏ, giải một vấn đề rất hẹp cho một nhóm khách rất hẹp |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Ngách B2B có thể không ở Reddit.** Founder Setter AI nói chủ doanh nghiệp "không check Reddit" (bảng). Reddit hợp với nỗi đau của người dùng cuối và của dev/maker, kém hơn với chủ doanh nghiệp.
- **Thấy nhiều người than ≠ có người trả tiền.** Chỉ 2/8 case có bằng chứng tiền trước build. Phần lớn đọc Reddit rồi build ngay (xem `VALIDATE.md` cổng 3 để lấy tín hiệu mạnh hơn).
- **Kho chỉ chứa người thắng.** 8 case; không có số người đọc Reddit, thấy nhu cầu giả, rồi thất bại.
- **Số mẫu nhỏ và một phần là lời host.** 2/10 step là host/expert mô tả, 8/10 là founder đã làm.
- **Dùng cho mục đích khác.** Một step trong kho dùng thread Reddit để viết copy quảng cáo (không phải chọn ý tưởng); đừng đếm nó như bằng chứng cho công thức này.

## Quyết định
- **QUA** nếu bước 4 đạt (≥3 thread, ≥2 người, cùng nỗi đau; ngưỡng đề xuất, chưa có số của kho) và biết họ đang dùng gì thay thế. Khi đó ứng viên đạt mức tín hiệu 4.
- **DỪNG** nếu chỉ có một nguồn hoặc một người, hoặc nỗi đau chỉ được tả bằng chữ của một người có lý do bán hàng.
- **TEST THÊM** nếu cộng đồng quá nhỏ hoặc ngách ở ngoài Reddit: trong 7 ngày đọc thêm 2 nơi khác (forum nền tảng, Discord), hoặc chuyển sang `s4-tiktok-comment-mining`.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ, vì cộng đồng tiếng Anh không bị khoá vùng; làm từ xa, $0, không đòi là người trong ngách.
- **Rào cản thật:** Reddit chặn tự động hoá nên mất công đọc tay; cần tiếng Anh đủ để hiểu cách họ tả nỗi đau (từ lóng, tên tool). Đừng đăng bài quảng cáo ngay vì sẽ bị chặn (founder trong kho cũng dặn xây quan hệ trước).
- **KHÔNG nên làm** khi khách của ngách không ở trong cộng đồng công khai nào (B2B truyền thống, người lớn tuổi) hoặc khi mình không thể tham gia tự nhiên (không hiểu ngôn ngữ ngách).
