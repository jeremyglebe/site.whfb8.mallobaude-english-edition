# The Revolt of Mallobaude - English Edition

An English-language reconstruction of the unofficial Warhammer Fantasy Battles 8th Edition supplement *The Revolt of Mallobaude*.

The repository contains two static, browser-readable books and a campaign army reference:

- `guide.html` - campaign and game guide
- `rules.html` - rules, army lists, characters, and scenarios
- `armies/index.html` - searchable roster cards for all five campaign armies, including outcome-dependent post-campaign entries
- `downloads/revolt-of-mallobaude-french-game-guide-v1.8.pdf` - preserved original French campaign guide
- `downloads/revolt-of-mallobaude-french-rules-v1.5.pdf` - preserved original French rules book
- `downloads/WHFB-End-Times-8.5.pdf` - preserved complete End Times 8.5 fan supplement
- `other-end-times-content.html` - a holding page for related End Times material that has not yet moved to its own site

Open `index.html` locally or visit the [GitHub Pages site](https://jeremyglebe.com/site.whfb8.mallobaude-english-edition/).

The separate [Lore of Undeath Summons Helper](https://jeremyglebe.com/site.whfb8.undeath-summons-helper/) lives in its own repository. It is linked from the holding page alongside the local End Times 8.5 PDF and spells reference.

Campaign-army rule disclosures combine the translated campaign rules with locally stored definitions from the [WHFB8 Online Rules Index](https://8th.whfb.app/), retaining a source link for each indexed rule. Run `python tools/build_rule_definitions.py` to refresh those definitions.

This is an unofficial, non-commercial fan project. It is not affiliated with or endorsed by Games Workshop. Warhammer and associated names, characters, and imagery remain the property of their respective owners.

## Reflowing rules chapters

`rules-reader.html` is a generated, mobile-friendly reading view for the campaign
rules, characters, profiles, army lists and scenarios (body pages 4–55).
The complete reconstructed book remains authoritative, with covers/front and back
matter and the original print layout. Wide stat tables and deployment diagrams
scroll independently on narrow screens while prose reflows.

After editing `rules.html`, run:

```sh
python tools/build_rules_reader.py
python tools/build_rules_reader.py --check
python -m unittest discover -s tools -p 'test*reader*.py'
```

The builder uses Python's standard library. It reuses existing semantic blocks
and explicitly curated page regions in `tools/reader_*.py`, rather than guessing
reading order across the entire book. It preserves the civil-war tables as tables and
the deployment diagrams as spatial SVGs. Add new pages only after reviewing their
reading order, tables and diagrams against the original layout. Do not edit the
generated reader directly or use a generic CSS flattening of positioned text.
