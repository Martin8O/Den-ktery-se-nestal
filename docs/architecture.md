# Architecture — how this book is built

An original Czech-language science-fiction novel (53,393 words ≈ 178 A5 pages), written natively
in Czech, one verifiable slice at a time. The method externalises the story's structure into
checkable artefacts so every step is locally correct and the book stays globally consistent.

> Reader-facing overview, statistics and method summary: `README.md`. This file is the working
> reference for anyone (human or agent) editing the repo.

## Repo layout

- `bible/` — the single source of truth for every fact of the world and the story:
  `world-rules.md` (the invented world's mechanics, LOCKED) · `characters.md` ·
  `plot-architecture.md` (parts → sequences → chapters, theme, twist dossiers) ·
  `chapter-grid.md` (one card per chapter — the drafting contract) ·
  `style-guide.md` (binding voice + language rules; its §8 lists ARE the gate's config) ·
  `foreshadowing-ledger.md` (every plant bound to its payoff) ·
  `invented-canon.md` (running log of every invented fact) · `timeline.md` · `glossary.md`.
- `manuscript/part-N/chNN-slug.md` — chapters with YAML front-matter
  (`chapter, part, title, pov, date_in_story, target_words, plants, payoffs, status`).
- `tools/gate.py` — one-command quality gate (stdlib only): front-matter schema, card mirror,
  word bands, banned lists (parsed from the style guide at run time), ledger cross-check,
  timeline, glossary, scaffold completeness. `--cards` audits the grid; `--selftest` proves every
  check fires; `--assemble` concatenates the book for the build.
- `tools/build.ps1` — EPUB + MOBI + A5 PDF via pandoc / Calibre / tectonic (`book/` carries
  front/back matter, metadata, cover).
- `tools/make_cover.py` — the cover, generated from code (Pillow, seeded RNG, no external
  assets); the title block auto-fits the clear column beside the seam.
- `docs/` — this file · `adr.md` (decision index).
- `Local/` — private, gitignored working area (plan, wiki, scratch, session state). Not published:
  it holds the prompt plan, the chain log and throwaway prose probes.

## The three invariants

1. **Bible-first** — no fact appears in prose without a home in `bible/`, logged in the same
   prompt that writes it. Once invented, a rule is law.
2. **Ledger discipline** — every setup (twist, planted object, promise) has a ledger row binding
   plant-chapter to payoff-chapter; chapter front-matter mirrors it; the gate cross-checks.
   Twists are designed before drafting, never bolted on.
3. **Gate green before anything is kept** — the gate runs inside every writing prompt;
   under-delivery is deepened in-run, never shipped.

## Fair play

Every twist must pass four tests: planted on the page before the reveal · present but not
telegraphed · derived by work shown on the page · recoverable by a careful blind reader.
Per-part review panels (voice / continuity / structure / blind twist audit) enforce this.
