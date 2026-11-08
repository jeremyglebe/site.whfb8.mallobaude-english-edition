"""Standalone guards for curated duke/rebel-vow pages before integration."""
import unittest
from collections import Counter
import re
from build_rules_reader import ROOT, DOM, style
from reader_dukes import render_page, TITLES

class DukeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = DOM((ROOT/'rules.html').read_text(encoding='utf-8')).root

    def test_exact_source_words_and_unique_consumption(self):
        for number in TITLES:
            page = next(self.root.find(lambda n:n.attrs.get('id') == f'rules-page-{number:02}'))
            source = ' '.join(n.text() for n in page.find(lambda n:n.has('pdf-line') and style(n,'top')<800))
            result = re.sub(r'<[^>]*>', ' ', render_page(number,page))
            from html import unescape
            result = unescape(result)
            words = lambda s:Counter(re.findall(r"[\w]+(?:['’][\w]+)*",s))
            self.assertEqual(words(source),words(result), number)

    def test_first_duke_finishes_before_second_starts(self):
        endings = {12:('choose his other options.', 'Duke Adalhard'),13:('base-to-base contact loses an Attack.', 'Duke Alberic'),14:('Ambush special rule.', 'Duke Bohemond'),15:("Lady's Blessing.", 'Duke Folcard'),16:('from an aquatic terrain feature.', 'Duke Cassyon'),17:('You may choose his other options.', 'Duke Theodoric')}
        for number,(ending,start) in endings.items():
            page = next(self.root.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
            result = DOM(render_page(number,page)).root.text()
            self.assertLess(result.index(ending),result.index(start),number)

if __name__=='__main__': unittest.main()
