def calculate_cost(unit):
    trait_cost_total = 50

    def add_bonuses(att, pow, defense, tough, mor):
        return int(att)+int(pow)+int(defense)+int(tough)+(int(mor)*2)

    def type_cost(total):
        return total*unit._type.cost_modifier

    def size_cost(total):
        return total*unit._size.cost_modifier

    def trait_cost(total):
        return total+trait_cost_total

    total_cost = add_bonuses(unit.total_attack_bonus(), unit.total_power_bonus(), unit.total_defense_bonus(), unit.total_toughness_bonus(), unit.total_morale_bonus()*2)
    total_cost = type_cost(total_cost)
    total_cost = size_cost(total_cost)
    total_cost *= 10
    total_cost = trait_cost(total_cost)
    total_cost += 30

    return str(round(total_cost,2))
