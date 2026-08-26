# dev_history — *Den, který se nestal*

> Professional changelog of progress + decisions. Newest entries on top. Decision index: `docs/adr.md`.

## 2026-08-26 — Publication audit: the repo was never actually public

**The finding.** ADR-013 recorded the repo as *published*, the README was rewritten for readers
and the privacy sweep was done — but the visibility switch was never flipped. For three weeks the
project's own documentation asserted a state the repository did not have. Found while preparing to
link the book from the author's public site, where a private repo would have answered every visitor
with a 404. The repo is public now, with the spoiler consequence of `bible/` re-accepted knowingly.

**Two paths from the author's disk, still in tracked files.** `CLAUDE.md` carried
`D:\Projekty\Scifi` in its title, and `tools/make_cover.py` hard-coded the same absolute path as
its default output — which also meant the cover generator could not run for anyone who cloned the
repo. The default now resolves relative to the script's own location; verified it points back at
`book/cover.png`.

**Statistics the E6 pass had silently invalidated.** The README's stat table and
`docs/architecture.md` still quoted the pre-E6 book: 53,393 words (now 53,470), a 13,837-word bible
(13,860), a 12-record decision index (14). The commit count was dropped from the table rather than
corrected — it invalidates itself on every housekeeping push, this one included. E6 was added to
the prompt table it had been missing from. The claim that *everything around the prose is English*
was corrected: the bible, the style guide and `CLAUDE.md` are Czech and always were.

**Verification.** `python tools\gate.py` → GREEN, 0 hard. `--cards` → GREEN, 0 warnings.
`--selftest` → GREEN, all 17 checks fired. `tools/make_cover.py` compiles and its resolved default
path checked by hand. → ADR-015

**Model-fit:** used frontier·high → mild overkill for the edits themselves, correct for the audit:
the finding that mattered (a published-state claim that was never true) came from checking the
world against the docs rather than reading the docs, and that habit is worth the tier.

## 2026-08-04 — E6 · De-mannerism pass: the audit's findings applied, no artificial flaws

A blind full-book audit ("does this read machine-written?") returned verdict (c) — *the machine
shows through excess competence, not weak writing* — with measured signatures: 93 % of the 67
scene/chapter endings landing on an aphorism, 106+ antithesis constructions, 883 em-dashes
(1/62 words), figurative-tic vocabulary, and not one scene without narrative function. The author
challenged the audit's "write a scene that goes nowhere" advice and the challenge was correct:
camouflage was rejected as a goal. Every change below was accepted only where it made the book
*read* better; the shrinking machine-signature is a side effect.

Done: 13 scene-break aphorisms dissolved into factual endings (carded chapter out-hooks
untouched); Halina's cafe monologue gets a lost thread and an off-target interruption; Roubal's
"three floors" lecture delivers its third floor untidily instead of on a raised finger; dash
density 883 → 819 with 4+-dash paragraphs 26 → 18; figurative *inventura* / *bez adjektiv* /
*po vrstvách* thinned; the third meta-reference to the i5/ch10 sentence and the self-naming of
the ch14 rhyme cut (the audit's single worst finding); one path in ch13 now rejected in disgust
and another rejected wrongly first; four small unsymbolic no-payoff details added (a bathroom
renovation, cheap chlebíčky, two schoolgirls buying one tulip, a cracked egg) which also lifted
three chapters back over their target band. Word count 53,470. Gate GREEN (0 hard), rebuilt all
three formats. → ADR-014

**Model-fit:** used frontier·high with a blind auditor sub-agent → fit; the audit's measured
counts (not impressions) are what made the edit scoped and defensible. Next time: run this audit
*inside* P2, before typesetting — it is a review lens like any other, and it found things four
cold reads did not.

## 2026-08-04 — Published: public GitHub repository, English README, personal data stripped

**Shipped.** The repo went public with a reader-facing English README covering the book, its
statistics, the three-prompt method, the chain runs, the review panels, the architecture, the
gate and the build — plus a spoiler warning above the fold, because `bible/` gives away every
twist in the book it belongs to. `docs/architecture.md` was re-pointed as the working reference
for people editing the repo, with the README carrying the overview.

**Privacy sweep before the first push.** The author is credited by first name only — cover,
colophon, EPUB/PDF metadata; the full surname is gone from every built artefact (verified by
reading the strings back out of the PDF and the EPUB, not by trusting the source). Third-person
references to the author in `CLAUDE.md` became "the author". `.claude/settings.json` was untracked
and gitignored: it pointed at hook scripts living outside this repo, so it was both machine-local
and a leak of an unrelated private directory. The names of unrelated private projects were
generalised in `docs/adr.md`, `tools/gate.py` and `tools/build.ps1`, whose defaults still carried
the reference project's title and language — those now default to this book. → ADR-013

**Verification.** Rebuilt all three formats on the new defaults (`powershell tools\build.ps1` with
no arguments now produces the right book): PDF 178 pages, EPUB creator `Martin`, rights line
correct, surname absent from both. Gate GREEN.

## 2026-08-04 — Title · *Nedoložení* → ***Den, který se nestal***

The author rejected the K0 working title as odd-sounding and un-Czech, and he was right —
`nedoložení` is a real word but lives only in officialese, so as a title it reads as a fragment
of a form. My first counter-proposal (a one-letter change to *Nedoložená*) was a bad answer to a
fair complaint; the second attempt offered four titles across genuinely different registers and
the author chose the most readable. Propagated everywhere the live title appears — assemble
config, EPUB/PDF metadata, colophon, cover, build stem, README, CLAUDE.md, style guide, plot
architecture, gate — while ADR-001 and the K0 entry below keep the working title as the record of
what was decided then. The cover generator now auto-fits the title block into the clear column
left of the seam, so a future title change costs nothing in layout. Rebuilt and re-verified: PDF
178 pages with the new title on the title page and no trace of the old one, EPUB metadata and
cover correct. Lesson: a "working title" that survives to the last prompt stops being provisional
without anyone deciding it should — re-open it explicitly before typesetting, not after.
→ ADR-012

## 2026-08-04 — P2 · Edited and typeset: EPUB + MOBI + 178-page A5 PDF, gate green

**Shipped.** The finished book. The author's brief for this pass was three words — *flow,
readability, interest* — and the whole prompt was scoped to them. 53,393 words (+354 vs. the P1
draft, all of it depth, none of it filler); all 21 units moved `draft` → `revised`.

**E1 — four independent full-book cold reads**, each given one lens and nothing but the
manuscript (no bible, no notes, no cards): pacing/flow · readability/clarity · pull/boredom-map ·
structure/coherence. Every reader graded all 21 units and named three qualities that must not be
damaged. **All four returned the same verdict: polish, no surgery.** Pull averaged 4.6/5 with no
unit below 4; the structural reader independently re-verified the book's calendar and the
plant→payoff closure. Reports kept at `Local/scratch/p2-e1-report-{1..4}-*.md`, triaged into one
worklist (`Local/scratch/p2-e2-worklist.md`) with the two-way calls recorded as D1–D5. → ADR-009

**E2 — line edit, three passes (one per part), ~40 named findings.** The convergent ones first:
the two consecutive monologue-heavy chapters got their long speeches broken into exchanges with
physical beats moved *inside* the sequences; the aphoristic paragraph-ending cadence — flagged
independently by two readers — was thinned book-wide while every chapter-closing beat was left
verbatim; the one passage where the core mechanic forced a re-read gained three sentences of
plumbing *before* its cost line; the book's biggest coincidence was paid for with an earlier
planted trace; the fastest turn in part III gained an on-page price; the densest reveal paragraph
was broken into steps. Six clarity bugs fixed (a referent with no antecedent, an unreadable word,
a surname arriving from nowhere, a pronoun four paragraphs from its owner, an unminted name, an
inconsistent count). Nothing was added to the ledger and no card changed.

**E3 — Czech language pass.** Zero hard calques and zero transgressives (the style guide bans
them); no synonym drift in the mechanism vocabulary; six curly quotes normalised back to the
source convention (typesetting converts them). **E4 — production.** `book/` gained metadata,
dedication and colophon; the cover is generated by `tools/make_cover.py` (Pillow, seeded, no
external assets — the stitch-and-needle-in-paper motif parked in K0). The first real PDF came out
at 139 A5 pages against the ~200-page target, so the type was raised to 11pt/2cm → **178 pages**.
→ ADR-010, ADR-011

**Verification (on the artefacts, not the source).** PDF: 178 pages, all Czech diacritics present,
Czech hyphenation active, table of contents and all three part titles correct, both framing
sentences read back out of the file. EPUB: `cs-CZ`, cover embedded, 22 chapter headings, Czech
text intact; MOBI converted from it under the Kindle profile. `python tools\gate.py` → **GREEN,
0 hard violations** (53 report-only notes, each defended in context or fixed). `--cards` → GREEN.
`--selftest` → GREEN, all 17 checks fired on seeded bad input. Ledger **14/14 paid**.

**Model-fit:** used frontier·high with the four cold reads as sub-agents → fit. The cold reads
were the load-bearing spend: three of the five most valuable fixes came from findings two readers
reached independently, and the "don't damage this" lists prevented an over-eager subtraction pass.
Next time: build the artefacts *early* — the page-count miss was invisible until the first real
PDF, and catching it at E4 nearly turned a typesetting parameter into a prose problem.

## 2026-08-04 — P1 · The whole novel drafted: 21/21 units, ledger 14/14 paid, gate green

**Shipped.** The complete first draft: 15 chapters + 6 interludes, **53,039 words**, every unit
inside its hard band, every chapter opening on its file-header artefact and closing on its
carded out-hook. All 21 files moved `stub` → `draft`.

**Method (unattended chain per `Local/chain-W.md`).** One unit per step: read the card + the
previous chapter + the open ledger rows → draft to the card → run the gate on the file → deepen
in-run if the draft came out skeletal (it consistently did: first passes landed ~40 % under
target and were deepened, never patched) → log new facts to `bible/` in the *same* step → append
a row to `Local/chain-log.md` (the resume point, which survived a mid-run context reset). No
STOP condition fired: the gate never went red twice on one unit, no ledger conflict, no content
question needed the author.

**Ledger.** All five twists fired on their carded chapters (T2 → ch08, T3 → ch10, T1 → ch11,
T4+T5 → ch15). `bible/foreshadowing-ledger.md` is **14/14 planted → paid**, front-matter mirrors
the grid on every file, gate-verified.

**Bible growth.** `invented-canon.md` INV-006 → INV-105 (one row per invented fact, all logged in
the prompt that used them); glossary extended with people, places, document codes and vocative
forms; `characters.md` corrected twice (supporting-cast age, first-cost chapter); `timeline.md`
unchanged — the drafted dates matched the S3 spine, including real 2031 Thursdays.

**Review panels (WP1 · WP2 · WP3), four independent readers each.** Voice · continuity ·
structure/pacing · a *blind* reader-guesser allowed to read nothing but the manuscript. Result:
**21/21 units "fit", zero redrafts**; ~60 findings triaged and fixed in place. Highlights: WP1
tightened prop-planting and removed a leaked line; WP2 caught six continuity contradictions and a
card that had drifted from the prose (card corrected, prose kept); WP3 removed a meta-explanation
that would have burned a twist early, reconciled the heist clock, and closed three softness
findings from the full-book audit. The final blind audit — 21 files, no bible — reported fair-play
"exceptional", the causal structure paradox-free, the ending "tenderness, not kitsch", and
independently verified the book's calendar against real 2031 dates. → ADR-007, ADR-008

**Verification (real runs, end of prompt).** `python tools\gate.py` → **GREEN, 0 hard violations**
(53 report-only notes: deliberate figures and the raw material for the P2 subtraction pass).
`--cards` → GREEN, 0 warnings. `--selftest` → GREEN, all 17 checks fired on seeded bad input.

**Model-fit:** used frontier·high, panels as sub-agents → fit. The per-unit gate + in-run
deepening was the load-bearing habit; the panels earned their cost three times over (every
serious defect came from a reader who had not written the text). Next time: draft the first pass
~50 % longer — the systematic under-shoot cost an extra deepening lap on nearly every unit.

## 2026-08-03 — K0 · Kickoff: premise locked, bible written, tooling green, plan approved

**Premise & story frame.** Ran a multi-agent premise panel: four independent concept authors
(one per angle: deep time / causal architecture / time-as-social-mechanism / expedition-origin)
against a written taste profile, then three independent judges scoring all concepts on
originality, twist craft, readability, emotional core and fit. Three concepts returned; the
causal-architecture concept won on originality and twist architecture and was hardened with
grafts from the runners-up (a cosmological vertical, a physical price for the mechanism, a
document-diff device used exactly twice, and a tender epilogue beat). Full panel output kept at
`Local/scratch/premise-panel-vysledky.json`. Working title *Nedoložení*. → ADR-001, ADR-002

**Bible (single source of truth), all written this prompt.**
- `bible/plot-architecture.md` — premise lock, theme sentence, the ending and its cost, three
  parts → sequences → chapters, five twist dossiers with their fair-play evidence, the
  cosmological vertical, and the reader contract.
- `bible/world-rules.md` — the invented mechanism's laws (LOCKED), its costs, its limits, the
  institution, the society, the spine dates.
- `bible/characters.md` — lead (want / wound / lie / arc), four supporting roles, the interlude
  voice, minor cast.
- `bible/chapter-grid.md` — 15 chapter cards + 6 interlude cards, every field filled
  (goal · friction · turn · out-hook · beats · plants/payoffs · cast · location · register ·
  tier); parts I ch01–05 · II ch06–10 · III ch11–15, frozen; word budget 52,200 + 5,000 = 57,200.
- `bible/foreshadowing-ledger.md` — 14 plant→payoff rows across five twists, each with its
  surface reading and its true reading.
- `bible/style-guide.md` — Czech, binding; POV rules, two voice registers, chapter shape,
  sentence-level rails, the front-matter schema, and §8/§9 (the gate's machine-readable config).
- `bible/timeline.md`, `bible/glossary.md`, `bible/invented-canon.md`.

**Tooling.** `tools/gate.py` adapted from the reference novel for a three-part Czech book:
thresholds re-set (chapters 2,800–4,200 hard / 3,200–3,800 target; interludes 550–1,100),
English-only machinery removed (manner-adverb -ly counting, American spellings, canon lists),
Czech lists wired (banned phrases + calques hard; calque-watch, filter words, said-bookisms,
epithets, overused adverbs report-only), Czech capitals and simile markers, suffix wildcards for
inflected forms, a declension-tolerant glossary lookup, a document-reference check replacing the
reference's site check, timeline reduced to the single POV thread, and `--assemble` interleaving
interludes at their book positions. `book/assemble.yaml` (Czech labels, part titles);
`tools/build.ps1` + `tools/local.ps1` carried over (portable tectonic on D:). → ADR-005

**Scaffold.** `manuscript/part-1..3` — 21 stub files whose front-matter mirrors the grid exactly.

**Verification (real runs, this prompt).** `python tools\gate.py --cards` → GREEN, 0 warnings
(15 chapters + 6 interludes parsed, 3 part titles, budget 57,200). `python tools\gate.py` →
GREEN, 0 warnings on the 21-file scaffold. `python tools\gate.py --selftest` → GREEN, all 17
checks fired on a seeded bad Czech fixture. `--assemble` verified for book order
(ch01, ch02, Fixace I, ch03–05, Fixace II, …), output discarded.

**Planning artefacts.** `Local/all prompts.md` (three author-facing prompts: K0 · P1 write ·
P2 edit & typeset, with tiers and modes), `Local/chain-W.md` (chain procedure + binding STOP
conditions + escalation rule), `Local/Prompts requirements.md` (the prompt standard),
`Local/Wiki/01-kucharka-sveta.md` (the worldbuilding cookbook), `CLAUDE.md`,
`docs/architecture.md`, `.claude/settings.json` (standing rules + commit guard), `.gitignore`.

**Model-fit:** used frontier·high with a multi-agent panel for the premise and a sub-agent for
the tooling port → fit. The panel was the right spend for an irreversible creative decision
(three judges disagreed, and the disagreement itself shaped the grafts); the tooling port was
correctly delegated (mechanical against a known reference, verified by three green runs). Next
time: one of the four concept agents died on output formatting — give the panel a fallback so a
lost angle doesn't silently shrink the field.
