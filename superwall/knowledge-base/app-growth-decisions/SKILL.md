---
name: app-growth-decisions
description: Evidence-backed decision support for consumer subscription apps, distilled from 56 founder/operator interviews (Superwall podcast, 43 h, 2024–2026) with every number linked to the exact second. Use when the user must decide something about building or growing a consumer/mobile subscription app — which idea to build and how to validate it, which acquisition channel first (TikTok, Instagram Reels, UGC creators, founder content, ASO/SEO, AI search, Meta/TikTok ads), how to run a creator program, paywall design and pricing, onboarding and retention, when to kill or double down, buying or selling an app — or wants benchmarks to judge their own numbers, or asks what successful app founders actually did.
---

# App growth decisions

A knowledge base for making decisions, not a library to summarise. Your job is to turn the user's situation into a recommendation backed by what operators in the corpus actually did and measured — and to say clearly where the evidence is thin.

## Files

| Path | What | Use it for |
|---|---|---|
| `decisions/*.md` | 9 decision cards: default answer, if/then rules with confidence tags, **thresholds table**, when the default flips, evidence for/against, traps, gaps | **Start here** for any decision. The thresholds tables are the main answer to "is my number good?" |
| `cases/INDEX.md` → `cases/*.md` | 42 case files: idea → product → marketing → verified numbers → lessons | Analogues to the user's situation; "who did this before" |
| `data/benchmarks.csv` | 195 outcome numbers (revenue, views, users, spend) with jump links; filter `kind = 'measured'`. Few conversion rates — use card thresholds for those. Covers the first 52 videos | Scale of outcomes: "how big did similar apps get, how fast" |
| `data/playbooks.csv` | 96 tactics: what it is, when to use, source link (first 52 videos) | Concrete tactics for a chosen path |
| `data/videos.csv` · `data/chapters.csv` | 56 videos with summaries · 639 chapters with links | Finding where a topic is discussed |
| `checklists/*.md` | paywall audit, UGC creator brief, ad testing tracker, onboarding teardown | Turning a decision into work |
| `scripts/search.py` | Full-text search over all transcripts; `--at <url-with-t=>` (or video id / folder + HH:MM:SS) reads 90 s from that point | Verifying a claim; finding what cards miss |
| `FORMAT.md` | Evidence rules + card/case formats | Before editing or adding anything |

Decision cards: `choose-idea` · `build-or-kill` · `choose-channel` · `ugc-creators` · `paid-ads` · `paywall-pricing` · `onboarding-retention` · `aso-search` · `buy-sell-exit`.

## Procedure

1. **Frame the decision.** Restate it as a choice between options. Map it to the cards it touches (usually 1–3; e.g. "start ads?" → `paid-ads` + `paywall-pricing` + `onboarding-retention`). If it spans several (e.g. "launch plan"), read `choose-idea` → `choose-channel` → the channel card.
2. **Collect inputs.** Each card lists the facts that change the answer ("Inputs to collect first"). Use what you already know from the conversation and the user's project; ask only for what's missing and decisive. Don't interrogate. If you can't ask (one-shot answer, user away), answer conditionally: state the assumption and show how the recommendation changes if it's wrong.
3. **Apply the rules.** Walk the card's decision rules against the user's situation. Check "When the default flips" before concluding. Score the user's own numbers against the thresholds table and `data/benchmarks.csv`.
4. **Find analogues.** Pick 2–3 cases from `cases/INDEX.md` closest to the user (category, price, channel, stage). Note where their situation differs.
5. **Verify what you'll lean on.** Before a number carries weight in your recommendation, open it: `scripts/search.py --at "<youtube link from the card>"`. Cards were audited, but a wrong number is the fastest way to a bad decision.
6. **Search past the cards when needed.** If the cards don't cover the question, search transcripts (`scripts/search.py "term" "term"`, `-c 2` for context) and chapters (`duckdb -c "select * from 'data/chapters.csv' where chapter ilike '%paywall%'"`). Say that the answer comes from raw transcript, not a reviewed card.

## Answer shape

Reply in the user's language. Keep it tight:

- **Recommendation** — the choice, in one or two sentences, plus the first concrete step.
- **Why** — the 2–4 rules/cases that drive it, each with its confidence tag and jump link.
- **What would change my mind** — the flip conditions that apply, and the cheapest test to check them.
- **Against** — the strongest counter-evidence or disagreeing operator.
- **Limits** — what the corpus can't tell them here.

## Know the corpus' biases — say them when they matter

- **Survivorship.** Guests are winners. Failure rates, base rates and median outcomes are mostly absent. Never present "X worked for them" as "X usually works."
- **Self-reported numbers.** Revenue/views are claims on a podcast, rarely audited.
- **Sponsors and sellers.** Superwall (host) sells paywall software; SideShift sells creators; Noise sells distribution; Clover Labs is an agency; many guests sell courses/agencies.
- **Scope.** Consumer mobile subscription apps, mostly US, mostly AI/lifestyle/education, 2024–2026. Weak evidence for B2B SaaS, enterprise, marketplaces, games with ads, or non-US markets — say so and lower confidence.
- **Decay.** Tactics, CPMs and algorithms change. Prefer newer videos when evidence conflicts; check `published` dates.

## Adding new videos

1. Download into `/Users/nguyencuong/Desktop/SAAS/superwall/youtube-transcript/superwall/` (baoyu-youtube-transcript skill).
2. `python3 scripts/build_data.py` — rebuilds `data/videos.csv` and `data/chapters.csv` (keeps existing summaries; write a summary for the new row).
3. Read the transcript; add or update case files and card evidence following `FORMAT.md`. Bump `last_reviewed` on cards you touch.
