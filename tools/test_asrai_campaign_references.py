"""Source-backed campaign disclosures: French Rules v1.5 pp34,36–38."""
import json
import subprocess
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class AsraiReferences(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(subprocess.check_output(['node','-e',"global.window={};for(const f of ['army-data','campaign-rule-definitions','rule-definitions'])require('./armies/'+f+'.js');console.log(JSON.stringify(window))"],cwd=ROOT))
        cls.entries=cls.data['CAMPAIGN_ARMY_DATA']['entries']
        cls.rules=cls.data['CAMPAIGN_RULE_DEFINITIONS']['definitions']

    def test_skaw_campaign_rule_not_ogre_rule(self):
        self.assertIn('The Falconer',self.entries['skaw']['specialRules'])
        self.assertNotIn('Loner',self.entries['skaw']['specialRules'])
        self.assertEqual(self.rules['The Falconer']['html'], '<p>Skaw can never join a unit, cannot use the General’s Leadership, and cannot be the General.</p>')
        self.assertEqual(self.rules['The Falconer']['sourceUrl'],'../rules.html#rules-page-37')
        self.assertEqual(self.data['WHFB_RULE_DEFINITIONS']['definitions']['Loner']['html'], '<p>Hunters cannot join any unit except a Sabretusk Pack, and can never be the General of an Ogre army. </p>')

    def test_ariel_conditional_rules(self):
        self.assertIn('In the creative cycle she has Forest Strider; in the destructive cycle she has Terror.',self.rules['Life Cycle']['html'])
        self.assertNotIn('Terror',self.entries['ariel']['specialRules'])
        self.assertNotIn('Forest Strider',self.entries['ariel']['specialRules'])

    def test_skaw_equipment(self):
        self.assertEqual(self.entries['skaw']['notes'],[
            'Any model hit by the Talon Whip loses 1 Attack, to a minimum of 1, for the rest of the turn.',
            'The Feather Cloak grants a 4+ armour save against ranged attacks.',
            'Hawks make three Strength 4 shooting attacks at a range of 24 inches, always hitting on 2+. All three attacks must target the same unit. In close combat, the hawks grant D3 additional Attacks.'
        ])

    def test_sceolan_buckler(self):
        self.assertEqual(self.entries['sceolan']['notes'],['The Bronze Buckler is a shield. For each close-combat Attack that rolls a 1 To Hit against Sceolan, he gains one Stomp Attack.'])

    def test_scarloc_command_and_equipment(self):
        rule=self.rules["Scarloc's Archers"]['html']
        for text in ['Pay the normal Deepwood Scouts unit cost.','no other option is available','two hand weapons instead of an Asrai bow','her Storm Witch ability is lost if she is removed','power level 3','lost if the unit flees']:
            self.assertIn(text,rule)
        notes=' '.join(self.entries['scarloc']['notes'])
        for text in ['magic weapon granting Armour Piercing','rank bonus, be Steadfast, and disrupt','despite being Skirmishers','Fear in non-Elves']:
            self.assertIn(text,notes)

    def test_actual_alliance_cards(self):
        script=r'''
const fs=require('fs'),vm=require('vm'),app={innerHTML:''},inert={addEventListener(){}};
const c={window:{addEventListener(){}},location:{hash:''},document:{body:{dataset:{army:'alliance-against-undeath'}},getElementById(id){return id==='army-app'?app:inert},querySelectorAll(){return []},querySelector(){return null}}};vm.createContext(c);
for(const f of ['army-data.js','army-variants.js','rule-definitions.js','campaign-rule-definitions.js','army.js'])vm.runInContext(fs.readFileSync('armies/'+f,'utf8'),c);
function card(id){const s=app.innerHTML.indexOf('id="unit-'+id+'"'),e=app.innerHTML.indexOf('<details class="unit-card',s+1);if(s<0)throw Error('Missing '+id);return app.innerHTML.slice(s,e<0?undefined:e);}
for(const [id,texts] of Object.entries({ariel:['creative cycle she has Forest Strider','destructive cycle she has Terror'],scarloc:['Armour Piercing','Fear in non-Elves','no other option'],skaw:['The Falconer','cannot use the General’s Leadership','three Strength 4','4+ armour save'],sceolan:['one Stomp Attack']}))for(const t of texts)if(!card(id).includes(t))throw Error(id+' missing '+t);
if(card('skaw').includes('Sabretusk') || card('skaw').includes('Ogre army'))throw Error('Wrong Ogre definition');
'''
        subprocess.run(['node','-e',script],cwd=ROOT,check=True)

if __name__=='__main__': unittest.main()
