class Combat:
    def __init__(self, attacker, defender):
        type_multiplier = {"Eau" : {"Terre":0.5, "Feu":2.0, 'Normal':1.0}, "Feu":{"Eau":0.5, "Terre":2.0, "Normal":1.0}, "Terre":{"Feu":0.5, "Eau":2.0}, "Normal":1.0}
        damage = attacker.attack * type_multiplier.get(attacker.type, {}).get(defender.type, 1.0)
        return int(damage)
    
    def apply_damage(defender, damage):
        defender.hp -= max(damage - defender.defense, 0)

    def determine_winner(pokemon, opponent):
        if pokemon.hp <= 0:
            return opponent.name
        elif opponent.hp <= 0:
            return pokemon.name
        else:
            return None