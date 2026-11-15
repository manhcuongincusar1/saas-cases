---
id: s9aLA4IOSZE
slug: geosports
product: GeoSports
founder: Frank Smith (X frankmikesmith) — creator video thể thao ngắn độc lập từ 2020 với 4+ triệu follower, không biết code, từng ra vài game nhỏ trước đó
tagline: Game web hằng ngày "chạm vào nơi sự việc xảy ra" cho fan thể thao — build bằng Claude trong một cuối tuần, lên khoảng $40K/tháng sau 3 tháng, chủ yếu từ quảng cáo programmatic
revenue_usd_month: 40000
revenue_basis: Founder nói "about $40,000 monthly" và mô tả/tiêu đề khớp. Gồm khoảng $30–35K quảng cáo programmatic (founder cho biết số liệu ads chưa đủ 30 ngày, hover khoảng $1.200/ngày) cộng khoảng 1.800 pro subs trên Stripe (phần nhỏ hơn). Không phải MRR thuần; phần lớn phụ thuộc traffic nên biến động
model: ad-supported-web-game
category: game web hằng ngày / trivia địa lý thể thao (có spin-off lịch sử, bóng đá)
audience: B2C — người chơi miễn phí xem quảng cáo; một phần nhỏ trả gói pro. Nhà quảng cáo programmatic mới là nguồn tiền lớn
started: ~3 tháng trước thời điểm quay (khoảng mùa hè 2026); build trong một cuối tuần
time_to_first_sale: không nêu rõ — khi mới nói chuyện lần đầu founder mới kiếm vài nghìn đô mỗi tháng
time_to_scale: ~3 tháng từ 0 tới ~$40K/tháng theo lời host và founder
team_size: 1 (solo theo mô tả; founder dùng "we" nhưng không nêu thêm ai)
funding: bootstrapped
main_channel: Truyền miệng qua chia sẻ điểm (53% share rate) khởi động bằng X của founder cộng chương trình "host" với nhân vật thể thao
tech_stack: [Claude Max 20x, Vercel Pro, MapLibre, Upstash Redis, Google Sheets, Stripe]
key_metrics:
  monthly_active_users: 700000
  pro_subscribers: 1800
  programmatic_ads_usd_month_low: 30000
  programmatic_ads_usd_month_high: 35000
  ads_usd_per_day: 1200
  organic_share_rate_pct: 53
  peak_players_one_day: 150000
  unique_players_first_month: 1000000
  founder_followers: 4000000
  traffic_from_founder_posts_pct: 2
difficulty: 4
video_url: https://www.youtube.com/watch?v=s9aLA4IOSZE
published: 2026-09-27
views: 135907
tags: [ai-coding, non-developer, solo-founder, ship-fast, trend-riding, clone-idea, distribution, content-marketing, bootstrapped]
---

# GeoSports — game web dựng trong 8 giờ bằng Claude, $40K/tháng nhờ quảng cáo và một cú viral trên X

> **Tóm tắt 30 giây:** Frank là creator video thể thao ngắn với hơn 4 triệu follower, không biết code. Anh thấy em trai chơi MapTap, nảy ra ý "bản thể thao" của nó, rồi build GeoSports bằng Claude trong một Chủ nhật (khoảng 8 giờ, nghỉ nốt thứ Hai để hoàn thiện). Mỗi ngày người chơi nhận 5 câu hỏi, chạm lên bản đồ ở nơi sự việc xảy ra rồi được chấm điểm và chia sẻ kết quả. Sau một cú viral (bài reply trên X lên 40.000 người chơi, hôm sau 150.000 người trong một ngày), game có khoảng 700.000 MAU, 53% share rate, và theo lời anh kiếm khoảng $40K/tháng — phần lớn (~$30–35K) là quảng cáo programmatic, phần còn lại là khoảng 1.800 pro subs. Hai điều video không nhấn mạnh: tiền chủ yếu là quảng cáo (không phải MRR) và số ads mới đo chưa tới 30 ngày; còn "8 giờ" là phần dễ thấy của một tay creator có 4 triệu follower đã làm game từ 2020.

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu tháng (founder nói) | **~$40.000** ([01:23](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=83s)) |
| Quảng cáo programmatic | **~$30–35K/tháng**, ~$1.200/ngày (số ads chưa đủ 30 ngày) ([01:39](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=99s)) |
| Pro subscriber (Stripe) | **~1.800** |
| MAU | **~700.000** |
| Share rate | **53%** (nếu 100.000 người chơi thì 53.000 chia sẻ điểm) |
| Số người chơi trong một ngày cao nhất | **150.000** |
| Người chơi duy nhất trong tháng đầu | **1 triệu+** |
| Thời gian từ build tới hiện tại | **~3 tháng** |
| Nhân sự | **1 (solo)** |

**Điểm đáng chú ý về con số:**
- Founder tự nói "a smaller percentage of this is the pro subs" và "the much larger number comes in through the ads". Nghĩa là **doanh thu chủ yếu là quảng cáo programmatic**, đo theo traffic/ngày, rất khác MRR của SaaS. Nếu traffic giảm, doanh thu giảm theo.
- Anh nói dashboard ads "very young... we actually don't even have a full 30 days yet" ([02:12](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=132s)). Con số $40K là **run-rate** chưa kiểm chứng qua nhiều tháng.
- Giá gói pro, tỉ lệ pro/active user, và churn **không nêu**. Cũng không nêu quảng cáo chạy qua mạng nào.
- Host nói "zero to 40k per month in 3 months", còn mô tả viết "built in just a few hours". Trong video, anh làm khoảng 8 giờ vào Chủ nhật rồi "canceled my schedule on that Monday and kept working" tới lúc "sent it out" — nên là cả cuối tuần chứ không phải đúng 8 giờ.
- Số share rate, MAU, subs là số founder tự trình bày bằng dashboard (anh có chiếu Stripe và ads), không có kiểm toán độc lập.

---

## 2. Sản phẩm giải quyết vấn đề gì

Founder gọi app là **Geo Games**, chứa nhiều spin-off: Geo Sports, Geo History, Geo Footy — "all the same game just for different niches" ([01:23](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=83s)). Trang chủ GeoSports: "daily sports geography game. Tap where it happened. Five questions" ([02:29](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=149s)). Mỗi ngày có 5 câu hỏi dạng gợi ý ("tailgating super fans themselves through tables in this NFL town"), người chơi chạm lên bản đồ càng gần đáp án càng nhiều điểm (xa hơn thì điểm thấp hơn, chấm xanh/vàng), rồi chia sẻ điểm.

Điểm mạnh theo founder: "we never had to teach people how to play this game". Game chạy trên web, nên chơi và chia sẻ được ngay trong X mà không rời app. Đây là **nhu cầu giải trí hằng ngày** chứ không phải vấn đề nghiệp vụ; sản phẩm thắng vì chơi 2 phút và có chuyện để khoe với bạn bè.

---

## 3. Ý tưởng đến từ đâu

- Em trai Frank chỉ cho anh game **MapTap**. Anh luôn thích bản đồ, quả địa cầu, Google Maps. Trên đường lái xe về sau đám cưới bạn vào Chủ nhật, anh nghĩ: "What if I had a sports version because MapTap doesn't do any sort of trivia" ([06:51](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=411s)).
- Anh gọi đó là "a remix of sorts" — mô hình **sao chép và cải tiến** một game đã có chứng cứ (MapTap), gắn vào ngách mà anh có audience và hiểu sâu (thể thao).
- Anh đã làm game từ 2020 (Five Card Draw ~110.000 người chơi: "It was not a small game, but it was very, very niche.") và vài game nữa; còn đang dự định ra mắt một game khác thì GeoSports "exploded out of nowhere after a weekend of work".
- Ghi chú: đây là case "đúng người, đúng thời điểm" hơn là phát hiện vấn đề mới.

---

## 4. Cách validate

Video không nói về validate bài bản (không khảo sát, không waitlist). Cách làm thực tế là **stealth launch + quan sát hành vi chia sẻ** ([10:39](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=639s)):

- Gửi cho vài người thân và bạn bè, thấy họ **tự chia sẻ** lại, rồi mới thấy yên tâm đăng lên social.
- Mở rộng bằng vài bài trên X; bài khiến game "đi" là một **reply vào tweet của chính mình** (tweet gốc nói về NBA, không phải game) — "that reply went completely viral". Sau đó có ~40.000 người chơi, hôm sau ("that Saturday") 150.000 người trong một ngày. Game mới 5 ngày tuổi.
- Họ "very unprepared on the retention side" nên phải xử lý gấp, chưa rõ chi tiết.

Điều đáng nhớ: tín hiệu validate là **tỉ lệ chia sẻ**, không phải lời khen. Chỉ số cuối cùng (53% share rate) là hệ quả, không phải thứ đo trước khi build.

---

## 5. Go-to-market ⭐

Video trả lời rõ câu hỏi "chỉ thành công vì có 4 triệu follower?" ([05:11](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=311s)):

- Founder nói: mỗi ngày anh đăng một trong năm câu hỏi lên X và Instagram story, đem về khoảng **2.000 click** — "about 2% of our daily traffic". 98% còn lại là người chơi "probably don't even know that I'm the founder". Anh cũng chỉ làm **một video** về game.
- Cơ chế tăng trưởng chính là **truyền miệng qua group chat**: kết quả có thể chia sẻ (điểm số, chấm màu), chơi trên web không cần cài đặt, "near zero friction", chơi được ngay trong X ([08:43](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=523s)).
- **Chương trình "host"** ([11:45](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=705s)): anh tạo vai trò host cho nhân vật thể thao/vận động viên trên X; DM những người có lượng follower lớn đã like bài về game, đề nghị họ viết 5 câu hỏi trong ngày. Khi game đăng lên với tên host, họ gần như luôn retweet nên game tới tệp người mới. Anh gọi đó là "cheat code", đồng thời là cách kết nối.
- Cập nhật hằng ngày (5 câu mới) tạo thói quen quay lại: "a very habitual game".

**Phải đọc kèm:** cú viral khởi đầu đến từ **reply trên tài khoản X của chính anh** ngay khi game còn sơ khai. Anh có hơn 4 triệu follower trên mạng xã hội (tuyên bố: "I'm very well known for that"). Việc "2% traffic mỗi ngày từ bài của anh" là về **trạng thái ổn định hiện tại**, không phải về cú khởi động. Video không đo được bao nhiêu trong 40.000 → 150.000 người chơi ban đầu đến trực tiếp từ audience của anh. Người không có audience gần như không có điểm xuất phát này.

---

## 6. Mô hình kiếm tiền & giá

Hai nguồn, tỉ trọng rất lệch:
1. **Quảng cáo programmatic: ~$30–35K/tháng**, ~$1.200/ngày. Doanh thu nhiều khả năng tăng theo số lượt chơi (suy luận của người viết); không nêu mạng quảng cáo hay CPM.
2. **Pro subscription qua Stripe: ~1.800 subscriber** (founder nói đây là "smaller percentage"). Giá và quyền lợi gói pro không nêu (người viết đoán là bản ít quảng cáo/thêm tính năng, nhưng video không nói).

Mô hình này là **ad-supported web game + freemium sub**. Quảng cáo phụ thuộc lượng người chơi hằng ngày mà bạn phải giữ lại mỗi ngày (retention là chìa khoá, và chính founder thừa nhận lúc viral họ "unprepared on the retention side").

---

## 7. Tech stack & chi phí

Theo [08:14](https://www.youtube.com/watch?v=s9aLA4IOSZE&t=494s) (ASR sai tên, đối chiếu cách đọc):

| Hạng mục | Công cụ |
|---|---|
| Build | **Claude Max (gói 20x)** — ASR ghi "cloud max" |
| Hosting | **Vercel Pro** + domain mua từ Vercel — ASR ghi "Verscell" |
| Bản đồ/quả địa cầu | **MapLibre** |
| Bảng xếp hạng và thống kê | **Upstash Redis** — ASR ghi "Up stash reddish" |
| Nội dung câu hỏi | **Google Sheets** |
| Pro subscription | **Stripe** |

Chi phí cụ thể **không nêu** ngoài việc tên gói (Claude Max 20x và Vercel Pro đều là gói trả phí). Cách làm: viết spec trước, nhờ Claude nghiên cứu MapTap, gặp khó thì hỏi Claude, chụp màn hình Vercel/domain rồi hỏi Claude xem cấu hình có đúng không. Anh khuyên build web trước vì gần như không ma sát.

---

## 8. Bài học & trích dẫn

> **"Geosports is only a success because of word of mouth. That is true still to this day."**

> **"We reached over 1 million unique players in less than one month without a fancy email campaign."**

> **"This still feels like a cheat code that people are willing to do this, but it's also an amazing networking tool."**

> **"The games exploded in 2026. But again, that's 6 years later. This did not happen overnight."**

**Bài học rút ra:**
- **Làm cho sản phẩm tự phát tán**: kết quả đẹp, chia sẻ được, không cần dạy cách chơi, không cần cài đặt.
- **Web trước, app sau**: "Don't be afraid to build for web first" — liên kết mở được trong X giúp người chơi thấy, chơi và chia sẻ tại chỗ.
- **Tận dụng người có audience bằng cách đưa cho họ vai trò** (host viết câu hỏi) thay vì xin quảng bá: họ có lý do để đăng.
- **Bắt đầu sớm trong 8 giờ liền** và dùng LLM để vượt qua điểm kẹt; chụp màn hình để hỏi.
- Founder chỉ ra mốc thời gian thật: 2007 làm video YouTube, 2020 mới nổi, 2026 game bùng nổ.

**Cần tỉnh táo:**
- Survivorship bias và "chưa kiểm chứng": $40K là run-rate sau 3 tháng, với ads chưa đủ 30 ngày. Game trivia/daily thường bay nhanh khi trend nguội (nhận định của người viết); video không có dữ liệu retention dài hạn.
- Tiêu đề "built in 8 hours" bỏ qua 6 năm làm creator và game, 4 triệu follower, việc xử lý tải lúc viral, và công việc sau đó (spin-off, host).
- Đây không phải case "người không có audience làm được". Chính founder nói "it's always smart to build an audience"; host cũng thừa nhận người có sẵn tư duy creator là nhóm thành công nhất ở làn sóng sản phẩm AI này.
- Nguồn tiền thật là quảng cáo; MRR SaaS thì chưa thể tách ra.

---

## 9. Áp dụng cho tôi (indie hacker ở VN, bán global)

**Sao chép được gì:**
- **Công thức "bản remix của một game/format đã chạy" + ngách có audience riêng**: MapTap (địa lý) + trivia thể thao. Cơ chế dùng lại được cho bất kỳ ngách có cộng đồng đam mê rõ.
- **Thiết kế vòng chia sẻ ngay từ đầu**: kết quả ngắn, dễ so sánh (điểm, màu), mỗi ngày một vòng mới, chơi trong trình duyệt không đăng ký.
- **Chương trình "host/guest curator"**: mời người có audience viết nội dung cho vòng ngày, họ đăng lại vì là nội dung của chính họ — thay cho xin quảng bá.
- **Stack mỏng để thử nhanh**: web (Vercel), Google Sheets làm CMS câu hỏi, Redis cho leaderboard, Stripe cho gói pro; AI viết code theo spec.

**Rào cản thật:**
- **Phân phối:** cú khởi động của Frank nhờ audience 4 triệu follower; không có điểm khởi đầu tương tự, bạn cần kế hoạch seed khác (nhóm cộng đồng, creator nhỏ làm host từ ngày đầu) và video không chứng minh cách đó đủ.
- **Cạnh tranh và rủi ro nhái:** game đơn giản dễ bị clone; chính GeoSports là bản remix của MapTap. Lợi thế bền vững là audience/host/thương hiệu, không phải mã.
- **Kỹ năng và tải:** viral cần hạ tầng chịu tải (Redis, hosting) và xử lý retention ngay lúc bùng nổ, dù Claude giảm phần code.
- **Kiếm tiền bằng ads:** cần đủ traffic mới tạo ra doanh thu đáng kể ($1.200/ngày ở ~700K MAU) và còn phải qua duyệt mạng quảng cáo; video không nói điều kiện hay CPM. Chi tiết chi trả cho người ở ngoài Mỹ và thuế cần tự kiểm tra.
- **Bối cảnh founder ở VN:** nội dung câu hỏi (thể thao Mỹ) cần hiểu văn hoá khán giả mục tiêu và viết tiếng Anh đúng giọng; kết nối với host trên X phụ thuộc DM tiếng Anh. Múi giờ ít quan trọng vì game tự động, nhưng thời điểm đăng bài viral thì có.

**Biến thể đáng thử ở thị trường trả cao:**
- **Daily game cho một cộng đồng đam mê nhỏ nhưng có độc giả Mỹ/Anh/Úc** (golf, F1, NFL fantasy, ẩm thực, bất động sản...), cùng khung "5 câu mỗi ngày + điểm chia sẻ được" và host là người nổi tiếng trong cộng đồng đó. Cửa: ngách có CPM quảng cáo cao và người chơi có thói quen chia sẻ kết quả. Thu từ ads cộng gói pro vài đô/tháng (ước lượng của người viết).
- **Phiên bản có thương hiệu cho newsletter/media**: bán một daily game tuỳ biến cho ấn phẩm hoặc podcast, thu phí cài đặt cộng phí hàng tháng. Ý tưởng của người viết, video không có dữ liệu.
- **Kênh B2C song song**: pro sub không quảng cáo/streak/thống kê cho người chơi thường xuyên, để giảm phụ thuộc vào ads.

**Khi nào KHÔNG nên làm:**
- Bạn không có audience, không có người host để mời, và không sẵn sàng đầu tư nhiều tuần để seed cộng đồng.
- Bạn cần doanh thu ổn định dự báo được: ads trên game daily biến động theo trend.
- Bạn không có nền hiểu ngách (thể thao, thể loại game) để viết nội dung đủ chất lượng mỗi ngày.
- Bạn kỳ vọng "8 giờ làm xong" nghĩa là hết việc: game này cần giữ chân người chơi và nội dung mới mỗi ngày.

---

## Nguồn

- Video: [I built this website in 8 hours with Claude. Now it makes $40K/month](https://www.youtube.com/watch?v=s9aLA4IOSZE) — Starter Story, 27/09/2026, 16:11, 136K views
- Transcript: [`transcript.md`](transcript.md)
