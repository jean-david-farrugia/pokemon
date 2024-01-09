class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def get_damage_multiplier(self, attacker_type, defender_type):
        type_multiplier = {"Eau": {"Terre": 0.5, "Feu": 2.0, "Normal": 1.0}, "Feu": {"Eau": 0.5, "Terre": 2.0, "Normal": 1.0}, "Terre": {"Feu": 0.5, "Eau": 2.0}, "Normal": 1.0}
        return type_multiplier.get(attacker_type, {}).get(defender_type, 1.0)

    def inflict_damage(self, defender, damage):
        defender.hp -= max(damage - defender.defense, 0)

    def get_winner(self, pokemon, opponent):
        if pokemon.hp <= 0:
            return opponent.name
        elif opponent.hp <= 0:
            return pokemon.name
        else:
            return None

    def get_loser(self, pokemon, opponent):
        if pokemon.hp <= 0:
            return pokemon.name
        elif opponent.hp <= 0:
            return opponent.name
        else:
            return None
       
    def register_pokemon(self, pokemon):
        pokedex = []
        pokedex.append(pokemon)
        print(f"{pokemon.name} a été ajouté à votre Pokédex!")
