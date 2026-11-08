"""Guards for curated army/profile reader regions, independent of integration."""
import unittest
from build_rules_reader import DOM,ROOT,Node,style
from reader_profiles import TITLES,render_page
from test_rules_reader import words,reading_text

class ProfileReaderTests(unittest.TestCase):
    def test_source_word_parity(self):
        root=DOM((ROOT/'tools/source/rules-layout.html.in').read_text(encoding='utf-8')).root
        for number in TITLES:
            with self.subTest(page=number):
                page=next(root.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
                layer=next(page.find(lambda n:n.has('rules-text')))
                nodes=[n for n in layer.children if isinstance(n,Node) and ((n.has('pdf-line') and style(n,'top')<800) or (n.has('rules-semantic') and not n.has('editorial-page-number')))]
                actual=DOM(render_page(number,page)).root
                self.assertEqual(words(reading_text(actual)),words(' '.join(reading_text(n) for n in nodes)))
                if number in (19,20,43,44):
                    table=next(actual.find(lambda n:n.tag=='table'))
                    self.assertEqual(len(list(table.find(lambda n:n.tag=='th' and n.attrs.get('scope')=='col'))),11)
                    self.assertEqual(len(list(table.find(lambda n:n.tag=='th' and n.attrs.get('scope')=='row'))),2)
                    shared=next(table.find(lambda n:n.attrs.get('rowspan')=='2'))
                    self.assertIn('special character',shared.text())
                    self.assertEqual(len(list(table.find(lambda n:n.tag=='tr'))),3)

if __name__=='__main__':unittest.main()
