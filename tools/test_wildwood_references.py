"""Wildwood disclosures from French Rules v1.5 pp25–29."""
import hashlib
import json
import subprocess
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT="const fs=require('fs'),vm=require('vm');const out={};for(const army of ['wildwood-host','alliance-against-undeath']){const app={innerHTML:''},inert={addEventListener(){}};const c={window:{addEventListener(){}},location:{hash:''},document:{body:{dataset:{army}},getElementById(id){return id==='army-app'?app:inert},querySelectorAll(){return []},querySelector(){return null}}};vm.createContext(c);for(const f of ['army-data.js','army-variants.js','rule-definitions.js','campaign-rule-definitions.js','army.js'])vm.runInContext(fs.readFileSync('armies/'+f,'utf8'),c);out[army]=app.innerHTML;}console.log(JSON.stringify(out));"
class WildwoodReferences(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages=json.loads(subprocess.check_output(['node','-e',SCRIPT],cwd=ROOT))
        cls.data=json.loads(subprocess.check_output(['node','-e',"global.window={};require('./armies/army-data.js');console.log(JSON.stringify(window.CAMPAIGN_ARMY_DATA))"],cwd=ROOT))
        cls.refs={x['id']:x for c in cls.data['armies']['wildwood-host']['categories'] for x in c['entries']}

    def test_alliance_render_unchanged(self):
        self.assertEqual(hashlib.sha256(self.pages['alliance-against-undeath'].encode()).hexdigest(),'11fb430660e1bf7484797c0a3cc23623537ef0e0849105cdd334f3fa10065da9')

    def test_branchwraith_choices(self):
        note=self.refs['branchwraith']['note']
        for text in ['Birch for +5 points','Oak for +10 points','Willow for +10 points','only join a unit with the same Aspect','Branchwych for +40 points','Level 2 Wizard','Greenwood Scythe (halberd)','Branchwraith or Branchwych','Bittergrub for +10 points','one close-combat Attack with Armour Piercing','character’s Weapon Skill, Initiative 4 and Strength 2']:
            self.assertIn(text,note)
        self.assertNotIn('choose only one upgrade',note)

    def test_dryad_aspects(self):
        note=self.refs['dryads']['note']
        for text in ['Birch for +1 point per model','Oak for +2','Willow for +2','Devastating Charge','Scaly Skin (5+)','−1 To Hit the Dryads in close combat','without an Aspect','+5 points per model','Eternal Hatred','−1 Leadership on enemies in contact']:
            self.assertIn(text,note)

    def test_kurnoth_and_quiverlings(self):
        note=self.refs['treekin']['note']
        for text in ['+3 points per model','cannot have more units of Kurnoth Hunters than Treekin','great weapon, a scythe (halberd), or a longbow','equipped with bows may take Quiverlings','Multiple Attacks (D3)','Initiative 4 and Strength 2']:
            self.assertIn(text,note)
        ancient=self.data['entries']['ancient-treekin']
        self.assertIn('If taken, Quiverlings grant Multiple Attacks (D3), with Initiative 4 and Strength 2.',ancient['notes'])
        self.assertNotIn('equipped with bows',' '.join(ancient['notes']))
        self.assertEqual([p['name'] for p in ancient['profiles']],['Tree Kin Elder'])
        self.assertIn('Scaly Skin (3+)',ancient['specialRules'])

    def test_optional_onager(self):
        for key in ['treeman','treeman-ancient']:
            note=self.refs[key]['note']
            for text in ['May take','+25 points','If taken','36 inches','small template','Strength 10','Strength 5','Move or Fire','D3 Wounds']:
                self.assertIn(text,note)
            self.assertNotIn('Wildwood Onager',self.data['entries'][key]['specialRules'])
        self.assertIn('not together with Strangleroots',self.refs['treeman']['note'])
        self.assertIn('may fire both weapons in the same phase',self.refs['treeman-ancient']['note'])

    def test_actual_wildwood_cards(self):
        page=self.pages['wildwood-host']
        for key,phrases in {'branchwraith':['Branchwych for +40 points','one close-combat Attack'], 'dryads':['without an Aspect','Eternal Hatred'], 'treekin':['cannot have more units','Multiple Attacks (D3)'], 'ancient-treekin':['If taken, Quiverlings'], 'treeman':['If taken','not together with Strangleroots'], 'treeman-ancient':['If taken','may fire both weapons']}.items():
            start=page.index('id="unit-'+key+'"');end=page.find('<details class="unit-card',start+1);card=page[start:end if end!=-1 else None]
            for text in phrases:self.assertIn(text,card)
if __name__=='__main__':unittest.main()
