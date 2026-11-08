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

Open `index.html` locally or visit the [GitHub Pages site](https://mallobaude.drowsy.games/).

The separate [Lore of Undeath Summons Helper](https://jeremyglebe.com/site.whfb8.undeath-summons-helper/) lives in its own repository. It is linked from the holding page alongside the local End Times 8.5 PDF and spells reference.

Campaign-army rule disclosures combine the translated campaign rules with locally stored definitions from the [WHFB8 Online Rules Index](https://8th.whfb.app/), retaining a source link for each indexed rule. Run `python tools/build_rule_definitions.py` to refresh those definitions.

This is an unofficial, non-commercial fan project. It is not affiliated with or endorsed by Games Workshop. Warhammer and associated names, characters, and imagery remain the property of their respective owners.

## Translated web documents

`guide.html` and `rules.html` are the canonical translated documents. Both are
responsive and retain their original parchment, illustrations and visual identity.
The original French PDFs remain available. `rules-reader.html` is only a legacy
redirect, not a separate version. Wide tables and deployment diagrams scroll
independently where their spatial relationships must be retained.

Rules translation/build input is `tools/source/rules-layout.html.in`. Its curated
text regions are reflowed by `tools/reader_*.py`; the same input also preserves
print typesetting in the canonical document. After editing the input, run:

```sh
python tools/build_rules_reader.py
python tools/build_rules_reader.py --check
python -m unittest discover -s tools -p 'test*reader*.py'
```

Do not edit the generated `rules.html` directly. Verify source-word parity,
reading order, artwork, tables and print output after changes. Translation must
follow the French source; source errors and proposed corrections belong in the
editorial ledger, not silent alterations to the translated rules.
