import unittest
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.ids=[];self.links=[];self.feed(path.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
class FourPersonTests(unittest.TestCase):
 def test_links_and_unique_ids(self):
  file=ROOT/'battles/four-person.html';p=Page(file)
  self.assertEqual(len(p.ids),len(set(p.ids)))
  for link in p.links:
   u=urlsplit(link)
   if u.scheme or u.netloc:continue
   target=(file.parent/unquote(u.path)).resolve() if u.path else file
   self.assertTrue(target.is_file(),link)
   if u.fragment:self.assertIn(unquote(u.fragment),Page(target).ids,link)
 def test_each_assignment_has_four_roles(self):
  s=(ROOT/'battles/four-person.html').read_text()
  self.assertEqual(s.count('class="battle-card assignment"'),13)
  for role in ['Bretonnia','Mousillon','Asrai','Arkhan']:
   self.assertEqual(s.count('<dt>'+role+'</dt>'),13)
 def test_house_rules_and_guest_rewards_explicit(self):
  s=(ROOT/'battles/four-person.html').read_text()
  for text in ['Suggested house rule.','none of Arkhan’s collected items or rewards','does not make Arkhan himself legal','alternative routes','One personal victory']:
   self.assertIn(text,s)
 def test_index_discoverability(self):
  self.assertIn('href="four-person.html"',(ROOT/'battles/index.html').read_text())
if __name__=='__main__':unittest.main()
