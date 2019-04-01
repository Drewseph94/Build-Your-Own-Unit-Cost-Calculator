class Unit:
    def __init__(self, ancestry, experience, equipment, unit_type, size):
        self._ancestry = ancestry
        self._experience = experience
        self._equipment = equipment
        self._type = unit_type
        self._size = size

    def total_attack_bonus(self):
        return self._ancestry.attack_bonus + self._experience.attack_bonus + self._equipment.attack_bonus + self._type.attack_bonus

    def total_power_bonus(self):
        return self._ancestry.power_bonus + self._experience.power_bonus + self._equipment.power_bonus + self._type.power_bonus

    def total_defense_bonus(self):
        return self._ancestry.defense_bonus + self._experience.defense_bonus + self._equipment.defense_bonus + self._type.defense_bonus

    def total_toughness_bonus(self):
        return self._ancestry.toughness_bonus + self._experience.toughness_bonus + self._equipment.toughness_bonus + self._type.toughness_bonus

    def total_morale_bonus(self):
        return self._ancestry.morale_bonus + self._experience.morale_bonus + self._equipment.morale_bonus + self._type.morale_bonus

class Ancestry:
    def __init__(self, name):
        self.name = name

        ancestries = {
            'Bugbear': {
                'bonuses': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 1},
                'traits': ['Martial']
            },
            'Dragonborn': {
                'bonuses': {'attack': 2, 'power': 2, 'defense': 1, 'toughness': 1, 'morale': 1},
                'traits': ['Courageous'],
            },
            'Dwarf': {
                'bonuses': {'attack': 3, 'power': 1, 'defense': 1, 'toughness': 1, 'morale': 2},
                'traits': ['Stalwart']
            },
            'Elf': {
                'bonuses': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 1},
                'traits': ['Eternal']
            },
            'Elf (Winged)': {
                'bonuses': {'attack': 1, 'power': 1, 'defense': 0, 'toughness': 0, 'morale': 1},
                'traits': ['Eternal']
            },
            'Ghoul': {
                'bonuses': {'attack': 1, 'power': 0, 'defense': 2, 'toughness': 2, 'morale': 0},
                'traits': ['Undead', 'Horrify', 'Ravenous']
            },
            'Gnoll': {
                'bonuses': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 1},
                'traits': ['Frenzy']
            },
            'Gnome': {
                'bonuses': {'attack': 1, 'power': -1, 'defense': 1, 'toughness': -1, 'morale': 1},
                'traits': []
            },
            'Goblin': {
                'bonuses': {'attack': -1, 'power': -1, 'defense': 1, 'toughness': -1, 'morale': 0},
                'traits': []
            },
            'Hobgoblin': {
                'bonuses': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 1},
                'traits': ['Bred For War', 'Martial']
            },
            'Human': {
                'bonuses': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 1},
                'traits': ['Courageous']
            },
            'Kobold': {
                'bonuses': {'attack': -1, 'power': -1, 'defense': 1, 'toughness': -1, 'morale': -1},
                'traits': []
            },
            'Lizardfolk': {
                'bonuses': {'attack': 2, 'power': 1, 'defense': -1, 'toughness': 1, 'morale': 1},
                'traits': ['Amphibious']
            },
            'Ogre': {
                'bonuses': {'attack': 0, 'power': 2, 'defense': 0, 'toughness': 2, 'morale': 1},
                'traits': ['Brutal']
            },
            'Orc': {
                'bonuses': {'attack': 2, 'power': 1, 'defense': 1, 'toughness': 1, 'morale': 2},
                'traits': ['Savage']
            },
            'Skeleton': {
                'bonuses': {'attack': -2, 'power': -1, 'defense': 1, 'toughness': 1, 'morale': 1},
                'traits': ['Undead', 'Mindless']
            },
            'Treant': {
                'bonuses': {'attack': 0, 'power': 2, 'defense': 0, 'toughness': 2, 'morale': 0},
                'traits': ['Siege Engine', 'Twisting Roots', 'Hurl Roots']
            },
            'Troll': {
                'bonuses': {'attack': 0, 'power': 2, 'defense': 0, 'toughness': 2, 'morale': 0},
                'traits': ['Regenerate']
            },
            'Zombie': {
                'bonuses': {'attack': -2, 'power': 0, 'defense': 2, 'toughness': 2, 'morale': 2},
                'traits': ['Undead', 'Mindless']
            }
        }

        self.attack_bonus = ancestries[self.name]['bonuses']['attack']
        self.power_bonus = ancestries[self.name]['bonuses']['power']
        self.defense_bonus = ancestries[self.name]['bonuses']['defense']
        self.toughness_bonus = ancestries[self.name]['bonuses']['toughness']
        self.morale_bonus = ancestries[self.name]['bonuses']['morale']
        self.traits = ancestries[self.name]['traits']


class Experience:
    def __init__(self, experience_level):
        self.experience_level = experience_level

        experiences = {
            'Green': {'attack': 0, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 0},
            'Regular': {'attack': 1, 'power': 0, 'defense': 0, 'toughness': 1, 'morale': 1},
            'Seasoned': {'attack': 1, 'power': 0, 'defense': 0, 'toughness': 1, 'morale': 3},
            'Veteran': {'attack': 1, 'power': 0, 'defense': 0, 'toughness': 1, 'morale': 3},
            'Elite': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 2, 'morale': 4},
            'Super Elite': {'attack': 2, 'power': 0, 'defense': 0, 'toughness': 2, 'morale': 5}
        }

        self.attack_bonus = experiences[self.experience_level]['attack']
        self.power_bonus = experiences[self.experience_level]['power']
        self.defense_bonus = experiences[self.experience_level]['defense']
        self.toughness_bonus = experiences[self.experience_level]['toughness']
        self.morale_bonus = experiences[self.experience_level]['morale']


class Equipment:
    def __init__(self, equipment):
        self.equipment = equipment

        equipment_types = {
            'Light': {'attack': 0, 'power': 1, 'defense': 1, 'toughness': 0, 'morale': 0},
            'Medium': {'attack': 1, 'power': 2, 'defense': 2, 'toughness': 1, 'morale': 1},
            'Heavy': {'attack': 1, 'power': 4, 'defense': 4, 'toughness': 1, 'morale': 2},
            'Super Heavy': {'attack': 1, 'power': 6, 'defense': 6, 'toughness': 1, 'morale': 3}
        }
        self.attack_bonus = equipment_types[self.equipment]['attack']
        self.power_bonus = equipment_types[self.equipment]['power']
        self.defense_bonus = equipment_types[self.equipment]['defense']
        self.toughness_bonus = equipment_types[self.equipment]['toughness']
        self.morale_bonus = equipment_types[self.equipment]['morale']


class Type:
    def __init__(self, type):
        self.type = type

        types = {
            'Flying': {
                'bonuses': {'attack': 0, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': 3},
                'cost_modifier': 2
            },
            'Archers': {
                'bonuses': {'attack': 0, 'power': 1, 'defense': 0, 'toughness': 0, 'morale': 1},
                'cost_modifier': 1.75
            },
            'Calvary': {
                'bonuses': {'attack': 1, 'power': 1, 'defense': 0, 'toughness': 0, 'morale': 2},
                'cost_modifier': 1.5
            },
            'Levies': {
                'bonuses': {'attack': 0, 'power': 0, 'defense': 0, 'toughness': 0, 'morale': -1},
                'cost_modifier': .75
            },
            'Infantry': {
                'bonuses': {'attack': 0, 'power': 0, 'defense': 1, 'toughness': 1, 'morale': 0},
                'cost_modifier': 1
            },
            'Siege Engine': {
                'bonuses': {'attack': 1, 'power': 1, 'defense': 0, 'toughness': 1, 'morale': 0},
                'cost_modifier': 1.5
            }
        }
        self.attack_bonus = types[self.type]['bonuses']['attack']
        self.power_bonus = types[self.type]['bonuses']['power']
        self.defense_bonus = types[self.type]['bonuses']['defense']
        self.toughness_bonus = types[self.type]['bonuses']['toughness']
        self.morale_bonus = types[self.type]['bonuses']['morale']
        self.cost_modifier = types[self.type]['cost_modifier']


class Size:
    def __init__(self, size):
        self.size = size

        sizes = {
            '1d4': .66,
            '1d6': 1,
            '1d8': 1.33,
            '1d10': 1.66,
            '1d12': 2
        }

        self.cost_modifier = sizes[self.size]
