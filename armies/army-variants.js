window.CAMPAIGN_ARMY_VARIANTS = {
  "version": 1,
  "armies": {
    "morrsliebs-laughing-masses": {
      "name": "Morrslieb's Laughing Masses",
      "subtitle": "Mousillon's peasantry erupting into monstrous new shapes beneath the grinning Chaos moon",
      "sourcePage": 45,
      "eyebrow": "The Year of Woe · Optional Four-Player Variant",
      "cardLabel": "Optional four-player army",
      "sourceLabel": "Daemonic Assault on Mousillon, pp. 45–46",
      "sourceHref": "../rules.html#rules-page-45",
      "books": [
        "WAP Beastmen · Discord Archive 8th Edition",
        "WAP Bretonnia · Discord Archive 8th Edition",
        "WAP Warriors of Chaos · Discord Archive 8th Edition",
        "WAP The Empire · Discord Archive 8th Edition",
        "WAP Cult of Ulric · Discord Archive 8th Edition",
        "The Revolt of Mallobaude"
      ],
      "sourceNote": "Use the listed WAP 8th Edition books for unit profiles and options.",
      "campaignRole": [
        {
          "title": "Daemonic Assault on Mousillon — Four-Player Variant",
          "detail": "Add the Laughing Masses as an independent fourth army. Apply only the changes below; otherwise use the printed scenario.",
          "changes": [
            {
              "title": "Moonclaw Leads the Masses",
              "detail": "Moonclaw, Son of Morrslieb is compulsory and must be the Laughing Masses' General."
            },
            {
              "title": "Morrslieb Laughs Last",
              "detail": "Before comparing the printed scenario's objective points, the Laughing Masses win outright if they have strictly more ordinary Victory Points than every other army. A tie is not enough; otherwise the Masses cannot win. If the Masses slay Kairos or Ku'gath, Mallobaude receives the printed point for that Daemon's death, but not the additional point for his own army delivering the killing blow. If the Masses slay Mallobaude, neither Daemon army scores points that require its own army to kill him."
            },
            {
              "title": "After the Laughter",
              "detail": "If the Laughing Masses win, Mallobaude does not receive the four Ancient Relic results, and the Masses receive no campaign reward."
            }
          ]
        }
      ],
      "rules": [
        {
          "name": "Stolen Bretonnian Engines",
          "detail": "Ballistas, Mangonels, Field Trebuchets, and Bombards all count as the same Rare choice for duplicate limits. Each Bombard counts as two Rare choices."
        }
      ],
      "categories": [
        {
          "name": "Heroes",
          "entries": [
            {
              "id": "wap-moonclaw"
            },
            {
              "id": "anarchist-jester"
            }
          ]
        },
        {
          "name": "Core Units",
          "entries": [
            {
              "id": "wap-mutants"
            },
            {
              "id": "wap-peasant-levy"
            },
            {
              "id": "wap-men-at-arms"
            },
            {
              "id": "wap-peasant-bowmen"
            }
          ]
        },
        {
          "name": "Special Units",
          "entries": [
            {
              "id": "wap-chaos-spawn"
            },
            {
              "id": "wap-squires"
            },
            {
              "id": "wap-yeomen"
            },
            {
              "id": "wap-forsaken"
            },
            {
              "id": "wap-flayerkin"
            },
            {
              "id": "wap-flagellants"
            },
            {
              "id": "wap-wolf-kin"
            }
          ]
        },
        {
          "name": "Rare Units",
          "entries": [
            {
              "id": "wap-ballista"
            },
            {
              "id": "wap-mangonel"
            },
            {
              "id": "wap-field-trebuchet"
            },
            {
              "id": "wap-bombard"
            },
            {
              "id": "wap-children-of-ulric"
            }
          ]
        }
      ]
    }
  },
  "entries": {
    "wap-moonclaw": {
      "name": "Moonclaw, Son of Morrslieb",
      "comparedTo": "Moonclaw, Son of Morrslieb in WAP Beastmen.",
      "points": "200 points",
      "unitSize": "1",
      "troopType": "Cavalry (Special Character)",
      "profiles": [
        {
          "name": "Moonclaw",
          "stats": { "M": "5", "WS": "3", "BS": "3", "S": "4", "T": "4", "W": "2", "I": "3", "A": "3", "Ld": "7" }
        },
        {
          "name": "Umbralok",
          "stats": { "M": "7", "WS": "3", "BS": "0", "S": "4", "T": "4", "W": "1", "I": "3", "A": "3", "Ld": "6" }
        }
      ],
      "equipment": ["Hand weapon", "Umbralok (mount)"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Primal Fury", "Ward save (5+)", "Magic Resistance (2)", "Wave of Insanity", "Unholy Zenith"],
      "options": [],
      "notes": ["Level 1 Wizard. Choose the Lore of Shadow or the Lore of the Wild."],
      "source": "Warhammer — Beastmen, Discord Archive 8th Edition, pp. 102 and 113",
      "status": "campaign",
      "statusLabel": "Laughing Masses character"
    },
    "anarchist-jester": {
      "name": "Anarchist Jester",
      "comparedTo": "Jules the Jester in WAP Bretonnia.",
      "points": "50 points (provisional)",
      "unitSize": "1",
      "troopType": "Infantry (Character)",
      "profiles": [
        {
          "name": "Anarchist Jester",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "4", "A": "1", "Ld": "6" }
        },
        {
          "name": "Warhorse (optional mount)",
          "stats": { "M": "8", "WS": "3", "BS": "0", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        }
      ],
      "equipment": ["Hand weapon"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "The Peasant's Duty", "Acrobatic", "I Will Taunt You Viciously a Second Time", "Skirmishers"],
      "options": [
        { "name": "Additional hand weapon", "cost": "+2 points" },
        { "name": "Flail", "cost": "+6 points" },
        { "name": "Great weapon", "cost": "+6 points" },
        { "name": "Throwing axes", "cost": "+4 points" },
        { "name": "Light armour", "cost": "+2 points" },
        { "name": "Shield", "cost": "+2 points" },
        { "name": "Warhorse", "cost": "+12 points", "description": "A mounted Jester becomes Cavalry and does not gain Skirmishers." },
        { "name": "Common magic items", "cost": "Up to 50 points" }
      ],
      "notes": [
        "The Anarchist Jester has Skirmishers while on foot. Taking a Warhorse changes his troop type to Cavalry, so he loses Skirmishers.",
        "Choose at most one of additional hand weapon, flail, or great weapon.",
        "The effects of I Will Taunt You Viciously a Second Time from multiple Anarchist Jesters do not stack."
      ],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 134 and 150 (Jules the Jester)",
      "status": "campaign",
      "statusLabel": "Laughing Masses character"
    },
    "wap-mutants": {
      "name": "Mutants",
      "comparedTo": "Mutants in WAP Beastmen.",
      "points": "3 points per model",
      "unitSize": "20+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Mutant",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "6" }
        },
        {
          "name": "Mutant Leader",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "6" }
        }
      ],
      "equipment": ["Hand weapon"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Chaos Mutations", "Skirmishers"],
      "options": [
        { "name": "Upgrade one Mutant to a Mutant Leader", "cost": "+10 points" }
      ],
      "source": "Warhammer — Beastmen, Discord Archive 8th Edition, pp. 67 and 115",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-peasant-levy": {
      "name": "Insane Peasant Levy",
      "comparedTo": "Peasant Levy in WAP Bretonnia.",
      "points": "2 points per model",
      "unitSize": "20+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Peasant",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "4" }
        },
        {
          "name": "Cackling Rabble Leader",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "4" }
        },
        {
          "name": "Truffle Hound",
          "stats": { "M": "7", "WS": "3", "BS": "0", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "3" }
        }
      ],
      "equipment": ["Hand weapon"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Disorganized Mob", "The Peasant's Duty", "Skirmishers", "Truffle Madness"],
      "options": [
        { "name": "Upgrade one Peasant to a Cackling Rabble Leader", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" },
        { "name": "Throwing weapons", "cost": "+½ point per model" },
        { "name": "Slings", "cost": "+1 point per model" },
        { "name": "Up to three Truffle Hounds", "cost": "+10 points each" },
        { "name": "Mark of Khorne", "cost": "+2 points per model", "description": "Frenzy. A model that already has Frenzy instead gains +1 Attack while its Frenzy lasts." },
        { "name": "Mark of Nurgle", "cost": "+2 points per model", "description": "+1 Toughness." },
        { "name": "Mark of Slaanesh", "cost": "+1 point per model", "description": "Immune to Psychology." },
        { "name": "Mark of Tzeentch", "cost": "+2 points per model", "description": "A 6+ Ward save; if the model already has a Ward save, improve it by 1 instead, to a maximum of 3+." }
      ],
      "notes": [
        "The unit may take one of the following Marks of Chaos, using the Beastmen version of each Mark.",
        "Each purchased Truffle Hound is a Warbeast equipped with fangs; its profile is shown above, but it remains attached to this parent unit until Truffle Madness reveals it."
      ],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 105, 109, and 153",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-men-at-arms": {
      "name": "Deranged Men-at-Arms",
      "comparedTo": "Men-at-Arms in WAP Bretonnia.",
      "points": "5 points per model",
      "unitSize": "10+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Man-at-Arms",
          "stats": { "M": "4", "WS": "3", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "6" }
        },
        {
          "name": "Ranting Yeoman Warden",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "6" }
        },
        {
          "name": "Truffle Hound",
          "stats": { "M": "7", "WS": "3", "BS": "0", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "3" }
        }
      ],
      "equipment": ["Hand weapon", "Halberd", "Light armour"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "The Peasant's Duty", "Skirmishers", "Truffle Madness"],
      "options": [
        { "name": "Upgrade one Man-at-Arms to a Ranting Yeoman Warden", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" },
        { "name": "Replace halberds with spears and shields", "cost": "Free" },
        { "name": "Shields while retaining halberds", "cost": "+½ point per model" },
        { "name": "Up to three Truffle Hounds", "cost": "+10 points each" },
        { "name": "Mark of Khorne", "cost": "+2 points per model", "description": "Frenzy. A model that already has Frenzy instead gains +1 Attack while its Frenzy lasts." },
        { "name": "Mark of Nurgle", "cost": "+2 points per model", "description": "+1 Toughness." },
        { "name": "Mark of Slaanesh", "cost": "+1 point per model", "description": "Immune to Psychology." },
        { "name": "Mark of Tzeentch", "cost": "+2 points per model", "description": "A 6+ Ward save; if the model already has a Ward save, improve it by 1 instead, to a maximum of 3+." }
      ],
      "notes": [
        "The unit may take one of the following Marks of Chaos, using the Beastmen version of each Mark.",
        "Each purchased Truffle Hound is a Warbeast equipped with fangs; its profile is shown above, but it remains attached to this parent unit until Truffle Madness reveals it."
      ],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 105 and 153",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-peasant-bowmen": {
      "name": "Nutty Peasant Bowmen",
      "comparedTo": "Peasant Bowmen in WAP Bretonnia.",
      "points": "5 points per model",
      "unitSize": "10+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Bowman",
          "stats": { "M": "4", "WS": "2", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        },
        {
          "name": "Giggling Villein",
          "stats": { "M": "4", "WS": "2", "BS": "4", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        },
        {
          "name": "Truffle Hound",
          "stats": { "M": "7", "WS": "3", "BS": "0", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "3" }
        }
      ],
      "equipment": ["Hand weapon", "Long bow"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "The Peasant's Duty", "Skirmishers", "Truffle Madness"],
      "options": [
        { "name": "Upgrade one Bowman to a Giggling Villein", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" },
        { "name": "Braziers (Flaming Attacks)", "cost": "+½ point per model" },
        { "name": "Light armour", "cost": "+½ point per model" },
        { "name": "Up to three Truffle Hounds", "cost": "+10 points each" },
        { "name": "Mark of Khorne", "cost": "+2 points per model", "description": "Frenzy. A model that already has Frenzy instead gains +1 Attack while its Frenzy lasts." },
        { "name": "Mark of Nurgle", "cost": "+2 points per model", "description": "+1 Toughness." },
        { "name": "Mark of Slaanesh", "cost": "+1 point per model", "description": "Immune to Psychology." },
        { "name": "Mark of Tzeentch", "cost": "+2 points per model", "description": "A 6+ Ward save; if the model already has a Ward save, improve it by 1 instead, to a maximum of 3+." }
      ],
      "notes": [
        "The unit may take one of the following Marks of Chaos, using the Beastmen version of each Mark.",
        "Each purchased Truffle Hound is a Warbeast equipped with fangs; its profile is shown above, but it remains attached to this parent unit until Truffle Madness reveals it."
      ],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 105, 108, and 153",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-chaos-spawn": {
      "name": "Chaos Spawn",
      "comparedTo": "Unmarked Chaos Spawn in WAP Beastmen.",
      "points": "50 points",
      "unitSize": "1",
      "troopType": "Monstrous Beast",
      "profiles": [
        {
          "name": "Chaos Spawn",
          "stats": { "M": "3D6", "WS": "3", "BS": "0", "S": "4", "T": "5", "W": "3", "I": "2", "A": "*", "Ld": "10" }
        }
      ],
      "equipment": ["Tentacles, claws, and teeth"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Fear", "Random Movement (3D6)", "Random Attacks (D6+1)", "Unbreakable"],
      "options": [],
      "notes": [],
      "source": "Warhammer — Beastmen, Discord Archive 8th Edition, p. 118",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-squires": {
      "name": "Loopy Squires",
      "comparedTo": "Squires in WAP Bretonnia.",
      "points": "7 points per model",
      "unitSize": "5+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Squire",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "6" }
        },
        {
          "name": "Howling Equerry",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "6" }
        }
      ],
      "equipment": ["Hand weapon", "Long bow"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "The Peasant's Duty", "Skirmishers"],
      "options": [
        { "name": "Upgrade one Squire to a Howling Equerry", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" },
        { "name": "Mark of Khorne", "cost": "+2 points per model", "description": "Frenzy. A model that already has Frenzy instead gains +1 Attack while its Frenzy lasts." },
        { "name": "Mark of Nurgle", "cost": "+2 points per model", "description": "+1 Toughness." },
        { "name": "Mark of Slaanesh", "cost": "+1 point per model", "description": "Immune to Psychology." },
        { "name": "Mark of Tzeentch", "cost": "+2 points per model", "description": "A 6+ Ward save; if the model already has a Ward save, improve it by 1 instead, to a maximum of 3+." }
      ],
      "notes": ["The unit may take one of the following Marks of Chaos, using the Beastmen version of each Mark."],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, p. 154",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-yeomen": {
      "name": "Unhinged Yeomen",
      "comparedTo": "Yeomen in WAP Bretonnia.",
      "points": "10 points per model",
      "unitSize": "5+",
      "troopType": "Cavalry",
      "profiles": [
        {
          "name": "Yeoman",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "6" }
        },
        {
          "name": "Shrieking Warden",
          "stats": { "M": "4", "WS": "3", "BS": "3", "S": "3", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "6" }
        },
        {
          "name": "Horse",
          "stats": { "M": "8", "WS": "3", "BS": "0", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        }
      ],
      "equipment": ["Hand weapon", "Horse (mount)"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Fast Cavalry", "The Peasant's Duty"],
      "options": [
        { "name": "Upgrade one Yeoman to a Shrieking Warden", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" },
        { "name": "Spears", "cost": "+1 point per model" },
        { "name": "Bows or crossbows", "cost": "+2 points per model" },
        { "name": "Shields", "cost": "+1 point per model" },
        { "name": "Light armour", "cost": "+1 point per model" },
        { "name": "Mark of Khorne", "cost": "+2 points per model", "description": "Frenzy. A model that already has Frenzy instead gains +1 Attack while its Frenzy lasts." },
        { "name": "Mark of Nurgle", "cost": "+2 points per model", "description": "+1 Toughness." },
        { "name": "Mark of Slaanesh", "cost": "+1 point per model", "description": "Immune to Psychology." },
        { "name": "Mark of Tzeentch", "cost": "+2 points per model", "description": "A 6+ Ward save; if the model already has a Ward save, improve it by 1 instead, to a maximum of 3+." }
      ],
      "notes": ["The unit may take one of the following Marks of Chaos, using the Beastmen version of each Mark."],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, p. 155",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-forsaken": {
      "name": "Forsaken",
      "comparedTo": "Forsaken in WAP Warriors of Chaos.",
      "points": "15 points per model",
      "unitSize": "5+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Forsaken",
          "stats": { "M": "6", "WS": "4", "BS": "0", "S": "4", "T": "4", "W": "1", "I": "4", "A": "D3", "Ld": "8" }
        }
      ],
      "equipment": ["Hand weapon", "Heavy armour"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Frenzy", "Immune to Psychology", "Random Attacks (D3)", "Skirmishers", "Freakish Mutations"],
      "options": [
        { "name": "Forsaken of Khorne", "cost": "+1 point per model", "description": "Hatred.", "group": "Forsaken of Chaos — choose one" },
        { "name": "Forsaken of Nurgle", "cost": "+1 point per model", "description": "Fear.", "group": "Forsaken of Chaos — choose one" },
        { "name": "Forsaken of Slaanesh", "cost": "+1 point per model", "description": "Swiftstride.", "group": "Forsaken of Chaos — choose one" },
        { "name": "Forsaken of Tzeentch", "cost": "+1 point per model", "description": "6+ Ward save.", "group": "Forsaken of Chaos — choose one" }
      ],
      "notes": [],
      "source": "Ravening Hordes — Warriors of Chaos, Discord Archive 8th Edition, pp. 4 and 21",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-flayerkin": {
      "name": "Ruin-Crawlers",
      "comparedTo": "Flayerkin in WAP Warriors of Chaos.",
      "points": "9 points per model",
      "unitSize": "5+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Ruin-Crawler",
          "stats": { "M": "4", "WS": "4", "BS": "3", "S": "4", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "7" }
        },
        {
          "name": "Ruin-Stalker",
          "stats": { "M": "4", "WS": "4", "BS": "3", "S": "4", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "7" }
        }
      ],
      "equipment": ["Two hand weapons"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Killing Blow", "Scouts", "Skirmishers", "Obstacle Strider"],
      "options": [
        { "name": "Upgrade one Ruin-Crawler to a Ruin-Stalker", "cost": "+10 points" }
      ],
      "notes": [],
      "source": "Ravening Hordes — Warriors of Chaos, Discord Archive 8th Edition, p. 23",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-flagellants": {
      "name": "Raving Mob",
      "comparedTo": "Flagellants in WAP The Empire.",
      "points": "9 points per model",
      "unitSize": "10+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Raver",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "6" }
        },
        {
          "name": "Rabble-Rouser",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "6" }
        }
      ],
      "equipment": ["Flail"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Frenzy", "Unbreakable", "The End is Nigh!", "Skirmishers"],
      "options": [
        { "name": "Upgrade one Raver to a Rabble-Rouser", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" }
      ],
      "source": "Ravening Hordes — The Empire, Discord Archive 8th Edition, pp. 3 and 16",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-wolf-kin": {
      "name": "Wolfmen",
      "comparedTo": "Wolf-Kin in WAP Cult of Ulric.",
      "points": "9 points per model",
      "unitSize": "10+",
      "troopType": "Infantry",
      "profiles": [
        {
          "name": "Wolfman",
          "stats": { "M": "4", "WS": "4", "BS": "3", "S": "4", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "8" }
        },
        {
          "name": "Pack Alpha",
          "stats": { "M": "4", "WS": "4", "BS": "3", "S": "4", "T": "3", "W": "1", "I": "3", "A": "2", "Ld": "8" }
        }
      ],
      "equipment": ["Hand weapon"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Crush the Weak", "Hatred", "Skirmishers", "Stubborn"],
      "options": [
        { "name": "Upgrade one Wolfman to a Pack Alpha", "cost": "+10 points" },
        { "name": "Musician", "cost": "+10 points" },
        { "name": "Standard bearer", "cost": "+10 points" },
        { "name": "Great weapons", "cost": "+2 points per model" },
        { "name": "Additional hand weapons", "cost": "+1 point per model" },
        { "name": "Shields", "cost": "+1 point per model" },
        { "name": "Light armour", "cost": "+1 point per model" }
      ],
      "notes": ["Choose at most one of great weapons or additional hand weapons."],
      "source": "Warhammer — Cult of Ulric, Discord Archive 8th Edition, pp. 40 and 57",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-ballista": {
      "name": "Ballista",
      "comparedTo": "Ballista in WAP Bretonnia.",
      "points": "35 points",
      "unitSize": "1 (2 Peasant Crew)",
      "troopType": "War Machine (Bolt Thrower)",
      "profiles": [
        {
          "name": "Ballista",
          "stats": { "M": "—", "WS": "—", "BS": "—", "S": "—", "T": "7", "W": "3", "I": "—", "A": "—", "Ld": "—" }
        },
        {
          "name": "Peasant Crew",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        }
      ],
      "equipment": ["Hand weapon (crew)"],
      "specialRules": ["Ambushers", "From Every Ruin", "War Machines From Every Ruin", "The Peasant's Duty"],
      "options": [
        { "name": "Wall Warden", "cost": "+10 points", "description": "Once per game, re-roll one Artillery die or failed To Hit roll." },
        { "name": "Additional Peasant Crew", "cost": "+3 points" }
      ],
      "notes": [],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 118 and 157",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-mangonel": {
      "name": "Mangonel",
      "comparedTo": "Mangonel in WAP Bretonnia.",
      "points": "85 points",
      "unitSize": "1 (3 Peasant Crew)",
      "troopType": "War Machine (Stone Thrower)",
      "profiles": [
        {
          "name": "Mangonel",
          "stats": { "M": "—", "WS": "—", "BS": "—", "S": "—", "T": "7", "W": "3", "I": "—", "A": "—", "Ld": "—" }
        },
        {
          "name": "Peasant Crew",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        }
      ],
      "equipment": ["Hand weapon (crew)"],
      "specialRules": ["Ambushers", "From Every Ruin", "War Machines From Every Ruin", "The Peasant's Duty"],
      "options": [
        { "name": "Wall Warden", "cost": "+15 points", "description": "Once per game, re-roll one Artillery die or failed To Hit roll." },
        { "name": "Additional Peasant Crew", "cost": "+3 points" }
      ],
      "notes": [],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 118 and 157",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-field-trebuchet": {
      "name": "Field Trebuchet",
      "comparedTo": "Field Trebuchet in WAP Bretonnia.",
      "points": "100 points",
      "unitSize": "1 (4 Peasant Crew)",
      "troopType": "War Machine (Stone Thrower)",
      "profiles": [
        {
          "name": "Field Trebuchet",
          "stats": { "M": "—", "WS": "—", "BS": "—", "S": "—", "T": "7", "W": "4", "I": "—", "A": "—", "Ld": "—" }
        },
        {
          "name": "Peasant Crew",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        }
      ],
      "equipment": ["Hand weapon (crew)"],
      "specialRules": ["Ambushers", "From Every Ruin", "War Machines From Every Ruin", "Field Trebuchet", "The Peasant's Duty"],
      "options": [
        { "name": "Wall Warden", "cost": "+15 points", "description": "Once per game, re-roll one Artillery die or failed To Hit roll." }
      ],
      "notes": [],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 119 and 157",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-bombard": {
      "name": "Bombard",
      "comparedTo": "Bombard in WAP Bretonnia.",
      "points": "90 points",
      "unitSize": "1 (3 Peasant Crew)",
      "troopType": "War Machine (Cannon)",
      "profiles": [
        {
          "name": "Bombard",
          "stats": { "M": "—", "WS": "—", "BS": "—", "S": "—", "T": "7", "W": "3", "I": "—", "A": "—", "Ld": "—" }
        },
        {
          "name": "Peasant Crew",
          "stats": { "M": "4", "WS": "2", "BS": "2", "S": "3", "T": "3", "W": "1", "I": "3", "A": "1", "Ld": "5" }
        }
      ],
      "equipment": ["Hand weapon (crew)"],
      "specialRules": ["Ambushers", "From Every Ruin", "War Machines From Every Ruin", "Bombard", "The Peasant's Duty"],
      "options": [
        { "name": "Wall Warden", "cost": "+15 points", "description": "Once per game, re-roll one Artillery die or failed To Hit roll." },
        { "name": "Additional Peasant Crew", "cost": "+3 points" }
      ],
      "notes": [],
      "source": "Warhammer — Bretonnia, Discord Archive 8th Edition, pp. 120 and 157",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    },
    "wap-children-of-ulric": {
      "name": "Werewolves",
      "comparedTo": "Children of Ulric in WAP Cult of Ulric.",
      "points": "15 points per model",
      "unitSize": "3+",
      "troopType": "War Beast",
      "profiles": [
        {
          "name": "Werewolf",
          "stats": { "M": "9", "WS": "4", "BS": "0", "S": "4", "T": "4", "W": "1", "I": "5", "A": "2", "Ld": "8" }
        },
        {
          "name": "Werewolf Alpha",
          "stats": { "M": "9", "WS": "4", "BS": "0", "S": "4", "T": "4", "W": "1", "I": "5", "A": "3", "Ld": "8" }
        }
      ],
      "equipment": ["Claws"],
      "specialRules": ["Ambushers", "From Every Ruin", "Charging From Ambush", "Ambushing From Buildings", "Crush the Weak", "Fear", "Frenzy", "Regeneration (5+)"],
      "options": [
        { "name": "Upgrade one Werewolf to a Werewolf Alpha", "cost": "+10 points" }
      ],
      "notes": [],
      "source": "Warhammer — Cult of Ulric, Discord Archive 8th Edition, pp. 41 and 58",
      "status": "campaign",
      "statusLabel": "Laughing Masses unit"
    }
  }
};
