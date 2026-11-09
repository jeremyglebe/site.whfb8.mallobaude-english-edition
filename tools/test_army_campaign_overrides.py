"""Campaign reference regressions against French Rules v1.5, pp18–27/42.
Node evaluates the actual JS data and renderer; this is not visual browser QA.
"""
import json
import subprocess
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class CampaignArmyOverrides(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('./armies/army-data.js');require('./armies/campaign-rule-definitions.js');console.log(JSON.stringify(window))"], cwd=ROOT))
        cls.entries = cls.data['CAMPAIGN_ARMY_DATA']['entries']
        cls.armies = cls.data['CAMPAIGN_ARMY_DATA']['armies']
        cls.rules = cls.data['CAMPAIGN_RULE_DEFINITIONS']['definitions']

    def test_campaign_arkhan(self):
        a = self.entries['arkhan-campaign']
        self.assertIn('Master Necromancer', a['troopType'])
        self.assertNotIn('Tomb King', a['troopType'])
        self.assertTrue({'Undead', 'Master of the Dead'} <= set(a['specialRules']))
        self.assertFalse({'The Hierophant', 'Nehekharan Undead'} & set(a['specialRules']))
        self.assertIn('Lore of Undeath', ' '.join(a['notes']))
        self.assertNotIn('nor General', ' '.join(a['notes']))
        self.assertNotIn('Fly', a['specialRules'])
        self.assertTrue({'The Tomb Blade of Arkhan','The Liber Mortis','Staff of Nagash'} <= set(a['equipment']))

    def test_rebel_specific_entries(self):
        ids = {r['id'] for c in self.armies['rebels-of-bretonnia']['categories'] for r in c['entries']}
        self.assertIn('mortal-black-grail-knights', ids)
        self.assertNotIn('black-grail-knights', ids)
        mortal = self.entries['mortal-black-grail-knights']
        self.assertNotIn('Undead', mortal['specialRules'])
        self.assertIn('Oath of the Black Grail', mortal['specialRules'])
        for key in ['rebel-wizard', 'rebel-wizard-lord']:
            self.assertIn(key, ids)
            entry = self.entries[key]
            self.assertEqual({o['name'] for o in entry['options'] if o['group']=='Mount'}, {'Warhorse'})
            self.assertEqual({o['name'] for o in entry['options'] if o['group']=='Lore'}, {'Lore of Fire','Lore of Shadow','Lore of Death','Lore of Beasts'})
            self.assertEqual(entry['specialRules'], ['Rebel Sorcery'])
            magic = next(o for o in entry['options'] if o['name']=='Magic Items')
            self.assertEqual(magic['cost'], 'Pay item costs')
            self.assertIn('not yet been verified', magic['description'])
        self.assertIn('two lowest', self.rules['Rebel Sorcery']['html'])

    def test_ancient_treekin(self):
        a = self.entries['ancient-treekin']
        self.assertEqual([p['name'] for p in a['profiles']], ['Tree Kin Elder'])
        self.assertIn('Scaly Skin (3+)', a['specialRules'])
        self.assertNotIn('Scaly Skin (4+)', a['specialRules'])

    def test_louen_and_vampire_lord_conditions(self):
        for key in ['louen-high-paladin','louen-dispossessed']:
            self.assertNotIn('The Army of the King', self.entries[key]['specialRules'])
        ref = next(r for r in self.armies['mousillon']['categories'][0]['entries'] if r['id']=='vampire-lord')
        self.assertIn('Only after the final victory', ref['note'])

    def test_source_profiles_and_editorial_policy(self):
        for key in ['mallobaude-black-knight','mallobaude-vampire-duke']:
            self.assertEqual(len(self.entries[key]['profiles']), 2)
        self.assertIn('Red Fury and Master Strike', self.rules['Blood Dragon Vampire']['html'])
        curse = self.rules['Curse of the Lady of the Lake']['html']
        self.assertIn('passes a save', curse)
        self.assertNotIn('passes a ward save', curse)
        self.assertIn('#ed-024', curse)

    def test_actual_renderer_all_armies(self):
        script = r"""
const vm=require('node:vm'),fs=require('node:fs');
const files=['army-data.js','army-variants.js','rule-definitions.js','campaign-rule-definitions.js','army.js'];
for (const army of ['rebels-of-bretonnia','mousillon','wildwood-host','alliance-against-undeath','crusade-army','morrsliebs-laughing-masses','']) {
 const app={innerHTML:''}; const inert={addEventListener(){}};
 const context={window:{addEventListener(){}},location:{hash:''},document:{body:{dataset:{army}},getElementById(id){return id==='army-app'?app:inert},querySelectorAll(){return []},querySelector(){return null}}};
 vm.createContext(context); for(const file of files)vm.runInContext(fs.readFileSync('armies/'+file,'utf8'),context);
 if(!app.innerHTML.includes('army-nav'))throw Error(army+' did not render');
 if(army==='rebels-of-bretonnia' && (!app.innerHTML.includes('unit-mortal-black-grail-knights') || !app.innerHTML.includes('Gain one free power die')))throw Error('Rebel override not rendered');
 if(army==='mousillon' && !app.innerHTML.includes('Master Necromancer'))throw Error('Arkhan override absent');
 if(army==='rebels-of-bretonnia' && !app.innerHTML.includes('<a href="../rules.html#rules-page-21">The Revolt of Mallobaude, p. 21;'))throw Error('Campaign card source link missing');
}
"""
        subprocess.run(['node','-e',script],cwd=ROOT,check=True)

if __name__ == '__main__': unittest.main()
