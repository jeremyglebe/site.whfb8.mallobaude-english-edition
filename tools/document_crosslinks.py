"""Reviewed internal references, not a blanket auto-linker for book page numbers.

External army-book page numbers and known erroneous source references remain
unlinked rather than misleadingly pointing at a page of this supplement.
"""
from html import escape
import re

# Only these local page references have been checked in their source context.
LOCAL_PAGES = {
    19: [18], 20: [18], 21: [18], 22: [18], 24: [18], 44: [18],
    45: [19], 47: [19, 12, 25], 50: [33], 51: [13], 52: [17],
}
GUIDE_TERMS = {
    'Daemonic Assault in Mousillon*': 'rules.html#rules-page-45',
    "Victor's Rewards*": 'rules.html#rules-page-11',
    "Victor's Reward*": 'rules.html#rules-page-11',
    'Ancient Relic*': 'rules.html#rules-page-11',
    'Bretonnian Rebels*': 'rules.html#rules-page-21',
    'Mallobaude the Black Knight*': 'rules.html#rules-page-19',
    'Mallobaude the Black Knight': 'rules.html#rules-page-19',
    'Mallobaude, Vampire Duke of Mousillon*': 'rules.html#rules-page-20',
    'Mousillon Army*': 'rules.html#rules-page-22',
    'Civil War (Bretonnia)*': 'rules.html#rules-page-08',
    'Civil War*': 'rules.html#rules-page-07',
    'Louen the High Paladin*': 'rules.html#rules-page-42',
    'Mallobaude, Vampire King of Bretonnia*': 'rules.html#rules-page-44',
    '3. The Battle of Châlons': '#stage-3',
    '5. The Conquest': '#stage-5',
    '7. The Road to Couronne': '#stage-7',
}


def link_text_nodes(html, replacements):
    """Keep original markup verbatim, touching eligible prose text only.

    Don't nest anchors, touch SVG diagrams, scripts, heading/navigation labels,
    or rewrite any text. Repeated runs are idempotent.
    """
    if not replacements:
        return html
    pattern = re.compile('|'.join(re.escape(k) for k in sorted(replacements, key=len, reverse=True)))
    blocked = []
    out = []
    for part in re.split(r'(<[^>]*>)', html):
        if part.startswith('<'):
            m = re.match(r'</?([a-zA-Z][\w:-]*)', part)
            if m:
                tag = m[1].lower()
                if tag in {'a','script','style','svg','nav','h1','h2','h3','h4','h5','h6'}:
                    if part.startswith('</'):
                        if tag in blocked: blocked.remove(tag)
                    elif not part.endswith('/>'): blocked.append(tag)
            out.append(part)
        elif blocked:
            out.append(part)
        else:
            out.append(pattern.sub(lambda m: '<a class="cross-reference" href="'+escape(replacements[m[0]],quote=True)+'">'+m[0]+'</a>', part))
    return ''.join(out)


def rules_links(content, page):
    replacements = {}
    for target in LOCAL_PAGES.get(page, []):
        for prefix in ('see page ', 'See page ', 'on page '):
            replacements[prefix+str(target)] = f'#rules-page-{target:02}'
    # Named companion references are identifiable, unlike external book names.
    if page in (5, 6, 56):
        replacements['Game Guide'] = 'guide.html#guide-page-11'
    if page == 39:
        replacements['Conclusions of the Game Guide'] = 'guide.html#conclusion-1'
    if page == 50:
        replacements['Battle of Quenelles rules'] = '#rules-page-49'
    return link_text_nodes(content, replacements)


def guide_links(html):
    # Guide source is semantic HTML; existing navigation stays untouched.
    parts = re.split(r'(?=<article\b)', html)
    output = [parts[0]]
    for part in parts[1:]:
        id_match = re.search(r'\bid="([^"]+)"', part.split('>',1)[0])
        own = '#'+id_match[1] if id_match else ''
        refs = {k:v for k,v in GUIDE_TERMS.items() if v != own}
        if own in {'#stage-2','#stage-4','#stage-5','#stage-7'}:
            refs.update({'See page 14':'#guide-page-14','page 14':'#guide-page-14'})
        output.append(link_text_nodes(part, refs))
    return ''.join(output)

if __name__ == '__main__':
    from pathlib import Path
    path=Path(__file__).resolve().parents[1]/'guide.html'
    path.write_text(guide_links(path.read_text(encoding='utf-8')),encoding='utf-8')
