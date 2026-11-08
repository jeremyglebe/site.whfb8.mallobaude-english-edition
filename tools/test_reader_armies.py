"""Regression guards for the curated allied armies/profile reader regions."""
import unittest
from build_rules_reader import ROOT, DOM, Node, style
from reader_armies import TITLES, render_page
from test_rules_reader import words, reading_text

class ArmyReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=DOM((ROOT/'rules.html').read_text(encoding='utf-8')).root
        cls.pages={int(p.attrs['data-source-page']):p for p in root.find(lambda n:n.has('rules-page'))}
    def rendered(self,number):
        return DOM(render_page(number,self.pages[number])).root
    def test_all_source_words_preserved(self):
        for number in TITLES:
            with self.subTest(page=number):
                layer=next(self.pages[number].find(lambda n:n.has('rules-text')))
                source=' '.join(reading_text(n) for n in layer.children if isinstance(n,Node) and n.has('pdf-line') and style(n,'top')<800)
                self.assertEqual(words(source),words(reading_text(self.rendered(number))))
    def test_stat_column_mapping(self):
        expected={34:['Ariel','5','4','4','4','4','4','9','2','10'],36:['Scarloc','5','6','6','4','3','2','7','3','9'],37:['Skaw','5','6','6','4','3','2','7','3','9'],38:['Sceolan','5','6','6','4','3','2','7','3','9'],40:['Chevalier-Moire','4','5','3','4','4','1','5','2','9']}
        for number,values in expected.items():
            with self.subTest(page=number):
                tbody=next(self.rendered(number).find(lambda n:n.tag=='tbody'))
                row=next(tbody.find(lambda n:n.tag=='tr'))
                cells=[n.text() for n in row.children if isinstance(n,Node)]
                self.assertEqual(cells[:10],values)
                self.assertTrue(next(row.find(lambda n:n.tag=='th')).attrs.get('scope')=='row')
    def test_shared_cavalry_type(self):
        table=next(self.rendered(40).find(lambda n:n.tag=='table'))
        shared=next(table.find(lambda n:n.attrs.get('rowspan')=='2'))
        self.assertEqual(shared.text(),'Cavalry')
    def test_stacked_unit_narratives_do_not_interleave(self):
        text=reading_text(self.rendered(31))
        self.assertLess(text.index('Ghost Blade'),text.index('THE BANSHEE'))
        self.assertLess(text.index('THE BANSHEE'),text.index('White Witch'))
        text=reading_text(self.rendered(29))
        self.assertLess(text.index('Bittergrub'),text.index('BRANCHWYCH'))
        self.assertLess(text.index('level 2 wizard'),text.index('SPITE-REVENANTS'))
    def test_repeated_source_special_units_heading_preserved(self):
        headings=[n.text() for n in self.rendered(32).find(lambda n:n.tag=='h3')]
        self.assertEqual(headings.count('Special Units'),2)
    def test_ariel_description_keeps_continuation_order(self):
        text=' '.join(reading_text(self.rendered(33)).split())
        self.assertIn('to shine with inner glow',text)

if __name__=='__main__':unittest.main()
