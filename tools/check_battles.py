from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
class P(HTMLParser):
 def __init__(self,s): super().__init__();self.ids=[];self.links=[];self.feed(s)
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  for attr in ('href','src'):
   if attr in a:self.links.append(a[attr])
for f in Path('battles').glob('*.html'):
 p=P(f.read_text());assert len(p.ids)==len(set(p.ids)),f
 for l in p.links:
  u=urlparse(l)
  if u.scheme:continue
  dest=(f.parent/unquote(u.path)).resolve() if u.path else f.resolve()
  assert dest.exists(),(f,l)
  if u.fragment and dest.suffix=='.html':assert u.fragment in P(dest.read_text()).ids,(f,l)
 print(f,'links and IDs pass')
