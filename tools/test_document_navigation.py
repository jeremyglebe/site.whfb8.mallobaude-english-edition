"""Canonical document navigation and content-preservation checks."""
import unittest
from build_rules_reader import DOM, ROOT

class DocumentNavigation(unittest.TestCase):
    def test_guide_contents_all_have_targets(self):
        doc=DOM((ROOT/'guide.html').read_text()).root
        ids={n.attrs['id'] for n in doc.find(lambda n:'id' in n.attrs)}
        rows=[]
        for ul in doc.find(lambda n:n.has('contents-list')):
            rows+=list(ul.find(lambda n:n.tag=='li'))
        self.assertEqual(len(rows),26)
        for row in rows:
            links=list(row.find(lambda n:n.tag=='a'))
            self.assertEqual(len(links),1)
            self.assertIn(links[0].attrs['href'][1:],ids)
        self.assertIn('guide-credits',ids)

    def test_rules_printed_contents_has_links(self):
        doc=DOM((ROOT/'rules.html').read_text()).root
        page=next(doc.find(lambda n:n.attrs.get('id')=='rules-page-03'))
        links=list(page.find(lambda n:n.tag=='a'))
        self.assertGreater(len(links),40)
        ids={n.attrs['id'] for n in doc.find(lambda n:'id' in n.attrs)}
        for link in links:self.assertIn(link.attrs['href'][1:],ids)

if __name__=='__main__':unittest.main()
