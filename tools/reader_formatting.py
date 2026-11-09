"""Reviewed semantic boundaries lost when printed columns were reflowed.

Only markup changes: labels/entries below are transcribed from the translated
text and checked against the French page structure. Never infer boundaries from
capitalisation or use typography as a substitute for checking the source.
"""
from html import escape, unescape
import re

# A paragraph starting with prefix has these discrete source headings. A pair
# (label, following text) disambiguates names also mentioned within body prose.
HEADINGS = {
19: [('Equipment', ['Equipment','Mount','Special Rules:', 'Virtue of Knightly Temper','Sense of Honour']),
     ('Magic Items', ['Magic Items', "Maldred's Black Blade (Magic Weapon)",'Cursed Shield of Mousillon (Magic Armour)','Chalice of Malfleur (Arcane Item)'])],
20: [('Equipment',['Equipment','Mount','Magic','Special Rules:','Lord of Death','Vampire of the Blood Dragon lineage']),('Honour or Death',['Honour or Death','No Mortal Son'])],
22: [('The Dead Shall Walk Among the Living:', ['The Dead Shall Walk Among the Living:'])],
26: [('Wildwood Onager:', ['Wildwood Onager:'])],
27: [('Quiverlings The',['Quiverlings'])],
28: [('Wildwood Aspect A',['Wildwood Aspect'])],
29: [('Bittergrub The',['Bittergrub'])],
30: [('Former Duke of Aquitaine',['Former Duke of Aquitaine'])],
31: [('Ghost Blade The',['Ghost Blade']),('Knight, Lord of the Dead The',['Knight, Lord of the Dead']),('Hover The',['Hover']),('White Witch The',['White Witch'])],
34: [('Life Cycle:', ['Life Cycle:','Magic:','Special Rules', "Sylph's Voice:",'Aura of the Fey Queen:','Magic Items','Berry Liqueur (Enchanted Item):','Acorns of Ages (Enchanted Item):']),
     ('The Bolt of Destiny', ['The Bolt of Destiny (Magic Weapon):','White Elm Wand (Arcane Item):','The Heart of Athel Loren (Enchanted Item):','Black Elm Wand (Arcane Item):']),
     ('Earthbind (casting value',['Earthbind (casting value 5+):'])],
36: [('Equipment Scarloc',['Equipment','Special Rules:']), ("Scarloc's Archers:",["Scarloc's Archers:"]),('Command Group:',['Command Group:']),('Storm Witch:',['Storm Witch:']),('Magic Items',['Magic Items']),('Hail of Doom Arrow (Scarloc)',['Hail of Doom Arrow (Scarloc)']),('Darkwood Rune Sword (Scarloc)',['Darkwood Rune Sword (Scarloc)']),('Standard of the Valiant Heart',['Standard of the Valiant Heart (Kaïa Stormwitch)']),('Carynx, the Horn of Beasts',['Carynx, the Horn of Beasts (Araflame Skaldeguerre)'])],
37: [('The Falconer',['The Falconer']),('Special Rules:',['Special Rules:']),('Magic items',['Magic items']),('The Talon Whip Each',['The Talon Whip']),('The Feather Cloak Assembled',['The Feather Cloak']),('Hawks Skaw',['Hawks'])],
38: [('Equipment:',['Equipment:']),('Special Rules:',['Special Rules:']), ("Loren's Bow:",["Loren's Bow:"]),('Bronze Buckler (magical Armour):',['Bronze Buckler (magical Armour):'])],
40: [('Unit size:', ['Unit size:','Equipment','Mount','Options']),('Knight of the Haven',['Knight of the Haven','Grail Vow','Guardians of Haven']),('Aura of the Fay',['Aura of the Fay','Royal Bodyguard'])],
41: [('Errantry War:',['Errantry War:']),('Experienced Leader:',['Experienced Leader:']),('Errantry Fervour:',['Errantry Fervour:']),('Glory or Death:',['Glory or Death:'])],
42: [('Louen de Couronne, the High Paladin',['Louen de Couronne, the High Paladin']),('Louen the Dispossessed, Wandering Paladin',['Louen the Dispossessed, Wandering Paladin'])],
43: [('Equipment:',['Equipment:']),('Mount:',['Mount:']),('The Crown of Bretonnia',['The Crown of Bretonnia (Enchanted Item):']),('The Dolorous Blade',['The Dolorous Blade (Magic Weapon):']),('The Silver Lance',['The Silver Lance of the Blessed (Magic Weapon):']),('Armour of the Green Knight',['Armour of the Green Knight (Magic Armour):']),('Special Rules',['Special Rules']),('Knight of the Haven:',['Knight of the Haven:']),('Grail Vow:',['Grail Vow:']),('Virtue of the Monster Slayer:',['Virtue of the Monster Slayer:']),("Lady's Blessing:",["Lady's Blessing:"]),('Aura of the Fay:',['Aura of the Fay:']),('Beloved King of Bretonnia:',['Beloved King of Bretonnia:'])],
44: [('Equipment Lance',['Equipment']),('Mount Dragmor',['Mount','Special Rules:','Reviled King of Bretonnia']),('Magic Mallobaude',['Magic']),('Magic Items',['Magic Items','The Crown of Bretonnia (Enchanted Item)'])],
48: [('The Briarmaven of Woe:',['The Briarmaven of Woe:']),("Mannfred's Spoils:",["Mannfred's Spoils:"])],
50: [('Flank Battles At',['Flank Battles'])],
51: [('SETUP ',['SETUP']),('FIRST TURN ',['FIRST TURN']),('GAME LENGTH ',['GAME LENGTH']),('VICTORY CONDITIONS ',['VICTORY CONDITIONS']),('SPECIAL RULES',['SPECIAL RULES']),('The Throne is at Stake:',['The Throne is at Stake:']),('Clash of Leaders:',['Clash of Leaders:']),('Central Battle:',['Central Battle:'])],
52: [('Play the paired scenarios',['In the Battle of Maisontaal']),("In Theodoric's Last Charge",["In Theodoric's Last Charge"])],
53: [('Civil War (Vampire Counts).',['The Crypt of Secrets:','Alakanash:'])],
54: [('Duel to the Death:',['Duel to the Death:'])],
55: [('Siege (see Blood in the Badlands).',['The Dead in the Walls:'])],
}

ARMY_STARTS = {
21: {'Lords':['Mallobaude the Black Knight','Bretonnian Lord','Master Sorcerer'],
'Hero':['Paladin','Sorcerers'],'Core Units':['Knight Errants','Knights of the Realm','Peasant Bowmen','Men-at-Arms'],
'Special Units':['Pegasus Knights','Mounted Yeomen','Rogues','Crossbowmen','Handgunners'],
'Rare Units':['Knights of the Black Grail','Trebuchet','Cannon','Bolt Thrower']},
22: {'Lords':['Mallobaude the Vampire Duke','Arkhan the Black','Heinrich Kemmler','The Red Duke','Master Necromancer','Bretonnian Lord','Vampire Duke'],
'Hero':['Krell','The Dark Knight','The Banshee','Wight King','Vampire (VC)','Necromancer','Cairn Wraith','Banshee (VC)','Paladin'],
'Core Units':['Skeleton Warriors','Black Knights','Zombies','Dire Wolves','Knights of the Realm','Peasant Bowmen','Men-at-Arms'],
'Special Units':['Grave Guard','Knights of the Black Grail','Ghouls','Giant Bats','Bat Swarm','Pegasus Knights','Mounted Yeomen','Crossbowmen','Handgunners'],
'Rare Units':['Hexwraiths','Crypt Horrors','Cairn Wraiths','Spirit Host','Terror of the Abyss','Trebuchet','Cannon','Mortar']},
}

def split_at_labels(text, labels):
    out=[];pos=0
    for label in labels:
        idx=text.find(label,pos)
        assert idx>=0,(text[:80],label)
        if idx>pos: out.append(('p',text[pos:idx].strip()))
        out.append(('h3',label));pos=idx+len(label)
    if pos<len(text):out.append(('p',text[pos:].strip()))
    return out


def bullet_markup(text):
    if text.startswith('- Upgrade a Chevalier-Moire'):
        text='• '+text[2:].replace(' - Upgrade',' • Upgrade').replace(' - The unit',' • The unit')
    if '•' not in text:return '<p>'+escape(text)+'</p>'
    first,*items=text.split('•')
    out='<p>'+escape(first.strip())+'</p>' if first.strip() else ''
    items=[i.strip() for i in items if i.strip()]
    if items:out+='<ul>'+''.join('<li>'+escape(i)+'</li>' for i in items)+'</ul>'
    return out


def format_page(content, number):
    # Source p32 wraps Morgiana's footnote into a new paragraph. Rejoin before
    # list conversion so the marker belongs to the correct army choice.
    if number==51:
        labels={label for _, group in HEADINGS[51] for label in group}
        content=re.sub(r'<p><strong>([^<]+)</strong>(.*?)</p>', lambda m: ('<h3>'+m[1]+'</h3>'+('<p>'+m[2].strip()+'</p>' if m[2].strip() else '')) if unescape(m[1]) in labels else m[0],content,flags=re.S)
    if number==43:
        content=re.sub(r'<p><strong>([^<]+)</strong>(.*?)</p>', lambda m: '<h3>'+m[1]+'</h3>'+('<p>'+m[2].strip()+'</p>' if m[2].strip() else ''),content,flags=re.S)
    if number==32:
        content=re.sub(r'Morgiana the Fay</p>\s*<p>\(\*\*\)', 'Morgiana the Fay (**)', content)
    def paragraph(m):
        raw=m[1]
        if '<' in raw:return m[0] # Existing semantic emphasis/links left intact.
        text=unescape(raw).strip()
        for category, starts in ARMY_STARTS.get(number,{}).items():
            if text.startswith(category+' '):
                body=text[len(category):].replace('•','')
                body=re.sub(r'(?<=\s)-(?=\s|$)','',body)
                body=' '.join(body.split())
                indices=[];pos=0
                for name in starts:
                    at=body.find(name,pos);assert at>=0,(number,name)
                    indices.append(at);pos=at+len(name)
                assert indices[0]==0
                entries=[body[a:b].strip() for a,b in zip(indices,indices[1:]+[len(body)])]
                return '<h3>'+category+'</h3><ul>'+''.join('<li>'+escape(x)+'</li>' for x in entries)+'</ul>'
        # Numbered explanatory footnotes must remain attached to their text.
        if number==22 and text.startswith('(1) Mallobaude'):
            parts=re.split(r' (?=\([23]\) )',text)
            return '<div class="army-notes">'+''.join('<p>'+escape(x)+'</p>' for x in parts)+'</div>'
        if number==32 and text.startswith('(*) Including'):
            parts=text.split(' (**) ')
            return '<p>'+escape(parts[0])+'</p><p>(**) '+escape(parts[1])+'</p>'
        for prefix,labels in ([] if number==43 else HEADINGS.get(number,[])):
            if text.startswith(prefix):
                return ''.join('<h3>'+escape(t)+'</h3>' if tag=='h3' else bullet_markup(t) for tag,t in split_at_labels(text,labels))
        # Literal printed bullets are discrete items, not punctuation in prose.
        if '•' in text:
            if number in (28,29) and text.endswith('•'):
                return '<p>'+escape(text[:-1].strip())+'</p>'
            if number==28 and text.startswith('Aspect of Birch:'):
                text=text.replace('a unit of - Dryads','a unit of Dryads')
                options,upgrade=text.split(' If it does not have an Aspect,',1)
                return bullet_markup('• '+options)+'<p>If it does not have an Aspect,'+escape(upgrade)+'</p>'
            if number==29 and text.startswith('Aspect of Birch:'):text='• '+text
            return bullet_markup(text)
        return m[0]
    return re.sub(r'<p>(.*?)</p>',paragraph,content,flags=re.S)
