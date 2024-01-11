class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def get_damage_multiplier(self, attacker_type, defender_type):
        type_multiplier = {"Eau": {"Terre": 0.5, "Feu": 2.0, "Normal": 1.0}, "Feu": {"Eau": 0.5, "Terre": 2.0, "Normal": 1.0}, "Terre": {"Feu": 0.5, "Eau": 2.0}, "Normal": 1.0}
        return type_multiplier.get(attacker_type, {}).get(defender_type, 1.0)

    def inflict_damage(self):
        damage_multiplier = self.get_damage_multiplier(self.attacker.type, self.defender.type)
        damage = self.attacker.puissance_attaque * damage_multiplier
        self.defender.points_de_vie -= max(damage - self.defender.defense, 0)

    def get_winner(self):
        if self.attacker.points_de_vie <= 0:
            return self.defender.nom
        elif self.defender.points_de_vie <= 0:
            return self.attacker.nom
        else:
            return None

    def get_loser(self):
        if self.attacker.points_de_vie <= 0:
            return self.attacker.nom
        elif self.defender.points_de_vie <= 0:
            return self.defender.nom
        else:
            return None

    def register_pokemon(self, pokemon):
        pokedex = []
        pokedex.append(pokemon)
        print(f"{pokemon.nom} a été ajouté à votre Pokédex!")
        
    def get_opponent_attack_power(self):
        damage_multiplier = self.get_damage_multiplier(self.attacker.type, self.defender.type)
        return self.defender.puissance_attaque * damage_multiplier
