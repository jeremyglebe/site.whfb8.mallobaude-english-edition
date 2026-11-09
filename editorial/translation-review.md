# French-source translation review

## 8 November 2026: campaign flow and scenarios

Source editions: French Game Guide v1.8 and French Rules v1.5 in `downloads/`.

### Coverage

- Compared Guide pages **8–34** with the French text, including all twelve stages, their branches, army restrictions, campaign consequences, three endings and chronology. This is a text-fidelity pass, not a full typographic or canonical-source audit.
- Compared Rules pages **45–55**, covering every scenario, with the French text. Also inspected page 44 while checking the transition into the scenario section.
- Visually inspected the French page 46 deployment diagram to verify that the disputed fortress annotation was not a text-extraction artefact.
- Existing editorial decisions ED-001–017 remain in force. No campaign choices, alternate endings, points or profiles were redesigned.
- Guide pages 1–7 and 35–36 and Rules pages 1–43 and 56 have **not** received this new comparison. Their pre-existing translation/review status is unchanged.

### Corrections in this pass

See ED-018–022 in `decisions.html` for the individual rationale:

- Rules p46: restore the optional-fortress note; remove the invented instruction to deploy the entire Bretonnian force inside.
- Guide p30: restore the explicit End Times-long prohibition on reusing executed or banished renegade Dukes.
- Rules p52: make clear that the monastery houses the crypt Arkhan seeks, rather than saying he protects it.
- Guide p12: restore approximately ten blessed lances rather than a dozen.
- Guide p28: restore the absence of an heir as the cause of the succession dispute.
- Rules p50: remove duplicated wording in the reinforcement recommendation.

### Source questions retained, not silently corrected

- **Guide p32, Servant of Nagash:** one bullet addresses Kemmler having been killed, but a later bullet says Kemmler flees if Arkhan was not killed, without an explicit surviving-Kemmler condition. The English preserves the source; do not invent a resurrection or a new branch. Clarification remains queued.
- **Guide pp25/27 versus Rules pp54/55:** the Guide calls the campaign a draw if both central protagonists survive, while the scenarios can still choose a battle winner on victory points or siege conditions. Both wordings are present in French. Distinguish battle victory from campaign conclusion and seek an editorial ruling before changing either.
- **Rules p44:** references to Vampire Counts army-book pp40–41 accompany Mallobaude's campaign equipment/rules, and the crown narrative gives 2522 despite the Guide's 2523 coronation. These are inherited source issues, not evidence of an English mistranslation; their intended references/date remain unverified.
- **Rules p53:** “Anneau de Feu Maudit” remains the literal “Ring of Cursed Fire” pending confirmation of the intended English item identity. Do not substitute a similarly named item without evidence.

### Verification limits

`git diff --check` and HTML parse/structure assertions pass. No project build/test command exists in this static repository. Headless Chromium could not launch in the executor because its process-singleton socket was denied (`Operation not permitted`), including the approved escalation attempt. Final rendered-page layout therefore remains to be checked; source PDF inspection is not a substitute for that check. These edits have not been committed, pushed or deployed.

## Second comparison: remaining pages

Compared Guide pp1–7/35–36 and Rules pp1–43/56 against the French. This completes text comparison coverage, **not correction completion or rendered-page sign-off**.

Implemented the following additional corrections:
- Guide pp5/6/36: images were not scanned from print; first King terminology; explicit absence of profiles/scenarios and requirement for companion rules.
- Rules pp2/3/56: restore omitted legal/art credits, latest-changes note, and back-cover descriptions/companion-book requirement. These newly wrapped blocks require visual QA.
- Rules pp6/8/10/11: Break tests rather than all Leadership tests; optional transformation recovery; captured rather than killed standards; Undead limitation; slaying rather than defeating a challenge opponent; optional item roll; free Blood Knights; minor rather than young noble.
- Rules pp14–19: false-friend about power, Greenskin infestation ownership, aquatic terrain feature restriction, Lady's adversaries, keep rather than dungeon, Bretonnian army eligibility.
- Rules pp24/26/27: unspecified save restored rather than the previous ward-only interpretation; Coeddil's Treeman Ancient baseline; distinct Treekin unit-champion baseline; great weapon terminology.
- Rules pp34/36/37/43: Creative Cycle restriction on White Elm Wand; Dark Magic; Steadfast/disrupt terminology; Forest Strider restored instead of Feather Cloak; Crown immunity narrowed to source's Panic only; omitted Silver Lance flavour restored.

### Remaining verified corrections to implement

Rules pp12–27: Duke's children took after him (p14); mourners rather than mourned (p15); free Pennon (p24); Coeddil's jealousy (p26); virtue/spell names and lingering names/grammar, including Knights of the Realm, disrupted, Master Strike, source-key D/N, dangling “There”.

Rules pp28–43: Bittergrub close-combat restriction (p29); Banshee pronoun and march moves (p31); forest misdirection (p33); spell cast against Ariel and Loremaster duplicate (p34); Bronze Buckler wording (p38); Chevaliers-Moires heading (p39); canonical Regrowth and Urannon's Thunderbolt (p40); show off rather than “roll mechanics” (p41); Gilles orders rather than commands the crusades (p42).

### Additional source-error / interpretation register

- Rules p24: French says successful “save”, not expressly “ward save”. ED-012's ward-only interpretation is now separate from the translation, which again preserves the ambiguity.
- Rules p22: source calls Vampire King Conclusion II, although it is III; preserve source and identify correction separately.
- Rules p21: existing English silently fixes Black Grail page23 reference to24. This remains **pending separation**, not a faithful source-reference translation yet.
- Rules p20: source equipment reference p40 appears wrong (equipment actually p19); do not silently repair.
- Rules p22/p24: all Blood Knights upgraded versus only one unit eligible is a French conflict; do not reconcile silently.
- Rules p32: source's last category repeats “Special Units”, while English silently substitutes Rare Units. This remains **pending separation**.
- Rules p43: Crown date2522 preserved despite Guide chronology difference.
- Rules p22: Terreur des Abysses/Abîmes identity unresolved; no substitution guessed.
- Rules p27: Quiverlings' Multiple Attacks (1D3) is in French; not silently changed to Multiple Shots.


## Third implementation pass

Implemented the queued meaning corrections on Rules pp12–42: children take after Duke; mourners mourn him; Pennon explicitly free; Coeddil's jealousy; Bittergrub close-combat restriction; Banshee pronoun and march moves; forest misdirection; spell cast against Ariel; duplicated Loremaster “of”; Bronze Buckler; Chevaliers-Moires; Regrowth/Urannon's Thunderbolt; show off; crusades raised at Gilles's command. Also repaired Adalhard/of Lyonesse, Knights of the Realm, disrupted, Master Strike and Dwarf roster key. Canonical virtue names and remaining low-impact copy edits still require a final terminology pass.

The two previously silent source corrections have now been separated: Rules p21 again prints source's page23 reference (the corrected reference is24); p32 again prints source's repeated Special Units category (the apparent intended correction is Rare Units). These corrections are documented here rather than substituted silently in the translation. This supersedes the earlier “pending separation” status above.

Layout QA remains pending for positioned text, particularly longer restored phrases and front/back matter. The source comparison covers all pages, but this is not a claim of exhaustive canonical terminology or independently verified army-book content. No deployment performed.


## Final terminology and independent checks

Independent rereads confirm the patched mechanics on pp24/26/27/29/34/37/43: Pennon cost, unspecified save, baseline units, great weapons, Bittergrub restriction, Creative Cycle, Forest Strider and Panic-only immunity. Caught and removed a duplicated “He has” at Coeddil's line continuation. Restored the legendary-founder introduction for Gilles. ED-012 now explicitly identifies itself as superseded for literal translation.

Regrowth is verified by matching V8 spell5, casting12+/15+, ranges24/48 and D3+1 restored Wounds between French https://assets.9thbuilder.com/fr/ninth_age/magic_paths/39 and English https://8th.whfb.app/spell/regrowth . Both army data/reference occurrences now use Regrowth too. No mechanical values changed in those files. Knightly Temper follows existing army definitions. Remaining terminology uncertainty: Virtue of Care / Vertu de Sollicitude mapping to Empathy pending independently checked army-book wording.


Virtue of Empathy subsequently verified and applied: https://whfb.lexicanum.com/wiki/Martrud cites Bretonnia6e p59; https://bibliotheque-imperiale.com/index.php/Les_Vertus_Chevaleresques identifies the same Martrud virtue as Vertu de Sollicitude. This resolves the immediately preceding terminology uncertainty. Identified correction queue is now implemented. Visual rendering and broader consistency of pre-existing army-reference mechanics remain outside completed verification.


## Crown wording clarification (Jeremy's request)

Rules p43 now states: “A unit with line of sight to the King automatically passes any Panic tests it is required to take.” This makes the existing Panic-only protection explicit without inventing a named special rule. The separate 18-inch Leadership benefit remains unchanged. Recorded as ED-026; no broader Immune to Psychology benefit is introduced.


## 9 November: final reader source artifacts

Checked French pp26/37/39: restored sentence stop after misfire; removed duplicated English “These” at column continuation; restored The Falconer ability heading (French Le Fauconnier) and Skaw as its sentence subject instead of duplicating the Special Rules summary; closed the Guide-reference parenthesis. These are English transcription/formatting artifacts, not corrections to the original rules. Updated authoritative tools/source/rules-layout.html.in and regenerated the reader.
