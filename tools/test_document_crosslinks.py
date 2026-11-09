import re
import unittest
from pathlib import Path
from build_rules_reader import DOM, ROOT
from document_crosslinks import rules_links, guide_links, link_text_nodes

class Crosslinks(unittest.TestCase):
    def test_targets_exist(self):
        count=0
        for name in ('guide.html','rules.html'):
            doc=DOM((ROOT/name).read_text()).root
            for a in doc.find(lambda n:n.tag=='a' and n.has('cross-reference')):
                path, anchor=a.attrs['href'].split('#')
                target=DOM((ROOT/(path or name)).read_text()).root
                ids={n.attrs.get('id') for n in target.find(lambda n:'id' in n.attrs)}
                self.assertIn(anchor,ids,a.html())
                count+=1
        self.assertGreater(count,40)
    def test_text_is_unchanged_and_idempotent(self):
        sample='<p>See page 14. <b>Civil War*</b></p><a href="#x">Civil War*</a>'
        wrapped='<article id="stage-2">'+sample+'</article>'
        changed=guide_links(wrapped)
        self.assertEqual(DOM(wrapped).root.text(),DOM(changed).root.text())
        self.assertEqual(changed,guide_links(changed))
        self.assertNotIn('<a href="#x"><a',changed)
    def test_external_or_wrong_source_reference_not_retargeted(self):
        self.assertEqual(rules_links('<p>see page 51 of the Vampire Counts army book</p>',24),'<p>see page 51 of the Vampire Counts army book</p>')
        self.assertNotIn('<a',rules_links('<p>separate rules on page 23</p>',21))
        self.assertNotIn('<a',rules_links('<p>Mallobaude the Vampire Duke (see page 19)</p>',51))
    def test_no_diagram_or_heading_linkification(self):
        sample='<h2>Civil War*</h2><svg><text>Civil War*</text></svg>'
        self.assertEqual(sample,link_text_nodes(sample,{'Civil War*':'rules.html#rules-page-07'}))
    def test_companion_and_quenelles(self):
        self.assertIn('href="guide.html#conclusion-1"',rules_links('<p>Conclusions of the Game Guide</p>',39))
        self.assertIn('href="#rules-page-49"',rules_links('<p>Battle of Quenelles rules</p>',50))

if __name__=='__main__':unittest.main()
