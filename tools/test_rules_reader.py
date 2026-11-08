#!/usr/bin/env python3
"""Content and structure guards for the partial semantic rules reader."""
import re
import unittest
from collections import Counter
from build_rules_reader import ROOT, DOM, TITLES, build, style


def reading_text(node):
    return " ".join(reading_text(c) if hasattr(c,"children") else c for c in node.children)

def words(text):
    return Counter(re.findall(r"[\w]+(?:['’][\w]+)*", text))

class ReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = DOM((ROOT/'tools/source/rules-layout.html.in').read_text(encoding='utf-8')).root
        cls.result = DOM(build()).root

    def test_generated_file_is_current(self):
        self.assertEqual((ROOT/'rules.html').read_text(encoding='utf-8'), build())

    def test_every_enabled_page_preserves_all_source_words(self):
        for number in TITLES:
            with self.subTest(page=number):
                original = next(self.source.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
                text_layer = next(original.find(lambda n:n.has('rules-text')))
                if number in (1,2,3,56):
                    nodes=[n for n in text_layer.children if hasattr(n,"has") and n.has("pdf-line")]
                elif number<=11:
                    nodes=[n for n in text_layer.children if hasattr(n,'has') and n.has('rules-semantic') and not n.has('editorial-page-number')]
                else:
                    nodes=[n for n in text_layer.children if hasattr(n,'has') and ((n.has('pdf-line') and style(n,'top')<800) or (n.has('rules-semantic') and not n.has('editorial-page-number')))]
                expected=words(' '.join(reading_text(n) for n in nodes))
                actual=next(self.result.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
                for n in actual.find(lambda n:n.has('page-source') or n.tag=='figcaption'):
                    n.children=[]
                self.assertEqual(expected, words(reading_text(actual)))

    def test_source_page_ids_unique_and_deep_links_resolve(self):
        ids=[n.attrs['id'] for n in self.result.find(lambda n:'id' in n.attrs)]
        self.assertEqual(len(ids),len(set(ids)))
        for a in self.result.find(lambda n:n.tag=='a'):
            href=a.attrs.get('href','')
            if href.startswith('#'):
                self.assertIn(href[1:],ids)

    def test_canonical_document_retains_every_illustration(self):
        for number in TITLES:
            source=next(self.source.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
            result=next(self.result.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
            html=result.html()
            for image in source.find(lambda n:n.tag=='img' and not n.has('page-background')):
                self.assertIn(image.attrs['src'],html,(number,image.attrs['src']))

    def test_no_separate_reader_navigation(self):
        for link in self.result.find(lambda n:n.tag=='a'):
            self.assertNotIn('rules-reader.html',link.attrs.get('href',''))
        redirect=(ROOT/'rules-reader.html').read_text()
        self.assertIn("location.replace('rules.html'+location.search+location.hash)",redirect)

    def test_caption_fragments_follow_horizontal_reading_order(self):
        page=next(self.result.find(lambda n:n.attrs.get('id')=='rules-page-39'))
        self.assertIn('Knight spirit of Grail, by KingArttu', reading_text(page))

    def test_column_continuations_remain_in_one_paragraph(self):
        expected={23:'lieutenant to Mallobaude.',29:"the character's WS, Initiative",
                  33:'to shine with inner glow',34:'its caster must immediately pass',
                  35:'It is even claimed that small bands',39:'(according to the outcomes',
                  44:'Vampire Counts Army Book 8 edition, page 41)'}
        for number,text in expected.items():
            page=next(self.result.find(lambda n:n.attrs.get('id')==f'rules-page-{number}'))
            self.assertTrue(any(text in reading_text(p) for p in page.find(lambda n:n.tag=='p')),number)

    def test_civil_war_table_remains_tabular(self):
        page=next(self.result.find(lambda n:n.attrs.get('id')=='rules-page-09'))
        table=next(page.find(lambda n:n.tag=='table'))
        self.assertEqual(len(list(table.find(lambda n:n.tag=='tr'))),12)
        self.assertEqual(len(list(table.find(lambda n:n.tag=='th' and n.attrs.get('scope')=='row'))),11)

    def test_diagrams_keep_spatial_svg_and_labels(self):
        for number in (46,48):
            page=next(self.result.find(lambda n:n.attrs.get('id')==f'rules-page-{number:02}'))
            svg=next(page.find(lambda n:n.tag=='svg'))
            self.assertTrue(list(svg.find(lambda n:n.tag=='path')))
            self.assertTrue(list(svg.find(lambda n:n.tag=='text')))

    def test_vertical_deployment_label_keeps_its_orientation(self):
        page=next(self.result.find(lambda n:n.attrs.get('id')=='rules-page-46'))
        label=next(page.find(lambda n:n.tag=='text' and n.text()=='Mallobaude deployment zone'))
        self.assertEqual(label.attrs.get('transform'),'rotate(-90 368.315 675.206)')

    def test_scenario_labels_become_headings(self):
        for number,label in [(49,'MULTIPLE BATTLE'),(50,'CONDITIONS OF VICTORY')]:
            page=next(self.result.find(lambda n:n.attrs.get('id')==f'rules-page-{number}'))
            self.assertIn(label,[n.text() for n in page.find(lambda n:n.tag=='h3')])

if __name__=='__main__':
    unittest.main()
