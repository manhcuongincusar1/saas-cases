# Starter Story — dữ liệu gốc YouTube

> 200 video · 50.4 giờ · 48.3 triệu lượt xem · kênh [@starterstory](https://www.youtube.com/@starterstory) (+1 video kênh phụ [@StarterStoryBuild](https://www.youtube.com/@StarterStoryBuild))

Chỉ giữ dữ liệu gốc lấy từ YouTube. Phần phân tích cũ (`case.md`, playbooks, `index.md`, `data/cases.csv`, web app, script) đã gỡ ngày 15/11/2026, lấy lại trong git commit `34ce9c8`.

## Cấu trúc

```
starter-story-kb/
├── README.md                 ← file này (mục lục video)
├── videos/<ngày>_<tiêu-đề>/
│   ├── transcript.md         ← transcript có timestamp + mô tả gốc + chapters (video mới: lấy qua bảng chép lời trên Chrome)
│   ├── meta.json             ← metadata gốc (yt-dlp): views, likes, chapters, tags...
│   └── screenshots/          ← ảnh 720p theo chapter (181 video đầu; video thêm sau không có)
├── _raw/
│   ├── subs/<id>.en.json3    ← caption gốc YouTube (179 video; video thêm sau lấy qua Chrome)
│   └── thumbs/<id>.webp      ← thumbnail
└── transcripts/              ← transcript lẻ ngoài kênh (Hasan Aboul Hasan, 1-page book)
```

Query bằng DuckDB:

```bash
duckdb -c "SELECT title, upload_date, view_count::INT AS views FROM read_json_auto('videos/*/meta.json') ORDER BY views DESC LIMIT 20"
```

## Toàn bộ video (mới nhất trước)

| Đăng | Video | Thời lượng | Views | Ảnh | json3 | YouTube |
|---|---|---:|---:|:-:|:-:|:-:|
| 08/11/2026 | [How I Made $1M Building 30 Micro-Apps](videos/2026-11-08_how-i-made-1m-building-30-micro-apps/transcript.md) | 16:53 | 74,973 |  |  | [▶](https://www.youtube.com/watch?v=X2T92MVx7xs) |
| 04/11/2026 | [I turned a viral idea into a $25K/month app](videos/2026-11-04_i-turned-a-viral-idea-into-a-25k-month-app/transcript.md) | 12:04 | 48,512 |  |  | [▶](https://www.youtube.com/watch?v=KgS3hbpxTzE) |
| 01/11/2026 | [How I Built It: $400K/Month iOS App](videos/2026-11-01_how-i-built-it-400k-month-ios-app/transcript.md) | 12:23 | 170,099 |  |  | [▶](https://www.youtube.com/watch?v=hnxn16HtLIk) |
| 29/10/2026 | [We Built a $2M App: This is How We Grew It _(Starter Story Build)_](videos/2026-10-29_we-built-a-2m-app-this-is-how-we-grew-it/transcript.md) | 20:15 | 78,767 |  |  | [▶](https://www.youtube.com/watch?v=N2oWiwbBnmQ) |
| 28/10/2026 | [I Make $30K/Month From the Most Boring Website on the Internet](videos/2026-10-28_i-make-30k-month-from-the-most-boring-website-on-the/transcript.md) | 13:07 | 215,329 |  |  | [▶](https://www.youtube.com/watch?v=pwvnH9S4j60) |
| 25/10/2026 | [I Built a $10K/Month App in 88 Days](videos/2026-10-25_i-built-a-10k-month-app-in-88-days/transcript.md) | 18:45 | 50,679 |  |  | [▶](https://www.youtube.com/watch?v=g9J_-5w9Nrs) |
| 21/10/2026 | [I quit my job to build this micro-saas. Now it makes $30K/month](videos/2026-10-21_i-quit-my-job-to-build-this-micro-saas-now-it-makes/transcript.md) | 15:58 | 147,610 |  |  | [▶](https://www.youtube.com/watch?v=RSlhgyAXsBI) |
| 18/10/2026 | [I built an app that makes $2K PER DAY](videos/2026-10-18_i-built-an-app-that-makes-2k-per-day/transcript.md) | 15:07 | 381,934 |  |  | [▶](https://www.youtube.com/watch?v=NuYO7DWzlaM) |
| 14/10/2026 | [I built this app for my dad. Now it makes $18K/month](videos/2026-10-14_i-built-this-app-for-my-dad-now-it-makes-18k-month/transcript.md) | 15:35 | 63,748 |  |  | [▶](https://www.youtube.com/watch?v=LrLDsvbdPr0) |
| 11/10/2026 | [My First SaaS Project Just Hit $11K/Month](videos/2026-10-11_my-first-saas-project-just-hit-11k-month/transcript.md) | 13:04 | 77,990 |  |  | [▶](https://www.youtube.com/watch?v=QXxESN94Y6s) |
| 07/10/2026 | [I Make $13K/Month From This Simple App](videos/2026-10-07_i-make-13k-month-from-this-simple-app/transcript.md) | 12:36 | 89,603 |  |  | [▶](https://www.youtube.com/watch?v=aLidq3_FwW0) |
| 04/10/2026 | [This crazy simple app makes $50K/month](videos/2026-10-04_this-crazy-simple-app-makes-50k-month/transcript.md) | 16:50 | 104,563 |  |  | [▶](https://www.youtube.com/watch?v=RypUD_Fuaqw) |
| 30/09/2026 | [I Built a $30K/Month Business From a Remote Island (How I Work)](videos/2026-09-30_i-built-a-30k-month-business-from-a-remote-island-ho/transcript.md) | 9:48 | 41,707 |  |  | [▶](https://www.youtube.com/watch?v=ICTRNFIdZvc) |
| 27/09/2026 | [I built this website in 8 hours with Claude. Now it makes $40K/month](videos/2026-09-27_i-built-this-website-in-8-hours-with-claude-now-it-m/transcript.md) | 16:11 | 135,907 |  |  | [▶](https://www.youtube.com/watch?v=s9aLA4IOSZE) |
| 20/09/2026 | [This Simple Widget Makes $50K/Month](videos/2026-09-20_this-simple-widget-makes-50k-month/transcript.md) | 13:38 | 122,537 |  |  | [▶](https://www.youtube.com/watch?v=mr4YV-9MY0Q) |
| 16/09/2026 | [How I Work: $140K/Month App Developer](videos/2026-09-16_how-i-work-140k-month-app-developer/transcript.md) | 8:44 | 62,262 |  |  | [▶](https://www.youtube.com/watch?v=0sO2OSN3jZw) |
| 13/09/2026 | [This app replaced my 9-5 ($155K/year)](videos/2026-09-13_this-app-replaced-my-9-5-155k-year/transcript.md) | 14:32 | 120,673 |  |  | [▶](https://www.youtube.com/watch?v=axH1e2cZSrw) |
| 09/09/2026 | [How I Built This $160K/Month Gym App](videos/2026-09-09_how-i-built-this-160k-month-gym-app/transcript.md) | 17:30 | 59,998 | ✓ |  | [▶](https://www.youtube.com/watch?v=OV09yPLf8BI) |
| 06/09/2026 | [I make $25K/month from one simple website](videos/2026-09-06_i-make-25k-month-from-one-simple-website/transcript.md) | 14:59 | 55,484 |  |  | [▶](https://www.youtube.com/watch?v=xEoLsAQFnOY) |
| 02/09/2026 | [I was stuck at $100 for 2 years until I made one change. Now my app makes $10K/month](videos/2026-09-02_i-was-stuck-at-100-for-2-years-until-i-made-one-chan/transcript.md) | 13:34 | 54,729 |  |  | [▶](https://www.youtube.com/watch?v=TUN8Y8__QGU) |
| 30/08/2026 | [The Insanely Obvious Secret Behind This $69K/Month SaaS](videos/2026-08-30_the-insanely-obvious-secret-behind-this-69k-month-sa/transcript.md) | 17:12 | 76,683 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=BA_fC95p43c) |
| 23/08/2026 | [I make $32K/month from 3 simple, boring websites](videos/2026-08-23_i-make-32k-month-from-3-simple-boring-websites/transcript.md) | 14:30 | 50,476 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=5-G9WHwQMwQ) |
| 22/08/2026 | [He built 100 apps and made $0. Can he fix it in 30 days?](videos/2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30-day/transcript.md) | 14:09 | 41,195 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=AoE1yX9ogCM) |
| 20/08/2026 | [How I Work: $22K/Month Solopreneur](videos/2026-08-20_how-i-work-22k-month-solopreneur/transcript.md) | 9:10 | 22,603 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=NFWV9wxRuv4) |
| 16/08/2026 | [I Spent 24 Hours With iOS Millionaires](videos/2026-08-16_i-spent-24-hours-with-ios-millionaires/transcript.md) | 13:35 | 69,201 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=sAr9FWEQZAk) |
| 12/08/2026 | [The Lazy Method: How I Build $10K/Month Apps](videos/2026-08-12_the-lazy-method-how-i-build-10k-month-apps/transcript.md) | 12:35 | 36,533 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=zrsGDDLP7WM) |
| 09/08/2026 | [I Copied A Huge App. Now I Make $80K/Month](videos/2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/transcript.md) | 13:45 | 65,931 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=GQ27QVp3SzQ) |
| 02/08/2026 | [How I Work: $40K/Month Solo App Builder](videos/2026-08-02_how-i-work-40k-month-solo-app-builder/transcript.md) | 10:00 | 60,478 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=k-aEdS28AH0) |
| 30/07/2026 | [How Postiz Went From $17K to $143K/Month in 4 Months](videos/2026-07-30_how-postiz-went-from-17k-to-143k-month-in-4-months/transcript.md) | 16:11 | 39,496 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=n7Obxh9-Rc8) |
| 26/07/2026 | [This Simple App Makes $18K/Month](videos/2026-07-26_this-simple-app-makes-18k-month/transcript.md) | 15:36 | 157,867 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=V_4kiR3R4QU) |
| 23/07/2026 | [I Make $50K Per Month Working 5 Hours A Week](videos/2026-07-23_i-make-50k-per-month-working-5-hours-a-week/transcript.md) | 13:49 | 66,491 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=DPb-M0Vt4uI) |
| 19/07/2026 | [This Stupidly Simple App Makes $100K/Month](videos/2026-07-19_this-stupidly-simple-app-makes-100k-month/transcript.md) | 17:35 | 112,528 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=EQfZCe3MkTU) |
| 15/07/2026 | [I Quit My Job at Meta to Build a $30K/Month SaaS](videos/2026-07-15_i-quit-my-job-at-meta-to-build-a-30k-month-saas/transcript.md) | 15:00 | 33,917 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=2_lpZ503ZGg) |
| 12/07/2026 | [She Built This $340K/Month App in 60 Days](videos/2026-07-12_she-built-this-340k-month-app-in-60-days/transcript.md) | 16:48 | 65,889 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Eg93po_DAYo) |
| 05/07/2026 | [This Insanely Simple App Makes $50K/Month](videos/2026-07-05_this-insanely-simple-app-makes-50k-month/transcript.md) | 19:16 | 309,900 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=uvIcGuN2iO8) |
| 01/07/2026 | [How I Work: $10M/Year Serial Entrepreneur](videos/2026-07-01_how-i-work-10m-year-serial-entrepreneur/transcript.md) | 11:28 | 81,904 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=jjUf7lrb_xQ) |
| 28/06/2026 | [How We Built This $20K/Month AI App](videos/2026-06-28_how-we-built-this-20k-month-ai-app/transcript.md) | 13:11 | 42,547 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=DiRxTfnHTaY) |
| 24/06/2026 | [I Turned This Spreadsheet Into a $30K/Month Micro-SaaS](videos/2026-06-24_i-turned-this-spreadsheet-into-a-30k-month-micro-saa/transcript.md) | 12:24 | 43,685 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=d8PdJJcEtE0) |
| 21/06/2026 | [I Built a $10K/Month App With This One System](videos/2026-06-21_i-built-a-10k-month-app-with-this-one-system/transcript.md) | 15:19 | 38,714 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=-VlJIgj6gM4) |
| 14/06/2026 | [The First App I Ever Built Makes $25K/Month](videos/2026-06-14_the-first-app-i-ever-built-makes-25k-month/transcript.md) | 18:00 | 147,170 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Q4k8JNYKJT0) |
| 10/06/2026 | [I Built A $1M SaaS In A Hidden Niche](videos/2026-06-10_i-built-a-1m-saas-in-a-hidden-niche/transcript.md) | 13:21 | 50,994 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=NPpky92ZfjA) |
| 07/06/2026 | [I Built Two Apps That Make $120K/Month](videos/2026-06-07_i-built-two-apps-that-make-120k-month/transcript.md) | 14:50 | 77,624 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=xWnqY2Mav4s) |
| 31/05/2026 | [I Built A $30K/Month App: Here's My Exact Process](videos/2026-05-31_i-built-a-30k-month-app-heres-my-exact-process/transcript.md) | 14:13 | 220,189 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=P4QodeA_lQ0) |
| 28/05/2026 | [I Built A Micro-Version Of A $1B SaaS. Now I Make $50K/Month](videos/2026-05-28_i-built-a-micro-version-of-a-1b-saas-now-i-make-50k/transcript.md) | 11:47 | 79,122 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Nnpz1wsTjBI) |
| 24/05/2026 | [I Built A $30K/Month in 35 Days](videos/2026-05-24_i-built-a-30k-month-in-35-days/transcript.md) | 18:20 | 85,389 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=vbEKEWtnndU) |
| 21/05/2026 | [I Make $1.7M/Year In The Most Boring Niche Imaginable](videos/2026-05-21_i-make-1-7m-year-in-the-most-boring-niche-imaginable/transcript.md) | 16:23 | 62,714 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=BHhg-l9AZpM) |
| 17/05/2026 | [My Two Apps Make $150K/Month Each](videos/2026-05-17_my-two-apps-make-150k-month-each/transcript.md) | 16:32 | 168,084 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=32vqaJa90kw) |
| 10/05/2026 | [I Built a $20K/Month App in 83 Days](videos/2026-05-10_i-built-a-20k-month-app-in-83-days/transcript.md) | 16:14 | 287,001 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=r4R_Hlw7sbo) |
| 26/04/2026 | [How I Work: $77K/Month Solopreneur](videos/2026-04-26_how-i-work-77k-month-solopreneur/transcript.md) | 10:39 | 301,402 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=D4fkiQfzw_I) |
| 19/04/2026 | [I Spent 24 Hours With A SaaS Millionaire](videos/2026-04-19_i-spent-24-hours-with-a-saas-millionaire/transcript.md) | 16:03 | 118,531 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=iVy5J7iE-3Q) |
| 12/04/2026 | [I Made $1.5M From An App You’ve Never Heard Of](videos/2026-04-12_i-made-1-5m-from-an-app-youve-never-heard-of/transcript.md) | 14:21 | 89,314 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=bq3-qH-CpYQ) |
| 08/04/2026 | [My App Makes $20K/Month: How I Found A Simple Idea And Turned It Into A Profitable Business](videos/2026-04-08_my-app-makes-20k-month-how-i-found-a-simple-idea-and/transcript.md) | 14:08 | 59,314 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=PIXXEAfo6MY) |
| 05/04/2026 | [How This App Makes $35K/Month](videos/2026-04-05_how-this-app-makes-35k-month/transcript.md) | 21:48 | 162,659 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=rGLXc1GmsaI) |
| 01/04/2026 | [I'm 14 And I Built A $14K/Month App](videos/2026-04-01_im-14-and-i-built-a-14k-month-app/transcript.md) | 13:28 | 281,495 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=dWeoSKLt_fc) |
| 29/03/2026 | [My App Made $120K in 24 Hours](videos/2026-03-29_my-app-made-120k-in-24-hours/transcript.md) | 23:35 | 220,760 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=DkmStHS8NP0) |
| 25/03/2026 | [I Built a $100K/Month Android App](videos/2026-03-25_i-built-a-100k-month-android-app/transcript.md) | 24:10 | 102,942 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=0pp4X58q_0s) |
| 22/03/2026 | [I Make $250K/Month From 13 Businesses (After Losing Everything to AI)](videos/2026-03-22_i-make-250k-month-from-13-businesses-after-losing-ev/transcript.md) | 11:45 | 44,829 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=spiC5m6AJNs) |
| 19/03/2026 | [I Make $17K/Month With One Strategy](videos/2026-03-19_i-make-17k-month-with-one-strategy/transcript.md) | 17:55 | 53,250 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=4KfFB-dh71Y) |
| 15/03/2026 | [I Make $60K/Month From the Most Boring SaaS on the Internet](videos/2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/transcript.md) | 12:06 | 256,592 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=LRX8TWC2hTM) |
| 11/03/2026 | [How This $250K/Month SaaS Got Its First 100 Users (Steal This Playbook)](videos/2026-03-11_how-this-250k-month-saas-got-its-first-100-users-ste/transcript.md) | 14:44 | 104,114 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=l4WEqPX52Cg) |
| 08/03/2026 | [I Built a $10K/Month SaaS Using Other People's Customers](videos/2026-03-08_i-built-a-10k-month-saas-using-other-peoples-custome/transcript.md) | 16:22 | 41,750 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=LKARRA0MvY4) |
| 04/03/2026 | [Zero to $40K/Month With One Marketing Channel (No Social Media)](videos/2026-03-04_zero-to-40k-month-with-one-marketing-channel-no-soci/transcript.md) | 19:46 | 54,074 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=E_rX4JJrYkY) |
| 01/03/2026 | [I Make $15K/Month From One Website](videos/2026-03-01_i-make-15k-month-from-one-website/transcript.md) | 16:19 | 119,709 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=qIlX7cQ2UdU) |
| 25/02/2026 | [I Built a Niche App to $9K MRR](videos/2026-02-25_i-built-a-niche-app-to-9k-mrr/transcript.md) | 15:29 | 68,896 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=7vz6b_Ohdl0) |
| 23/02/2026 | [I sold my company](videos/2026-02-23_i-sold-my-company/transcript.md) | 10:39 | 97,903 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=v-uhjlMg9L0) |
| 11/02/2026 | [How I Built a $12K/Month Micro-SaaS](videos/2026-02-11_how-i-built-a-12k-month-micro-saas/transcript.md) | 17:21 | 58,502 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=W48emwbUlUE) |
| 08/02/2026 | [I Make $150K/Month From 20 Tiny Apps](videos/2026-02-08_i-make-150k-month-from-20-tiny-apps/transcript.md) | 16:53 | 150,903 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=9sJ2R0rM3CA) |
| 05/02/2026 | [I Make $16K/Month... Even In A "Tiny" Niche](videos/2026-02-05_i-make-16k-month-even-in-a-tiny-niche/transcript.md) | 17:21 | 99,982 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=hYF4fQYlrso) |
| 01/02/2026 | [I Made $500K From 8 Different Income Streams](videos/2026-02-01_i-made-500k-from-8-different-income-streams/transcript.md) | 15:17 | 36,321 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=47QXbPGyzBI) |
| 28/01/2026 | [How I Built It: $17K/Month Open Source SaaS](videos/2026-01-28_how-i-built-it-17k-month-open-source-saas/transcript.md) | 22:52 | 35,875 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=RPM4ImzcIFc) |
| 25/01/2026 | [How I Used Reddit to Build a $34K/Month SaaS](videos/2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas/transcript.md) | 16:42 | 78,259 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=pvjalHFNM9Q) |
| 21/01/2026 | [How I Built a $13K/Month SaaS](videos/2026-01-21_how-i-built-a-13k-month-saas/transcript.md) | 23:08 | 43,254 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=R4BS_UiTBPw) |
| 18/01/2026 | [I Built a $20K/Month Mobile App: Here’s My Entire Playbook](videos/2026-01-18_i-built-a-20k-month-mobile-app-heres-my-entire-playb/transcript.md) | 17:34 | 211,225 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=yBjcmMhXSDk) |
| 14/01/2026 | [I built a $14K/month SaaS using Discord](videos/2026-01-14_i-built-a-14k-month-saas-using-discord/transcript.md) | 15:16 | 47,594 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=9r0qPeSJGog) |
| 11/01/2026 | [How My App Hit $60K/Month in 2 Months](videos/2026-01-11_how-my-app-hit-60k-month-in-2-months/transcript.md) | 19:51 | 113,749 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=XifgHi9R5Rc) |
| 07/01/2026 | [How I Grew My App to $13K/month (Even Though I Hate Marketing)](videos/2026-01-07_how-i-grew-my-app-to-13k-month-even-though-i-hate-ma/transcript.md) | 14:55 | 252,461 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Adl5_lJfkEE) |
| 04/01/2026 | [How I built my first SaaS without an audience ($25K/month)](videos/2026-01-04_how-i-built-my-first-saas-without-an-audience-25k-mo/transcript.md) | 14:58 | 73,609 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=FCGpgPZqmkY) |
| 28/12/2025 | [How I Used Twitter to Hit $10K/Month](videos/2025-12-28_how-i-used-twitter-to-hit-10k-month/transcript.md) | 20:09 | 45,703 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=VYT-ip21P08) |
| 20/12/2025 | [How We Grew Our App to $30K/Month](videos/2025-12-20_how-we-grew-our-app-to-30k-month/transcript.md) | 12:47 | 48,053 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=ST2ROUFbdvU) |
| 17/12/2025 | [My mobile app made $800K in 365 days](videos/2025-12-17_my-mobile-app-made-800k-in-365-days/transcript.md) | 13:18 | 60,161 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=LYdJ3dfNCVs) |
| 14/12/2025 | [How I grew my mobile app to $17K per month](videos/2025-12-14_how-i-grew-my-mobile-app-to-17k-per-month/transcript.md) | 20:57 | 120,540 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=8kM-JcKpcDs) |
| 11/12/2025 | [I make $10K/month from 28 apps](videos/2025-12-11_i-make-10k-month-from-28-apps/transcript.md) | 14:01 | 243,263 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=vw2Yc4Y1PsU) |
| 09/12/2025 | [I shipped my app in 12 hours and now it makes $15K/month](videos/2025-12-09_i-shipped-my-app-in-12-hours-and-now-it-makes-15k-mo/transcript.md) | 13:01 | 129,798 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=k2jecxFu2as) |
| 07/12/2025 | [I Built 4 SaaS Apps to $100K MRR: Here's My Exact Playbook](videos/2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-playb/transcript.md) | 18:59 | 264,884 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=xeUhKuJbeWQ) |
| 04/12/2025 | [I make $120K/year from 3 mobile apps](videos/2025-12-04_i-make-120k-year-from-3-mobile-apps/transcript.md) | 14:05 | 36,789 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=SJOFUBNHYqU) |
| 02/12/2025 | [How I Built It: $30K/month Micro-SaaS (Subscribr Breakdown)](videos/2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-breakd/transcript.md) | 16:29 | 94,099 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=7KqlwjBM_tM) |
| 30/11/2025 | [My Apps Failed Until I Discovered This Playbook ($35K/month apps)](videos/2025-11-30_my-apps-failed-until-i-discovered-this-playbook-35k/transcript.md) | 14:08 | 63,052 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=-OPKa8DIzKU) |
| 24/11/2025 | [How he makes $250K per month from a simple app (Letterly Breakdown)](videos/2025-11-24_how-he-makes-250k-per-month-from-a-simple-app-letter/transcript.md) | 13:49 | 90,282 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=wvYej-2KWDg) |
| 20/11/2025 | [Our Mobile App Made $85K in 8 months](videos/2025-11-20_our-mobile-app-made-85k-in-8-months/transcript.md) | 12:55 | 33,531 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=nsn94Ad47GY) |
| 18/11/2025 | [How We Built It: $30K/month Mobile App](videos/2025-11-18_how-we-built-it-30k-month-mobile-app/transcript.md) | 10:49 | 38,114 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=rCV-TVCnF6Q) |
| 16/11/2025 | [My website makes $35K/month (built in 3 hours)](videos/2025-11-16_my-website-makes-35k-month-built-in-3-hours/transcript.md) | 14:26 | 91,055 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=LWPN-PAhtLA) |
| 13/11/2025 | [How I Built It: $400K/Month Mobile App (Gravl)](videos/2025-11-13_how-i-built-it-400k-month-mobile-app-gravl/transcript.md) | 15:34 | 249,456 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=2dfMUtHlQik) |
| 09/11/2025 | [I flipped 4 apps and made $500,000](videos/2025-11-09_i-flipped-4-apps-and-made-500-000/transcript.md) | 16:41 | 113,495 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=PmyXmpkTIdc) |
| 02/11/2025 | [I Built 3 SaaS Apps to $200K MRR: Here's My Exact Playbook](videos/2025-11-02_i-built-3-saas-apps-to-200k-mrr-heres-my-exact-playb/transcript.md) | 13:39 | 986,266 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=67zh8_yiPh4) |
| 30/10/2025 | [I vibe coded a $12K/month mobile app (Stoppr Breakdown)](videos/2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-breakdown/transcript.md) | 10:05 | 54,688 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=orYTlk_BhW8) |
| 28/10/2025 | [My 2 apps made $1.5M](videos/2025-10-28_my-2-apps-made-1-5m/transcript.md) | 14:43 | 478,836 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=9WWvLj-NqEE) |
| 26/10/2025 | [I vibe coded a $20K/month mobile app in 14 days](videos/2025-10-26_i-vibe-coded-a-20k-month-mobile-app-in-14-days/transcript.md) | 13:26 | 619,584 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=CwHD6Fg-Mjs) |
| 23/10/2025 | [How I built a $30K/month mobile app](videos/2025-10-23_how-i-built-a-30k-month-mobile-app/transcript.md) | 14:50 | 86,209 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=T5zMsTw8GWQ) |
| 21/10/2025 | [I made $1M flipping apps](videos/2025-10-21_i-made-1m-flipping-apps/transcript.md) | 11:01 | 52,574 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=plrni3IBEyI) |
| 19/10/2025 | [I Found a Business for Sale and Rebuilt It Into $20K/Month](videos/2025-10-19_i-found-a-business-for-sale-and-rebuilt-it-into-20k/transcript.md) | 12:52 | 77,337 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=4BsxnGRbF4k) |
| 16/10/2025 | [I rebuilt a $1B app and now make $14K/month](videos/2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month/transcript.md) | 14:24 | 92,066 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=88BbTpbWVpY) |
| 14/10/2025 | [Teen From Kazakhstan Makes $1M/Year Online](videos/2025-10-14_teen-from-kazakhstan-makes-1m-year-online/transcript.md) | 10:00 | 50,663 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=YtyJ4reSQY0) |
| 11/10/2025 | [I built a $100K/month AI app](videos/2025-10-11_i-built-a-100k-month-ai-app/transcript.md) | 11:09 | 115,037 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=DV7bBCAABg4) |
| 08/10/2025 | [My app failed, then I changed one thing, and made $80K](videos/2025-10-08_my-app-failed-then-i-changed-one-thing-and-made-80k/transcript.md) | 12:38 | 51,373 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=hYW9YDwHE20) |
| 04/10/2025 | [I Built a $1M SaaS Using YouTube](videos/2025-10-04_i-built-a-1m-saas-using-youtube/transcript.md) | 12:09 | 68,358 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=VZ1XspToV1E) |
| 01/10/2025 | [My two apps made $30M](videos/2025-10-01_my-two-apps-made-30m/transcript.md) | 11:33 | 129,200 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=w8oUlfgvcTI) |
| 27/09/2025 | [How We Built a $10K/mo SaaS](videos/2025-09-27_how-we-built-a-10k-mo-saas/transcript.md) | 13:12 | 57,383 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=3eY71OS4MFw) |
| 24/09/2025 | [This app replaced my 9-5 ($150K/year)](videos/2025-09-24_this-app-replaced-my-9-5-150k-year/transcript.md) | 13:33 | 196,949 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=w3zxMrwWrt0) |
| 20/09/2025 | [The $1M Mobile App Playbook](videos/2025-09-20_the-1m-mobile-app-playbook/transcript.md) | 23:55 | 127,552 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=hKqLceTPLWM) |
| 17/09/2025 | [I Quit YouTube & Built a $1M App (Without My Audience)](videos/2025-09-17_i-quit-youtube-built-a-1m-app-without-my-audience/transcript.md) | 15:55 | 51,759 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=laRliIVNZgU) |
| 13/09/2025 | [My app makes $41K/month](videos/2025-09-13_my-app-makes-41k-month/transcript.md) | 11:47 | 139,779 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=a1EXyJlSx9g) |
| 10/09/2025 | [How I Made $65K in 3 Days](videos/2025-09-10_how-i-made-65k-in-3-days/transcript.md) | 15:45 | 126,595 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=BNr1JOQdSN0) |
| 06/09/2025 | [Our simple app made $100K in 90 days](videos/2025-09-06_our-simple-app-made-100k-in-90-days/transcript.md) | 11:31 | 152,250 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=1nfPvJKrYYQ) |
| 31/08/2025 | [This app made over $1M](videos/2025-08-31_this-app-made-over-1m/transcript.md) | 15:15 | 632,069 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=VfNRd5Rk0cM) |
| 27/08/2025 | [How I Built a $4M Business (Simple Strategy)](videos/2025-08-27_how-i-built-a-4m-business-simple-strategy/transcript.md) | 11:40 | 74,885 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=MLAH5OZ5FO8) |
| 23/08/2025 | [How I Finally Built a $10K/Month SaaS (30 Failures)](videos/2025-08-23_how-i-finally-built-a-10k-month-saas-30-failures/transcript.md) | 11:48 | 60,756 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=rPguT9z6kRQ) |
| 16/08/2025 | [How We Built It: $900K Open Source SaaS](videos/2025-08-16_how-we-built-it-900k-open-source-saas/transcript.md) | 14:37 | 187,323 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=F8i0kkrQ8_o) |
| 13/08/2025 | [How I Built It: $23K/month micro-saas](videos/2025-08-13_how-i-built-it-23k-month-micro-saas/transcript.md) | 11:08 | 315,009 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=NvtsM8Nk72c) |
| 09/08/2025 | [How I Used Reddit To Build a $25K/Month Business](videos/2025-08-09_how-i-used-reddit-to-build-a-25k-month-business/transcript.md) | 14:35 | 160,796 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=3X4VneEHvig) |
| 02/08/2025 | [I Copied a $100M SaaS, Undercut Their Prices, and Hit $10K/Month](videos/2025-08-02_i-copied-a-100m-saas-undercut-their-prices-and-hit-1/transcript.md) | 10:31 | 258,870 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=_KaFS4Dxs5k) |
| 30/07/2025 | [My AI App Makes $100K/Month](videos/2025-07-30_my-ai-app-makes-100k-month/transcript.md) | 12:30 | 78,062 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=miEUhwSR2-0) |
| 26/07/2025 | [I cloned 3 apps and now make $35K/month](videos/2025-07-26_i-cloned-3-apps-and-now-make-35k-month/transcript.md) | 13:38 | 1,043,597 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=8BtHk-oNlN0) |
| 24/07/2025 | [My Side Project Makes $15K/Month (Quit My 9-5)](videos/2025-07-24_my-side-project-makes-15k-month-quit-my-9-5/transcript.md) | 14:55 | 103,722 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=ZGwQoRw7mh8) |
| 20/07/2025 | [I make $40K/month with this one website](videos/2025-07-20_i-make-40k-month-with-this-one-website/transcript.md) | 10:52 | 1,046,569 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=EF3uyvHHBfM) |
| 09/07/2025 | [How I Used Reddit to Hit $17K MRR (With ZERO Audience)](videos/2025-07-09_how-i-used-reddit-to-hit-17k-mrr-with-zero-audience/transcript.md) | 13:16 | 277,469 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=BaWUPamqWlA) |
| 02/07/2025 | [How I Built A $1M Business in 117 Days](videos/2025-07-02_how-i-built-a-1m-business-in-117-days/transcript.md) | 12:46 | 134,688 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=E_sPvPHwpuk) |
| 25/06/2025 | [This App Makes $25,000/Month](videos/2025-06-25_this-app-makes-25-000-month/transcript.md) | 14:48 | 567,632 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=HBCwzfFbopE) |
| 21/06/2025 | [How I Built It: $15K/month Mobile App](videos/2025-06-21_how-i-built-it-15k-month-mobile-app/transcript.md) | 13:26 | 281,476 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=gpn1jEoWT4A) |
| 18/06/2025 | [I Make $100K/Year From 2 AI Side Projects](videos/2025-06-18_i-make-100k-year-from-2-ai-side-projects/transcript.md) | 13:13 | 160,417 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=CoqAxV6b6j4) |
| 14/06/2025 | [I Built a $1M SaaS 100% with No Code (Bubble)](videos/2025-06-14_i-built-a-1m-saas-100-with-no-code-bubble/transcript.md) | 14:06 | 130,533 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=x9TUDb4sLE0) |
| 11/06/2025 | [How I Built It: $9K/Month Micro-SaaS](videos/2025-06-11_how-i-built-it-9k-month-micro-saas/transcript.md) | 15:36 | 173,445 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=npcL7oRZQlI) |
| 07/06/2025 | [I Built an App with Cursor and Made $100K on Launch Day](videos/2025-06-07_i-built-an-app-with-cursor-and-made-100k-on-launch-d/transcript.md) | 14:08 | 205,531 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=4hMg_CZauJs) |
| 04/06/2025 | [How to Use AI to Find a $1M Idea [Reddit, Claude]](videos/2025-06-04_how-to-use-ai-to-find-a-1m-idea-reddit-claude/transcript.md) | 24:27 | 546,935 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=L_FY6aW9cJ4) |
| 31/05/2025 | [I Make $250K/Month From 20 Apps](videos/2025-05-31_i-make-250k-month-from-20-apps/transcript.md) | 18:01 | 94,694 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=En34iY-rQc0) |
| 24/05/2025 | [I Built an App with Cursor, Made $30K, and Quit My Job.](videos/2025-05-24_i-built-an-app-with-cursor-made-30k-and-quit-my-job/transcript.md) | 14:01 | 725,187 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=jpSY4MlWX50) |
| 21/05/2025 | [From Zero to $42K/Month in 90 Days with AI](videos/2025-05-21_from-zero-to-42k-month-in-90-days-with-ai/transcript.md) | 18:56 | 174,282 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=0T55DRYqeeA) |
| 07/05/2025 | [I Got Rejected From YC, Then Built a $200M Startup](videos/2025-05-07_i-got-rejected-from-yc-then-built-a-200m-startup/transcript.md) | 15:03 | 61,943 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=PSx0vcUY-sk) |
| 30/04/2025 | [My Coding Game Makes $1M Per Month](videos/2025-04-30_my-coding-game-makes-1m-per-month/transcript.md) | 17:15 | 195,375 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=tMkpiFIW8Xg) |
| 23/04/2025 | [I Spent 24 Hours With Roblox Millionaires](videos/2025-04-23_i-spent-24-hours-with-roblox-millionaires/transcript.md) | 20:30 | 4,151,743 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=8xgnm6SynH4) |
| 19/04/2025 | [My Apps Make $4.5M/Year With $0 Marketing](videos/2025-04-19_my-apps-make-4-5m-year-with-0-marketing/transcript.md) | 18:13 | 345,620 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=vLLBzUZr6-s) |
| 12/04/2025 | [I Make $60K/Month with 4 Apps](videos/2025-04-12_i-make-60k-month-with-4-apps/transcript.md) | 17:46 | 117,451 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=KpVPST_P4W8) |
| 31/03/2025 | [I Locked Myself In A Room, Made 17 Apps, & Sold 2 for $265,000](videos/2025-03-31_i-locked-myself-in-a-room-made-17-apps-sold-2-for-26/transcript.md) | 17:43 | 284,047 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=zPijWd9uk-I) |
| 25/03/2025 | [I Built a $10K/Month App from My Mom’s Basement](videos/2025-03-25_i-built-a-10k-month-app-from-my-moms-basement/transcript.md) | 19:09 | 236,833 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=qeY283nBhIA) |
| 18/03/2025 | [The $10M AI SaaS Playbook](videos/2025-03-18_the-10m-ai-saas-playbook/transcript.md) | 28:35 | 143,666 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=KcCnqLBhvXY) |
| 08/03/2025 | [I Quit My Job & Accidentally Built A $10M Business](videos/2025-03-08_i-quit-my-job-accidentally-built-a-10m-business/transcript.md) | 21:00 | 81,922 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=gU9FtZIfb_M) |
| 26/02/2025 | [The Underdog: From $200K in Debt to $1M App Maker](videos/2025-02-26_the-underdog-from-200k-in-debt-to-1m-app-maker/transcript.md) | 18:16 | 81,478 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=h9R6ZeNruuI) |
| 07/02/2025 | [The Underdog: From Life Changing Accident to $100M/Year](videos/2025-02-07_the-underdog-from-life-changing-accident-to-100m-yea/transcript.md) | 16:17 | 125,579 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=BeRKQkU5Ceo) |
| 22/01/2025 | [How I Built It: $20K/Month AI App as a Non-Technical Founder](videos/2025-01-22_how-i-built-it-20k-month-ai-app-as-a-non-technical-f/transcript.md) | 15:09 | 83,004 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=yue9in5oh64) |
| 29/12/2024 | [He Made $10M with 3 iPhone Apps](videos/2024-12-29_he-made-10m-with-3-iphone-apps/transcript.md) | 20:24 | 260,856 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=5u9u8yzPEpA) |
| 17/12/2024 | [The Underdog: He Turned His Last $1,000 Into $150M](videos/2024-12-17_the-underdog-he-turned-his-last-1-000-into-150m/transcript.md) | 22:07 | 324,674 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=ZEIPj7QbZeI) |
| 02/12/2024 | [I Make $15K/Month With 2 AI Apps](videos/2024-12-02_i-make-15k-month-with-2-ai-apps/transcript.md) | 16:08 | 343,903 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=G4nsGvL4Fo0) |
| 22/11/2024 | [How I Built It: $12K/Month Micro SaaS](videos/2024-11-22_how-i-built-it-12k-month-micro-saas/transcript.md) | 15:27 | 388,922 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=TCGXT7ySco8) |
| 07/11/2024 | [How I Built It: $37K/Month Notion App](videos/2024-11-07_how-i-built-it-37k-month-notion-app/transcript.md) | 18:00 | 153,023 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=WuzxmeUP6ro) |
| 30/10/2024 | [The day I hit reset on my life](videos/2024-10-30_the-day-i-hit-reset-on-my-life/transcript.md) | 10:56 | 287,705 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=xZDofUHbZHA) |
| 21/10/2024 | [9 Things That Make Me $1.8M/Year](videos/2024-10-21_9-things-that-make-me-1-8m-year/transcript.md) | 12:57 | 43,654 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=GFnBp8lMIf4) |
| 15/10/2024 | [How I Built It: $10K/Month AI Image Generator](videos/2024-10-15_how-i-built-it-10k-month-ai-image-generator/transcript.md) | 14:21 | 133,801 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=mjCa8IFjM2E) |
| 24/09/2024 | [How I Built It: $40K/Month iPhone App](videos/2024-09-24_how-i-built-it-40k-month-iphone-app/transcript.md) | 17:01 | 1,329,106 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=loXc0Tyi4R4) |
| 01/09/2024 | [Faceless: From Immigrant to $1M/Year](videos/2024-09-01_faceless-from-immigrant-to-1m-year/transcript.md) | 18:50 | 86,528 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=TNZmNIYv050) |
| 18/08/2024 | [How I Built It: $20K/Month Chrome Extension](videos/2024-08-18_how-i-built-it-20k-month-chrome-extension/transcript.md) | 13:13 | 303,135 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=ty9ZcimL6VE) |
| 05/08/2024 | [The Underdog: From $10/hr to $1.5M/Year](videos/2024-08-05_the-underdog-from-10-hr-to-1-5m-year/transcript.md) | 20:09 | 653,180 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=WGVxAmmJUmY) |
| 28/07/2024 | [I Turned $150 into $2M/Year](videos/2024-07-28_i-turned-150-into-2m-year/transcript.md) | 16:13 | 220,014 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=8yCXyCN_NR0) |
| 22/07/2024 | [I Built A $1M SaaS In 87 Days](videos/2024-07-22_i-built-a-1m-saas-in-87-days/transcript.md) | 19:03 | 296,872 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=WctFUP4w0sc) |
| 13/07/2024 | [He Quit His Job And Makes $10M/Year Writing Online](videos/2024-07-13_he-quit-his-job-and-makes-10m-year-writing-online/transcript.md) | 17:50 | 83,312 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=OoFqTMPW_3E) |
| 22/06/2024 | [They Make $1.4M/Year With AI](videos/2024-06-22_they-make-1-4m-year-with-ai/transcript.md) | 13:40 | 134,078 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=b5JhfGHafZA) |
| 15/06/2024 | [I Make $1M/Year As An Introvert](videos/2024-06-15_i-make-1m-year-as-an-introvert/transcript.md) | 14:49 | 353,367 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=trNGj1BN1GU) |
| 08/06/2024 | [The Multipreneur: He Makes $10M/Year With 6 Businesses](videos/2024-06-08_the-multipreneur-he-makes-10m-year-with-6-businesses/transcript.md) | 14:08 | 247,357 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=akM6P97_0B8) |
| 01/06/2024 | [I Hacked Reddit To Build A $1M Business](videos/2024-06-01_i-hacked-reddit-to-build-a-1m-business/transcript.md) | 9:05 | 169,802 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=ptT0tfzeu8I) |
| 12/05/2024 | [I Make $1M/Month From Bed](videos/2024-05-12_i-make-1m-month-from-bed/transcript.md) | 15:17 | 143,837 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=dphK9rh2F5U) |
| 04/05/2024 | [I Turned One Website Into $1M/Year](videos/2024-05-04_i-turned-one-website-into-1m-year/transcript.md) | 15:18 | 131,923 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=7pCgbhUWW54) |
| 27/04/2024 | [I Make $5M/Year With 3 Businesses](videos/2024-04-27_i-make-5m-year-with-3-businesses/transcript.md) | 15:51 | 302,434 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=zTKYJWAEl78) |
| 18/04/2024 | [I Made $2.5M Selling A Digital Product](videos/2024-04-18_i-made-2-5m-selling-a-digital-product/transcript.md) | 15:29 | 127,963 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=OKl0C3zg0LU) |
| 06/04/2024 | [I Built A $1M App In 5 Hours](videos/2024-04-06_i-built-a-1m-app-in-5-hours/transcript.md) | 14:38 | 928,321 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=u8sW-NhGfXw) |
| 30/03/2024 | [I Make $1M/Year With One Website](videos/2024-03-30_i-make-1m-year-with-one-website/transcript.md) | 14:47 | 438,918 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=7LZ0MTkNr34) |
| 23/03/2024 | [I Built This $5M/Year Business From A Van](videos/2024-03-23_i-built-this-5m-year-business-from-a-van/transcript.md) | 10:17 | 147,593 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=6iqo7lNR_m0) |
| 10/03/2024 | [I Made $30M With My Side Project](videos/2024-03-10_i-made-30m-with-my-side-project/transcript.md) | 10:18 | 48,918 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=uBGbvKScavk) |
| 03/03/2024 | [The Underdog: From Dead Broke to $30,000,000](videos/2024-03-03_the-underdog-from-dead-broke-to-30-000-000/transcript.md) | 14:19 | 537,736 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=GGxUH6EXF9I) |
| 18/02/2024 | [I Make $2.4M/Year With 6 YouTube Channels](videos/2024-02-18_i-make-2-4m-year-with-6-youtube-channels/transcript.md) | 13:23 | 1,441,850 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=G5cbMnFXcj0) |
| 11/02/2024 | [I Built a $1M AI App [No Code]](videos/2024-02-11_i-built-a-1m-ai-app-no-code/transcript.md) | 16:13 | 744,144 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=IZsQqarWXtY) |
| 28/01/2024 | [The Underdog: From His Parent’s Basement to $25M](videos/2024-01-28_the-underdog-from-his-parents-basement-to-25m/transcript.md) | 14:08 | 2,189,818 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Gv2fzC96Z40) |
| 13/01/2024 | [The $1.8M Solopreneur Playbook](videos/2024-01-13_the-1-8m-solopreneur-playbook/transcript.md) | 11:39 | 487,603 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=vedkm3ZmHIE) |
| 01/01/2024 | [How I Built A $1M Business From This Starbucks](videos/2024-01-01_how-i-built-a-1m-business-from-this-starbucks/transcript.md) | 9:37 | 902,244 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=T_wEmB5MapE) |
| 20/12/2023 | [I Quit My $250K Job To Become an Author](videos/2023-12-20_i-quit-my-250k-job-to-become-an-author/transcript.md) | 13:16 | 19,669 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=lWwZ-fsD8gM) |
| 15/11/2023 | [I Became A Venture Capitalist With Only $1,000](videos/2023-11-15_i-became-a-venture-capitalist-with-only-1-000/transcript.md) | 17:26 | 92,571 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=p3xa6mpxvOY) |
| 02/11/2023 | [The Multipreneur: He’s Building A $10M Portfolio of Income Streams](videos/2023-11-02_the-multipreneur-hes-building-a-10m-portfolio-of-inc/transcript.md) | 18:21 | 343,556 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=nzVcbrLl9VU) |
| 18/10/2023 | [They Built A $2M Business To Fund Their Dreams](videos/2023-10-18_they-built-a-2m-business-to-fund-their-dreams/transcript.md) | 14:37 | 57,496 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=e6COsh5wfNA) |
| 04/10/2023 | [He Built A $2.5M/Year Business In 2 Years](videos/2023-10-04_he-built-a-2-5m-year-business-in-2-years/transcript.md) | 14:13 | 118,026 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=i6kCkGmJc9M) |
| 27/09/2023 | [The Underdog: He Turned His Last $4,000 Into $48M](videos/2023-09-27_the-underdog-he-turned-his-last-4-000-into-48m/transcript.md) | 13:15 | 1,516,501 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=IuoscQiQQLg) |
| 20/09/2023 | [He's Launching A New $1M Business Every Month](videos/2023-09-20_hes-launching-a-new-1m-business-every-month/transcript.md) | 14:52 | 161,057 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=wqN-gjnpns8) |
| 30/08/2023 | [Meet The Kid Who Made $1M with ChatGPT](videos/2023-08-30_meet-the-kid-who-made-1m-with-chatgpt/transcript.md) | 12:07 | 1,046,733 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=irEi7DVBHdA) |
| 23/08/2023 | [I Made $2.3M Writing Like a 5th Grader](videos/2023-08-23_i-made-2-3m-writing-like-a-5th-grader/transcript.md) | 13:08 | 111,180 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=9pP4qSrt5GU) |
| 11/07/2023 | [I Make $845,601 Writing This Online...](videos/2023-07-11_i-make-845-601-writing-this-online/transcript.md) | 12:30 | 140,281 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=5MaPEK-yVVY) |
| 21/06/2023 | [How To Build A $100M Podcast Empire](videos/2023-06-21_how-to-build-a-100m-podcast-empire/transcript.md) | 14:58 | 29,803 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Fk2J2U7669o) |
| 07/06/2023 | [I Make $11M/Year Selling One Product](videos/2023-06-07_i-make-11m-year-selling-one-product/transcript.md) | 13:19 | 436,556 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=5C3YCTL-36c) |
| 17/05/2023 | [I Make $1.3M/Year With One Skill](videos/2023-05-17_i-make-1-3m-year-with-one-skill/transcript.md) | 10:57 | 1,045,911 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=dXKzST0FE-A) |
| 24/04/2023 | [The Solopreneur: He Makes $1.7M With 0 Employees](videos/2023-04-24_the-solopreneur-he-makes-1-7m-with-0-employees/transcript.md) | 12:02 | 663,689 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=v6IF-lVuvbs) |
| 17/04/2023 | [Zero to $1.1B from Flipping Websites](videos/2023-04-17_zero-to-1-1b-from-flipping-websites/transcript.md) | 18:43 | 247,034 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=Km0FNcBI9CM) |
| 09/04/2023 | [He Turned $500 Into $10M](videos/2023-04-09_he-turned-500-into-10m/transcript.md) | 18:22 | 752,051 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=CnE_fLDqa7M) |
| 03/04/2023 | [He Makes $125,000/year As A Niche YouTuber](videos/2023-04-03_he-makes-125-000-year-as-a-niche-youtuber/transcript.md) | 17:13 | 36,731 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=DZTApvWzMuY) |
| 27/03/2023 | [He Built A $600,000 One Person Business (with video editing)](videos/2023-03-27_he-built-a-600-000-one-person-business-with-video-ed/transcript.md) | 20:29 | 187,649 | ✓ | ✓ | [▶](https://www.youtube.com/watch?v=BskeAo66er0) |
| 16/03/2023 | [How To Make $30K/month With Cooking](videos/2023-03-16_how-to-make-30k-month-with-cooking/transcript.md) | 8:57 | 28,785 | ✓ |  | [▶](https://www.youtube.com/watch?v=hCvy-Rt7Naw) |
