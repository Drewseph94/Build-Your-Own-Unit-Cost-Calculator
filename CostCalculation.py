def calculate_cost(unit):
    # attack_bonus = 2
    # power_bonus = 2
    # defense_bonus = 2
    # toughness_bonus = 1
    # morale_bonus = 1
    # bonuses = {'attack':0, 'power':0, 'defense':0, 'toughness':0, 'morale':0}
    #
    # experience_level = 'green'
    # equipment_level = 'light'
    #
    # unit_type = 'levy'
    # unit_size = 'd4'
    #
    trait_cost_total = 50

    type_modifiers = {'Levy':.75, 'Infantry':1, 'Calvary':1.5, 'Siege Engine':1.5, 'Archer':1.75, 'Flying':2}
    size_modifiers = {'d4':.66, 'd6':1, 'd8':1.33, 'd10':1.66, 'd12':2}

    # def calculate_experience_bonuses(experience):
    #     if experience == 'green':
    #         return {'attack':0, 'power':0, 'defense':0, 'toughness':0, 'morale':0}
    #     elif experience == 'regular':
    #         return {'attack':1, 'power':0, 'defense':0, 'toughness':1, 'morale':1}
    #     elif experience == 'seasoned':
    #         return {'attack':1, 'power':0, 'defense':0, 'toughness':1, 'morale':2}
    #     elif experience == 'veteran':
    #         return {'attack':1, 'power':0, 'defense':0, 'toughness':1, 'morale':3}
    #     elif experience == 'elite':
    #         return {'attack':2, 'power':0, 'defense':0, 'toughness':2, 'morale':4}
    #     elif experience == 'super-elite':
    #         return {'attack':2, 'power':0, 'defense':0, 'toughness':2, 'morale':5}

    # def calculate_equipment_bonuses(equipment):
    #     if equipment == 'light':
    #         return {'attack':0, 'power':1, 'defense':1, 'toughness':0, 'morale':0}
    #     elif equipment == 'medium':
    #         return {'attack':1, 'power':2, 'defense':2, 'toughness':1, 'morale':1}
    #     elif equipment == 'heavy':
    #         return {'attack':1, 'power':4, 'defense':4, 'toughness':1, 'morale':2}
    #     elif equipment == 'super-heavy':
    #         return {'attack':1, 'power':6, 'defense':6, 'toughness':1, 'morale':3}

    # def calculate_type_bonuses(unit_type):
    #     if unit_type == 'flying':
    #         return {'attack':0, 'power':0, 'defense':0, 'toughness':0, 'morale':3}
    #     elif unit_type == 'archer':
    #         return {'attack':0, 'power':1, 'defense':0, 'toughness':0, 'morale':1}
    #     elif unit_type == 'calvary':
    #         return {'attack':1, 'power':1, 'defense':0, 'toughness':0, 'morale':2}
    #     elif unit_type == 'levy':
    #         return {'attack':0, 'power':0, 'defense':0, 'toughness':0, 'morale':-1}
    #     elif unit_type == 'infantry':
    #         return {'attack':0, 'power':0, 'defense':1, 'toughness':1, 'morale':0}
    #     elif unit_size == 'siege_weapon':
    #         return {'attack':1, 'power':1, 'defense':0, 'toughness':1, 'morale':0}

    def add_bonuses(att, pow, defense, tough, mor):
        return int(att)+int(pow)+int(defense)+int(tough)+(int(mor)*2)

    def type_cost(total):
        print(unit._type.cost_modifier)
        return total*type_modifiers[unit._type.cost_modifier]

    def size_cost(total):
        return total*size_modifiers[unit._size.cost_modifier]

    def trait_cost(total):
        return total+trait_cost_total

    # experience_bonuses = calculate_experience_bonuses(experience_level)
    # equipment_bonuses = calculate_equipment_bonuses(equipment_level)
    # unit_type_bonuses = calculate_type_bonuses(unit_type)

    total_cost = 0
    total_cost = add_bonuses(unit.total_attack_bonus(), unit.total_power_bonus(), unit.total_defense_bonus(), unit.total_toughness_bonus(), unit.total_morale_bonus()*2)
    total_cost = type_cost(total_cost)
    total_cost = size_cost(total_cost)
    total_cost *= 10
    total_cost = trait_cost(total_cost)
    total_cost += 30

    print(total_cost)
    return total_cost
