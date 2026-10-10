---
decision: How fast and what should I build first, and when do I kill, pivot or double down on an app?
use_when: User is about to build an MVP, picking a build stack (no-code / AI coding / native) or scope; has launched and doesn't know whether to keep going; is torn between several apps and one; sees churn after a viral spike; is deciding whether to quit a job, take a loan or scale spend; is holding an app they no longer work on.
related: [choose-idea, onboarding-retention, paywall-pricing, choose-channel, ugc-creators, paid-ads, buy-sell-exit]
last_reviewed: 2026-10-08
---

# How fast and what should I build, and when do I kill, pivot or double down?

## Inputs to collect first
- **Stage**: pre-build / launched <1 month / 1–6 months / revenue but flat.
- **Funnel numbers**:
  - new users per week
  - view→install and install→trial→paid conversion
  - retention: D1/D7/D30, or month-2/3 paid churn, or year-1 resubscribe
  - revenue per install (RPI) and CAC
- **Where it breaks**: no views / views but no installs / installs but no payment / payment then churn / retained but not growing.
- **Runway and risk**: job, savings, debt appetite, solo or team, other apps competing for time.
- **Build skills**: engineer, AI coding, no-code; iOS only or both platforms.
- **Goal**: cash-flow, sell the app, or raise and go big.

## Default answer
Build only the one core action behind the result people saw in your validation video, ugly, in ~2–4 weeks, and keep distribution running in parallel. After launch, stop touching the product for about two weeks and push distribution until at least tens of new users a week come in. Then find the stage that breaks before deciding anything:
- views don't turn into installs → fix the content angle
- installs don't pay → fix onboarding or paywall
- payers churn → fix the product or the audience

Kill quickly when nobody pays after a real distribution push. Double down only when payback math or retention curves support it. Expect retention to be the broken part.

## Decision rules
1. **Scope v1 to the one thing users do every day; let it be ugly.**
   - Sunflower: v1 was a timer, Fiverr graphics and a journal, and the timer is still the most important feature. "Build the smallest thing… it can be ugly as hell."
   - GlamUp's MVP "was all brown, the app barely worked," while distribution ran at the same time.
   - Shepherd "broke a ton" and still hit $75k MRR.
   - Pushscroll's first version was essentially two screens.

   **[strong]** — [Kobe timer](https://www.youtube.com/watch?v=zFfBuyKoaDM&t=1061s), [Kobe v1](https://www.youtube.com/watch?v=zFfBuyKoaDM&t=1304s), [Nicole](https://www.youtube.com/watch?v=Bf12MNPO-Js&t=394s), [Dan Kwan](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1355s), [Pushscroll](https://www.youtube.com/watch?v=PdudtXwEsOQ&t=620s) · [sunflower](../cases/sunflower.md), [glamup-sprout](../cases/glamup-sprout.md), [dan-kwan-apps](../cases/dan-kwan-apps.md)
2. **Time-box the build to ~2–4 weeks, then ship features in ~2-week bursts.** Halo: 2–3 weeks. Shepherd: a "two-week build alongside a two-week growth sprint." GlamUp: 3 weeks to a month. Pep AI: late January → end of February. Stronger finished the app within about two weeks of its viral mock-up. Daniel (Cal AI): "human motivation only lasts about 2 weeks" per feature. Pep ships 2–3 updates a week. Speed matters because copycats arrive within weeks (rule 12). **[strong]** — [Halo](https://www.youtube.com/watch?v=PFfo4JySptw&t=226s), [Dan Kwan](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1352s), [Nicole](https://www.youtube.com/watch?v=Bf12MNPO-Js&t=381s), [Pep](https://www.youtube.com/watch?v=mOpYezjqU9c&t=263s), [Stronger](https://www.youtube.com/watch?v=si3HzkBTPl4&t=1949s), [Daniel](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=1865s), [Pep cadence](https://www.youtube.com/watch?v=mOpYezjqU9c&t=2072s)
3. **Use the fastest stack you can keep iterating on. Design screens first, then generate code.**
   - Caleb designed the whole UI in Figma in 3 days, then a CTO built it. His first app was built in FlutterFlow (no-code).
   - Evan (non-technical) went from Figma to a Claude-built prototype.
   - Connor codes with Cursor or Claude Code: React Native for a simple ~2-week app, Swift when he will iterate a lot. iOS-first because Android is at most ~15% of revenue.
   - Raphael used Buildbox (no-code) at 13, then hired Unity devs once money came in.
   - If you are the distribution person, partner with a builder rather than learn to code (Casper).

   "AI/no-code is good enough for v1" is **[strong]**. Any specific tool choice is **[weak]**. Note: many episodes carry sponsor reads for AI app builders; treat those as ads, not evidence. — [Caleb Figma](https://www.youtube.com/watch?v=yw5iIgO4PbY&t=1914s), [Caleb FlutterFlow](https://www.youtube.com/watch?v=yw5iIgO4PbY&t=708s), [Evan](https://www.youtube.com/watch?v=qYYeu0E-1SI&t=322s), [Connor stack](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=1528s), [Connor RN](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=1615s), [Connor Android](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=1577s), [Raphael](https://www.youtube.com/watch?v=FIgn-1kbzZw&t=548s), [Casper](https://www.youtube.com/watch?v=I10xtUiXfeY&t=448s)
4. **Right after launch → two weeks of distribution only, then judge.** Julian's mentor: "for the next two weeks, don't touch the product… if nothing happens, no one probably cares and you should probably pivot." You need "at least 30 to 100 people in the door per week" before any experiment means anything. Coconote's lesson from an earlier failure: "if you build it, they will not come." **[medium]** — [Julian](https://www.youtube.com/watch?v=zdbimhZjm7k&t=330s), [Julian volume](https://www.youtube.com/watch?v=zdbimhZjm7k&t=360s), [Coconote](https://www.youtube.com/watch?v=E_4gRy4O03w&t=1399s)
5. **Before killing, find the broken stage. Each stage has a different fix.**
   - **Views but no installs** = an intent or angle problem. Yannis's scratch-map video changed only its overlay text and went from zero downloads to moving App Store ranks. See [ugc-creators](ugc-creators.md).
   - **Installs but no money** = onboarding or paywall. Jack Friks needed ~8 months "to realize that downloads don't equal money." See [paywall-pricing](paywall-pricing.md).
   - **Paid then churn** = product or audience. Dawson's SMB Market client got 40M views and ~$1.2M, then ~45% churn 2–3 months later; the fix was changing the creator audience, not the app.
   - **Retained but not growing** = distribution or monetization. Flame had strong retention, no distribution and no monetization, and nearly ran out of money.

   **[strong]** — [Yannis](https://www.youtube.com/watch?v=eh1SDHX84vQ&t=2405s), [Jack](https://www.youtube.com/watch?v=CtqEbgutSb4&t=219s), [Dawson](https://www.youtube.com/watch?v=VGJWRjz6nq8&t=1000s), [Dawson churn](https://www.youtube.com/watch?v=VGJWRjz6nq8&t=1033s), [Flame](https://www.youtube.com/watch?v=pb4JIH8FubE&t=845s)
6. **Give a content format time before declaring it dead, but don't confuse a dead format with a dead product.**
   - Jay (Bloom): "90 days is the minimum… to make any video viral."
   - Matt's best creator needed 25 videos before passing 10k views.
   - Driss spent 6 months at zero views on a channel before it broke.
   - Product-level answers can come in days instead: Roger Chen bought ads before launch because organic UGC breakouts "took like two three months."

   **[strong]** — [Jay](https://www.youtube.com/watch?v=AtYlYzw40vo&t=2613s), [Matt](https://www.youtube.com/watch?v=Ca_VnMTosRo&t=743s), [Driss](https://www.youtube.com/watch?v=szgT-8gXd3s&t=1320s), [Roger](https://www.youtube.com/watch?v=jZ1W85VdIBk&t=531s)
7. **Kill or pause when** (a) a real push gets no paying users (rule 4); (b) the market ceiling is visibly too low (paruresis: 30%+ conversion but $5–10k lifetime, so Caleb moved on); (c) you no longer work on it. On (c), Connor: don't let sunk cost keep it dormant; sell it or give an influencer a large equity stake ("a small win is better than zero"). Make the call early: Halo's main regret is delaying hard decisions; "act on the gut feeling." **[strong]** — [paruresis](https://www.youtube.com/watch?v=yw5iIgO4PbY&t=729s), [Connor equity](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=2615s), [Connor sunk cost](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=2683s), [Halo](https://www.youtube.com/watch?v=PFfo4JySptw&t=3361s) · [paruresis-app](../cases/paruresis-app.md)
8. **Pivot toward what users actually use, not what you planned.**
   - Flame: users came back for the daily couples question, not the AI coach. Rebuilding around it took D30 retention from 0.8% to 4.2%, then ~30%, then 50%.
   - Sunflower's founder didn't believe in the AI sponsor until usage "blew me away": "build everything… then trim."
   - Pep removed bloodwork ("no one used it") and added a long-requested calculator.
   - Jack moved his time to PostBridge because it "did so much better" than his app.

   **[strong]** — [Flame](https://www.youtube.com/watch?v=pb4JIH8FubE&t=702s), [Flame D30](https://www.youtube.com/watch?v=pb4JIH8FubE&t=13s), [Kobe](https://www.youtube.com/watch?v=zFfBuyKoaDM&t=1160s), [Pep](https://www.youtube.com/watch?v=mOpYezjqU9c&t=1968s), [Jack](https://www.youtube.com/watch?v=CtqEbgutSb4&t=675s)
9. **Double down (more spend, a loan, quitting your job) only on measured economics.**
   - Halo saw conversion per view stay constant and an LTV:CAC of "five to one or six to one." He then emptied his bank account and took a ~$100k loan, ran at break-even for the first half of the climb, then turned profitable.
   - Sway grew organically to ~$30–40k/mo, then repurposed videos as ads and reached ~4–5× (host's math).
   - Steve: reach "at least a $3 RPI before you can think about Meta."

   **[strong]** — [Halo](https://www.youtube.com/watch?v=PFfo4JySptw&t=3035s), [Halo loan](https://www.youtube.com/watch?v=PFfo4JySptw&t=3066s), [Sway](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=645s), [Sway 4–5×](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=742s), [Steve](https://www.youtube.com/watch?v=Y6RstwPUWdU&t=1029s) · [halo-ai](../cases/halo-ai.md), [sway-ai](../cases/sway-ai.md)
10. **Don't pour money into a leaky app. Retention is the usual weak spot.** Several founders say it outright:
    - Reed: "I haven't found product market fit yet… my churn is high." He is holding back celebrity partners: "we're not ready for it."
    - Raphael: "never really cracked retention" across ~50 apps.
    - Dan Kwan paused all creator ops on Shepherd to build social loops.
    - Bloom: "people overlook product market fit."

    Fixes that worked: Cal AI added streaks, groups and leaderboards; PrayScreen reached 60% D30. Benchmarks are in the table below.

    **[strong]** — [Reed](https://www.youtube.com/watch?v=9655E10fxsk&t=623s), [Reed celebs](https://www.youtube.com/watch?v=9655E10fxsk&t=1514s), [Raphael](https://www.youtube.com/watch?v=FIgn-1kbzZw&t=838s), [Dan Kwan](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1549s), [Bloom](https://www.youtube.com/watch?v=AtYlYzw40vo&t=46s), [Cal AI](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=1663s), [PrayScreen](https://www.youtube.com/watch?v=NmIHgCRd04E&t=335s) · [fitted](../cases/fitted.md), [raphael-kramer-meme-games](../cases/raphael-kramer-meme-games.md), [bloom](../cases/bloom.md)
11. **Early on, or when the goal is cash flow → take many cheap shots and move your time to whatever shows pull. Once one app retains and pays back → concentrate.**
    - Many shots: Lots sold his 4th app and tells newcomers to get a first small win. Nicole has built 4 apps. Raphael shipped ~50 games. Hunter Isaacson mentions a "TestFlight graveyard" of apps that never launched. Social runs 22 apps.
    - Concentrate: Sunflower, Coconote and Pingo each scaled a single app to $1M+ ARR. Josh: push one channel to its ceiling before adding the next.
    - Daniel's untested variant: churn out many apps and give big influencers equity to promote them.

    Many shots early: **[strong]**. Concentrate after proof: **[medium]**. — [Lots](https://www.youtube.com/watch?v=NmIHgCRd04E&t=1115s), [Nicole](https://www.youtube.com/watch?v=Bf12MNPO-Js&t=19s), [Raphael](https://www.youtube.com/watch?v=FIgn-1kbzZw&t=853s), [Hunter](https://www.youtube.com/watch?v=DTree0unT_0&t=1771s), [Social](https://www.youtube.com/watch?v=oxr_Dz1vhdU&t=254s), [Josh](https://www.youtube.com/watch?v=u4tpE9AvBpc&t=2966s), [Daniel](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=2752s)
12. **Assume a working app gets copied within weeks; speed and a moat beat secrecy.** Coconote: "a hundred of those copycat products next week, maybe sooner." Peter (Stronger): look for technical or social moats, or internal tooling rivals can't see, because otherwise you get copied within 1–2 weeks. PrayScreen: ~70 lookalike listings 2–3 months after launch. **[strong]** — [Coconote](https://www.youtube.com/watch?v=E_4gRy4O03w&t=2487s), [Peter](https://www.youtube.com/watch?v=si3HzkBTPl4&t=3025s), [PrayScreen](https://www.youtube.com/watch?v=NmIHgCRd04E&t=17s)
13. **Leave your job when the app covers your costs, or when you have a fallback.** YourMove quit at a ~$20k/mo revenue line (≈$10k profit, enough to cover expenses). Jay (Nomad Table) quit within a week of getting the idea, with savings and big-tech re-hire as a safety net. **[medium]** — [YourMove](https://www.youtube.com/watch?v=CyaWU1qxQg4&t=3065s), [YourMove profit](https://www.youtube.com/watch?v=CyaWU1qxQg4&t=3196s), [Nomad Table](https://www.youtube.com/watch?v=RVnnqTrSKZY&t=3042s)

## Thresholds to score yourself
| Metric | Good / bad threshold | What it means | Source |
|---|---|---|---|
| v1 build time | 2–4 weeks (Halo 2–3 wk, Shepherd 2 wk, GlamUp 3 wk–1 mo, Connor ~2 wk) | Longer = over-scoped for a test | [Halo](https://www.youtube.com/watch?v=PFfo4JySptw&t=226s), [Shepherd](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1352s), [Nicole](https://www.youtube.com/watch?v=Bf12MNPO-Js&t=381s), [Connor](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=1615s) |
| Post-launch volume | ≥30–100 new users/week | Below this, experiments are noise | [Julian](https://www.youtube.com/watch?v=zdbimhZjm7k&t=360s) (heuristic, 2025-11) |
| Content–market fit | ~5–6 videos >10k views in a first-month creator campaign; ≥5k views on copied formats; 75–80% hold past 3 s | Content works; the problem is downstream | [Nick, SideShift](https://www.youtube.com/watch?v=F2dVvzvwtBY&t=605s) (COI), [Joseph 2025](https://www.youtube.com/watch?v=_9agAuKOOPg&t=5444s), [Jay](https://www.youtube.com/watch?v=RVnnqTrSKZY&t=1676s) |
| Content patience | 90 days minimum; ~25 videos for a new creator | Don't kill a format sooner | [Jay](https://www.youtube.com/watch?v=AtYlYzw40vo&t=2613s), [Matt](https://www.youtube.com/watch?v=Ca_VnMTosRo&t=743s) |
| Scale trigger: payback | LTV:CAC ~5–6:1 with steady conversion per format | Spend (even borrowed) scales predictably | [Halo](https://www.youtube.com/watch?v=PFfo4JySptw&t=3035s) (measured, 2026-03) |
| Scale trigger: paid | RPI ≥$3 before Meta; ~$30–40k/mo organic before ads | Paid ads won't just burn cash | [Steve](https://www.youtube.com/watch?v=Y6RstwPUWdU&t=1029s), [Sway](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=645s) |
| D30 retention | 50–60% exceptional (Flame, PrayScreen daily-habit apps); 0.8% = broken product | Retained enough to invest | [Flame](https://www.youtube.com/watch?v=pb4JIH8FubE&t=13s), [PrayScreen](https://www.youtube.com/watch?v=NmIHgCRd04E&t=335s) |
| Year-1 resubscribe | 50% amazing / 40 good / 30 okay / 20 bad (dating lower) | Revenue quality, valuation | [Josh](https://www.youtube.com/watch?v=u4tpE9AvBpc&t=1028s) (heuristic, COI M&A) |
| Organic share of installs | ≥50% great, 35–50 good, <20 = paid-acquisition treadmill | Whether growth is earned or bought | [Josh](https://www.youtube.com/watch?v=u4tpE9AvBpc&t=1239s) |
| Wrong-audience churn | ~45% churn within 2–3 months after a big campaign | Change audience/creators before scaling | [Dawson](https://www.youtube.com/watch?v=VGJWRjz6nq8&t=1033s) (secondhand, client) |
| Time to real money | 14 days (Shepherd $75k MRR) → 45 days ($100k ARR, Coconote) → 70 days ($100k revenue, Pep AI) → 8 months (Jack) → 1.5 years to first $1k (YourMove) | Slow ≠ dead if usage keeps rising | [Shepherd](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1355s), [Coconote](https://www.youtube.com/watch?v=E_4gRy4O03w&t=2015s), [Pep](https://www.youtube.com/watch?v=mOpYezjqU9c&t=206s), [Jack](https://www.youtube.com/watch?v=CtqEbgutSb4&t=219s), [YourMove](https://www.youtube.com/watch?v=CyaWU1qxQg4&t=465s) |
| Quit-job line | ~$20k/mo revenue ≈ $10k profit | Covers costs without savings burn | [YourMove](https://www.youtube.com/watch?v=CyaWU1qxQg4&t=3196s) |

## When the default flips
- **Slow but rising → persist, don't kill.** YourMove took 2.5 years to real money (1.5 years to the first $1k) and kept going because users kept coming and friends asked "can I use it?" That pull is the signal, not revenue alone. Coconote: "momentum is like oxygen." — [YourMove pull](https://www.youtube.com/watch?v=CyaWU1qxQg4&t=362s), [YourMove timeline](https://www.youtube.com/watch?v=CyaWU1qxQg4&t=454s), [Coconote](https://www.youtube.com/watch?v=E_4gRy4O03w&t=236s) · [yourmove-ai](../cases/yourmove-ai.md)
- **Social or network-effect apps.** Judge by density, invites and K-factor, not paid CAC. Revenue per user is lower, so paid ads rarely pay back (Nomad Table). Dan Kwan deliberately paused UGC to build social loops. — [Nomad Table](https://www.youtube.com/watch?v=RVnnqTrSKZY&t=2165s), [Dan Kwan](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1549s) · [nomad-table](../cases/nomad-table.md)
- **Regulated or sensitive domains limit "ship ugly."** Pep AI cleared its dosage calculator with attorneys before shipping. Sunflower routes anything "remotely scary" to a clinical team and builds where model companies lack outcome data. — [Pep](https://www.youtube.com/watch?v=mOpYezjqU9c&t=1911s), [Kobe safety](https://www.youtube.com/watch?v=zFfBuyKoaDM&t=1418s), [Kobe](https://www.youtube.com/watch?v=zFfBuyKoaDM&t=1701s)
- **Search-led (ASO) apps run on a different clock.** Rank-driven revenue can be flat and passive for years (Cardstock ~$10k/mo for two years) until rank is lost. Kill and scale criteria follow keyword rank, not virality. See [aso-search](aso-search.md). — [Cardstock](https://www.youtube.com/watch?v=CAi50V_eIRA&t=1177s) · [cardstock](../cases/cardstock.md)
- **Strong at distribution, weak at product.** Partner with a product or engineering owner instead of churning more apps. Raphael says he's "never been a product guy" and is now taking a bigger swing; Casper gives equity to a builder. — [Raphael](https://www.youtube.com/watch?v=FIgn-1kbzZw&t=823s), [Casper](https://www.youtube.com/watch?v=I10xtUiXfeY&t=448s)

## Evidence for
- **Shepherd / Dan Kwan** (*measured*, 2025-10): concept → chart in a 2-week build plus 2-week sprint, 7 videos, $75k MRR in two weeks despite bugs; then paused creator ops for social loops — [00:22:35](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1355s), [00:23:00](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=1380s) · [case file](../cases/dan-kwan-apps.md)
- **Halo AI / Dillion** (*measured*, 2026-03): 2–3-week build; LTV:CAC ~5–6:1 → ~$100k personal loan; break-even for roughly the first half of the climb to $300k/mo — [00:51:21](https://www.youtube.com/watch?v=PFfo4JySptw&t=3081s) · [case file](../cases/halo-ai.md)
- **Pep AI / Cedric** (*measured*, 2026-06): ~5-week build, 2–3 updates a week, removes unused features; $100k revenue in 70 days — [00:03:26](https://www.youtube.com/watch?v=mOpYezjqU9c&t=206s) · [case file](../cases/pep-ai.md)
- **Sunflower / Kobe** (*measured*, 2026-03): core = timer; ~$0 → $1M annualized in ~10 months — [00:00:13](https://www.youtube.com/watch?v=zFfBuyKoaDM&t=13s) · [case file](../cases/sunflower.md)
- **Flame** (*measured*, 2026-02): pivot to the feature users came back for; D30 0.8% → 4.2% → ~30% → 50% — [00:10:45](https://www.youtube.com/watch?v=pb4JIH8FubE&t=645s), [00:00:13](https://www.youtube.com/watch?v=pb4JIH8FubE&t=13s) · [case file](../cases/flame-couples.md)
- **Sway / Daniel** (*measured*, 2026-05): organic ceiling ~$30–40k/mo, then ads — [00:10:45](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=645s) · [case file](../cases/sway-ai.md)
- **Jack Friks** (*measured*, 2025-12): ~8 months before an app made real money (peak $15k/mo); a 30-day challenge app hit $1,000 in its first month; he shifted time to whichever product pulled — [00:03:52](https://www.youtube.com/watch?v=CtqEbgutSb4&t=232s), [00:19:44](https://www.youtube.com/watch?v=CtqEbgutSb4&t=1184s)
- **Social studio / Patrick** (*measured*, 2026-07): 22 apps, both built and bought; tests ads for apps before they exist — [00:04:14](https://www.youtube.com/watch?v=oxr_Dz1vhdU&t=254s), [00:07:01](https://www.youtube.com/watch?v=oxr_Dz1vhdU&t=421s) · [case file](../cases/social-app-studio.md)
- **Jungle / Julian** (*heuristic*, 2025-11): mentor's rule of two weeks of distribution only; ≥30–100 new users/week to learn anything — [00:05:30](https://www.youtube.com/watch?v=zdbimhZjm7k&t=330s) · [case file](../cases/jungle-study.md)
- **PrayScreen / Lots** (*measured*, 2025-09): 60% D30; ~70 copycat listings within 2–3 months; his 4th sold app — [00:05:35](https://www.youtube.com/watch?v=NmIHgCRd04E&t=335s), [00:00:17](https://www.youtube.com/watch?v=NmIHgCRd04E&t=17s) · [case file](../cases/prayscreen.md)
- **Conch AI / Dan Kwan** (*measured*, 2025-10): "in about 30 days, we hit a million ARR, did 500k in a month" — [00:00:00](https://www.youtube.com/watch?v=2cDIFx4WWD0&t=0s)

## Evidence against / where operators disagree
- **Kill fast vs persist.** Julian (2 weeks of distribution, then pivot) and Halo (act early) favour speed. YourMove (2.5 years), Jack (8 months), Driss (6 months at zero) and Jay (90 days per format) favour persistence. Reconciliation: kill on *absence of pull* (nobody pays, nobody returns, usage flat). Persist when usage or retention rises and only conversion or distribution lags.
- **Ugly-fast vs quality.** Nicole and Kobe ship ugly. Connor prefers Swift for quality on apps he'll iterate. Coconote and Peter argue a mere MVP gets cloned within weeks, so the lasting edge is continuous "wow" or tooling.
- **Monetize early vs grow free.** Flame stayed free too long and nearly ran out of money. Fitted plans to *remove* its hard paywall to unblock growth. Peter's accidental hard paywall raised revenue but killed sharing. See [paywall-pricing](paywall-pricing.md).
- **Portfolio vs one app.** Raphael's ~50 games produced only small exits and no retained product; Lots, Nicole and Social show portfolios can compound skills and capital. The corpus has no head-to-head comparison.
- **Organic vs paid for the scale-up.** Joseph Choi (2026-09, COI): organic tops out at ~$1–3M/yr, then re-use winning organic videos as ads — [00:03:12](https://www.youtube.com/watch?v=0mOLs315i04&t=192s). Nomad Table avoids paid entirely for a social app. Kobe argues burner-account UGC won't take you from $1M to $100M.

## Traps
- **Polishing before distribution.** Coconote's first music app taught them "if you build it, they will not come."
- **Scaling spend on a leaky funnel.** Reed is holding off; Dawson's client saw ~45% churn after 40M views.
- **Waiting to make hard calls.** Halo says delayed decisions "all add up" at scale.
- **Sunk cost on dormant apps.** Connor: "Like no, you're not [going to do something with it later]" — sell it or give away equity — [00:44:10](https://www.youtube.com/watch?v=zpTXi8WxeM0&t=2650s).
- **Downloads ≠ money.** Jack spent 8 months learning this.
- **Retention ignored while chasing virality.** Raphael's games were "developed to be good on a TikTok video," with "super low retention" — [00:10:29](https://www.youtube.com/watch?v=FIgn-1kbzZw&t=629s).
- **Hiring an agency at $0/mo.** Joseph Choi: at $0 MRR "you shouldn't be hiring an agency"; drive the strategy yourself first — [00:14:17](https://www.youtube.com/watch?v=0mOLs315i04&t=857s) (COI: he sells a community).

## Gaps
- **No base rates.** There is no denominator of apps that followed this process and died, so the "kill after X" thresholds are single-operator heuristics.
- **No category D1/D7 retention benchmarks** in the corpus; only scattered D30 points and Josh's year-1 resubscribe rule.
- **No data on build cost** (dev hours, agency vs in-house), only build time.
- **No controlled comparison** of no-code vs AI-coded vs native apps on outcomes, and little Android-first or web-first build evidence.
- **Survivorship and self-reporting.** Every number is self-reported on a show hosted by Superwall (sells paywalls). Several guests sell courses, communities, agencies (Evo, Clover), creator marketplaces (SideShift) or M&A services (Josh, Steve Young).
