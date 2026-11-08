"""Curated regions for army and allied-character source pages 25–41.

Every boundary is page-specific. In particular the whole-width introductions,
stacked units and profile tables must never be treated as ordinary columns.
"""
from html import escape
import re

TITLES = {
25:'Traitors and unreliable allies: Wildwood Host',26:'Treemen and Coeddil',
27:'Ancient Treekin and Kurnoth Hunters',28:'Dryads and Spirit Dryads',
29:'Branchwraiths, Branchwyches and Spite-Revenants',30:'The Red Duke',
31:'The Dark Knight and the Banshee',32:'The Alliance Against Undeath',
33:'Ariel, Queen of Athel Loren',34:'Ariel: profile and rules',35:"Scarloc’s Archers",
36:'Scarloc: profile and rules',37:'Skaw the Falconer',38:'Sceolan the Old',
39:'After the campaign: Chevaliers-Moires',40:'Chevaliers-Moires: profile and rules',41:'Crusade Army',
}

# (low y, high y, column split); None means full-width region. Reading order is
# top region first, then left column followed by right column within each band.
REGIONS = {
25:[(0,290,None),(290,700,300),(700,800,None)],
26:[(0,100,None),(100,290,300),(290,800,None)],
27:[(0,210,None),(210,800,300)],
28:[(0,100,None),(100,250,300),(250,280,None),(280,800,300)],
29:[(0,100,None),(100,260,300),(260,290,None),(290,570,300),(570,800,None)],
30:[(0,100,None),(100,800,300)],
31:[(0,100,None),(100,410,300),(410,435,None),(435,650,300),(650,800,None)],
32:[(0,160,None),(160,650,300),(650,800,None)],
33:[(0,100,None),(100,800,300)],
34:[(0,135,None),(175,800,300)],
35:[(0,100,None),(100,800,300)],
36:[(0,130,None),(175,800,300)],
37:[(0,100,None),(100,300,300),(300,375,None),(420,435,None),(435,800,300)],
38:[(0,260,None),(300,800,300)],
39:[(0,220,None),(220,700,300),(700,800,None)],
40:[(0,130,None),(175,800,300)],
41:[(0,100,None),(100,800,300)],
}
TABLES = {34:(135,175,140.6,[153.4]),36:(130,175,134.6,[147.4]),
37:(375,420,382.9,[395.7]),38:(260,300,265.9,[283.8]),
40:(130,175,133.6,[146.6,159.0])}


def table(lines, number):
    from build_rules_reader import style, rows
    low,high,heading_y,row_ys=TABLES[number]
    headers=sorted([n for n in lines if abs(style(n,'top')-heading_y)<1],key=lambda n:style(n,'left'))
    assert [' '.join(n.text().split()) for n in headers]==['M','WS','BS','S','T','W','I','A','Ld','Type'],number
    xs=[style(n,'left') for n in headers]
    # Columns centred on printed stat headings; first name column is wider.
    cuts=[(76+xs[0])/2]+[(a+b)/2 for a,b in zip(xs,xs[1:])]
    cells=[[[] for _ in range(11)] for y in row_ys]
    for n in lines:
        if n in headers: continue
        x,y=style(n,'left'),style(n,'top')
        col=sum(x>=cut for cut in cuts)
        row=min(range(len(row_ys)),key=lambda i:abs(y-row_ys[i]))
        if number==40 and col==10: row=0 # Cavalry is a shared mount/model type.
        cells[row][col].append(n)
    def content(nodes):
        return escape(' '.join(' '.join(n.text().split()) for n in sorted(nodes,key=lambda n:(style(n,'top'),style(n,'left')))))
    out='<div class="table-scroll profile-scroll" tabindex="0"><table class="profile-table"><thead><tr><th scope="col" aria-label="Model"></th>'
    out+=''.join('<th scope="col">'+content([n])+'</th>' for n in headers)+'</tr></thead><tbody>'
    for i,row in enumerate(cells):
        out+='<tr>'
        for col,nodes in enumerate(row):
            if number==40 and i==1 and col==10:continue
            tag='th' if col==0 else 'td'
            attr=' scope="row"' if col==0 else (' rowspan="2"' if number==40 and col==10 else '')
            out+=f'<{tag}{attr}>'+content(nodes)+f'</{tag}>'
        out+='</tr>'
    return out+'</tbody></table></div>'


def render_prose(lines):
    from build_rules_reader import prose,rows,style
    # These army-list labels are separate physical rows, not words guessed
    # inside narrative prose. Preserve the source's repeated Special Units.
    out=[];pending=[]
    for y,parts in rows(lines):
        text=' '.join(' '.join(n.text().split()) for n in parts)
        title = any(style(span,'font-size') >= 13 for part in parts for span in part.find(lambda n:n.tag=='span'))
        if title or text in ('Lords','Hero','Core Units','Special Units','Rare Units'):
            out.append(prose(pending));pending=[]
            tag='h2' if title else 'h3'
            leader = re.fullmatch(r'(.+?) (\.{3,}) (.+)', text) if title else None
            if leader:
                name, dots, cost = leader.groups()
                out.append('<h2 class="profile-heading"><span>'+escape(name)+'</span> '
                           '<span class="profile-leader" aria-hidden="true">'+dots+'</span> '
                           '<span class="profile-cost">'+escape(cost)+'</span></h2>')
            else:
                out.append(f'<{tag}>'+escape(text)+f'</{tag}>')
        else:pending.extend(parts)
    out.append(prose(pending))
    return '\n'.join(out)


def render_page(number,page):
    from build_rules_reader import Node,style
    layer=next(page.find(lambda n:n.has('rules-text')))
    lines=[n for n in layer.children if isinstance(n,Node) and n.has('pdf-line') and style(n,'top')<800]
    semantic=[n for n in layer.children if isinstance(n,Node) and n.has('rules-semantic') and not n.has('editorial-page-number')]
    assert not semantic, f'Page {number} acquired semantic replacement: update curated reader'
    out=[];consumed=[]
    bands=[(lo,hi,split,'prose') for lo,hi,split in REGIONS[number]]
    if number in TABLES:
        lo,hi,*_=TABLES[number];bands.append((lo,hi,None,'table'))
    for lo,hi,split,kind in sorted(bands):
        region=[n for n in lines if lo<=style(n,'top')<hi]
        consumed.extend(region)
        if kind=='table':out.append(table(region,number));continue
        cols=[region] if split is None else [[n for n in region if style(n,'left')<split],[n for n in region if style(n,'left')>=split]]
        for col in cols:
            if col:out.append('<div class="reader-block">'+render_prose(col)+'</div>')
    assert len(consumed)==len(lines) and len({id(n) for n in consumed})==len(lines),f'Unassigned or duplicated fragments page {number}'
    for image in page.find(lambda n:n.tag=='img' and not n.has('page-background')):
        out.append('<figure><img src="'+escape(image.attrs['src'],quote=True)+'" alt="'+escape(image.attrs.get('alt') or f'Illustration from source page {number}',quote=True)+'"></figure>')
    return '\n'.join(out)
