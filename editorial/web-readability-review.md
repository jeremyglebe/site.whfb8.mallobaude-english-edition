# Web readability review — 8 November 2026

## Scope

The guide's screen presentation now reflows independently of its print layout. Text and translations are unchanged by the screen CSS. Narrow screens use single-column stages, chronology, rosters and sidebars; screen prose is enlarged with more line spacing. Previously absolutely positioned notes now flow after their associated text instead of colliding with it. Navigation links have sufficient contrast against the dark bar and wrap on phones.

## Visual QA

Background local Chromium QA was performed in a disposable copy on Jeremy-PC, against the final translation snapshot for this batch.

- Guide: all 36 pages checked at 390px and 1440px. No measured overflow, clipping, overlapping panels or broken images. Representative stage and chronology screenshots inspected.
- Guide print: all 36 A4 pages pixel-identical to the final translated HTML rendered with original print CSS. This compares CSS effects, not translation changes against the old text.
- Rules: targeted final audit of pages 2, 3, 26, 29, 34, 37, 40, 43, 46, 50, 52 and 56. Layout repairs needed on 3, 26, 29, 34, 37, 40, 50, 52 and 56. Final targeted audit reports no clipping/collisions and 56 A4 output pages.
- QA evidence retained at `C:\Users\jerem\Documents\Codex\2026-11-08\task\mallobaude-visual-qa\output\playwright\translation-final`.

## Limits

The complete rules book retains its fixed-position page reconstruction. A separate generated reading view now reflows pages 4–11 and 45–55; character profiles and army lists remain in the original layout. Do not apply the guide’s reflow CSS blindly to those pages. Selected rules pages were visually validated, not every page or every rule. This does not certify whole-book translation accuracy. No commit, push or deployment performed by QA.

## Rules reading view (incremental)

`rules-reader.html` is generated from `rules.html`, not a second translation source. The first curated pass covers campaign rules and scenarios (19 source pages). Original page anchors and return links are retained; the Civil War table uses semantic row/column headers, and deployment diagrams retain spatial SVG coordinates in independently scrollable regions. Original print styling is unchanged.

Run `python tools/build_rules_reader.py` after changing source translations, then `python tools/test_rules_reader.py`. Seven tests check current generation, per-page source-word parity, unique anchors and internal links, table structure, and spatial diagrams. The builder also asserts each enabled positioned fragment is consumed exactly once. These checks do not alone certify reading order; curated columns and visual QA are necessary.

Background Chromium QA checked all 19 sections at 390px and 1440px: no measured clipping, overlaps, broken images, or whole-page overflow; curated column order checked against original pages. Both deployment diagrams scroll independently. Fixed the page 46 vertical label rotation, two scenario section headings, the page 10 contents label, and explicit UTF-8 handling on Windows. All 56 original print pages remain pixel-identical after adding the reading-view navigation link.

Evidence: `C:\Users\jerem\Documents\Codex\2026-11-08\task\mallobaude-visual-qa\output\playwright\reader-final` includes metrics, screenshots, original page comparisons, verification and PDF. Browser coverage is Chromium only. Page 7's decorative illustration is not reproduced in the reader; its credit remains and original layout is linked. The reader is not complete coverage of the 56-page book. No deployment has been performed.

## Body-page extension

The reader now includes pages 12–44 through curated biography, profile and army-list renderers (`tools/reader_dukes.py`, `tools/reader_profiles.py`, `tools/reader_armies.py`), bringing coverage to body pages 4–55. Profile statistics use scoped column/row headers and shared type cells where appropriate; wide tables scroll independently. Eighteen tests pass, including exact source-word parity, biography order and stat-value association. Background Chromium QA checked all 52 sections at 390px and 1440px with no unintended page overflow or clipping, and visually compared all 33 added pages against their original layouts. All nine profile tables retain correct stat/header alignment, wrapped labels and isolated mobile scrolling; all 12 illustrations on newly covered pages are retained. QA fixes address five overflowing dot-leader headings, 13 false paragraph breaks across nine pages, and page 39 caption-fragment order. All 56 original print pages retain identical MediaBoxes and pixel-identical rendering at 72 DPI. Evidence is in the PC QA `output/playwright/expanded-final` directory. Coverage remains Chromium only; French fidelity is a separate review. Original source HTML remains unchanged by this extension.
