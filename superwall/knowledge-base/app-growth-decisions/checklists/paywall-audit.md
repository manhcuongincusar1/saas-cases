# Paywall audit

**Use when** installs grow but revenue doesn't, or before scaling paid acquisition.
**Decision card:** [paywall-pricing](../decisions/paywall-pricing.md). If this sheet and the card disagree, the card wins. Onboarding side: [onboarding-teardown](onboarding-teardown.md).

> **Conflict of interest.** Most paywall heuristics here come from Vah Bagdasarian (paywall agency, builds on Superwall) and Jonathan Parra (ex-Superwall designer, now an agency), both speaking on Superwall's own show. Their claims are tagged *agency*. Operator-measured results carry more weight.

What fixing the paywall alone can do: one of Vah's clients went from 1.1% to ~4% install→paid between April and September. Organic installs stayed flat at ~40–50k a month, with no paid spend (*agency, measured on a client*) — [00:06:47](https://www.youtube.com/watch?v=24QMRDXck70&t=407s), [00:07:11](https://www.youtube.com/watch?v=24QMRDXck70&t=431s).

---

## Step 1 — Funnel numbers

Split by platform (iOS/Android) and country (US vs rest) before you judge anything.

| Metric | Yours | Pass | Fail | Source |
|---|---|---|---|---|
| Install → paywall view | | 85–90% | ≤ 50–55% → fix onboarding first ([onboarding-teardown](onboarding-teardown.md)) | Phoenix Do [00:11:37](https://www.youtube.com/watch?v=D7eaHcznLZU&t=697s) · [00:12:38](https://www.youtube.com/watch?v=D7eaHcznLZU&t=758s) |
| Trial start rate | | > 15% (Vah) | < 15% means "a lot of work to do" (Vah). < 5% is below Steve's floor of "at least a five and maybe 10%" | [00:04:51](https://www.youtube.com/watch?v=24QMRDXck70&t=291s) · [Steve 00:29:55](https://www.youtube.com/watch?v=Y6RstwPUWdU&t=1795s) |
| Trial → paid | | > 30% (Vah); 30–40% is the "industry average" (Steve) | Below it with OK trial starts = product problem (Steve) | [00:05:01](https://www.youtube.com/watch?v=24QMRDXck70&t=301s) · [00:30:00](https://www.youtube.com/watch?v=Y6RstwPUWdU&t=1800s) |
| Install → paid, **no-trial** apps, US-heavy traffic | | ≥ 10% "really good"; 4–10% "not terrible but not great" | < 4%. Vah calls 4% "the bare minimum" | [00:05:37](https://www.youtube.com/watch?v=24QMRDXck70&t=337s) · [00:07:22](https://www.youtube.com/watch?v=24QMRDXck70&t=442s) |
| Install → paid, **trial** apps | | Judge trial start and trial→paid separately (rows above) | Don't apply the no-trial 4% floor directly. Meeting both of Vah's trial thresholds gives ≈ 15% × 30% ≈ 4.5% install→paid, if trial start is counted per install. That is derived arithmetic; Vah doesn't state it | — |

Don't copy another app's paywall or its numbers as your target:
- Parra: the same paywall in the same category "could just flounder completely" in one app versus another — [00:31:41](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=1901s).
- Vah: copying a friend's paywall "fails … many many times every week" — [00:04:31](https://www.youtube.com/watch?v=24QMRDXck70&t=271s).

---

## Step 2 — Score the paywall

Mark each line **Yes / No / N/A**. Every No becomes a row in Step 3.

### Macro: gate, placements, offer (test these first)

- [ ] **The gate is a deliberate choice** (card rules 1–2):
  - Gate the core action (a hard paywall or a required trial) when the problem is pressing and traffic is high-intent.
  - Keep the core free when growth depends on sharing.
  - Evidence for the gate:
    - Steve: trial start went from 6% to 13% when he removed the X, and trial→paid didn't change — [00:20:13](https://www.youtube.com/watch?v=Y6RstwPUWdU&t=1213s).
    - Stronger: about +25% after going hard — [00:25:15](https://www.youtube.com/watch?v=si3HzkBTPl4&t=1515s). They admit it "does reduce your K factor" — [00:25:22](https://www.youtube.com/watch?v=si3HzkBTPl4&t=1522s).
  - Dissent: Phoenix Do says a hard paywall means the app is bad (*heuristic*) — [00:14:17](https://www.youtube.com/watch?v=D7eaHcznLZU&t=857s).
- [ ] **A taste of the product before the paywall is a test, not a requirement.**
  - Allow it only if it costs the user zero effort. Example: PushScroll lets users try push-up detection inside onboarding — [00:49:12](https://www.youtube.com/watch?v=PdudtXwEsOQ&t=2952s).
  - Against: GlamUp got +50% conversion by gating right after onboarding instead of letting users explore first — [00:44:42](https://www.youtube.com/watch?v=Bf12MNPO-Js&t=2682s).
  - Against: Sway lost users by asking for photo uploads before the paywall — [00:21:41](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=1301s). See [onboarding-retention](../decisions/onboarding-retention.md) rule 8.
- [ ] **Every placement exists before you optimize any one of them.** Placements: onboarding, session start (≤ 1 a day), after the core action or a usage limit, transaction abandonment, trial cancel (Vah) — [00:07:50](https://www.youtube.com/watch?v=24QMRDXck70&t=470s), [00:41:17](https://www.youtube.com/watch?v=24QMRDXck70&t=2477s).
  - Vah says the onboarding paywall gets "probably most of your conversions".
  - Welltory gets "over 60%" of its conversions after day one — [00:40:34](https://www.youtube.com/watch?v=tv5hEdmbUTM&t=2434s).
- [ ] **Transaction abandonment shows one more offer.** Options: reframe the price, discount the **annual plan only**, or offer a longer trial.
  - Vah: "Don't discount weekly. Don't discount monthly … We tested like dozens of times" — [00:34:20](https://www.youtube.com/watch?v=24QMRDXck70&t=2060s).
  - Discount depth: Parra uses 25–33% — [00:19:52](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=1192s). PushScroll uses ~80% — [00:55:48](https://www.youtube.com/watch?v=PdudtXwEsOQ&t=3348s). Nobody has compared depths head-to-head.
- [ ] **Trial apps: a multi-step paywall with a trial timeline.** For example: today you start, in two days we remind you, in three days you're charged — [00:14:30](https://www.youtube.com/watch?v=24QMRDXck70&t=870s).
  - Vah puts the lift on trial starts at "20 to even 40%" (*agency heuristic, his average*) — [00:14:40](https://www.youtube.com/watch?v=24QMRDXck70&t=880s).
  - He also says many multi-step paywalls in the App Store "don't do it right" and may see no uplift — [00:15:41](https://www.youtube.com/watch?v=24QMRDXck70&t=941s).
- [ ] **The paywall shows what the trial contains, day by day.** Clear 30 changed only its first paywall screen, from a feature slideshow to a 7-day program. Conversion went from ~18–20% to 30% (*measured*) — [00:24:35](https://www.youtube.com/watch?v=cYcU4_HQdIk&t=1475s).
- [ ] **The annual plan is selected by default**, with weekly or monthly as the secondary option.
  - Sway defaulted to annual "to collect more revenue up front"; weekly was "a lot slower growth" — [00:19:34](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=1174s), [00:19:51](https://www.youtube.com/watch?v=ukGtpnfBpvU&t=1191s).
  - **When this flips:** short-lived needs (dating, job hunting), AI wrappers and young audiences can do better weekly-first. Halo runs weekly-only. See card rule 7.
- [ ] **At most two plans are visible, ordered by length.** The rest go behind "view all plans" (Parra) — [00:11:02](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=662s).

### Design (macro)

- [ ] **The layout is one page: heading, bullets, CTA.** Not a comparison table.
  - Parra: bullet-list paywalls "are one of the few paywalls that perform well across the board" — [00:33:08](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=1988s).
  - In his experience, tables do worse than bullets or visuals — [00:26:12](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=1572s).
  - His +111%: he replaced a comparison table and a 3/6/12-month grid with one product image, "try for 50% off" and a Continue button — [00:26:04](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=1564s). That is a **whole-paywall** change, not a button test.
- [ ] **If the rest of the app is native, a plain native-looking paywall has been tested.** It beat custom designs "by quite a long shot", twice (Parra) — [00:47:32](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=2852s).

### Micro: copy (test last; the wins exist but are small and slow to prove)

- [ ] **Plan names are plain.** "Annual plan" and "Weekly plan", not "AI Assistant Weekly" — [00:08:05](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=485s).
- [ ] **"No commitment, cancel anytime" sits near the CTA.** Parra calls it a "very granular percentage bump" — [00:07:52](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=472s).
- [ ] **The CTA says "Continue"**, which Parra uses "in a lot of cases" — [00:08:48](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=528s).
  - His +10% example bundled cleaner plan names, cancel-anytime and Continue — [00:06:21](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=381s).
  - He says the biggest driver of that lift was the product group, not the button — [00:08:58](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=538s).
- [ ] **"Limited time" appears only in the heading of a one-time-offer paywall.** On a regular paywall, keep just the discount (e.g. "70% off"). The small badge text "is just too small" — [00:09:43](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=583s).

### Is the paywall hiding a retention problem?

- [ ] **Year-1 resubscribe rate is tracked.** Josh's scale: 50% is amazing, 40 good, 30 OK, 20 bad. Not for dating apps — [00:17:08](https://www.youtube.com/watch?v=u4tpE9AvBpc&t=1028s).
  - A paywall can "trick" people into paying for year one; renewal is "the real test" — [00:19:33](https://www.youtube.com/watch?v=u4tpE9AvBpc&t=1173s).
  - If renewal is weak, go to [onboarding-retention](../decisions/onboarding-retention.md).

---

## Step 3 — Test queue

**Order: macro before micro.**
- Stronger: "people are too quick to go on to the micro level" — [00:23:57](https://www.youtube.com/watch?v=si3HzkBTPl4&t=1437s).
- Parra: do design and packaging first and price tests later. Price cohorts are "a pain in the ass to manage" — [00:37:05](https://www.youtube.com/watch?v=lkwX_kc0NS8&t=2225s).

**If you have never tested anything** (Vah, [00:41:55](https://www.youtube.com/watch?v=24QMRDXck70&t=2515s)):
- A/B test a multi-step paywall.
- Add transaction-abandonment and session-start paywalls without testing them first. In Vah's words: "You don't need to experiment. You just need to build your foundation."

**Make each test a big change.** Each test is one hypothesis, but a macro test can swap a whole screen or flow; Parra's +111% was a whole redesign. Don't tweak one small element at a time on low volume. Coconote got "a lot of small wins" but couldn't "make big progress" that way — [00:28:58](https://www.youtube.com/watch?v=E_4gRy4O03w&t=1738s).

**Pass/fail:** don't call a winner on a ~2% difference after one week. Stronger: "that's just standard deviations" — [00:23:12](https://www.youtube.com/watch?v=si3HzkBTPl4&t=1392s).

| # | Change | Macro / micro | Metric it should move | Baseline | Variant | Volume / days | Ship / kill |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

---

## Step 4 — Results log

| Date | What changed | Metric | Before | After | Kept? |
|---|---|---|---|---|---|
| | | | | | |
