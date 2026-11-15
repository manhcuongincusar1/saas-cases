---
id: hnxn16HtLIk
slug: brainrot
product: Brainrot
founder: Yoni Smolyar — cựu kỹ sư phần mềm doanh nghiệp, làm content build in public trên Instagram trước khi launch, cùng co-founder Brock Anderson
tagline: App screen time gamified với "bộ não thú cưng" bị thối dần khi bạn lướt mạng xã hội — tăng từ ~$10K lên ~$400K/tháng trong khoảng một năm nhờ audience có sẵn, influencer và paid ads
revenue_usd_month: 400000
revenue_basis: Theo lời founder "about 400,000 a month in revenue", lặp lại hai lần trong video. Không nói rõ là MRR hay doanh thu cash; vì app "mostly sell annual subscriptions" nên con số nhiều khả năng gồm cả tiền gói năm thu trước (suy luận của người viết). Không có dashboard trong video, không có chi phí quảng cáo hay lợi nhuận. Khớp với tiêu đề "$400K/Month".
model: mobile-app-subscription
category: productivity — screen time và chặn app có yếu tố game
audience: B2C — người dùng iPhone muốn giảm thời gian lướt mạng xã hội
started: ra mắt mùa hè 2025, build trong khoảng một tháng
time_to_first_sale: ngày launch — khoảng $10.000 doanh thu trong ngày đầu theo trí nhớ của founder
time_to_scale: khoảng một năm từ ~$10K/tháng lên ~$400K/tháng
team_size: 2 (hai co-founder) cộng contractor và freelancer thuê qua Upwork
funding: không nêu
main_channel: audience Instagram sẵn có và waitlist trước launch, sau đó influencer content và paid ads
tech_stack: [Mixpanel, Firebase, Supabase, Superwall, AppStack, Claude Code, Codex, Upwork]
key_metrics:
  monthly_revenue_usd: 400000
  starting_revenue_usd_month: 10000
  launch_day_revenue_usd: 10000
  downloads_total: 2000000
  users_total_approx: 150000
  instagram_followers_pre_launch_min: 100000
difficulty: 4
video_url: https://www.youtube.com/watch?v=hnxn16HtLIk
published: 2026-11-01
views: 170099
tags: [mobile-app, subscription, influencer-marketing, paid-ads, waitlist, personal-brand, build-in-public, scratch-own-itch, distribution, niche-app]
---

# Brainrot — app screen time "bộ não thú cưng" lên $400K/tháng, nhờ audience có sẵn trước khi launch

> **Tóm tắt 30 giây:** Yoni Smolyar, kỹ sư phần mềm ở công ty lớn, nghiện điện thoại và nảy ra ý tưởng "what if a brain rots or you brain rot?" — một app screen time có bộ não thú cưng thối dần theo thời gian bạn lướt Instagram, YouTube, X. Điểm khác thường: trước khi launch anh đã có khoảng 100.000-150.000 follower Instagram nhờ vài tháng build in public và kéo người vào waitlist, nên ngày đầu app thu khoảng $10.000 (theo trí nhớ của anh). Từ đó, đòn bẩy tăng trưởng là phân tích power user, nhân đôi những gì đang chạy (influencer content và paid ads), và bắt tay co-founder Brock Anderson. Sau khoảng một năm, founder nói app đạt "about 400,000 a month in revenue", mua chủ yếu qua gói năm, khoảng vài triệu lượt tải. Video không đưa dashboard, giá, chi phí quảng cáo hay lợi nhuận, nên con số $400K cần đọc như lời kể chưa kiểm chứng, và lợi thế audience 100K+ trước launch gần như không sao chép được với người chưa có.

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu hiện tại (founder nói) | **~$400.000/tháng** |
| Doanh thu thời điểm launch | **~$10.000/tháng** |
| Doanh thu ngày launch đầu | **~$10.000** ("I think") |
| Lượt tải tích luỹ | **"a couple million"** |
| Số user | **"150-something thousand"** (không rõ là MAU, subscriber hay user đăng ký) |
| Follower Instagram trước launch | **~100.000-150.000** |
| Thời gian | **~1 năm** (launch mùa hè 2025) |
| Nhân sự | **2 co-founder** + contractor Upwork |

[00:00](https://www.youtube.com/watch?v=hnxn16HtLIk&t=0s) và [01:24](https://www.youtube.com/watch?v=hnxn16HtLIk&t=84s) là các đoạn nói con số.

**Lưu ý khi đọc con số:**
- Không có màn hình dashboard nào trong video; toàn bộ là lời founder nói.
- Founder nói "about 400,000 in revenue, 150-something thousand users" liền một câu mà không phân loại — không rõ $400K là MRR hay doanh thu tháng, vì gói năm chiếm phần lớn nên cash thu có thể lệch so với MRR chuẩn hoá. Đây là điều video không giải thích.
- Không có chi phí quảng cáo, phí Apple, lợi nhuận hay số subscriber trả phí. "$400K" là doanh thu, không phải lợi nhuận.
- Mốc "$10K/tháng" lúc đầu và "$10K ngày đầu" đều là trí nhớ của founder ("I think"), không phải số đối chiếu.

---

## 2. Sản phẩm giải quyết vấn đề gì

Brainrot là **app screen time dạng game** ([01:24](https://www.youtube.com/watch?v=hnxn16HtLIk&t=84s)): một **bộ não thú cưng** sống trong app, sức khoẻ giảm ("rots") càng nhiều thời gian bạn dùng các app gây nghiện. Trong demo ([10:31](https://www.youtube.com/watch?v=hnxn16HtLIk&t=631s)):
- Bộ não có chỉ số sức khoẻ (lúc demo là 97%).
- Thống kê thời gian dùng từng app theo ngày, đặt luật chặn app theo giờ.
- Cơ chế cốt lõi: khi mở một app bị chặn (ví dụ Instagram), người dùng phải đi qua một **flow ngắn có ma sát** (trong demo là cuộc "gọi FaceTime từ bộ não của mình"). Founder nói thế là đủ để đổi thói quen.

Nỗi đau: sao lãng bởi điện thoại. Founder thừa nhận mình có thể tải một app chặn thông thường, và "I wasn't the first to come up with this concept" — khác biệt là **định dạng game có nhân vật** và cái tên meme. Video không nói đối thủ nào, cũng không nói mức độ giữ chân hay hiệu quả thật sự trong việc giảm screen time.

---

## 3. Ý tưởng đến từ đâu

Hai nguồn xếp chồng nhau ([03:03](https://www.youtube.com/watch?v=hnxn16HtLIk&t=183s)):

1. **Scratch your own itch**: Yoni nghiện Instagram, YouTube, Twitter; nảy ra "what if a brain rots or you brain rot?" và thấy chưa ai làm app đó.
2. **Có audience trước**: anh theo dõi giới indie hacker (nhắc tới Starter Story, Pat Walls, Peter Levels — những người "had this inbuilt distribution") và muốn có phân phối tương tự, nên bắt đầu làm content kể câu chuyện founder phía sau hậu trường. Khi nảy ra ý tưởng app, anh đã có sẵn tệp người xem.

Về động lực: "I was excited enough to drop everything and go heads down on this for a month." Host nói app được build "in a couple weeks"; Yoni nói một tháng — hai cách nói khác nhau, video không làm rõ cái nào chính xác.

---

## 4. Cách validate

Video **không nói** có customer interview hay landing test riêng. Cách validate thực tế là **waitlist qua audience**: anh đăng "I'm building an app, sign up for the waitlist" và giữ độ hồi hộp trước launch ([04:10](https://www.youtube.com/watch?v=hnxn16HtLIk&t=250s)), rồi launch và thu khoảng $10.000 trong ngày đầu.

Hạn chế quan trọng: tín hiệu này bị **bơm bởi audience sẵn có** — 100K+ follower. Doanh thu ngày đầu chứng minh anh bán được cho người đã theo dõi anh, chưa chứng minh app tự bán được cho người lạ. Bằng chứng cho phần "người lạ" nằm ở giai đoạn sau, khi anh scale bằng influencer và paid ads (xem mục 5), nhưng video không đưa CAC hay ROAS.

---

## 5. Go-to-market ⭐ — audience sẵn có, phân tích power user, rồi nhân đôi cái đang chạy

### Trước launch: audience và waitlist ([04:10](https://www.youtube.com/watch?v=hnxn16HtLIk&t=250s))
~100K-150K follower Instagram và một waitlist. Chính anh gọi đây là "a bit of an unusual story". Anh kể bước này nhằm làm một "shadowy figure who just moves in silence" thành người dám xuất hiện công khai.

### Sau launch: ba đòn bẩy anh nêu ([04:43](https://www.youtube.com/watch?v=hnxn16HtLIk&t=283s))

1. **Hiểu power user.** Có dữ liệu sau launch thì phải xem ai là power user, ai là user thường; đây là "a big unlock for us". Ở phần lời khuyên ([07:28](https://www.youtube.com/watch?v=hnxn16HtLIk&t=448s)): đẩy analytics sang Mixpanel hoặc PostHog, tìm "activation moment", xem nhóm nào hoạt động nhiều nhất rồi tìm cách đưa các user còn lại tới hành vi đó.
2. **Nhân đôi cái đang chạy.** "If something is working, try to do 10 times more of that thing." Với họ, thứ tạo tăng trưởng đầu tiên là **influencer content và paid ads** — họ "just simply scaled what we knew". Video **không cho** tên nền tảng ads, ngân sách, CPA, số influencer hay tỷ lệ chuyển đổi.
3. **Co-founder.** Hợp tác với Brock "was a huge force multiplier" ([05:32](https://www.youtube.com/watch?v=hnxn16HtLIk&t=332s)). Khi quay lại bài học năm 2026 anh khuyên: nếu từng thử solo nhiều lần mà chưa thắng thì đừng đi một mình — tìm co-founder bổ trợ kỹ năng, hoặc xây đội bằng equity.

### Thí nghiệm nhỏ và độ trễ ([07:45](https://www.youtube.com/watch?v=hnxn16HtLIk&t=465s))
Thử nhiều thay đổi nhỏ (bỏ một slide onboarding, đổi thứ tự màn hình); phần lớn không có tác dụng, nhưng 1 trong 10 có thể đổi quỹ đạo. Anh cũng nhấn mạnh độ trễ giữa nỗ lực và kết quả — đừng tự mãn.

### Điều video không nói
Tỷ lệ phân bổ doanh thu giữa organic, influencer và ads; số liệu retention; việc audience Instagram đóng góp bao nhiêu phần trong $400K; mức churn của gói năm khi gia hạn.

---

## 6. Mô hình kiếm tiền & giá

- **Subscription**, "mostly sell annual subscriptions" ([01:39](https://www.youtube.com/watch?v=hnxn16HtLIk&t=99s)).
- Paywall quản lý bằng **Superwall** ([10:04](https://www.youtube.com/watch?v=hnxn16HtLIk&t=604s)).
- **Giá cụ thể, trial, hard hay soft paywall: video không nêu.**
- Lời khuyên về chọn ý tưởng: xây thứ có LTV rất cao hoặc thứ người dùng mở mỗi ngày ([09:24](https://www.youtube.com/watch?v=hnxn16HtLIk&t=564s)) — Brainrot thuộc nhóm thứ hai về nhịp sử dụng, nhưng chưa rõ về LTV.

Nhận xét của người viết: gói năm thường thu tiền trước nên làm doanh thu tháng cash cao hơn MRR chuẩn hoá và là điều cần kiểm tra khi so sánh với case khác.

---

## 7. Tech stack & chi phí

| Hạng mục | Công cụ |
|---|---|
| Analytics | **Mixpanel**; **Firebase** (analytics và experiments) |
| Công cụ nội bộ và tracking | **Supabase** (ASR ghi "Superbase") |
| Paywall | **Superwall** |
| Attribution cho paid ads | **AppStack** (ASR/tên có thể chưa chuẩn) |
| Coding và việc nội bộ | **Claude Code** và **Codex** |
| Thuê ngoài | **Upwork** (contractor, freelancer) |

Video không nêu chi phí hạ tầng hay chi phí marketing. Lưu ý host nói nhầm tên app thành "Brainscape" một lần ở phần hỏi stack — bỏ qua, đây là ASR/lỡ lời, tên đúng theo mô tả là Brainrot.

---

## 8. Bài học & trích dẫn

- **Audience là một dạng vốn.** Case này khác phần lớn case "app đơn giản" trong kho ở chỗ có phân phối sẵn từ ngày đầu — thứ gần như không thể mua nhanh.
- **Đo trước, nhân đôi sau.** Phân tích power user và chỉ nhân lên cái đã chứng minh.
- **Đừng đi solo nếu đã thất bại nhiều lần một mình.** Đây là lời khuyên cá nhân, không có dữ liệu so sánh.
- **Độ nhỏ của thí nghiệm:** 9/10 lần không đổi gì, 1/10 đổi quỹ đạo.

> **"I was excited enough to drop everything and go heads down on this for a month."**

> **"You should double down on what's working for you. If something is working, try to do 10 times more of that thing."**

> **"Don't chase trends or copy apps to try to make a quick buck."**

> **"Nine out of 10 of the times, it will not move the needle, but one in 10 times, it can be trajectory changing."**

**Góc nhìn tỉnh táo:** có tính mỉa mai khi founder khuyên "don't chase trends" trong khi tên app bám theo thuật ngữ "brain rot" đang viral và anh khởi động bằng audience mạng xã hội 100K+. Survivorship bias rất mạnh: ta không thấy những app screen time có audience tương tự nhưng không tăng. Cũng không có dữ liệu để biết $400K bền hay chỉ là đỉnh sau chiến dịch ads.

---

## 9. Áp dụng cho tôi (indie hacker ở VN, bán global)

**Sao chép được gì:**
- **Công thức "audience trước, app sau":** kể quá trình build trên Instagram/X, gom waitlist, đo bao nhiêu người đăng ký trước khi viết dòng code lớn. Đây là cơ chế, không cần ngách screen time.
- **Quy trình phân tích sau launch:** gắn Mixpanel/PostHog, xác định activation moment và nhóm power user, rồi kéo user thường theo hành vi đó.
- **Nguyên tắc "nhân 10 lần cái đang chạy"** thay vì thử mọi kênh, cộng thí nghiệm nhỏ liên tục trên onboarding và paywall (Superwall).
- **Cơ chế friction có thương hiệu:** biến một hành vi khó duy trì (bỏ lướt điện thoại) thành trải nghiệm có nhân vật và cảm xúc — cơ chế đáng tái dùng cho bất kỳ app thay đổi thói quen nào.

**Rào cản thật:**
- **Phân phối:** lợi thế lớn nhất của Yoni là 100K-150K follower trước launch, kết quả của một thời gian dài làm content. Nếu không có, doanh thu ngày đầu $10K gần như không lặp lại được.
- **Vốn:** influencer và paid ads cần ngân sách; video không nêu bao nhiêu. Ở mức $400K/tháng nhiều khả năng có phần chi phí lớn mà ta không thấy.
- **Cạnh tranh:** app screen time và chặn app là danh mục đông; khác biệt hiện tại là cái tên và nhân vật, dễ bị bắt chước.
- **Tiếng Anh và thương hiệu cá nhân:** để làm đúng công thức này cho khách Mỹ/EU, bạn phải xuất hiện bằng tiếng Anh trên hình ảnh và video — rào cản thật với founder ở VN nếu không quen lên hình (nhận định của người viết).
- **Múi giờ:** làm việc với influencer ở Mỹ cần xử lý chênh giờ khi giao tiếp (nhận định của người viết).

**Biến thể đáng thử ở thị trường trả cao:**
- **App thay đổi thói quen có nhân vật cho ngách nhỏ hơn, gắn với nhu cầu tài chính/sức khoẻ rõ:** ví dụ app giảm tiêu dùng bốc đồng (pet "thủng ví" khi bạn tiêu quá tay) hoặc ngủ muộn; trả phí gói năm cỡ vài chục USD (ước tính của người viết). Có cửa vì cơ chế game + friction đã chứng minh được ở một danh mục khác.
- **Xây audience nhỏ nhưng đúng ngách (vài nghìn follower) thay vì 100K:** dùng waitlist để đo nhu cầu, rồi chạy thử một vài influencer nhỏ trước khi bơm ads. Có cửa vì chi phí thấp, giảm rủi ro khi chưa có tệp lớn.
- **Tìm co-founder làm marketing/creator** bổ trợ cho kỹ năng build của bạn — đúng lời khuyên của Yoni và cách giải rào cản phân phối.

**Khi nào KHÔNG nên làm:**
- Khi bạn chưa có audience và không có ngân sách thử ads/influencer.
- Khi không thể kiên trì làm content công khai nhiều tháng trước launch.
- Khi ngách là danh mục "hyper-competitive" và đây là lần đầu bạn làm app — chính Yoni khuyên tránh.
- Khi bạn kỳ vọng con số $400K/tháng là mốc thực tế; nó là một đầu ra hiếm, không đại diện cho mức trung bình.

---

## Nguồn

- Video: [How I Built It: $400K/Month iOS App](https://www.youtube.com/watch?v=hnxn16HtLIk) — Starter Story, 01/11/2026, 12:23, 170K views
- Transcript: [`transcript.md`](transcript.md)
