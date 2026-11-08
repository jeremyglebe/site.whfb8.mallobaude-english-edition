#!/usr/bin/env python3
"""Build the curated, reflowing rules chapters from rules.html (stdlib only).

Not a generic PDF text flattener: only reviewed page regions are enabled.
Run with --check in CI to detect a stale reader after translation edits.
"""
from dataclasses import dataclass, field
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import argparse
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    def has(self, name):
        return name in self.attrs.get('class', '').split()

    def text(self):
        return ''.join(c.text() if isinstance(c, Node) else c for c in self.children)

    def find(self, predicate):
        for c in self.children:
            if isinstance(c, Node):
                if predicate(c):
                    yield c
                yield from c.find(predicate)

    def html(self, clean=False):
        attrs = self.attrs.copy()
        if clean:
            attrs.pop('style', None)
        content = ''.join(c.html(clean) if isinstance(c, Node) else escape(c) for c in self.children)
        attr_text = ''.join(f' {k}="{escape(v or "", quote=True)}"' for k, v in attrs.items())
        return f'<{self.tag}{attr_text}>' + ('' if self.tag in VOID else content + f'</{self.tag}>')

class DOM(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.stack = [self.root]
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def style(node, key, default=0):
    m = re.search(r'(?:^|;)\s*' + re.escape(key) + r':\s*([\d.-]+)', node.attrs.get('style', ''))
    return float(m[1]) if m else default


def inner(node):
    return ''.join(c.html(True) if isinstance(c, Node) else escape(c) for c in node.children)


def semantic(node):
    if node.has('editorial-title'):
        return '<h2>' + inner(node) + '</h2>'
    if node.has('civil-table'):
        rows = list(node.find(lambda n: n.has('civil-row')))
        heading = next(node.find(lambda n: n.has('civil-heading')))
        cells = [c for c in heading.children if isinstance(c, Node)]
        output = '<div class="table-scroll"><table><thead><tr>' + ''.join('<th scope="col">' + inner(c) + '</th>' for c in cells) + '</tr></thead><tbody>'
        for row in rows:
            roll = next(row.find(lambda n: n.has('civil-roll')))
            entry = next(row.find(lambda n: n.has('civil-entry')))
            output += '<tr><th scope="row">' + inner(roll) + '</th><td>' + inner(entry) + '</td></tr>'
        return output + '</tbody></table></div>'
    return '<div class="reader-block">' + inner(node) + '</div>'


def rows(lines):
    """Rejoin fragments on one physical baseline within ONE curated column."""
    result = []
    for line in sorted(lines, key=lambda n: (style(n, 'top'), style(n, 'left'))):
        y = style(line, 'top')
        if not result or abs(result[-1][0] - y) > 0.7:
            result.append([y, []])
        result[-1][1].append(line)
    for _, parts in result:
        parts.sort(key=lambda n: style(n, 'left'))
    return result


def prose(lines):
    output, paragraph, last_y = [], [], None
    def flush():
        if paragraph:
            text = ' '.join(paragraph)
            labels = r'(ARMIES|SETUP|FIRST TURN|DURATION OF THE GAME|SPECIAL RULES|VICTORY CONDITIONS|CONDITIONS OF VICTORY|MULTIPLE BATTLE)'
            pieces = re.split(r'\b' + labels + r'\b', text)
            for i, piece in enumerate(pieces):
                if not piece.strip():
                    continue
                output.append(('<h3>' + piece + '</h3>') if i % 2 else ('<p>' + piece.strip() + '</p>'))
            paragraph.clear()
    for y, parts in rows(lines):
        text = ' '.join(' '.join(n.text().split()) for n in parts)
        spans = [s for n in parts for s in n.find(lambda x: x.tag == 'span')]
        heading = bool(spans) and max(style(s, 'font-size') for s in spans) >= 14
        if heading:
            flush()
            output.append('<h2>' + escape(text) + '</h2>')
        else:
            if last_y is not None and y-last_y > 16:
                flush()
            paragraph.append(escape(text))
        last_y = y
    flush()
    return '\n'.join(output)


def diagram(page, lines, page_number):
    """Keep spatial diagram relationships intact rather than flattening labels."""
    svg = next(page.find(lambda n: n.tag == 'svg' and n.has('page-vectors')))
    # Both deployment diagrams occupy the bottom portion of the original page.
    output = f'<figure class="deployment"><figcaption>Deployment diagram, source page {page_number}. Scroll horizontally to inspect on a narrow screen.</figcaption><div class="diagram-scroll" tabindex="0" role="region" aria-label="Deployment diagram for page {page_number}"><svg xmlns="http://www.w3.org/2000/svg" viewBox="55 430 490 350" role="img" aria-label="Deployment diagram from source page {page_number}">'
    output += ''.join(c.html() if isinstance(c, Node) else escape(c) for c in svg.children)
    for line in lines:
        for span in line.find(lambda n: n.tag == 'span'):
            x = style(line,'left')+style(span,'left')
            y = style(line,'top')+style(span,'top')+style(span,'font-size',8)
            rotation = f' transform="rotate(-90 {style(line,"left")} {style(line,"top")})"' if line.has('vertical-up') else ''
            output += f'<text x="{x}" y="{y}"{rotation} font-size="{style(span,"font-size",8)}" font-family="Georgia, serif">{escape(span.text())}</text>'
    return output + '</svg></div></figure>'


TITLES = {4:'Introduction and credits',5:'How to use this supplement',6:'Campaign and Bretonnian rules',7:'Civil War',8:'Civil War rules',9:'Bretonnian Civil War table',10:'Vampire Counts Civil War table',11:"Victor’s rewards",45:'Daemonic Assault on Mousillon',46:'Daemonic Assault: rules and deployment',47:'The Battle of Châlons',48:'Châlons: rules and deployment',49:'The Battle of Quenelles',50:'Quenelles: On the Flanks',51:'Quenelles: Father and Son',52:'Attack on La Maisontaal',53:'Duel of Necromancers',54:'The Battle of Couronne',55:'The Siege of Mousillon'}


import sys
# Renderer helpers must share the same Node type for both CLI and imported use.
if __name__ == "__main__":
    sys.modules["build_rules_reader"] = sys.modules[__name__]
import reader_dukes, reader_profiles, reader_armies
RENDERERS = {n: module.render_page for module in (reader_dukes, reader_profiles, reader_armies) for n in module.TITLES}
TITLES.update({n: title for module in (reader_dukes, reader_profiles, reader_armies) for n, title in module.TITLES.items()})
TITLES = dict(sorted(TITLES.items()))

# Verified sentence continuations split by source columns or PDF line spacing.
# Match exact boundary words so future translation changes require review.
PARAGRAPH_JOINS = {
    23: [('lieutenant to', 'Mallobaude.')],
    24: [('leave them and', 'their souls remain'), ('edition; army book', 'Vampire Counts')],
    29: [("the character's", 'WS, Initiative')],
    33: [('to shine with', 'inner glow'), ('website update for', 'Games Workshop')],
    34: [('Wounds are distributed', 'as if they had'), ('She has', 'Magic Resistance'), ('its caster must', 'immediately pass')],
    35: [('It is even claimed that', 'small bands')],
    37: [('Update on the site', 'Games Workshop')],
    39: [('(according to', 'the outcomes')],
    44: [('Vampire Counts Army Book 8', 'edition, page 41)')],
}


def join_reviewed_paragraphs(content, number):
    for end, start in PARAGRAPH_JOINS.get(number, []):
        boundary = re.escape(escape(end)) + r'</p>\s*(?:</div>\s*<div class="reader-block">\s*)?<p>' + re.escape(escape(start))
        content, count = re.subn(boundary, lambda _: escape(end) + ' ' + escape(start), content)
        assert count == 1, (number, 'Review paragraph continuation', end, start)
    return content


def build():
    source = (ROOT/'rules.html').read_text(encoding='utf-8')
    root = DOM(source).root
    pages = {int(n.attrs['data-source-page']): n for n in root.find(lambda n: n.has('rules-page'))}
    sections = []
    for number, title in TITLES.items():
        page = pages[number]
        text_layer = next(page.find(lambda n:n.has('rules-text')))
        blocks = [n for n in text_layer.children if isinstance(n,Node)]
        content = ''
        if number in RENDERERS:
            content = RENDERERS[number](number, page)
        elif number <= 11:
            # These pages explicitly hide the older PDF-line layer in rules.css.
            nodes = [n for n in blocks if n.has('rules-semantic') and not n.has('editorial-page-number')]
            assert nodes, f'Missing semantic source on page {number}'
            content = '\n'.join(semantic(n) for n in nodes)
        else:
            lines = [n for n in blocks if n.has('pdf-line') and style(n,'top')<800]
            semantics = [n for n in blocks if n.has('rules-semantic') and not n.has('editorial-page-number')]
            consumed = []
            if number == 51:
                content = prose(lines)+'\n'+'\n'.join(semantic(n) for n in semantics)
                consumed = lines
            elif number in (46,48):
                body = [n for n in lines if style(n,'top')<400]
                # p48 uses 3 equal columns; p46 has two wider columns.
                bounds = [0,225,380,600] if number == 48 else [0,300,600]
                for start,end in zip(bounds,bounds[1:]):
                    region = [n for n in body if start<=style(n,'left')<end]
                    content += prose(region)
                    consumed += region
                labels = [n for n in lines if style(n,'top')>=400]
                content += diagram(page, labels, number)
                consumed += labels
            else:
                start_y = 190 if number == 45 else (145 if number == 50 else 100)
                headers = [n for n in lines if style(n,'top')<start_y]
                content += prose(headers)
                consumed += headers
                for start,end in [(0,195),(195,370),(370,600)]:
                    region = [n for n in lines if style(n,'top')>=start_y and start<=style(n,'left')<end]
                    content += '<div class="reader-block">'+prose(region)+'</div>'
                    consumed += region
                for image in page.find(lambda n:n.tag=='img' and not n.has('page-background')):
                    content += f'<figure><img src="{escape(image.attrs["src"])}" alt="Illustration from source page {number}"></figure>'
            assert len(consumed)==len(lines) and len({id(n) for n in consumed})==len(lines), f'Unassigned or duplicated text on page {number}'
        content = join_reviewed_paragraphs(content, number)
        sections.append(f'<section class="reader-page" id="rules-page-{number:02}" data-source-page="{number}" aria-label="{escape(title)}"><header class="page-source"><span>Source page {number}</span><a href="rules.html#rules-page-{number:02}">Original page layout</a></header>{content}</section>')
    links = ''.join(f'<li><a href="#rules-page-{n:02}">{escape(title)} <span>p. {n}</span></a></li>' for n,title in TITLES.items())
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mallobaude — Rules reading view</title><meta name="source-sha256" content="{hashlib.sha256(source.encode()).hexdigest()}">
<link rel="stylesheet" href="styles/common.css"><link rel="stylesheet" href="styles/rules-reader.css"></head>
<body class="reader"><nav class="site-bar" aria-label="Site"><a href="index.html">Project home</a><a href="guide.html">Game Guide</a><a href="rules.html">Complete rules book</a><a href="#contents">Contents</a></nav>
<main class="reader-shell"><header class="reader-intro"><p class="kicker">The Revolt of Mallobaude</p><h1>Rules reading view</h1><p>Reflowing campaign rules and scenarios, generated from the current English translation. This reading view covers the book’s body text on pages 4–55, including character profiles, army lists, campaign rules and scenarios. Covers and front/back matter remain in the <a href="rules.html">complete rules book</a>.</p><p>For the original page design or printing, use the complete rules book. Deployment diagrams retain their spatial layout.</p></header>
<nav id="contents" class="reader-contents" aria-label="Reading view contents"><h2>Contents</h2><ol>{links}</ol></nav>
{''.join(sections)}</main></body></html>'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args = parser.parse_args()
    result = build()
    destination = ROOT/'rules-reader.html'
    if args.check:
        if not destination.exists() or destination.read_text(encoding='utf-8')!=result:
            raise SystemExit('Reading view is stale: run python tools/build_rules_reader.py')
        print('Reading view matches rules.html; all curated text regions assigned once.')
    else:
        destination.write_text(result, encoding='utf-8', newline='\n')
        print(f'Built {destination.name}: {len(TITLES)} source pages')
