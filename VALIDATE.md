# Validate trước khi build

> Tổng hợp từ:
> - `superwall/knowledge-base/app-growth-decisions/decisions/choose-idea.md`, `build-or-kill.md`, `aso-search.md`
> - `starter-story-kb/playbooks/02-validate.md`
> - bài học trả giá bằng Hairmint (`product-1k-2/REVIEW-2026-11-15.md`)
>
> Ngày: 15/11/2026. Mục tiêu: app hoặc micro-SaaS bán cho khách global trả cao (US/UK/CA/AU/EU), founder solo làm từ VN.

## Nguyên tắc

1. **Validate là để thay cho việc build, không phải một bước trước khi build.** Pat Walls: một cuộc nói chuyện 15 phút đáng giá hơn 70 app tự build ra.
2. **Đếm tiền, không đếm view hay email.**
   - 120.000 view chỉ ra 8 trial (Flame).
   - Waitlist 40–50k người, chỉ ~0,5% đăng ký khi launch (Massive).
   - 90 trong ~2.000 người đăng ký đã trả $5 trước khi app tồn tại (Runafy). Đây mới là tín hiệu.
3. **Đừng nghĩ ý tưởng từ trang trắng.** Lấy nhu cầu đã được chứng minh (app đang kiếm tiền, format đang viral) rồi đưa sang một nhóm khách hoặc góc chưa ai phục vụ tốt.
4. **Không có kênh thì không có ý tưởng.** Chỉ tiếp tục khi một trong hai điều sau đúng:
   - (a) xem vài giây video là hiểu;
   - (b) người ta gõ đúng tên vấn đề vào ô tìm kiếm.
5. **Kiểm tra ngược chiều chính giả thuyết của mình.** Hairmint chết vì tôi chỉ nhìn số rating mà không đọc ai đang để lại rating.

## Quy trình 4 cổng

Trượt một cổng thì dừng. Không viết code trước cổng 3.

### Cổng 1: kiểm tra tại bàn (≤1 giờ, $0)

| # | Câu hỏi | Ngưỡng qua | Cách kiểm |
|---|---|---|---|
| 1.1 | **Đã có tiền ngay cạnh chưa?** | Có 1–3 app **trong đúng ngách con** kiếm ≥$100k/tháng (luật của Caleb). App $5k/tháng thì chưa đủ. Đối thủ gọi vốn lớn thì không tính, vì vốn che mất việc kinh tế có lãi hay không | Top grossing theo genre ở US/GB/CA/AU (RSS iTunes). Doanh thu đã xác minh trên TrustMRR/RevenueCat. Sensor Tower/AppMagic chỉ là ước tính, thường lệch nhau 10–30 lần |
| 1.2 | **Thuốc giảm đau hay vitamin?** | Có kiểu "bỏ $X, lấy lại hơn $X", hoặc nỗi đau rõ ràng (tiếng ồn khi ngủ, migraine, hẹn hò). Nếu landing page phải giải thích vì sao vấn đề quan trọng thì đó là vitamin | Tự hỏi: app có trực tiếp giải quyết vấn đề không, hay chỉ "cho biết" hoặc "cho xem"? |
| 1.3 | **Có kênh không?** | (a) hiểu trong 2 giây video, hoặc (b) có cụm từ tìm kiếm cụ thể | Route ASO (Steve Young): autofill có cụm từ đó, keyword volume ≥~30, **app #2–3 có ~100+ review**, ít app đặt cụm từ trong tên. **Từ khoá trống trơn (top 3 có 0–1 review) chưa phải cơ hội. Nó có thể nghĩa là chưa ai kiếm được tiền ở đó** |
| 1.4 | **Có rơi vào hình dạng ý tưởng xấu không?** | Tránh: AI companion đơn thuần, ảnh AI cho vui/hype, game chỉ để quay TikTok, mạng xã hội | Đối chiếu `choose-idea.md` rule 11 |
| 1.5 | **Ngách có vừa cỡ không?** | Đủ hẹp để thắng, đủ rộng để đáng làm. Ngách siêu hẹp thường kẹt ở ~$10k/tháng. Conversion cao chưa chắc là business (paruresis: chuyển đổi 30%+ mà cả đời chỉ $5–10k) | Ước số người có vấn đề × tỉ lệ trả tiền × giá |

### Cổng 2: soi lại bằng chứng (2–3 giờ, $0)

Đây là cổng Hairmint đã bỏ qua.

| # | Câu hỏi | Ngưỡng qua | Cách kiểm |
|---|---|---|---|
| 2.1 | **Ai thật sự đang dùng đối thủ?** | Người dùng thật trùng nhóm mình định bán (tuổi, khả năng trả tiền) | Đọc **100+ review gần nhất** qua RSS `itunes.apple.com/{cc}/rss/customerreviews/page={n}/id={id}/sortby=mostrecent/json`. Điểm rating cao mà review có chữ toàn 1★ thường là do app nhắc người dùng chấm 5 sao |
| 2.2 | **Họ ghét gì ở đối thủ?** | Có chỗ yếu mình làm tốt hơn được (onboarding, paywall, độ chính xác) | Gom theo chủ đề: tiền, sai kết quả, lỗi, huỷ gói |
| 2.3 | **V: format này có viral thật không?** | Có NHIỀU video >100k view từ tài khoản **<5k follower** | Tìm trên TikTok. Video lớn từ tài khoản lớn chỉ chứng minh người đó nổi tiếng, không chứng minh format |
| 2.4 | **S: làm số lượng được không?** | Làm được 100 video như vậy (AI hoặc thuê UGC) | Tự đánh giá |
| 2.5 | **C: video có ra đơn không?** (quan trọng nhất) | Comment hỏi "app gì?", "ở đâu?", "bao nhiêu tiền?" chiếm phần đáng kể | Đọc 50–250 comment trên 3–5 video lớn. Ví dụ: video Hair Snap 5,4M view có ~0/252 comment hỏi app (toàn trêu). Video HairLoss AI có ~5/51 (~10%) |
| 2.6 | **Nhóm mình tiếp cận được có phải nhóm sẽ trả tiền không?** | Cùng một nhóm | Hairmint trượt cổng này: creator looksmax kéo về teen, còn người có tiền là nhóm 25–45 |
| 2.7 | **Nỗi đau có được viết công khai không?** | Comment "làm sao để…", subreddit có người xin giúp, người dùng của app rộng hơn đòi một bản hẹp hơn | Reddit (agent và Chrome đều bị chặn, phải mở tay), comment TikTok/YouTube |
| 2.8 | **Có creator để thuê không, giá bao nhiêu?** | Ngách có nhiều creator giá hợp lý, chưa bị app khác làm "mệt" | Đếm creator, xem ai đã từng nhận tài trợ app |
| 2.9 | **Clone tới mức nào rồi?** | Không bị đổ app mới. Nếu có, mình phải có lợi thế rõ | Đếm số app ra trong 6–12 tháng gần nhất (Hairmint: 40 app trong 2026) |

### Cổng 3: test nhu cầu trước khi code (1–2 tuần, $0–500)

Cần đạt **ít nhất mức 5** trên thang tín hiệu bên dưới mới được build.

Làm 1–2 trong các cách sau:
- **Nội dung trước sản phẩm.** Copy 3 format đang chạy, đăng 15–30 bài. Mốc tốt: ~5k view mỗi bài, 75–80% người xem giữ quá 3 giây. Đếm DM và comment hỏi mua.
  - Pushscroll đăng video của một app chưa tồn tại.
  - Stronger dùng mock-up làm bằng Canva, được ~15k follower trong một tuần.
- **Thu tiền trước.** Landing page có nút pre-order kiểu "early adopter $5". Mốc tham khảo: ~4,5% người đăng ký trả tiền (Runafy).
- **Làm dịch vụ bằng tay trước.** Sway thu $15 cho mỗi lần review profile hẹn hò làm tay, trước khi có app.
- **5 cuộc gọi theo Mom Test.**
  - Hỏi "Anh đang giải quyết chuyện này thế nào?", "Lần gần nhất gặp nó là khi nào?", "Nó tốn của anh bao nhiêu?".
  - Không bao giờ hỏi "Anh thấy ý tưởng của tôi thế nào?".
- **Ads để test (có tranh cãi).** Will Baker nói ads không validate được ý tưởng, vì CPA xấu không cho biết lỗi ở ý tưởng hay ở quảng cáo. Roger Chen và studio Social thì vẫn chạy ads cho app chưa tồn tại và so với benchmark. Chỉ dùng khi có ngân sách và đã có benchmark để so.

**Thang tín hiệu** (Starter Story):

| Mức | Tín hiệu | Giá trị |
|---|---|---|
| 1 | Bạn bè khen ý tưởng hay | Vô nghĩa |
| 2 | Video về vấn đề này có nhiều view | Chưa đủ, còn phải xem chữ C |
| 3 | App tương tự đang được rao bán, có doanh thu (acquire.com, Flippa) | Có người trả tiền thật |
| 4 | Người ta tự khai dữ liệu của mình trong comment | Nhu cầu có sẵn |
| 5 | **Comment hỏi mua** | **Ngưỡng tối thiểu để build** |
| 6 | Cùng một nỗi đau lặp lại qua nhiều cuộc gọi Mom Test | Đủ để build |
| 7 | Người lạ chủ động DM xin sản phẩm | Rất mạnh |
| 8 | **Có người trả tiền dù sản phẩm còn thô** | Chốt |

### Cổng 4: build và phán quyết

- **Build:** chỉ một hành động cốt lõi, xấu cũng được, trong 2–4 tuần.
- **Sau launch:** 2 tuần chỉ làm phân phối, không đụng vào sản phẩm.
- **Cần đủ lượng trước khi kết luận:** ≥30–100 user mới/tuần. Dưới mức đó thì mọi thí nghiệm đều là nhiễu.
- **Tìm đúng khâu gãy trước khi giết app:**

  | Khâu gãy | Sửa gì |
  |---|---|
  | Có view nhưng không có install | Góc nội dung |
  | Có install nhưng không ai trả tiền | Onboarding, paywall |
  | Trả tiền rồi bỏ | Sản phẩm, hoặc sai nhóm khách |

- **Giết khi:** đẩy phân phối thật mà không ai trả tiền; trần thị trường quá thấp; hoặc mình không còn làm nữa. Một app đang ngủ thì bán đi hoặc chia equity cho creator. Đừng giữ vì tiếc công.
- **Kiên nhẫn với từng format:** tối thiểu 90 ngày, hoặc ~25 video với một creator mới. Format chết không có nghĩa là sản phẩm chết.

## Rào cản riêng của founder ở VN bán ra global

- **Thu tiền pre-order.** Stripe thường không mở cho pháp nhân VN. Dùng merchant-of-record (Polar, Lemon Squeezy, Paddle, Creem…), nhưng phải kiểm điều kiện nhận seller ở VN trước khi chọn. App Store thì đã thu hộ.
- **TikTok bị khoá theo vùng.** Tài khoản đăng từ VN thường được phân phối cho người xem ở VN, và kết quả tìm kiếm cũng bị cá nhân hoá theo VN (đã thấy khi kiểm Hairmint).
  - Muốn test nội dung cho US/UK, thuê creator ở đó: tham khảo Fitted trả $20/video, Flame thuê UGC Đông Âu $1/video.
  - Hoặc dùng kênh ít khoá vùng hơn: Reddit, X, Reels, Shorts.
- **Mom Test:** cần tiếng Anh và lệch múi giờ. Đặt lịch qua DM hoặc Reddit, hoặc cho người dùng thêm quota để đổi lấy một cuộc gọi.
- **Lợi thế:** chi phí sống thấp nên chịu được 90 ngày cho mỗi format.

## Scorecard: copy cho mỗi ý tưởng

```
Ý tưởng:            Ngày:            Người chấm:
Nhóm khách trả tiền (tuổi, nước, vì sao trả):

Cổng 1 (tại bàn)
[ ] 1.1 Tiền đã có cạnh:   app ≥$100k/th trong ngách con = ______ (nguồn: ______)
[ ] 1.2 Thuốc giảm đau:    ______
[ ] 1.3 Kênh:              video 2 giây? ___  /  cụm tìm kiếm: "______", review của #2–3: ___
[ ] 1.4 Không phải hình dạng ý tưởng xấu
[ ] 1.5 Vừa cỡ:            ______

Cổng 2 (soi bằng chứng)
[ ] 2.1 Đã đọc ___ review của ______ → người dùng thật là: ______
[ ] 2.2 Họ ghét: ______
[ ] 2.3 V: ___ video >100k view từ tài khoản <5k follower
[ ] 2.4 S: ______
[ ] 2.5 C: ___/___ comment hỏi mua trên ___ video
[ ] 2.6 Nhóm có kênh = nhóm trả tiền?
[ ] 2.7 Nỗi đau công khai ở: ______
[ ] 2.8 Creator: ___ người, ~$___/video
[ ] 2.9 Clone 12 tháng qua: ___ app

Cổng 3 (test trước code) → mức tín hiệu đạt được: ___ / 8 (cần ≥5)
   Cách test: ______   Kết quả: ______

Quyết định:  BUILD / DỪNG / TEST THÊM (cái gì, tới ngày nào)
```

## Ví dụ: chấm lại Hairmint

| Cổng | Kết quả | Vì sao |
|---|---|---|
| 1.1 Tiền đã có cạnh | ❌ | Không app rụng tóc nào có doanh thu ≥$100k/tháng đã xác minh. Hair Snap không có trong top 100 grossing Lifestyle. Tiền nằm ở Hims (telehealth, có quản lý) |
| 1.2 Thuốc giảm đau | ❌ | App scan và preview chỉ "cho xem", không chữa được gì |
| 1.3 Kênh | ⚠️ | Video before/after thì có. Nhưng từ khoá "hair transplant" có top 3 với 0–1 review, nghĩa là chưa ai chứng minh từ khoá đó ra tiền |
| 2.1 Ai dùng đối thủ | ❌ | Hair Snap: teen, người hỏi tóc xoăn, nam rất trẻ |
| 2.3 V | ✅ | Format "tóc mỏng → glow up" có video hàng triệu view |
| 2.5 C | ❌ | Video 5,4M view có ~0/252 comment hỏi app |
| 2.6 Nhóm có kênh = nhóm trả | ❌ | Kênh kéo về teen, người có tiền là nhóm 25–45 |
| 2.9 Clone | ❌ | 40 app ra trong 2026 |
| Cổng 3 | — | Bỏ qua, build luôn trong một đêm |

**Kết luận:** nếu chạy bộ lọc này trước khi build thì Hairmint đã dừng ở cổng 1, mất chưa tới 3 giờ.
