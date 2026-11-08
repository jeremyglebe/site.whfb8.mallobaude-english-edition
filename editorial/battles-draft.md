# Battles: initial consolidated draft

Working branch: `draft/battles-section`. Not published or linked from the main navigation yet.

## Scope

- `battles/index.html`: initial section landing page.
- `battles/year-of-woe.html`: one consolidated battle, narrative → forces → setup → rules → scoring → campaign outcome.
- `styles/battles.css`: responsive parchment/art presentation, not a fixed print-page reproduction.

The faithful guide and rules translations are untouched. This is a clearly labeled editorial consolidation, requested by Jeremy as a new section. No End Times continuation is invented. No hex-map mechanism is imported from the separate hypothetical Lustria follow-up.

## Sources checked

French Guide v1.8 p. 12 and Rules v1.5 pp. 45–46 and 11, extracted directly from repository PDFs and compared with the corrected translation. The deployment SVG comes from the corrected English page 46. The first battle is fan-authored, with official background credited by the guide, not an official GW scenario.

Lustria format context recovered from ChatGPT conversation 69c65486-21ac-8329-b436-675f9380a402, messages 426aedfe-2959-42da-b225-ac88759c574a and nearby: independent scenario/defense HTML, with procedures and rules together. The original attached HTML was not recovered, so this draft adopts its practical organization rather than claiming to duplicate its visual layout.

The `site.whfb8.end-of-times` repository was read for its source-research structure. Its research indexes are not substitutes for verified original rule text. No official scenario has yet been ported into this initial section.

## Still needed before calling the first battle self-contained

- Integrate verified Multiplayer Battle and No One Can Be Trusted mechanics from Triumph & Treachery.
- Integrate verified Chaos Ascendant: Tzeentch from Glottkin.
- Integrate the referenced Blood in the Badlands fortress mechanics if fortress use remains supported.
- Decide how to present (not silently repair) the optional-fortress versus compulsory-war-machine-placement contradiction.
- Review whether the general winner's reward is additional to the four Ancient Relic outcome in this optional prelude. The French guide only specifies four relic rewards; this draft adds no extra reward on its own authority.
- Collate required character profiles or deliberate inline disclosures, since this initial draft still links Mallobaude's profile and relies on army books.
- Visual/browser QA on phone and desktop, plus integration with the canonical-document redesign currently being completed in a separate workspace.

## Editing policy

Use explicit source labels. Historical victory must not be written as the forced game result. Actual outcomes determine the next step. Keep uncertain survival/continuity questions visible rather than inventing a resurrection rule. Point-budget example is labeled as an arithmetic example, not a recommended battle size.

## Verification performed

- All local links/anchors and image paths checked.
- Required mechanical numbers and all three scoring rows checked against French.
- No duplicate HTML IDs.
- `git diff --check` clean.
- No runtime or visual-browser QA yet; do not publish based solely on these checks.

## Follow-up: Châlons

Added `battles/chalons.html`, directly compared with French Guide15 / Rules47–48, with arrival path checked against Guide13 and next-stage dependencies against16. Source-compared common and Bretonnian Civil War tables are embedded from corrected translation. Character profiles, Wildwood list, generic Pitched Battle scoring and full reward choices still need consolidation. The section explicitly shows that Stage2 intervenes; no false direct Year of Woe→Châlons branch.

Source-only detail: arrival at maximum3 inches vs abduction/return at less than3 inches is retained rather than silently flattened to one inclusive radius.

## Verification command

Run `python tools/check_battles.py` from repository root to validate draft navigation, anchors, local assets and unique IDs. This does not replace visual or rules review.

## Follow-up: The Revolt

Added `battles/revolt.html` to avoid omitting Stage2 between the prologue and Châlons. It gathers context, target-selection sequence, army requirements, the initial duke roster and corruption outcomes, and eligible Common/Bretonnia rewards (Mousillon rewards omitted as expressly prohibited at this stage). Core Pitched Battle procedure still pending verification. New local links/IDs pass.

## Verified official procedures integrated (8 November)

Read-only PC source audit completed in task `01a1bd71-4ab1-7392-bbd6-fe04a5d7c021`. It visually verified original owned scans: T&T PDF5–6/printed16–17; Glottkin BookII PDF13–14/printed12–13 and PDF21/printed20; Blood in Badlands PDF92–94/printed89–91; Core PDF160–162/printed142–144 plus official v1.8 update PDF2 and6. Original files remain private; draft contains procedural summaries, not copied PDFs.

Year of Woe now includes multiplayer phases/turns, Chaos Ascendant and referenced fortress rules. The Revolt includes explicitly labeled Battleline interpretation; both Revolt and Châlons include corrected100-VP victory threshold. Earlier pending-source bullets above are superseded by this entry. Army profiles still rely on links/books. No broad T&T or Badlands extra modules imported. Summoning restriction, absent fortress, enemy-held open gate and Châlons side-change VP ambiguities remain visible rather than silently resolved.

## Repeat visual QA

PC headless Chromium verified all four pages at1440px and390px, 46 cross-page links, images, anchors, phone tables and diagram panning. All mechanical fixes passed; no additional checked rules discrepancies. Final small corrections: duke names now block-level with entry spacing; optional-fortress note moved from SVG into caption to avoid touching tower; Revolt status badge corrected. Source ambiguities and army-profile dependencies remain. Suitable for private draft review; not deployed.

## Publication integration

The first three entries are published incrementally as a consolidated working campaign, with unresolved source interpretations and linked army profiles explicitly marked. Added navigation from the homepage, guide and canonical rules. Integrated onto main after ED-026 without modifying existing translations. Earlier pending-source and private-review-only notes are historical checkpoints, superseded by the completed source/QA passes above and this publication decision.
