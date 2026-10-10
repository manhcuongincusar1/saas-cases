---
id: 1nfPvJKrYYQ
slug: natural-write-tiktok-copy-playbook
product: Natural Write
founder: Nikita Logvinenko + Evgeniy Mikholap (+ Alexander lo phần kỹ thuật)
tagline: Chọn KÊNH PHÂN PHỐI trước rồi mới chọn sản phẩm — thấy TikTok đầy video về AI humanizer nên build một cái trong 2 tuần, rồi copy 1-1 chính những video viral đó
revenue_usd_month: 27000
revenue_basis: video nêu 3 tháng liên tiếp — $41K, $32K, $27K, cộng lại $100K. Tôi lấy $27K vì đó là tháng gần nhất VÀ đường doanh thu đang GIẢM đều; con số $100K trong tiêu đề là tích luỹ 90 ngày, không phải run rate. Không có ảnh dashboard nào xác nhận, chỉ có lời founder nói
model: micro-saas-subscription
category: ai-writing-tools (AI humanizer, bypass AI detector)
audience: B2C — chủ yếu học sinh sinh viên nộp bài ở trường và đại học, thêm marketer và doanh nghiệp
started: khoảng tháng 6/2025 — sản phẩm build xong trong 2 tuần
time_to_first_sale: ngay từ video TikTok ĐẦU TIÊN
time_to_scale: $41K ngay trong tháng đầu
team_size: 3
funding: bootstrapped
main_channel: TikTok organic tự quay mặt — copy 1-1 video viral đã có sẵn trong ngách
tech_stack: [Next.js, PostgreSQL, Coolify, NextAuth, Resend]
key_metrics:
  tiktok_views: 9 triệu view (tổng mọi tài khoản)
  website_visits: 300.000
  signups: 250.000
  visit_to_signup: 80%
  revenue_90_days: 100.000 USD
  monthly_curve: 41K rồi 32K rồi 27K — giảm dần
  infra_cost: khoảng 65 USD/tháng (server 35 + Resend 20 + VPN 5 + số điện thoại 5)
replicability_vn: 4
difficulty: 2
video_url: https://www.youtube.com/watch?v=1nfPvJKrYYQ
published: 2025-09-06
views: 152250
---

# Natural Write — $100K trong 90 ngày từ một tài khoản TikTok

> **Tóm tắt 30 giây:** Hai người bạn ở Serbia và Ba Lan không tìm ý tưởng rồi mới tìm cách bán. Họ làm ngược lại: lướt TikTok, thấy **rất nhiều video về AI humanizer đang viral**, coi đó là bằng chứng có cầu và có kênh rẻ, rồi mới build sản phẩm **trong 2 tuần**. Video TikTok đầu tiên đã ra đơn đầu tiên. 90 ngày sau: **9 triệu view, 250.000 signup, $100K doanh thu**, chi phí vận hành khoảng **$65/tháng**. Nhưng con số họ tự đọc ra lại kể một câu chuyện khác với tiêu đề: **$41K → $32K → $27K**. Đây là case dạy rất nhiều về TikTok organic, và cũng là case cảnh báo rất rõ về tuổi thọ của kênh đó.

![$100.000 trong 90 ngày](screenshots/01_00m52s_usd-100-000.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu 90 ngày | $100K |
| Tháng 1 / tháng 2 / tháng 3 | **$41K / $32K / $27K** (giảm dần) |
| Tổng view TikTok | ~9 triệu |
| Lượt truy cập website | ~300.000 |
| Signup | ~250.000 |
| Tỉ lệ visit → signup | **80%** |
| Thời gian build sản phẩm | 2 tuần |
| Chi phí hạ tầng | ~$65/tháng |
| Quy mô đội | 3 người |

**Ba chú thích về số liệu, đọc trước khi tin:**

1. Phần intro của video nói *"got 250,000 downloads"*. Nhưng Natural Write là **web app**, và về sau chính founder nói rõ **250K là signup**, không phải download. Tiêu đề của kênh đang dùng từ sai.
2. Không có một ảnh chụp dashboard Stripe/analytics nào trong toàn bộ video. Tất cả số đều là lời nói.
3. Tỉ lệ **80% visit → signup** là con số cao bất thường tới mức chính Pat Walls phải kêu lên *"that is crazy"*. Xem mục 6 để hiểu vì sao nó có thể có thật — và vì sao nó vẫn không phải điều đáng ghen tị.

## 2. Ngược đời quan trọng nhất: chọn kênh TRƯỚC, chọn sản phẩm SAU ⭐⭐⭐

Đa số case trong kho này bắt đầu bằng "tôi có một vấn đề cá nhân". Nikita và Evgeniy bắt đầu bằng **"kênh nào đang rẻ"**.

> *"Trong lúc research, chúng tôi để ý là **có quá nhiều video về humanizer**, và tôi nghĩ okay, mình cũng làm được cái đó, **và nó dễ quảng bá trên TikTok vì đang là chủ đề nóng**. Chúng tôi quyết định — hai tuần làm sản phẩm, rồi bắt đầu quảng bá."*

Bước 1 trong playbook của họ nói toạc ra cơ chế:

> *"Step one, **do your niche research before you even start coding** because you need to find **proofs**. Proof rằng bạn có đối thủ trên TikTok, và proof rằng những đối thủ đó **đang có video viral** trên TikTok."*

**Cơ chế vì sao cách này hiệu quả:** đa số sản phẩm indie chết vì phân phối, không phải vì sản phẩm. Bằng cách yêu cầu **hai bằng chứng** (có đối thủ + đối thủ đang viral), họ loại bỏ rủi ro lớn nhất *trước khi* bỏ ra 2 tuần code. Có đối thủ nghĩa là có người trả tiền. Đối thủ đang viral nghĩa là **thuật toán TikTok hiện đang chịu phân phối chủ đề này miễn phí** — cửa sổ đang mở.

**Khi nào cơ chế này hết hiệu quả:** khi cửa sổ đóng. Mục 8 sẽ cho thấy nó đóng nhanh thế nào.

Đối chiếu với [GlowUp](../2025-12-17_my-mobile-app-made-800k-in-365-days/case.md) — founder đó còn cực đoan hơn: làm content viral **trước cả khi viết code**. Cùng một logic, khác mức độ.

![0 đến $100K trong 3 tháng](screenshots/03_02m58s_ch-0-to-100k-in-3-months.jpg)

## 3. Thuê influencer thất bại, tự quay mặt thì thắng ⭐⭐

Đây là chi tiết dễ bị lướt qua nhất nhưng đáng tiền nhất:

> *"Đầu tiên chúng tôi thử **thuê influencer và trả tiền cho họ làm video**. Nhưng đó là trải nghiệm thất bại vì họ **tạo ra một ít view và gần như không có conversion**. Sau đó chúng tôi quyết định tự tạo tài khoản TikTok của mình và **bắt đầu tự quay chính mình**."*

**Cơ chế:** influencer được trả tiền tối ưu cho **view**, vì view là thứ họ bán. Founder tối ưu cho **đơn hàng**. Khi bạn thuê người ngoài làm video ở giai đoạn chưa biết format nào chuyển đổi, bạn đang trả tiền để học một bài học mà **bạn không được giữ lại**: họ giữ kinh nghiệm, bạn giữ hoá đơn.

Lời khuyên cuối video của Nikita chính là điều này, nói thẳng ra:

> *"Bạn cần **tự mình bắt đầu hành trình TikTok**. Tự tìm ra cái gì hiệu quả, **rồi mới** nghĩ đến chuyện giao việc hay thuê người."*

**Mâu thuẫn trong kho:** [Pep AI](../2026-05-24_i-built-a-30k-month-in-35-days/case.md) đi thẳng vào influencer trong ngách và một story post ra $1.000. [CalBuddy](../2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) rev-share với influencer lớn. Vậy ai đúng?

**Điều kiện phân định:** influencer hiệu quả khi bạn đã **biết trước format nào chốt đơn** và chỉ cần nhân bản (Pep AI có ngách peptide với KOL chuyên biệt, khán giả đã sẵn ý định mua). Influencer thất bại khi bạn **chưa biết format nào chốt** — lúc đó bạn không mua phân phối, bạn đang mua sự bối rối có trả phí. Natural Write ở giai đoạn thứ hai.

## 4. Playbook TikTok 7 bước — bản đầy đủ ⭐⭐⭐

Bản rút gọn founder tự tóm tắt: *"set up tài khoản đàng hoàng → tìm video viral trong ngách → copy lại → đăng 1 video/ngày → khi viral rồi mới thử ý tưởng riêng."*

Bản chi tiết:

### Bước 1 — Niche research trước khi code
TikTok Search và **Creator Search Insights** (công cụ có sẵn trong app TikTok) là hai thứ họ gọi là *"best friend"*. Tìm hai bằng chứng đã nói ở mục 2.

### Bước 2 — Tạo tài khoản đúng cách (phần hiếm khi ai nói ra) ⭐⭐⭐
Nguyên văn, đây là checklist mà rất ít video chịu công khai:

- Nếu bạn **không ở đúng thị trường mục tiêu**, bạn cần: **VPN**, **một chiếc iPhone**, **số điện thoại của thị trường mục tiêu**, **email mới**, **Apple ID mới**.
- *"It is very important your first TikTok account should be registered on your phone number."* — tài khoản đầu tiên **phải** đăng ký bằng số điện thoại, không phải bằng email hay social login.

**Vì sao quan trọng với người Việt:** đây chính là rào cản kỹ thuật số 1 khi bạn ở VN mà muốn bán cho Mỹ. TikTok phân phối video theo tín hiệu địa lý của tài khoản. Nếu bạn đăng từ tài khoản Việt Nam, video của bạn sẽ được đẩy tới người Việt — và người Việt không phải khách hàng của bạn. Chi phí giải quyết: **$5/tháng VPN cho 5 thiết bị + $5/tháng cho một số điện thoại US** (họ nói rõ con số này ở phần tech stack).

### Bước 3 — Warm up
**30-50 phút mỗi ngày trong 3-5 ngày**: like video, để lại comment, follow creator, dùng search để tìm video trong ngách.

**Cơ chế:** bạn đang dạy thuật toán tài khoản này thuộc về ngách nào **trước khi** nó phải đoán từ video đầu tiên của bạn. Nếu bỏ bước này, video đầu tiên bị đẩy tới nhóm người xem ngẫu nhiên, tương tác thấp, và tài khoản bị đóng khung sai ngay từ đầu.

### Bước 4 — Recreate what works
Làm **bản sao 1-1 chất lượng cao** của video viral trong ngách. Một chi tiết kỹ thuật họ nhấn mạnh: *"It is very important to add captions **in TikTok editor**"* — dùng chính trình sửa của TikTok để gắn phụ đề, không phải công cụ ngoài.

### Bước 5 — Đăng
**Một video/ngày**, vào **nửa sau của ngày** theo giờ của thị trường mục tiêu.

### Bước 6 — Innovate
Chỉ khi video đã bắt đầu viral và bạn đã hiểu cơ chế, mới bắt đầu thử format riêng.

### Bước 7 — Scale
Tạo thêm nhiều tài khoản và thuê creator. (Lưu ý: "9 triệu view **from all our accounts**" — họ đã nhân bản tài khoản. Cùng mô hình trang trại tài khoản như [GlowUp](../2025-12-17_my-mobile-app-made-800k-in-365-days/case.md) ở đỉnh điểm chạy 7 tài khoản.)

![Mổ xẻ chiến lược TikTok](screenshots/05_04m30s_ch-tiktok-strategy-deep-dive.jpg)

## 5. Hai video viral được mổ xẻ — và con số gây sốc ⭐⭐⭐

**Video 1:** *"you have an essay to submit in 5 minutes"* — dùng cảnh từ một phim hài Mỹ với Jim Carrey. Cấu trúc: **cho thấy vấn đề ở mức căng thẳng cao nhất** (bạn còn 1 phút để nộp bài) rồi đưa giải pháp theo cách hài hước.

- Làm mất **vài giờ**.
- Đạt **4 triệu view**.
- *"Format này đã được creator khác chứng minh rồi. Chúng tôi chỉ copy lại và nó hiệu quả rất tốt."*

**Video 2:** demo trước-sau trần trụi — text 100% AI-generated → bấm → text 100% human-written.

> *"Once it gets viral, we start getting a lot of sales **immediately**."*

**Và đây là con số đắt nhất cả video:**

> *"Funny stuff here. **Video gốc có khoảng 150K view, nhưng bản copy của Evgeniy được 1,5 triệu view.**"*

**Bản sao ăn gấp 10 lần bản gốc.**

**Cơ chế vì sao điều này có thể xảy ra — và vì sao nó thay đổi cách bạn nghĩ về "sáng tạo nội dung":** TikTok phân phối theo **nội dung của từng video**, gần như không theo uy tín tài khoản. Một video là một lần thử độc lập. Khi bạn copy một format đã viral, bạn đã loại bỏ rủi ro *"format này có ăn không"* và chỉ còn lại rủi ro *"lần thả này có gặp đúng nhóm khán giả không"*. Bạn cũng có lợi thế mà bản gốc không có: bạn **biết trước** nó ăn, nên bạn quay kỹ hơn, cắt gọn hơn, phụ đề rõ hơn.

Lời khuyên cuối của Evgeniy đúc lại đúng điểm này:

> *"**Don't over complicate it.** Bỏ qua chuyện phát minh format TikTok của riêng bạn và **chỉ cần nhân bản cái đang viral sẵn**."*

Đây là cùng một triết lý với [CalBuddy](../2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) (copy nguyên app đã thành công về thị trường nội địa) — chỉ khác là Natural Write copy ở tầng **content**, CalBuddy copy ở tầng **sản phẩm**.

![Ví dụ TikTok viral](screenshots/07_07m47s_ch-viral-tiktok-examples.jpg)

## 6. Phễu thật: 9 triệu view → $100K

| Tầng | Con số | Tỉ lệ chuyển tiếp |
|---|---|---|
| View TikTok | 9.000.000 | — |
| Truy cập website | 300.000 | **3,3%** |
| Signup | 250.000 | **80%** |
| Doanh thu | $100.000 | — |

**Hai điều cần rút ra, và điều thứ hai quan trọng hơn:**

**(a) Vì sao 80% visit → signup là con số có thể có thật.** Với công cụ dạng humanizer, người dùng đến từ một video đã cho họ thấy **chính xác** thao tác họ sẽ làm (dán text → bấm nút → nhận kết quả). Họ không đến để "tìm hiểu", họ đến để dùng ngay. Signup gần như chắc chắn là miễn phí và đứng chắn trước kết quả. Trong tình huống đó, 80% không phải phép màu marketing — đó là **thiết kế phễu**: bạn đặt cổng đăng ký đúng vào khoảnh khắc người dùng đã muốn thứ ở phía sau.

**(b) Nhưng hãy làm phép chia mà video không làm:** $100.000 chia cho 250.000 signup = **$0,40 doanh thu trên mỗi người đăng ký**. Và $100.000 chia cho 9 triệu view = **khoảng $0,011 trên mỗi view**.

Đây là con số bạn phải nhớ nếu định copy mô hình này: **TikTok organic tạo ra rất nhiều lưu lượng chất lượng cực thấp về mặt tiền**. Nó chỉ ra tiền khi (1) sản phẩm gần như không tốn chi phí biến đổi, và (2) bạn có thể tạo view ở quy mô hàng triệu mà không trả tiền. Bỏ một trong hai điều kiện, mô hình sụp.

## 7. Tech stack và chi phí — $65/tháng cho một business $100K

| Hạng mục | Công cụ / chi phí |
|---|---|
| Framework | Next.js |
| Database | PostgreSQL |
| Deploy / hosting | **Coolify** (self-host PaaS) |
| Auth | NextAuth *(ASR đọc là "Next AL" — tôi suy ra NextAuth vì đó là lựa chọn chuẩn của stack Next.js; hãy coi đây là suy đoán)* |
| Email | Resend — $20/tháng |
| Server | $35/tháng |
| VPN | $5/tháng cho 5 thiết bị |
| Số điện thoại US | $5/tháng mỗi số |

> *"Ngoài chi phí thời gian của chúng tôi, chi phí để vận hành business này là **rất thấp**."*

**Điểm đáng học:** họ dùng **Coolify** để self-host thay vì Vercel. Với một sản phẩm gọi LLM ở phía sau và có 250K người dùng miễn phí, hoá đơn serverless sẽ giết bạn — self-host trên một VPS $35 là lựa chọn có tính toán, không phải tiết kiệm vặt.

Lưu ý: **$35/tháng không bao gồm chi phí API của mô hình AI**. Video không nhắc tới chi phí inference dù đây là một AI humanizer. Đây là một lỗ hổng đáng ngờ trong bản kê khai chi phí — hoặc họ tự host mô hình nhỏ trên chính server đó, hoặc con số này chưa đầy đủ.

![Chi phí server $35](screenshots/09_09m55s_usd-35.jpg)

## 8. Điều video KHÔNG nói: đường doanh thu đang đi xuống ⭐⭐⭐

Đây là phần quan trọng nhất của case này, và nó nằm ngay trong câu nói của chính founder ở giây thứ 15:

> *"First months $41K, second months $32K, and third months $27K."*

Vẽ ra: **-22% rồi -16%**. Ba tháng liên tiếp giảm.

Tiêu đề video là *"Our simple app made $100K in 90 days"* — kỹ thuật thì đúng. Nhưng nếu tháng 4 tiếp tục xu hướng này, doanh thu sẽ về khoảng $22-23K. Kênh không hỏi câu này. Không ai trong video nhắc tới nó.

**Cơ chế vì sao TikTok organic có hình dạng đường cong này:**

1. **Bão hoà format.** Bạn copy format viral. Sau vài tuần, format đó đã đến với gần hết nhóm khán giả quan tâm. Cùng một video giờ chạm tới người đã xem 5 lần rồi.
2. **Người sau bắt chước bạn.** Chính chiến lược của bạn (copy cái đang viral) được người khác dùng để copy **bạn**. Ngách humanizer là ngách zero-moat — hàng trăm bản sao xuất hiện trong vài tuần.
3. **Cạn nguồn cầu dồn nén.** Nhóm người "đang cần humanizer ngay bây giờ" là hữu hạn. Đợt đầu bạn thu hoạch phần dễ nhất.
4. **Tính mùa vụ.** Khách hàng chính là sinh viên. $41K rơi vào khoảng tháng 6/2025 — cuối kỳ. $27K rơi vào tháng 8 — nghỉ hè. Đây có thể là lời giải thích lành tính nhất, và cũng là lời cảnh báo: **doanh thu của bạn có nhịp học kỳ**.

**Cảnh báo thiên kiến nguồn:** Starter Story (nay thuộc HubSpot) bán khoá học Starter Story Build. Video này có **ba lần chèn quảng cáo** cho chính khoá học đó cộng một quảng cáo trả tiền cho Vanta ở phút 6:26. Cấu trúc kể chuyện được chọn để làm nổi bật con số tích luỹ $100K và làm mờ đường cong giảm. Đây không phải nói dối — nhưng nó là **lựa chọn khung hình**, và bạn phải tự nhìn ra khung hình còn lại.

Thêm một điểm nữa mà video hoàn toàn né: **sản phẩm này phục vụ gian lận học thuật**. Nguyên văn: *"text này thường **bypass hầu hết AI detector** và chủ yếu phổ biến ở **trường học và đại học** cho **sinh viên**."* Đó là mô hình kinh doanh có rủi ro nền tảng đặc thù — App Store/Google Play có chính sách về academic dishonesty, các cổng thanh toán có thể từ chối, và các trường đang tăng cường phát hiện. Bạn cần quyết định trước khi bắt đầu, không phải sau.

## 9. Mâu thuẫn với các founder khác trong kho ⭐⭐

| Quan điểm | Ai nói | Đúng khi nào |
|---|---|---|
| Tự quay TikTok organic, copy format viral, $0 quảng cáo | Nikita + Evgeniy (case này) | Ngách đã có content viral sẵn để copy; sản phẩm có demo trực quan trong 5 giây; chi phí biến đổi gần 0 |
| Organic trước để tìm format, **rồi** đổ tiền ads nhân lên | [PuffCount](../2025-09-20_the-1m-mobile-app-playbook/case.md), [Go Tall](../2026-07-19_this-stupidly-simple-app-makes-100k-month/case.md) | Bạn có vốn và LTV đủ cao để chịu CAC; muốn doanh thu bền chứ không phải đợt sóng |
| **Cố tình KHÔNG** dùng UGC/organic, chỉ chạy paid ads | [Glowly + Overflow](../2026-08-12_the-lazy-method-how-i-build-10k-month-apps/case.md) | Bạn muốn hệ thống chạy vài giờ/tuần và chấp nhận trần thấp hơn để đổi lấy tính dự đoán được |
| Personal brand khổng lồ rồi mới ra app | [Stella](../2026-07-12_she-built-this-340k-month-app-in-60-days/case.md) | Bạn đã có 2,8 triệu follower sẵn — không áp dụng được cho người mới |

**Hoà giải:** Natural Write chứng minh TikTok organic có thể ra $41K trong tháng đầu **mà không cần đồng nào**. Nhưng nó cũng chứng minh — bằng chính đường cong của mình — rằng organic một mình **không giữ được mức đó**. Ba case còn lại đều đã đi tiếp bước mà Natural Write chưa đi: chuyển sóng organic thành hệ thống paid có thể lặp lại.

**Kết luận thực dụng:** dùng playbook của Natural Write để **tìm ra format nào chốt đơn với $0**. Rồi khi có format, làm điều PuffCount làm — đổ ads vào chính format đó. Đừng dừng ở bước một và tưởng mình đã có business.

## 10. Áp dụng cho tôi (indie hacker VN)

**Sao chép được ngay:**

- **Đảo ngược thứ tự tìm ý tưởng.** Đừng hỏi "tôi nên build gì". Hỏi: *"trên TikTok/YouTube Shorts, chủ đề công cụ nào đang có nhiều video viral mà tôi build được trong 2 tuần?"* Mở TikTok Search + Creator Search Insights, tìm **hai bằng chứng**: có đối thủ, và đối thủ đang viral.
- **Checklist tài khoản là thứ đáng tiền nhất trong video này** cho người ở VN. VPN ($5/tháng/5 thiết bị) + iPhone + số điện thoại thị trường mục tiêu ($5/tháng) + email mới + Apple ID mới. Đăng ký tài khoản đầu bằng **số điện thoại**. Warm up 30-50 phút/ngày trong 3-5 ngày trước khi đăng video đầu tiên. Tổng chi phí thử nghiệm: **dưới 300 nghìn đồng/tháng**.
- **Copy 1-1 rồi mới sáng tạo.** Bạn không cần ý tưởng content. Bạn cần khả năng tái tạo một format đã ăn, có phụ đề, mỗi ngày một cái. Đây là công việc kỷ luật chứ không phải công việc sáng tạo — hợp với người không tự tin về tiếng Anh vì nhiều format viral gần như không cần thoại.
- **Stack self-host.** Next.js + PostgreSQL + Coolify trên VPS ~$35 là mô hình chi phí đúng khi bạn sắp có hàng trăm nghìn người dùng miễn phí.

**Rào cản thật, không tô hồng:**

- **Bạn không ở thị trường mục tiêu, và đó là chi phí thật.** VPN có thể bị TikTok phát hiện. Số điện thoại ảo thường bị từ chối. iPhone thật là bắt buộc theo lời họ. Nếu tài khoản bị đóng khung sai địa lý ở tuần đầu, bạn phải bỏ và làm lại từ đầu — mất 1 tuần warm up mỗi lần.
- **Đây là mô hình đợt sóng, không phải mô hình tài sản.** Đường $41K → $32K → $27K là dữ liệu, không phải suy đoán. Hãy lập kế hoạch tài chính theo giả định doanh thu tháng 6 chỉ còn 40-50% tháng 1. Nếu bạn cần thu nhập ổn định để bỏ việc, mô hình này **không** cho bạn điều đó.
- **Ngách zero-moat.** Sản phẩm là một wrapper 2 tuần. Bất kỳ ai xem video này cũng build được. Rào cản duy nhất của họ là tốc độ thực thi TikTok — và rào cản đó hết hạn.
- **Rủi ro thanh toán và đạo đức.** Sản phẩm bán cho sinh viên để qua mặt hệ thống phát hiện AI của trường. Stripe/Paddle có thể xem đây là ngành rủi ro. Ngoài ra bạn phải tự trả lời câu hỏi liệu bạn có muốn xây business này không — video không hỏi bạn câu đó.
- **Chi phí AI inference là ẩn số.** Bản kê $65/tháng của họ không có dòng nào cho model API. Với 250K người dùng, nếu bạn gọi GPT/Claude cho mỗi request, hoá đơn thật có thể lớn hơn doanh thu. Hãy tính chi phí biến đổi mỗi request **trước khi** mở cửa miễn phí.
- **Không có ảnh dashboard nào.** Toàn bộ số liệu là lời kể. Với một video có ba lần bán khoá học, đây là điều đáng ghi nhớ.

**Khi nào KHÔNG dùng mô hình này:**

- Khi sản phẩm của bạn **không demo được trong 5 giây**. TikTok thưởng cho thứ có thể cho xem trước-sau. Một công cụ B2B với chu kỳ bán 3 tuần không có gì để quay.
- Khi bạn cần **doanh thu dự đoán được**. Mô hình này cho bạn một đợt sóng, không cho bạn một đường thẳng.
- Khi **chi phí biến đổi mỗi người dùng của bạn khác 0 đáng kể**. Với 250K signup, mỗi cent chi phí biến đổi là $2.500. Phễu này chỉ hoạt động ở gần-zero.
- Khi bạn muốn xây một thứ để **bán lại**. Người mua định giá theo tính bền của doanh thu. Một đường cong giảm 22% mỗi tháng gần như không bán được.

## Nguồn

- Video: <https://www.youtube.com/watch?v=1nfPvJKrYYQ> (11:31, đăng 06/09/2025, 152.250 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
- Lưu ý ASR: transcript tự động đọc "Natural Write" thành "natural right", "Evgeniy" thành "Yavghini"/"Yini"/"Yuini", "Postgres" thành "Postgress". Tên đúng lấy từ `description` trong meta.json và tài khoản X của hai founder.
