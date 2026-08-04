# CLAUDE.md — *Den, který se nestal* (D:\Projekty\Scifi)

Původní česky psaný SF román (~57k slov ≈ 200 stran A5), psaný NATIVNĚ ČESKY, jeden ověřitelný
krok po druhém. **Dělba práce:** veškerá obsahová rozhodnutí (svět, postavy, zvraty, věty) patří
asistentovi; metoda, rozsah a tempo patří autorovi. **Žádné obsahové otázky autorovi; ŽÁDNÉ
SPOILERY v chatu** — zvraty se v konverzaci označují jen ledger id (T1…T5, P-T*-*).

> `Local/` je soukromá, gitignorovaná pracovní zóna (plán, wiki, scratch, stav sezení).

## Přečti nejdřív, každé sezení
1. `Local/bootstrap.md` (aktuální stav, další krok) → pak relevantní `bible/` + `Local/Wiki/`
   sekce pro daný prompt.

## Co to je
- Premisa/struktura/zvraty: `bible/plot-architecture.md` (SPOILERY) · rozhodnutí: `docs/adr.md`.
- Plán: `Local/all prompts.md` (3 autorské prompty: K0 příprava · P1 psaní · P2 redakce+sazba;
  uvnitř řetězy dle `Local/chain-W.md`) · standard promptů: `Local/Prompts requirements.md`.

## Tvrdé zásady
- **Disk C: zakázán** — veškerá perzistence na D: (`Local/scratch/` pro pokusy).
- **Bible-first:** žádný fakt v próze bez domova v `bible/`, zapsán TÝMŽ promptem; jednou
  vynalezené pravidlo je zákon; rukopis nikdy neodporuje bibli.
- **Ledger disciplína:** zvraty/planty/payoffy jen přes `bible/foreshadowing-ledger.md`;
  front-matter `plants:`/`payoffs:` v synchronu (gate kontroluje); po S3 změny jen na WPn.
- **Jazyk:** próza i bible ČESKY (nativně, nikdy přes angličtinu); kód/identifikátory/commity
  anglicky; chat s autorem prostou češtinou bez žargonu.
- **Tvrdé příběhové zábrany (ADR-001):** nikdo necestuje časem (jen informace, Z7) · žádní
  mimozemšťané/stvořitelé · vyprávění nelže (klam jen rámem) · Zapisovatelka nikdy nelže ·
  násilí dle style-guide §3 (18+, bez sexuálního násilí, bez násilí na dětech na stránce) ·
  konec: cena zaplacena, něha bez laciné útěchy (F-VI).
- `Local/` a `data/` se nikdy necommitují; commit jen ve wrap-upu („X je hotové" autorizuje);
  scoped add, žádné slepé `git add -A`. Docs jen ve wrap-upu, nikdy uprostřed promptu.

## Konvence
- Kapitoly: `manuscript/part-N/chNN-slug.md` (fixace `iN-fixace-N.md`), YAML front-matter
  `chapter, part, title, pov, date_in_story, target_words, plants, payoffs, status`.
  Pásma: kapitola cíl 3,2–3,8k / tvrdě 2,8–4,2k slov; fixace 0,7–1,0k / 0,55–1,1k.
- POV: er-forma minulý čas, jedna hlava (Tereza); fixace ich-forma přítomný čas (`pov: none`);
  rejstříky dle `bible/style-guide.md` (závazné; §8 = konfigurace gate).
- Prozaické pokusy → `Local/scratch/`, nikdy commit, nikdy doslovné znovupoužití.

## Příkazy
- Gate: `python tools\gate.py` (zeleně před každým commitem) · `--cards` audit gridu ·
  `--selftest` důkaz, že kontroly koušou · `--assemble F` sestavení knihy.
- Build EPUB/MOBI/A5 PDF: `powershell tools\build.ps1` (tectonic na D:, viz tools/local.ps1).

## Workflow
„Jedeme «X»" → just-in-time upřesnění + plán → provedení s verifikací BĚHEM → „«X» je hotové" →
štíhlý wrap-up (gate, ADR, changelog, bootstrap head ≤5×5, model-fit, scoped commit). Každý další
krok ohlásit s tierem + `▶ Spustit na: <model> · <effort>`. Řetězené běhy: `Local/chain-W.md`
(STOP podmínky závazné). Eskalace prózy: nikdy nezáplatovat slabou kapitolu — redraft výš
(`Local/Prompts requirements.md` §4).
