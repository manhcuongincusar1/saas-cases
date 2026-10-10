---
id: OV09yPLf8BI
slug: symmetry
product: Symmetry (symmetry.club)
founder: Mauro Botanes (22 tuổi) + co-founder David López (tên hiện trên dashboard PostHog) + các co-founder khác, đều từng là YouTuber fitness
tagline: App ghi chép buổi tập, bê nguyên ngách bão hoà ở Mỹ sang thị trường nói tiếng Tây Ban Nha — chạy bằng UGC công nghiệp và một cỗ máy A/B test
revenue_usd_month: 160000
revenue_basis: "Revenue 28 ngày gần nhất = $160.324 trên dashboard RevenueCat (gross, trước phí store và trước khi chia ~50% cho creator). CÙNG dashboard đó ghi MRR = $101.757 — con số headline $160K KHÔNG phải MRR"
mrr_usd: 101757
model: mobile-app-subscription
category: fitness / gym tracking — thị trường nói tiếng Tây Ban Nha (Tây Ban Nha + Mexico)
audience: B2C — người tập gym ở Tây Ban Nha và Mexico, cả người mới lẫn người tập lâu năm
started: công ty lập ~2024 ("started the company 2 years ago"); app launch 06/06/2025
time_to_first_sale: không nêu
time_to_scale: ~12 tháng từ launch tới $160K/tháng; cú hích lớn nhất rơi vào tháng 1 (mùa vụ gym đầu năm)
team_size: nhỏ — Mauro + các co-founder (dùng "we/chúng tôi", không nêu con số); cộng mạng lưới creator thuê ngoài
funding: không nêu (không nhắc tới gọi vốn)
main_channel: UGC công nghiệp — 566 tài khoản, 79.000 video, 762 triệu view (số trên dashboard nội bộ); trả creator gần 50% doanh thu
tech_stack: [Claude + MCP, PostHog, Superwall, RevenueCat, WhisperFlow, Notion, Slack]
key_metrics:
  downloads_total: 3000000
  mrr_usd: 101757
  revenue_28d_usd: 160324
  active_subscriptions: 32531
  active_trials: 169
  active_customers_28d: 1073268
  new_customers_28d: 499442
  ugc_accounts: 566
  ugc_videos: 79000
  ugc_views_dashboard: 762000000
  ugc_likes: 40000000
  ugc_comments: 447000
  ugc_engagement_pct: 5.51
  ugc_outliers: 667
  ugc_outlier_rate_pct: 0.8
  best_video_views: 17000000
  creator_rev_share_pct: 50
  experiment_min_runtime_days: 14
replicability_vn: 3
difficulty: 4
video_url: https://www.youtube.com/watch?v=OV09yPLf8BI
published: 2026-09-09
views: 59998
tags: [mobile-app, health, ugc, ugc-system, localization, ab-testing, data-driven, superwall, creator-revenue-share, okr, activation, saturated-market]
---

# Symmetry — $160K/tháng trong 1 năm: bê ngách bão hoà sang thị trường tiếng Tây Ban Nha, rồi A/B test mọi thứ

> **Tóm tắt 30 giây:** Mauro, 22 tuổi, cùng vài người bạn từng làm YouTuber fitness, build Symmetry — app ghi chép buổi tập (gym tracking), một ngách **bão hoà nhất App Store**. Điểm khác biệt không phải sản phẩm: (1) họ không đánh thị trường Mỹ mà đánh **thị trường nói tiếng Tây Ban Nha** (Tây Ban Nha + Mexico); (2) phân phối bằng **UGC công nghiệp** — 566 tài khoản, 79.000 video, trả creator **gần một nửa doanh thu**; (3) quyết định build cái gì bằng **thí nghiệm có kiểm soát**, không bằng cảm tính hay feedback form. Kết quả: 3 triệu lượt tải, **MRR $101.757** và **$160.324 doanh thu 28 ngày**, sau đúng 1 năm kể từ ngày launch (06/06/2025).
>
> **Giá trị lớn nhất của video này không nằm ở con số mà ở quy trình quyết định sản phẩm** — phần 4 và 5 bên dưới.
>
> 🔍 **Bốn điều chỉ thấy được khi đọc ảnh chụp màn hình, không có trong lời kể** — các ô ⚠️ ở phần 1, phần 5 (hai ô) và phần 8.

---

## 1. Con số

Founder show thẳng dashboard **RevenueCat** trên sóng. Đây là toàn bộ số đọc được từ ảnh:

![](screenshots/01_01m58s_dashboard-revenuecat-mrr-usd-101-757.jpg)

| Chỉ số (đọc từ dashboard) | Giá trị |
|---|---|
| **MRR** | **$101.757** |
| **Revenue — 28 ngày gần nhất** | **$160.324** |
| Active Subscriptions | **32.531** |
| Active Trials | **169** |
| Active Customers (28 ngày) | **1.073.268** |
| New Customers (28 ngày) | **499.442** |
| Tổng lượt tải (iOS + Android, lời founder) | **~3.000.000** |
| Thời gian từ launch tới đây | **~12 tháng** (launch 06/06/2025) |
| Tỷ lệ chia cho creator | **gần 50% doanh thu** |
| Thời gian tối thiểu một A/B test | **2 tuần** |

> ⚠️ **Phát hiện 1 — "$160K/tháng" KHÔNG phải MRR.** Tiêu đề video và cả cuộc phỏng vấn dùng con số **$160.324**, nhưng ngay cạnh nó trên cùng dashboard là **MRR $101.757**. Chênh lệch $58.567 là phần thu một lần / trả trước theo năm dồn vào cửa sổ 28 ngày đó. **Doanh thu định kỳ thật là ~$102K/tháng.** Không ai nói dối ở đây — chỉ là con số dễ đọc nhầm, và nó nằm ngay trên màn hình.

**Bốn con số suy ra (tôi tự tính từ dashboard, không phải lời founder):**

- $101.757 MRR / 32.531 subscription ≈ **$3,13/tháng cho mỗi người đang trả phí**. Đây là mức giá rất thấp — hợp lý với thị trường Tây Ban Nha + Mexico, và là chìa khoá để hiểu vì sao cả mô hình phải chạy bằng **số lượng cực lớn**.
- 32.531 subscription / 1.073.268 active customer ≈ **3,0% tỷ lệ chuyển sang trả phí**. Tức **97% người dùng không trả đồng nào** — freemium thuần.
- 499.442 khách mới / 28 ngày ≈ **~17.800 người mới mỗi ngày**. Cỗ máy UGC phải nuôi đúng con số này mỗi ngày mới giữ được nhịp.
- Nếu $160K là gross: Apple/Google lấy 15-30%, rồi **gần 50% nữa chia cho creator**. Founder không nói 50% đó tính trên gross hay net, nên **không suy ra được lợi nhuận** từ video này. Đừng đọc $160K như tiền bỏ túi.

---

## 2. Sản phẩm giải quyết vấn đề gì

Symmetry là **app ghi chép buổi tập**: lên kế hoạch tập, xem trước buổi tập, bấm bắt đầu, ghi mức tạ và số rep cho từng bài, kèm video hướng dẫn động tác.

![](screenshots/10_13m44s_app-workout-plan-upper-body.jpg)

Hai tính năng người dùng thích nhất lại **không phải phần ghi chép**:

- **Rank** — mỗi nhóm cơ và mỗi bài tập có một thứ hạng riêng, hiển thị trên **sơ đồ cơ thể tô màu theo nhóm cơ**, và hạng được đặt tên theo kiểu game: trên ảnh là **"DIAMOND I"**. Có level để lên.

![](screenshots/11_14m06s_app-ranks-diamond-i.jpg)

- **Mạng xã hội kiểu Strava** — feed bạn bè đăng buổi tập của họ (toàn bộ bằng tiếng Tây Ban Nha: *"Jueves de Piernas"* — thứ Năm tập chân), streak không được để đứt trước mặt bạn bè.

![](screenshots/12_14m16s_app-social-feed.jpg)

Nói cách khác: phần lõi là công cụ nhàm chán ai cũng làm được, phần giữ chân là **trò chơi + áp lực xã hội**.

**Ngách này bão hoà đến mức nào:** founder tự gọi là "one of the most saturated app markets". Điều đó không ngăn được anh — vì anh không cạnh tranh trên cùng sân.

---

## 3. Ý tưởng đến từ đâu

Đây là **scratch-your-own-itch đúng nghĩa, cộng với lợi thế phân phối có sẵn**:

- Mauro **từng béo phì**, gym là thứ thay đổi đời anh. Lý do build Symmetry là muốn chia sẻ sự thay đổi đó với người khác.
- Trước Symmetry, Mauro **và các co-founder đều là YouTuber fitness**. Suy nghĩ của nhóm: *"YouTube tốt, nhưng chúng tôi muốn giúp được nhiều người hơn. Làm sao đây?"* → gộp lại làm app.

**Điểm ăn tiền thật sự — chọn thị trường, không phải chọn ý tưởng:** có hàng trăm app gym tracking ở Mỹ. Nhóm này bê nguyên loại sản phẩm đã được chứng minh sang **thị trường nói tiếng Tây Ban Nha**, nơi cạnh tranh mỏng hơn hẳn, và trở thành "app fitness tăng trưởng nhanh nhất thị trường Tây Ban Nha".

> 📌 Đây là mẫu hình **localization arbitrage**: không phát minh danh mục mới, mà lấy danh mục đã chứng minh ở thị trường tiếng Anh rồi làm thật tốt ở một ngôn ngữ chưa ai làm tử tế. Lưu lại — phần 10 sẽ nói vì sao đây là điểm giống Việt Nam nhất trong cả case.
>
> **Case song sinh trong kho:** [CalBuddy](../2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) — app đếm calo **tiếng Hebrew**, cũng bê nguyên danh mục đã thắng ở Mỹ về thị trường ngôn ngữ nhỏ, cũng làm $80K/tháng. Hai case, hai ngôn ngữ, cùng một cơ chế. Khác nhau ở kênh: CalBuddy dùng **quảng cáo trả tiền** (tận dụng CPM nội địa rẻ), Symmetry dùng **UGC chia doanh thu**. Đọc cả hai để thấy cùng một arbitrage có ít nhất hai đường phân phối.

---

## 4. Cách validate ⭐ — ba giai đoạn build, và vì sao hai giai đoạn đầu đều sai

Đây là đoạn đắt nhất video. Mauro tự tổng kết hành trình quyết định-build-cái-gì thành ba giai đoạn:

| Giai đoạn | Cách làm | Kết quả (lời founder) |
|---|---|---|
| 1 | Build **cái chúng tôi muốn** | *"terrible idea"* |
| 2 | Build **cái user yêu cầu** — lấy thẳng từ feedback form | *"mediocre" (tầm thường)* |
| 3 | Build theo **cách khoa học và có phương pháp** | → $160K/tháng |

**Giai đoạn 2 mới là phần gây bất ngờ.** Hầu hết lời khuyên indie hacker dừng ở "hãy nghe user". Mauro nói nghe user một cách trực tiếp (form feedback → build cái họ xin) chỉ cho kết quả **tầm thường**. Lý do: *"people normally are incorrect about what is important to build and what is not important"* — người ta, kể cả user, đánh giá sai cái gì quan trọng.

### Nguyên lý ưu tiên: mỗi màn hình có "đòn bẩy" khác nhau

- Dark theme / light theme → chỉ ảnh hưởng ~**2% DAU**.
- **Paywall** → ảnh hưởng gần như toàn bộ người dùng, một cách triệt để. (Có hẳn phần mềm sinh ra chỉ để A/B test một màn hình này.)
- Trong Symmetry: **màn hình tìm bài tập** (exercise search) có tác động **rất lớn** tới activation và retention. Còn màn hình đầu tiên sau khi đăng nhập để xem buổi tập — *"we've done a lot of things there and doesn't seem to change anything"*.

> **Việc của bạn không phải build nhiều tính năng, mà là tìm ra vài màn hình có đòn bẩy cao rồi vắt kiệt chúng bằng A/B test.**

### Activation — định nghĩa đúng cho từng loại sản phẩm

Mauro nói rõ: *"nếu bạn đẩy được activation, retention sẽ theo sau."* Nhưng activation của mỗi sản phẩm khó dễ khác nhau một trời một vực:

| Sản phẩm | Activation là gì | Độ ma sát |
|---|---|---|
| App đếm calo | Chụp một tấm ảnh | Gần như bằng không |
| **Symmetry (gym tracking)** | **Phải thật sự đi tới phòng gym và ghi lại buổi tập** | Cực cao — phải đổi hành vi của người mới, hoặc đổi thói quen của người tập lâu năm |

Bài học rút ra: **trước khi chọn ngách, hãy nhìn xem activation của nó ma sát tới mức nào** — nó quyết định bạn sẽ phải làm bao nhiêu việc để giữ một người dùng.

### Chỉ số cần theo dõi (theo thứ tự ưu tiên của founder)

1. **Downloads** — đặc biệt khi app còn mới: *"the more downloads, the more revenue, it's proportional"*.
2. **Activation** — tuỳ sản phẩm, nhưng với Symmetry đây là chỉ số sống còn.
3. **Retention tuần 1 và retention 30 ngày** — đúng với hầu hết app.
4. **ARPU (doanh thu trung bình mỗi lượt tải)** — quyết định **bạn được phép trả creator bao nhiêu** cho mỗi lượt tải họ mang về. ARPU **chênh lệch rất lớn giữa các nước** nên phải theo dõi tách bạch theo từng thị trường.

> 📌 Điểm nối quan trọng giữa sản phẩm và marketing: ARPU không phải chỉ số báo cáo cho vui — nó là **trần chi phí mua một lượt tải**. Cả mô hình chia 50% doanh thu cho creator chỉ đứng được vì họ biết chính xác con số này theo từng thị trường.

---

## 5. Quy trình thí nghiệm — "EVELYN" ⭐

Tên hệ thống nội bộ: **EVELYN = Experiment Velocity Engine Lifting Your Numbers** — database Notion chứa toàn bộ A/B test, thí nghiệm chạy trên PostHog.

![](screenshots/07_11m46s_evelyn-experiment-database.jpg)

> ⚠️ **Phát hiện 2 — phụ đề tự động của YouTube nghe nhầm hai cái tên.** Trên màn hình là **"Lifting Your Numbers"** (phụ đề ghi "Listing"), và cái bảng OKR 90 ngày tên thật là **"War Map"** (phụ đề ghi "warm-up"). Nếu chỉ đọc transcript thì cả hai thuật ngữ đều sai.

**Cấu trúc database đọc được từ ảnh** — bốn cột, theo đúng thứ tự tư duy:

| Cột | Nội dung |
|---|---|
| **User Problem (DB)** | Vấn đề người dùng, liên kết sang một database riêng — nguồn gốc của mọi thí nghiệm |
| **Hypothesis** | Giả thuyết. Có dòng ghi thẳng *"(Inferred — no pre-launch hypothesis)"* hoặc *"No formal hypothesis was recorded"* — họ **thành thật ghi lại cả những lần làm ẩu**, thay vì chế giả thuyết ngược |
| **Experiment Name** | Tooltip ghi rõ quy tắc đặt tên: *"thay đổi sản phẩm cụ thể đang được test. Ngắn và cụ thể (vd: Autolog Sets, Commit with Signature). Không phải vấn đề, không phải giả thuyết."* |
| **Status** | Idea → Designing and Building → Running → Analyzing → Done |

**Sáu thí nghiệm thật nhìn thấy trong bảng** (đủ để hình dung họ test cái gì):
`Save empty workout as routine` · `Landing page social proof` · `ONB/RBD — Remove ranked body diagram from onboarding` · `Symmetry Intelligence — In-App AI Chatbot` · `Onboarding Android Paywall Provider (RevenueCat vs Legacy)` · `Workout Preview Goals/Value Section`

Hai shortcut họ gắn vào đầu database: `/evelyn-idea-creator` để thêm ý tưởng, `/post-mortem-creator` để phân tích kết quả — **quy trình được đóng gói thành lệnh, không phụ thuộc trí nhớ ai.**

### Luồng chuẩn: từ vấn đề, không phải từ giải pháp

> *"You're not coming from a solution place. You must come from a problem space."*

1. **Vấn đề là gì?** — nguồn: phỏng vấn người dùng (database của EVELYN bắt đầu từ đây).
2. **Làm sao biết vấn đề đó có thật?**
3. **Giả thuyết & giải pháp** — liệt kê nhiều phương án khác nhau cho cùng một vấn đề.
4. **Mỗi giả thuyết đẩy được chỉ số bao nhiêu?**
5. **Có guardrail metric nào cần canh không?** (chỉ số không được phép tụt khi đang đẩy chỉ số chính)
6. **A/B test mọi thứ** — bản control (app hiện tại) vs bản mới.
7. **Chạy tối thiểu 2 tuần** rồi mới phân tích.

### Hai lớp dữ liệu — cái gì và tại sao

| | Dữ liệu định lượng | Dữ liệu định tính |
|---|---|---|
| Nguồn | Event analytics, funnel | Nói chuyện với user, post trên Discord/Reddit |
| Trả lời | **Cái gì** đang xảy ra, mất người ở **chỗ nào** | **Tại sao** nó xảy ra |
| Thiếu nó thì | Không biết đang chảy máu ở đâu | Biết chỗ chảy máu nhưng đoán mò nguyên nhân |

**Lỗi phổ biến nhất Mauro thấy:** *"the most common error I see everybody is not tracking anything... they don't have any events at all in their app."* Hỏi "tỷ lệ rớt ở bước này là bao nhiêu?" → "ờ... tôi không biết."

**Quy tắc mật độ tracking:** càng sớm trong funnel, càng phải chi tiết. **Onboarding phải track từng màn hình một.**

### Hai kết quả thật được show trên màn hình — đọc số trực tiếp từ PostHog

**Thí nghiệm 1 — thất bại (và đó là kết quả có giá trị):**

![](screenshots/08_12m06s_experiment-inconclusive-172k-users.jpg)

| Biến thể | Người dùng | Conversion `start_training_session` | Delta | Chance to win | Significant |
|---|---|---|---|---|---|
| control | 56.456 | 51,68% | — | — | — |
| without_quick_workouts | 56.822 | 51,99% | +0,61% | 85,3% | **No** |
| with_quick_workouts | 58.770 | 51,72% | +0,09% | 56,0% | — |

**172.048 người dùng** đi qua thí nghiệm này. Hai thiết kế hoàn toàn khác nhau. Kết quả: **+0,61% và +0,09%, không có ý nghĩa thống kê.** Kết luận của Mauro: *"This is an inconclusive test. Let's focus on other areas of the app."*

**Thí nghiệm 2 — thắng, chỉ bằng một màn hình:**

![](screenshots/09_12m28s_experiment-commit-signature-won.jpg)

| | Giá trị |
|---|---|
| Tên thí nghiệm | **Commit with signature** — một màn hình ở cuối onboarding, người dùng "ký" cam kết sẽ đi tập |
| Phương pháp | Bayesian / 95% · Exposures **127K** (chia 49,8% / 50,0%) |
| Chỉ số chính | `start_training_session` (funnel) |
| control | **38,52%** (24,4K / 63,4K) — 63.438 người |
| with_commit_signature | **39,84%** (25,4K / 63,7K) — 63.702 người |
| Delta | **+3,44%** · Win probability **>99,9%** · Significant: **Yes** |
| Credible interval (95%) | **[2,02% – 4,85%]** |
| Kết luận | **Won** |

> ⚠️ **Phát hiện 3 — "+3% retention" thật ra là "+3,44% trên activation".** Chỉ số trên màn hình là `start_training_session` — tức **tỷ lệ người bắt đầu một buổi tập**, đúng định nghĩa *activation* mà chính Mauro nói ở phần trước, không phải retention. Anh nói nhanh nên gọi là "retention". Chi tiết này không làm case xấu đi — ngược lại, nó khớp chính xác với luận điểm của anh: **đẩy activation thì retention theo sau.**

> Đây là lập luận thuyết phục nhất cho việc A/B test: hai thiết kế công phu trên 172.000 người → 0. Một màn hình chữ ký cam kết trên 127.000 người → +3,44% với độ tin cậy >99,9%. **Không ai đoán trước được điều đó.** (Xem thêm tag `commitment-metric` trong kho — mẫu hình "bắt người dùng cam kết trong onboarding" xuất hiện ở nhiều case app khác.)

### OKR 90 ngày — bảng "War Map"

![](screenshots/06_08m06s_war-map-q2-2026-okr-dashboard.jpg)

- Chu kỳ **90 ngày**, mỗi chu kỳ là một bảng tên **"War Map"** (trên ảnh: *War Map Q2 2026*) — *"because we're going to war"*. Nó là một **dashboard PostHog**, không phải tài liệu Notion.
- Trong một War Map có: mục tiêu marketing, mục tiêu sản phẩm, và bảng chỉ số theo dõi **hằng tuần, nếu không muốn nói là hằng ngày**.
- **Chi tiết đắt giá trên ảnh:** biểu đồ chính tên *"First time open — Total vs Spanish vs English (last 60 days)"*. Họ tách **lần mở app đầu tiên theo ngôn ngữ**, và đường tiếng Anh gần như nằm sát đáy trong khi tiếng Tây Ban Nha chiếm gần trọn tổng số (đỉnh ~17.000 lượt/ngày). **Chỉ số trung tâm của công ty được định nghĩa quanh lựa chọn thị trường** — đúng tinh thần phần 3.
- **Quy tắc đặt mức tham vọng:** sản phẩm càng mới, OKR càng phải tham vọng. *"Tăng 10% conversion rate trong 90 ngày rất dễ nếu app bạn mới ra tuần trước. Còn nếu bạn là Netflix thì không dễ vậy."*

---

## 6. Mô hình kiếm tiền & giá

**Subscription trên app di động** (iOS + Android). Video **không nêu mức giá cụ thể** cũng không nêu ARPU bằng con số — chỉ nói ARPU là chỉ số họ theo dõi rất kỹ và nó chênh lệch lớn giữa các nước.

**Nhưng dashboard cho phép suy ra:** $101.757 MRR / 32.531 subscription ≈ **$3,13/tháng mỗi người trả phí**. Và 32.531 / 1.073.268 active customer ≈ **3,0% chuyển đổi sang trả phí**. Hai con số này giải thích toàn bộ cấu trúc kinh doanh: **giá rất thấp + chuyển đổi rất thấp ⇒ bắt buộc phải có lưu lượng khổng lồ.** Không có cỗ máy UGC thì mô hình này không tồn tại.

Điều đáng chú ý hơn giá là **cấu trúc chi phí**: gần **50% doanh thu đi thẳng cho creator**. Founder giải thích lý do chủ động trả cao: *"This way they are incentivized to do more content and to stay in Symmetry for the long run."*

> 📌 Đây là đánh đổi có chủ đích: **hy sinh biên lợi nhuận để mua lòng trung thành của kênh phân phối**. Khi kênh phân phối của bạn là 500 tài khoản do người khác vận hành, giữ được họ quan trọng hơn giữ được biên.

---

## 7. Tech stack & chi phí

| Hạng mục | Công cụ |
|---|---|
| Code & phân tích hằng ngày | **Claude + MCP** — nối thẳng MCP tới PostHog, Superwall, RevenueCat để đọc dữ liệu ngay trong Claude |
| Nhập liệu bằng giọng nói | **WhisperFlow** — *"I like to speak with my computer, that way I'm faster than typing"* |
| A/B test paywall | **Superwall** |
| A/B test & analytics sản phẩm | **PostHog** |
| Quản lý subscription | **RevenueCat** |
| Tài liệu nội bộ | **Notion** |
| Trao đổi nội bộ | **Slack** |

Stack gọn, toàn công cụ phổ thông. Chi tiết đáng học không phải danh sách công cụ mà là **nối MCP vào các nguồn dữ liệu** — biến việc hỏi "thí nghiệm này chạy ra sao rồi" thành một câu hỏi bằng tiếng nói thay vì mở ba dashboard.

Video **không nêu** chi phí vận hành hằng tháng.

---

## 8. Go-to-market: UGC công nghiệp

### Thứ tự thử — hai cái đầu đều trượt

1. **Cộng đồng YouTube sẵn có** (họ là YouTuber fitness) → có một cú spike download nhỏ lúc launch, rồi hết. *"We thought it was going to be really good for growing the app. It wasn't."*
2. **Influencer marketing** → *"it didn't work."*
3. **UGC** → trúng. *"We were really good at it and we just did more and better."*

> ⚠️ Chi tiết dễ bỏ qua: **một nhóm YouTuber fitness có sẵn audience vẫn không growth được app bằng chính audience đó.** Nếu bạn đang tính "tôi có 50K follower, tôi sẽ dùng nó để launch app" — đây là case phản chứng.

### Dòng thời gian tăng trưởng

| Mốc | Diễn biến |
|---|---|
| 06/06/2025 | Launch — spike nhỏ nhờ audience YouTube cũ, rồi tắt |
| Hè 2025 | Thử UGC, **chỉ ~30.000 download** — giai đoạn mò mẫm |
| Q4/2025 | Nhích nhẹ |
| **Tháng 1/2026 (Q1)** | **Spike lớn** — *"Maybe people go to the gym more in January"* |
| Từ đó tới nay | Ổn định ở mức cao |

> 📌 **Mùa vụ là một phần của câu chuyện này.** Cú nhảy lớn nhất trùng với tháng 1 — tháng cả thế giới quyết tâm đi gym. Đó là may mắn có tính toán: hệ thống UGC đã sẵn sàng từ mùa hè trước để hứng trọn đợt sóng. Nếu làm ngách có mùa vụ, hãy build hạ tầng phân phối **trước mùa**.

### Bên trong cỗ máy UGC

Họ có **dashboard nội bộ riêng** để theo dõi cỗ máy này:

![](screenshots/02_04m08s_dashboard-ugc-566-accounts-79k-videos.jpg)

| Chỉ số trên dashboard | Giá trị |
|---|---|
| Posted videos | **79K** |
| **Active accounts** | **566** (+537 so với kỳ trước, **+1.851,7%**) |
| Views | **762M** |
| Likes | **40M** |
| Comments | **447K** |
| Engagement | **5,51%** |
| **Outliers** | **667 video — chỉ 0,8% tổng số post** |

> ⚠️ **Phát hiện 4 — lời kể "gần 8 tỷ view", dashboard ghi 762 triệu.** Chênh gần 10 lần. Bộ lọc thời gian/nền tảng phía trên dashboard bị làm mờ nên không kiểm chứng được là hai con số đang đo hai thứ khác nhau hay không. **Khi trích case này, hãy dùng 762M — con số có bằng chứng trên màn hình.**

**Con số quan trọng nhất của cả phần này là 0,8%.** Chỉ 667 trên 79.000 video trở thành outlier. Đó chính là định lượng của "trò chơi số lượng": **cứ 125 video mới có 1 video thật sự bùng nổ** — và bạn không biết trước cái nào.

Suy ra thêm: 762M view / 79K video ≈ **~9.600 view trung bình mỗi video**. Còn 566 tài khoản chạy trong ~12 tháng ≈ **~215 video mỗi ngày** cho cả hệ thống. Đây là một dây chuyền sản xuất, không phải "làm content".

- **Phân loại video theo format, rồi chia nhỏ thành sub-format.** Mọi video đều được track để biết format nào đang chạy — dashboard có cả bảng *Top Videos* và *Top Countries*.

![](screenshots/03_04m16s_dashboard-ugc-top-videos-countries.jpg)

- **Format thắng được show trên video:** màn hình khoá iPhone với một thông báo — bạn gái nhắn tin chia tay — và ngay bên dưới là thông báo của Symmetry: *"Go to the gym and work out."*

![](screenshots/04_04m24s_ugc-format-lock-screen-notification.jpg)

- Một video theo đúng format đó đạt **17 triệu view · 760K like · 17K share · 53K lượt lưu**:

![](screenshots/05_04m32s_viral-video-17m-views.jpg)

- **Trả creator gần 50% doanh thu**, để họ làm nhiều hơn và ở lại lâu dài.

**Cơ chế cốt lõi:** không đi tìm một video viral. Đi tìm **format** lặp lại được, rồi nhân bản format đó qua hàng trăm tài khoản, và đo từng sub-format để biết cái nào còn sống. Con số 0,8% outlier nói rằng **cỗ máy được thiết kế để chịu được 99,2% thất bại.**

> So sánh trong kho: [Glam Up + Sprout](../2026-05-17_my-two-apps-make-150k-month-each/case.md) chạy 200+ creator và 400-500 triệu view/tháng; [Flame](../2026-06-21_i-built-a-10k-month-app-with-this-one-system/case.md) chạy 15-20 tài khoản trên 5 điện thoại ở quy mô nhỏ hơn nhiều. Symmetry nằm ở đầu trên của phổ này. **Ba case đều cho cùng một kết luận: UGC là trò chơi số lượng có hệ thống đo lường, không phải trò chơi sáng tạo.**

---

## 9. Bài học & trích dẫn

> **"First, we built what we wanted — terrible idea. Second, we built what users wanted — mediocre. And now we approach a methodical and scientific way of actually building useful things."**

> **"Adding one screen increased 3% retention. That is why you have to AB test everything."**

> **"The earlier the product is, the more ambitious your OKRs have to be."**

> **"Play long-term games with long-term people."** — lời khuyên cuối của Mauro. Công ty lập 2 năm trước, app mới launch 1 năm trước. *"We were really bad when we started but we never surrendered."*

**Chốt lại của host (Pat Walls)** — đáng ghi nhớ ngang lời founder:

> *"Most of the tests that you run and the things that you try don't move the needle at all. And I think just doing those and seeing that and knowing that those things don't matter is like really powerful."*

Ý nghĩa: giá trị của việc chạy thí nghiệm không chỉ nằm ở những lần thắng, mà ở **danh mục những thứ bạn đã chứng minh là vô nghĩa**. Lần sau ai đó đề xuất "đổi landing page đi", "sửa trang settings đi" — bạn đã có dữ liệu để nói không, và dành thời gian đó cho thứ có đòn bẩy.

> *"Maybe focus more on marketing than product often."* — và đúng như vậy: case này kiếm $160K/tháng bằng một sản phẩm ai cũng làm được, nhờ phân phối và đo lường.

---

## 10. Áp dụng cho tôi (indie hacker VN)

**Sao chép được ngay — gần như không tốn tiền:**

- ✅ **Track sự kiện trong sản phẩm trước khi làm bất cứ thứ gì khác.** Lỗi số 1 Mauro thấy ở mọi người là không có event nào cả. Onboarding track từng màn hình. PostHog có free tier rất rộng.
- ✅ **Khung "cái gì / tại sao"**: analytics trả lời *mất người ở đâu*, phỏng vấn user trả lời *vì sao*. Thiếu vế nào cũng thành đoán mò. Với sản phẩm nhỏ ở VN, vế "tại sao" thậm chí dễ hơn — nhắn Zalo/Messenger trực tiếp cho user.
- ✅ **Nguyên lý đòn bẩy màn hình**: trước khi build tính năng, hỏi "cái này chạm tới bao nhiêu % người dùng, và chạm mạnh cỡ nào?" Dark mode 2% vs paywall 100%.
- ✅ **Màn hình cam kết cuối onboarding** — rẻ đến mức nực cười, ở case này đổi lấy +3% retention. Thử ngay, không cần xin phép ai.
- ✅ **OKR 90 ngày với mức tham vọng tỷ lệ nghịch với tuổi sản phẩm.** Sản phẩm mới thì đặt mục tiêu to, vì cải thiện 10% trên nền thấp là dễ.
- ✅ **Nối MCP từ Claude tới PostHog/RevenueCat** — đúng stack anh đang dùng được, biến việc đọc số thành hội thoại.

**Có thể sao chép nhưng phải chỉnh:**

- 🔶 **Localization arbitrage chính là chỗ Việt Nam giống Tây Ban Nha nhất trong cả case.** Công thức: lấy một danh mục app đã được chứng minh ở thị trường tiếng Anh, làm bản tiếng Việt thật tử tế, đánh vào cạnh tranh mỏng. Nhưng phải nhìn thẳng khác biệt: Tây Ban Nha + Mexico là **~500 triệu người nói tiếng Tây Ban Nha**, với ARPU Tây Ban Nha gần mức EU. Việt Nam là ~100 triệu người với ARPU app thấp hơn hẳn. **Cùng công thức, nhưng trần doanh thu khác hẳn một bậc.**
- 🔶 **Chia 50% doanh thu cho creator** chỉ vận hành được khi ARPU đủ cao để phần còn lại nuôi được công ty. Symmetry sống được ở mức **$3,13/người trả phí/tháng** là nhờ **1,07 triệu active customer** — tức mô hình không dựa vào giá mà dựa vào khối lượng. Ở VN, giá còn thấp hơn và dân số nhỏ hơn 5 lần, nên bê nguyên tỷ lệ 50% rất dễ khiến mô hình âm. Hãy **tính ngược từ ARPU thực đo được** ra mức trả tối đa cho mỗi lượt tải — đúng như Mauro làm — thay vì bê tỷ lệ 50% sang.

**Rào cản thật:**

- ⚠️ **Đây không phải case solo founder.** 500 tài khoản, 80.000 video/năm là công việc vận hành của cả một đội. Người làm một mình không chạy nổi quy mô này — đọc để lấy cơ chế, đừng lấy quy mô làm mục tiêu năm đầu.
- ⚠️ **Nền tảng có sẵn:** nhóm này là YouTuber fitness trước khi làm app. Họ đã có sẵn kỹ năng làm nội dung ngắn, hiểu thuật toán, hiểu tâm lý người xem trong ngách. Đó là **vài năm lợi thế tích luỹ không nằm trong video**.
- ⚠️ **Activation ma sát cao là lời cảnh báo cho người chọn ngách.** Mauro nói thẳng: bắt người ta đi gym rồi ghi lại buổi tập là "crazy friction". Anh chịu được vì có cả bộ máy đẩy download bù vào. Nếu anh không có bộ máy đó, **hãy chọn ngách mà activation chỉ tốn một thao tác** (kiểu chụp ảnh của app đếm calo).
- ⚠️ **A/B test cần lưu lượng.** Chạy tối thiểu 2 tuần chỉ có ý nghĩa khi đủ người dùng để kết quả không phải nhiễu. Với app vài trăm user/tháng, A/B test paywall sẽ cho kết quả vô nghĩa — giai đoạn đó hãy ở vế **định tính** (nói chuyện với user), rồi mới chuyển sang định lượng khi có lưu lượng.

**Điều dễ hiểu sai:** đừng đọc case này thành "hãy làm app gym". Ba cơ chế đáng mang đi là (1) **chọn thị trường ngôn ngữ chưa được phục vụ tử tế trong một danh mục đã chứng minh**, (2) **phân phối là trò chơi hệ thống có đo lường, không phải trò chơi sáng tạo**, (3) **quyết định build cái gì bằng thí nghiệm có control, vì cả bạn lẫn user đều đoán sai cái gì quan trọng**.

**Đọc kèm:**
- [CalBuddy — app đếm calo tiếng Hebrew, $80K/tháng](../2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) — **case song sinh**, cùng cơ chế localization arbitrage nhưng phân phối bằng quảng cáo trả tiền thay vì UGC. Đọc trước tiên nếu anh quan tâm hướng "làm bản tiếng Việt của danh mục đã chứng minh".
- [Glam Up + Sprout — 4 app, mỗi app $150K/tháng](../2026-05-17_my-two-apps-make-150k-month-each/case.md) — cùng cỗ máy UGC nhưng nhìn từ góc vận hành creator.
- [Flame — hệ thống VSC](../2026-06-21_i-built-a-10k-month-app-with-this-one-system/case.md) — bản UGC quy mô nhỏ, làm được bởi một người.
- [Gravl — $440K/tháng](../2025-11-13_how-i-built-it-400k-month-mobile-app-gravl/case.md) — cũng là app fitness trong ngách bão hoà, nhưng thắng bằng quảng cáo trả tiền thay vì UGC.
- [72 app, $0 doanh thu](../2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30-day/case.md) — mặt trái: build không đo lường thì bao nhiêu app cũng bằng không.

---

## Nguồn

- Video: [How I Built This $160K/Month Gym App](https://www.youtube.com/watch?v=OV09yPLf8BI) — Starter Story, 09/09/2026, 17:30, 60K views
- Transcript: [`transcript.md`](transcript.md) · Ảnh: [`screenshots/`](screenshots/) — 12 ảnh 720p cắt tại các mốc có dashboard/số liệu
- Sản phẩm: <https://symmetry.club/> · Founder: [@Mauro_Botanes](https://x.com/Mauro_Botanes)

**Ghi chú về phương pháp:** bốn ô ⚠️ trong case này đến từ việc **đọc pixel trên dashboard**, không từ transcript — MRR $101.757 (không phải $160K), "War Map" và "Lifting Your Numbers" (phụ đề tự động nghe nhầm), `start_training_session` (activation, không phải retention), và 762M view (không phải 8 tỷ). Transcript một mình sẽ cho ra một case sai ở cả bốn chỗ.
