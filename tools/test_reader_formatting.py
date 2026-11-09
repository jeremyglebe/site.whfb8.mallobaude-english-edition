import unittest
from build_rules_reader import DOM, build, ROOT

class FormattingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=DOM(build()).root
    def page(self,n):
        return next(self.root.find(lambda x:x.attrs.get('id')==f'rules-page-{n:02}'))
    def test_named_rules_are_headings(self):
        for n, expected in {19:['Equipment','Mount','Sense of Honour'],20:['Honour or Death','No Mortal Son'],34:["Sylph's Voice:",'Aura of the Fey Queen:','White Elm Wand (Arcane Item):'],36:['Command Group:','Storm Witch:'],40:['Options','Guardians of Haven','Royal Bodyguard'],43:['The Crown of Bretonnia (Enchanted Item):'],53:['The Crypt of Secrets:','Alakanash:']}.items():
            headings=[x.text() for x in self.page(n).find(lambda x:x.tag=='h3')]
            for label in expected:self.assertIn(label,headings,(n,label))
    def test_all_reviewed_headings_are_present(self):
        from reader_formatting import HEADINGS
        for n, groups in HEADINGS.items():
            headings=[x.text() for x in self.page(n).find(lambda x:x.tag=='h3')]
            for _, labels in groups:
                for label in labels:self.assertIn(label,headings,(n,label))
    def test_no_literal_bullets_in_body_paragraphs(self):
        for n in range(4,56):
            for p in self.page(n).find(lambda x:x.tag=='p'):
                self.assertNotIn('•',p.text(),n)
    def test_army_entries_and_annotations_stay_together(self):
        items=[x.text() for x in self.page(22).find(lambda x:x.tag=='li')]
        self.assertEqual(len(items),40)
        self.assertIn('Knights of the Black Grail (RM) (3)',items)
        self.assertIn('Skeleton Warriors (VC) (can take bows in place of hand weapons for +2 points per model)',items)
        self.assertIn('Morgiana the Fay (**)',[x.text() for x in self.page(32).find(lambda x:x.tag=='li')])
    def test_louen_title_not_sentence_fragment(self):
        p=self.page(42)
        self.assertIn('Louen de Couronne, the High Paladin',[x.text() for x in p.find(lambda x:x.tag=='h3')])
        self.assertTrue(any(x.text().startswith('Louen the High Paladin depicts') for x in p.find(lambda x:x.tag=='p')))
    def test_guide_has_semantic_lists(self):
        guide=DOM((ROOT/'guide.html').read_text()).root
        self.assertGreater(len(list(guide.find(lambda x:x.tag=='li'))),100)
        self.assertFalse(any('•' in p.text() for p in guide.find(lambda x:x.tag=='p')))

if __name__=='__main__':unittest.main()
