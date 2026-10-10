# Format & evidence rules

Read this before adding or editing a decision card or a case file.

## Paths

- Skill root: `~/.claude/skills/app-growth-decisions/`
- Transcripts (read-only source of truth): `/Users/nguyencuong/Desktop/SAAS/superwall/youtube-transcript/superwall/<folder>/transcript.md`
  (`meta.json` has title, date, chapters; `transcript-sentences.json` has every sentence with a start time)
- `scripts/search.py "term" "other term"` — find sentences across all videos, with a jump-to-second link
- `scripts/search.py --at <folder-substring> HH:MM:SS` — read 90 s of transcript from a timestamp
- `data/videos.csv` (56 videos: id, folder, title, date, summary) · `data/chapters.csv` (639 chapters with links)
- `data/benchmarks.csv` (195 numbers; `kind` = measured | secondhand | heuristic | hypothetical | target, `note` = correction) · `data/playbooks.csv` (96 tactics, `note` = correction) — cover the first 52 videos; every row re-verified against transcripts 2026-10-08

## Evidence rules (non-negotiable)

1. **Every number and every quote links to the exact second**: `https://www.youtube.com/watch?v=<videoId>&t=<seconds>s`.
2. **Verify in the transcript before writing it down.** Synthesized material (old case studies, HTML reports, playbooks) contains errors — an audit found 10: wrong timestamps, one claim attributed to the wrong video, four overstated claims. Open the timestamp with `search.py --at` and confirm the number and its meaning. If you cannot confirm it, drop it, or keep it marked `(unverified)`.
3. **Label the kind of evidence**: *measured* (operator reports their own result), *heuristic* (operator's rule of thumb / opinion), *secondhand* (someone describing another company).
4. **Confidence tag on every rule**: **[strong]** = 3+ independent operators agree · **[medium]** = 2 · **[weak]** = 1 operator, or opinion only.
5. **Flag conflicts of interest** where relevant: Superwall sells paywall software and hosts the show; SideShift sells creator marketplace access; Noise is a distribution platform; Clover Labs is an agency; many guests sell courses or agencies.
6. **Date-stamp tactics** with the video's publish date — CPMs, algorithms and platform rules decay. Prefer the newest evidence when cases conflict.
7. Keep disagreement visible. Do not average conflicting advice into mush; say who says what and under which conditions.

Write in English (matches transcript vocabulary, so grep works). Be dense: no filler, no motivational prose.

## Decision card — `decisions/<slug>.md` (≤ ~250 lines)

```markdown
---
decision: <the question, one line>
use_when: <situations that should trigger reading this card>
related: [other-card-slugs]
last_reviewed: YYYY-MM-DD
---

# <Question>

## Inputs to collect first
Facts about the user's situation that change the answer (budget, stage, platform, audience, price point, team size...). The agent asks for any it doesn't know.

## Default answer
2–5 sentences: what to do by default and why.

## Decision rules
Ordered if/then rules. Each ends with a confidence tag and links.
- If <condition> → <action>. **[strong]** — [Case](link), [Case](link)

## Thresholds to score yourself
| Metric | Good / bad threshold | What it means | Source |

## When the default flips
Conditions under which the opposite choice is right, with evidence.

## Evidence for
- **Case** (*measured*, YYYY-MM) — claim with number — [hh:mm:ss](link) · [case file](../cases/<slug>.md)

## Evidence against / where operators disagree

## Traps
Mistakes operators in the corpus admit to.

## Gaps
What this corpus cannot answer (so the agent says so instead of guessing).
```

## Case file — `cases/<slug>.md` (≤ ~120 lines)

```markdown
---
app: <name(s)>
operator: <person, role>
category: <e.g. AI photo editor, study app>
primary_channel: <TikTok UGC | Instagram | ASO | Meta ads | ...>
headline: <one line with the key verified numbers>
videos: [<videoId>, ...]
published: YYYY-MM-DD   # date of main source video
---

# <App> — <one line: why this case matters for decisions>

## Idea — how they found it
## Product — what they built and the key product choices
## Marketing — channel, formats, creator/ads machine
## Numbers
| Number | Context | Kind (measured/heuristic/secondhand) | Link |
## Lessons → decisions
- <lesson> → [card](../decisions/<card>.md)
## Caveats
Self-reported numbers, conflicts of interest, survivorship, how dated.
```

## Canonical slugs

Decision cards: `choose-idea`, `build-or-kill`, `choose-channel`, `ugc-creators`, `paid-ads`, `paywall-pricing`, `onboarding-retention`, `aso-search`, `buy-sell-exit`.

Case files (link only to these, or cite the transcript directly):
`studyfetch`, `yannis-reposter-model`, `glamup-sprout`, `pingo`, `coconote`, `halo-ai`, `pep-ai`, `sway-ai`, `sunflower`, `nomad-table`, `fitted`, `jenni-ai`, `noise`, `dan-kwan-apps` (Conch AI / Arise / Shepherd), `stronger`, `raphael-kramer-meme-games`, `bloom`, `payout`, `cal-ai`, `cluely`, `rizzgpt-umax`, `clover-labs`, `sideshift`, `marcus-burke-meta-ads`, `dawson-gibbs-ugc`, `green-noise-steve-young`, `cardstock`, `yourmove-ai`, `paruresis-app`.
Additional case files may exist — run `ls cases/` to see them.
