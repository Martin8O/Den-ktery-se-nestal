# Den, který se nestal

**A finished Czech science-fiction novel — and the entire machine that produced it.**

This repository holds a complete 53,000-word original novel written natively in Czech, together
with the worldbuilding bible it was written against, the foreshadowing ledger that binds every
setup to its payoff, the one-command quality gate that had to pass before any page was kept, and
the build pipeline that turns the manuscript into an EPUB, a MOBI and a 178-page A5 PDF.

The prose and the story bible are Czech. Everything engineered around them — code, repo docs,
commit messages — is English; `CLAUDE.md` is Czech because it is written for the author.

> ### ⚠️ Spoilers
> `bible/` is the story's design document. `plot-architecture.md`, `foreshadowing-ledger.md` and
> `invented-canon.md` contain **every twist, in full, with its mechanism**. If you intend to read
> the book, read `manuscript/` (or a built file) and stay out of `bible/`.

---

## The book

A verifier at the Institute of Retrospection measures what the past can prove. Her job rests on a
single doctrine: *one person's memory weighs nothing*. Then a case crosses her desk in which the
only thing that disagrees with the record is a memory of her own.

Bureaucratic SF: no time travel, no aliens, no chosen one. The horror is administrative and the
tenderness is earned. Rated 18+ — violence is brief, consequential and never sexual; the worst
things in the book happen inside forms.

| | |
|---|---|
| **Length** | 53,470 words · 178 pages (A5) |
| **Shape** | 3 parts × 7 units = 15 chapters + 6 first-person interludes |
| **Chapter band** | 2,800–4,200 words hard, 3,200–3,800 target — every unit inside it |
| **POV** | Close third, past tense, one head; interludes are first person, present tense |
| **Twists** | 5, tracked across 14 plant → payoff rows, all paid |
| **Invented facts** | 105 canon entries, every one logged in the prompt that first used it |
| **Bible** | 13,860 words across 9 documents |
| **Formats** | EPUB · MOBI · A5 PDF, built by one command |
| **Written in** | 2 days · 3 author-facing prompts, plus one later editing pass |

## How it was made

The book was written by an AI agent (Claude Code) under a method the author designed and drove.
The division of labour was fixed on day one and never moved: **every content decision — world,
characters, twists, sentences — belonged to the model. Every method, scope and pace decision
belonged to the author.** The author read no spoilers during production; twists were discussed in
chat only by ledger id.

The whole novel ran on **three author-facing prompts** — with one more editing pass added after
the repository was published:

| Prompt | What it did |
|---|---|
| **K0 · Kickoff** | Multi-agent premise panel (4 independent concepts × 3 independent judges), then the full bible: world rules, characters, plot architecture, a 21-card chapter grid, the foreshadowing ledger, the Czech style guide. Quality gate ported and proved. Manuscript scaffolded as 21 stub files. |
| **P1 · Write** | All 21 units, one per step, unattended. Each step: read the card + the previous chapter + the open ledger rows → draft to the card → run the gate → deepen in-run if thin → log new facts to the bible in the *same* step. A four-reader review panel after each part. |
| **P2 · Edit & typeset** | Four independent blind full-book cold reads, a three-pass line edit, a Czech language pass, cover and typesetting, final verification. |
| **E6 · De-mannerism** | A blind audit asked one question — *does this read machine-written?* — and answered it with counts, not impressions. Its findings were applied wherever they made the book read better. No artificial flaws: camouflage was rejected as a goal. |

### The chain

P1 and P2 ran as **unattended chains**: the agent kept going, unit after unit, without asking,
until either the work was done or a written STOP condition fired — gate red twice on one unit, a
ledger conflict, a part boundary reached, or a content decision that genuinely needed the author.
None of them ever fired. A `Local/chain-log.md` line per step doubled as the resume point, and it
earned its keep: it survived a mid-run context reset without losing a step.

### Review, not self-assessment

Sixteen independent reading passes were run by agents that had never written the text:

- **P1 — three panels, four readers each.** Voice · continuity against the bible · structure and
  pacing · a *blind* reader-guesser, allowed to read nothing but the manuscript, whose job was to
  guess the twists early and score fair play.
- **P2 — four blind full-book cold reads.** Flow · readability · pull (a chapter-by-chapter
  boredom map) · structure. Each reader also named three things that must not be damaged in the
  edit; those lists were treated as binding.

Result: 21/21 units passed on the first draft, zero chapters redrafted, ~60 findings fixed in P1
and ~40 in P2. The convergent findings — the ones two readers reached independently without
talking — turned out to be the valuable ones every single time.

### Escalation, not patching

A weak chapter was never patched. The rule was: if a review says a unit is not a fit, re-run the
whole prompt at a higher effort level, keeping its card, its plants and its bible entries, and
throw the prose away. It never had to be used — but knowing it existed is what kept "good enough"
from being an option.

## Architecture

### Three invariants

1. **Bible-first.** No fact reaches the prose without a home in `bible/`, written in the same step
   that used it. Once invented, a rule is law. The manuscript never contradicts the bible.
2. **Ledger discipline.** Every setup is a row in `foreshadowing-ledger.md` binding a plant
   chapter to a payoff chapter, with its surface reading and its true reading. Chapter
   front-matter mirrors those ids and the gate cross-checks both directions: no plant without a
   payoff, no payoff without a plant.
3. **Green before kept.** The gate runs inside every writing step. A draft that comes out thin is
   deepened in-run, never shipped and never patched later.

### Fair play

Every twist had to pass four tests before it was allowed to exist: **planted on the page** before
the reveal · **present but not telegraphed** · **derived by work shown on the page** · and
**recoverable by a careful blind reader**. The last one is not a matter of opinion here — a blind
agent that had read only the manuscript was asked to guess, and its guesses were scored.

### Repo layout

```
bible/          the single source of truth  (SPOILERS)
  world-rules.md          the invented mechanics, LOCKED after K0
  characters.md           want / wound / lie / arc per character
  plot-architecture.md    parts → sequences → chapters, theme, twist dossiers
  chapter-grid.md         21 cards: goal · friction · turn · out-hook · beats · plants
  style-guide.md          binding voice + language rules; §8 IS the gate's config
  foreshadowing-ledger.md every plant bound to its payoff
  invented-canon.md       running log of all 105 invented facts
  timeline.md  glossary.md

manuscript/part-N/        the prose; YAML front-matter mirrors the grid
tools/gate.py             the quality gate (1,167 lines, stdlib only)
tools/build.ps1           EPUB + MOBI + A5 PDF
tools/make_cover.py       the cover, generated (Pillow, seeded, reproducible)
book/                     front matter, colophon, metadata, cover
docs/adr.md               decision index — 14 records, the "why" of the project
docs/architecture.md      method notes
dev_history.md            a professional changelog, newest first
```

## The quality gate

```bash
python tools/gate.py            # full run over manuscript/ against bible/
python tools/gate.py --cards    # audit the chapter grid itself
python tools/gate.py --selftest # prove every check fires on seeded bad input
python tools/gate.py --assemble out.md
```

Seventeen checks, standard library only, no dependencies. Among them:

- **Front-matter schema** — nine keys, right order, right types, on every file.
- **Card mirror** — title, date and the `plants:`/`payoffs:` lists must match the grid exactly.
  The grid is the contract; prose that drifts from its card fails.
- **Word bands** — hard bands fail, target bands warn.
- **Banned phrases and calques** — hard failures. Clichés and translationese from English.
- **Register lists** — filter verbs, said-bookisms, epithets, overused adverbs, simile density:
  report-only, but every report must be defended in context or fixed.
- **Ledger cross-check** — plants and payoffs reconciled in both directions.
- **Timeline** — front-matter dates against `timeline.md`; the POV thread must be strictly
  increasing; book order monotonic.
- **Glossary** — a repeated capitalised term must exist in the glossary, with a
  declension-tolerant lookup so Czech inflection doesn't produce false alarms.

Two details that make it more than a linter:

**The style guide is parsed at run time.** The banned lists live in `bible/style-guide.md` §8, not
in the Python. Extending the guide extends the gate, with no code change — the writing rules and
the enforcement can never drift apart.

**`--selftest` proves the checks bite.** It seeds a deliberately broken copy of the manuscript and
asserts that all seventeen checks fire on it. A green gate means nothing if the checks are asleep;
this is how you know they aren't.

## Build it

```bash
python tools/gate.py
```

```powershell
powershell tools\build.ps1
```

Needs `python` (assembly), `pandoc` (EPUB/PDF), `ebook-convert` from Calibre (MOBI) and any LaTeX
engine for the PDF — `tectonic` is the light option. Machine-specific engine paths belong in
`tools/local.ps1`, which is gitignored. `powershell tools\build.ps1 -Check` reports what's
missing without building anything.

## What transfers

The novel is the artefact; the method is the point. Four things did the heavy lifting and none of
them are specific to this book, this language or this genre:

1. **Externalise structure into checkable artefacts.** A grid card is a contract, a ledger row is
   an obligation, and both are machine-verifiable. Long-form coherence stops depending on anyone
   remembering chapter 3 while writing chapter 14.
2. **Make the writing rules executable.** A style guide nobody enforces is a wish. One that a gate
   parses at run time is a constraint.
3. **Separate writing from judging.** Every serious defect found in this project was found by an
   agent that had not written the text. Self-review found almost nothing.
4. **Prove your checks fire.** `--selftest` was the cheapest and most valuable thing in the repo.

## Licence

The manuscript, the bible and the cover are © 2026 the author. All rights reserved — no
reproduction, distribution or derivative works without permission.

The tooling in `tools/` is published so the method can be read and copied. If you want to reuse it
in your own project, open an issue and ask; the answer will almost certainly be yes.
