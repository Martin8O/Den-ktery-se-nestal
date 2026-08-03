# dev_history — *Nedoložení*

> Professional changelog of progress + decisions. Newest entries on top. Decision index: `docs/adr.md`.

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
