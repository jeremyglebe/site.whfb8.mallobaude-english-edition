"""Curated layouts for Mallobaude army lists and named character profiles.

Coordinates identify source regions only. Text is always read from rules.html.
"""
from html import escape
import re

TITLES = {19:'Mallobaude the Black Knight',20:'Mallobaude the Vampire Duke',21:'The Rebels of Bretonnia',22:'The Mousillon Army',23:'Arkhan the Black',24:'Black Grail Knights',42:'The Kings of Bretonnia',43:'Gilles le Breton',44:'Mallobaude the Vampire King'}


def profile_table(lines, number, header_y=None, second_y=None):
    from build_rules_reader import style, rows
    # Two actor rows share a unit Type. Wrapped actor names stay in their row.
    if header_y is None:
        header_y, second_y = {19:(193.996,231.556),20:(156.916,194.596),43:(156.916,182.116),44:(408.966,446.526)}[number]
    heads=sorted([n for n in lines if abs(style(n,'top')-header_y)<1],key=lambda n:style(n,'left'))
    assert len(heads)==10,(number,'headers',len(heads))
    centers=[style(n,'left') for n in heads]
    edges=[0,150]+[(a+b)/2 for a,b in zip(centers,centers[1:])]+[600]
    def col(n):
        x=style(n,'left')
        return next(i for i,(a,b) in enumerate(zip(edges,edges[1:])) if a<=x<b)
    body=[n for n in lines if n not in heads]
    def text(ns):
        return escape(' '.join(' '.join(n.text().split()) for _,rr in rows(ns) for n in rr))
    out='<div class="table-scroll profile-scroll" tabindex="0" role="region" aria-label="Character profile"><table class="profile-table"><thead><tr><th scope="col" aria-label="Model"></th>'
    out+=''.join('<th scope="col">'+text([n])+'</th>' for n in heads)+'</tr></thead><tbody>'
    used=list(heads)
    for row in range(2):
        out+='<tr>'
        for column in range(11):
            if column==10 and row==1:continue
            ns=[n for n in body if col(n)==column and (column==10 or (style(n,'top')>=second_y)==bool(row))]
            used+=ns
            tag='th' if column==0 else 'td'
            attrs=' scope="row"' if column==0 else (' rowspan="2"' if column==10 else '')
            out+=f'<{tag}{attrs}>'+text(ns)+f'</{tag}>'
        out+='</tr>'
    assert len(used)==len(lines) and len({id(n) for n in used})==len(lines)
    return out+'</tbody></table></div>'


def render_page(number,page):
    from build_rules_reader import Node, style, prose, semantic
    layer=next(page.find(lambda n:n.has('rules-text')))
    lines=[n for n in layer.children if isinstance(n,Node) and n.has('pdf-line') and style(n,'top')<800]
    sem=[n for n in layer.children if isinstance(n,Node) and n.has('rules-semantic') and not n.has('editorial-page-number')]
    used=[];out=[]
    def region(y0,y1,x0=0,x1=600,table=False):
        ns=[n for n in lines if y0<=style(n,'top')<y1 and x0<=style(n,'left')<x1]
        used.extend(ns)
        out.append(profile_table(ns,number) if table else '<div class="reader-block">'+prose(ns)+'</div>')
    def columns(y0,y1,split=300):
        region(y0,y1,0,split);region(y0,y1,split,600)
    def images():
        for image in page.find(lambda n:n.tag=='img' and not n.has('page-background')):
            out.append(f'<figure><img src="{escape(image.attrs["src"])}" alt="Illustration from source page {number}"></figure>')
    if number in (19,20):
        top,bottom={19:(185,250),20:(150,220)}[number]
        region(0,top);region(top,bottom,table=True)
        columns(bottom,640 if number==20 else 800)
        if number==20:region(640,800)
    elif number==21:
        region(0,100);columns(100,550);columns(550,800)
    elif number==22:
        region(0,100);columns(100,580);region(580,800);images()
    elif number==23:
        # The old bullet positions were not moved when the translated lines
        # rewrapped. Rebuild the five original items from their sentence starts.
        region(0,100);region(100,400)
        body = [n for n in lines if 400 <= style(n,'top') < 800]
        used.extend(body)
        from build_rules_reader import rows
        text = ' '.join(' '.join(n.text().split()) for _, parts in rows(body)
                        for n in parts if n.text().strip() != '•')
        items = re.split(r' (?=Replace his Undead rule|Ignore the Liche High Priest|Arkhan does not count|He has the Master of the Dead)', text)
        assert len(items) == 5, (number, 'Expected five Arkhan rules')
        out.append('<ul>' + ''.join('<li>'+escape(item)+'</li>' for item in items) + '</ul>')
        images()
    elif number==24:
        region(0,100);columns(100,760,290);images();region(760,800)
    elif number==42:
        region(0,150)
        region(150,230);columns(230,400)
        region(400,500);columns(500,700);region(700,800)
    elif number==43:
        region(0,150);region(150,195,table=True)
        out.extend(semantic(n) for n in sorted(sem,key=lambda n:style(n,'left')))
        region(195,800)
    elif number==44:
        region(0,150);columns(150,400)
        region(400,470,table=True);columns(470,800)
    else:raise ValueError(number)
    assert len(used)==len(lines) and len({id(n) for n in used})==len(lines),(number,'Unconsumed/duplicated text')
    return '\n'.join(out)
