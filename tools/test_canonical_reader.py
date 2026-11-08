"""Regressions for the unified screen document's artwork and reading order."""
import unittest
from build_rules_reader import ROOT, DOM, build


class CanonicalLayoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = DOM(build()).root
        cls.source = DOM((ROOT/'tools/source/rules-layout.html.in').read_text(encoding='utf-8')).root

    def page(self, number):
        return next(self.result.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))

    def test_all_original_illustrations_have_responsive_images(self):
        for number in range(1,57):
            source = next(self.source.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
            expected = sorted(n.attrs['src'] for n in source.find(lambda n:n.tag=='img' and not n.has('page-background')))
            actual = sorted(n.attrs['src'] for n in self.page(number).find(lambda n:n.tag=='img'))
            self.assertEqual(expected, actual, number)

    def test_cover_panels_do_not_interleave(self):
        self.assertIn('THE REVOLT OF MALLOBAUDE', next(self.page(1).find(lambda n:n.tag=='h1')).text())
        edition = next(self.page(1).find(lambda n:n.has('cover-edition'))).text()
        self.assertIn('8TH EDITION',edition)
        self.assertNotIn('unofficial',edition)

    def test_back_cover_summary_stays_out_of_narrative(self):
        page = self.page(56)
        summary = next(page.find(lambda n:n.has('cover-summary')))
        self.assertEqual(2,len(list(summary.find(lambda n:n.tag=='li'))))
        paragraphs = [n.text() for n in page.find(lambda n:n.tag=='p')]
        self.assertTrue(any('Yet in the darkness' in p and 'Civil war rages' in p for p in paragraphs))
        self.assertTrue(any('other End Times campaigns' in p for p in paragraphs))

    def test_contents_footer_follows_both_columns(self):
        text = self.page(3).text()
        self.assertLess(text.index('The Siege of Mousillon'),text.index('Document version'))

    def test_arkhan_rules_remain_five_separate_items(self):
        items = list(self.page(23).find(lambda n:n.tag=='li'))
        self.assertEqual(5, len(items))
        self.assertTrue(items[1].text().startswith('Replace his Undead rule'))
        self.assertTrue(items[4].text().startswith('He has the Master of the Dead'))
        self.assertFalse(any('•' in item.text() for item in items))

    def test_no_separate_reader_link(self):
        self.assertFalse(list(self.result.find(lambda n:n.tag=='a' and 'rules-reader.html' in n.attrs.get('href',''))))


if __name__ == '__main__':
    unittest.main()
