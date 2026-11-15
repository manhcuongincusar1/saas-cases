---
id: g10-referral-viral-loop
strategy: G10
title: "Vòng giới thiệu và lan truyền ngay trong sản phẩm (bằng chứng founder còn ít)"
label: manual                  # đây là tính năng trong sản phẩm: người làm quyết định cơ chế, agent chỉ giúp liệt kê và đo
time: "2–3 giờ để chọn cơ chế; thời gian build tuỳ cơ chế"
cost: "$0 (credit thưởng là chi phí biên của mình)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

## Dùng khi
Sản phẩm đã có vài người dùng thật, và hành động chính của người dùng tự nhiên có người thứ hai tham gia hoặc nhìn thấy (chia sẻ kết quả, mời bạn cùng dùng, gửi link). Công thức **mỏng**: 8 case, chỉ 1 case kể con số. Không dùng thay cho `g1-first-10-users` khi chưa có người dùng nào, và không dùng khi người dùng dùng một mình, âm thầm.

## Đầu vào
Một hành động trong sản phẩm mà người dùng đã làm với người khác (hoặc có thể làm): xem kết quả, chia sẻ asset, mời bạn.

## Các bước
1. **[manual] Tìm hành vi chia sẻ có sẵn.** Magic Music: người dùng chia sẻ bài hát qua web view và không biết mình đang chia sẻ app; người xem thấy nút "Create your own song" rồi tải app. Việc làm: liệt kê 3 thứ người dùng đã gửi cho người khác (kết quả, ảnh, link).
2. **[manual] Gắn tên sản phẩm vào thứ được chia sẻ.** Stagetimer: mỗi link chia sẻ có logo kèm tên app (stagetimer.io) để người xem nhớ tên rồi tới dùng; không có thưởng giới thiệu. Glam Up: mẫu chia sẻ có tên app.
3. **[manual] Nếu kết quả có giá trị, thêm cách mở khoá bằng lời mời.** Glam Up: paywall có hai lối, trả tiền để xem kết quả, hoặc mời 3 bạn bằng mã để mở miễn phí. GlowUp: mời 3 bạn để nhận một look miễn phí; người xem đăng mã mời trong comment video.
4. **[manual] Nếu đã có khách trả tiền, thử referral trả bằng credit.** Parakeet Chat: khách giới thiệu khách; khi khách mới trả tiền, người giới thiệu nhận khoảng một tháng credit miễn phí.
5. **[manual] Với sản phẩm cần người khác mới dùng được, ưu tiên mật độ.** Lobby: làm tính năng mời và chia sẻ ngay trong sản phẩm, thêm chụp ảnh nhóm khi đang gọi video (ảnh boomerang đăng story, người chưa vào tò mò quay lại); founder nói vấn đề mật độ không giải được bằng content marketing.
6. **[manual] Đo:** số lượt chia sẻ hoặc mời, số người mới đến từ link, tỉ lệ đăng ký, số người trả tiền. Chưa đo được thì chưa biết vòng có chạy hay chỉ nhìn thấy nút.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): mỗi cơ chế một dòng: số lượt chia sẻ hoặc mời, số người mới đến từ đó, tỉ lệ thành người dùng, tỉ lệ thành người trả tiền, thưởng đã phát (nếu có).

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 14 ngày, ≥3 người mới đăng ký đến từ link hoặc mã chia sẻ của người dùng cũ. Kho chỉ có một con số về quy mô (Glam Up, bảng bên dưới), không đủ làm ngưỡng.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 9 step trong 8 video |
| Case (video, case) có step này | 8, trong đó 7 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 0/9 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 4/7 |
| Case full không nêu existing_audience | 7/7 |
| Case full video không kể bằng chứng nhu cầu trước launch | 3/7 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.0 tháng (12.0–12.0), n=1 |
| Kênh scale trả tiền / thuần organic / không nêu | 1 / 6 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g10-referral-viral-loop.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
**Bằng chứng founder còn ít.** Mục con (câu truy vấn: `engine/recipes/g10-referral-viral-loop.extra.sql`; một case có thể thuộc nhiều cơ chế): mời bạn để mở khoá ở 2 case (Glam Up, GlowUp); referral trả bằng credit ở 1 (Parakeet Chat); link hoặc asset chia sẻ có tên app ở 3 (Stagetimer, Magic Music, Glam Up); vòng xã hội/mật độ ở 3 (Lobby, Shepherd, NGL). Chỉ Glam Up kể con số riêng của vòng giới thiệu (khoảng 1,6 triệu lượt yêu cầu chia sẻ, tự khai). Shepherd nói đang siết vòng xã hội, "đang làm, chưa xong". Số tháng tới mức doanh thu hiện tại chỉ có n=1, không rút trung vị. Theo `community_insider` của 7 case full: 3 người trong cuộc, 3 ghi rõ **outsider** (GlowUp, Parakeet Chat, Stagetimer), 1 không nêu; đừng gộp 3 và 1. Không có step chỉ host; 7 step từ video 2025, 2 từ video 2026.

## Bằng chứng từ kho
Mọi câu là của founder hoặc người nói trong video; không có câu host. Số kết quả lấy từ step và `first_users` của kho (tự khai).

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Nicole (Glam Up) (founder) · `2026-05-11_she-makes-400kmo-from-ai-apps-while-in-college` · 00:09:20 | "around 1. 6 million total requests of people sharing the app" | founder kể: mã mời, khoảng 1,6 triệu lượt yêu cầu chia sẻ app (số tự khai, không kiểm) |
| Hunter Isaacson (NGL) (founder) · `2025-07-25_meet-the-guy-who-solved-growing-apps-hunter-isaa` · 00:10:36 | "And it's way easier to get a download by saying get your own messages than saying, hey, download this app." | founder nói: kêu gọi 'lấy tin nhắn của bạn' dễ hơn kêu gọi tải app (cơ chế link gắn vào story) |
| Jordan (Parakeet Chat) (founder) · `2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of` · 07:58 | "Lots of people who like these products want to talk about it. So, it's all word of mouth." | founder nói: tăng trưởng toàn bộ là truyền miệng; chương trình referral credit nằm ở step của kho |
| Lots (Magic Music) (founder) · `2025-11-09_i-flipped-4-apps-and-made-500-000` · 08:40 | "But, what they tend to do is actually share an asset within the app, so they don't even know that they're sharing the app." | người nói trong video nói: người dùng chia sẻ asset trong app và không biết mình đang chia sẻ app |
| Roger Chen (Lobby) (founder) · `2025-12-06_how-i-built-the-1-app-on-the-app-store-twice` · 00:20:51 | "we know that the answer is really really to double down whatever it takes um to get our density up." | founder nói: giải pháp là nâng mật độ người dùng bằng mọi giá |
| Roger Chen (Lobby) (founder) · `2025-12-06_how-i-built-the-1-app-on-the-app-store-twice` · 00:22:07 | "this is not something that's solvable through content marketing" | founder nói: vấn đề mật độ không giải được bằng content marketing |
| Roger Chen (Lobby) (founder) · `2025-12-06_how-i-built-the-1-app-on-the-app-store-twice` · 00:25:40 | "it has to be a shared experience." | founder nói: sản phẩm phải là một trải nghiệm chung (cơ sở của tính năng mời và chụp ảnh nhóm) |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Bằng chứng founder còn ít.** 8 case, chỉ 1 kể số lượt chia sẻ; không có số chuyển đổi hay tỉ lệ người mới đến từ vòng giới thiệu ở case nào. Kho chỉ chứa người thắng: người thêm nút mời mà không ai dùng không có trong kho.
- **Vòng giới thiệu thường đi cùng một kênh khác mạnh hơn.** Glam Up còn có tài khoản TikTok của founder (video đầu đạt 10 triệu view) và traffic đổ về từ một app copy cùng tên đi viral; GlowUp có một video khoảng 48 triệu view đem khoảng 60.000 lượt tải. Đừng gán toàn bộ kết quả cho mã mời.
- **Mật độ có thể là rào chính.** Lobby cần đủ người cùng dùng; founder kể quá trình dài hơn dự kiến (quãng thời gian chưa rõ trong kho) và nói content marketing không giải được. Sản phẩm một người dùng không có vòng này.
- **Chưa xong cũng là bằng chứng.** Shepherd (nói đang làm, chưa xong) cho thấy đây là việc founder làm sau khi đã có tăng trưởng từ kênh khác, không phải trước.
- **Phân biệt với truyền miệng tự nhiên.** Parakeet Chat nói toàn bộ tăng trưởng là truyền miệng, nhưng chương trình referral credit chỉ là một step; truyền miệng không có cơ chế thuộc `g1`/`g3`, không tính vào đây.

## Quyết định
- **QUA** nếu sau 14 ngày có ≥3 người mới đăng ký đến từ link hoặc mã chia sẻ (đề xuất, chưa có số của kho). Giữ cơ chế và đo tiếp tỉ lệ trả tiền.
- **DỪNG** nếu 0 lượt chia sẻ sau 14 ngày: người dùng không có lý do chia sẻ; bỏ thưởng, quay lại `g1`/`g3` để lấy người dùng bằng kênh khác.
- **TEST THÊM** nếu có chia sẻ nhưng không có người mới: sửa trang người nhận thấy (tên app, nút tải) 7 ngày (đề xuất, chưa có số của kho), như Magic Music (nút "Create your own song").

## Cho solo founder bán global (từ VN)
- **Chép được:** việc thêm tên app vào link/asset chia sẻ, nút mời, mã mời; là code, không cần vốn, làm từ xa.
- **Rào cản thật:** vòng chỉ chạy khi đã có người dùng (không tự tạo người dùng đầu); referral bằng credit cần thanh toán đã chạy (nếu bán ngoài store: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN): dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN trước khi chọn; App Store/Play thì đã thu hộ); thưởng bằng "mời 3 bạn mở khoá" giảm doanh thu từ người trả tiền (Glam Up giữ cả hai lối; kho không cho biết tỉ lệ).
- **KHÔNG nên làm** khi sản phẩm dùng một mình và kín đáo (tài chính cá nhân, sức khoẻ nhạy cảm), hoặc khi chưa có người dùng nào: dùng `g1-first-10-users` trước.
