class Combat:
    # Initialisation de la classe Combat
    def __init__(self, attacker, defender):
        self.attacker = attacker  # Le Pokemon qui attaque
        self.defender = defender  # Le Pokemon qui défend

    # Méthode pour obtenir le multiplicateur de dégâts en fonction du type de l'attaquant et du défenseur
    def get_damage_multiplier(self, attacker_type, defender_type):
        # Dictionnaire des multiplicateurs de dégâts en fonction des types de Pokemon
        type_multiplier = {"Eau": {"Terre": 0.5, "Feu": 2.0, "Normal": 1.0}, "Feu": {"Eau": 0.5, "Terre": 2.0, "Normal": 1.0}, "Terre": {"Feu": 0.5, "Eau": 2.0}, "Normal": 1.0}
        # Retourne le multiplicateur de dégâts pour les types donnés, ou 1.0 si aucun multiplicateur n'est défini
        return type_multiplier.get(attacker_type, {}).get(defender_type, 1.0)

    # Méthode pour infliger des dégâts au défenseur
    def inflict_damage(self):
        # Calcule le multiplicateur de dégâts en fonction des types de l'attaquant et du défenseur
        damage_multiplier = self.get_damage_multiplier(self.attacker.type, self.defender.type)
        # Calcule les dégâts à infliger
        damage = self.attacker.puissance_attaque * damage_multiplier
        # Inflige les dégâts au défenseur, en tenant compte de sa défense
        self.defender.points_de_vie -= max(damage - self.defender.defense, 0)

    # Méthode pour déterminer le gagnant du combat
    def get_winner(self):
        # Si l'attaquant n'a plus de points de vie, le défenseur est le gagnant
        if self.attacker.points_de_vie <= 0:
            return self.defender.nom
        # Si le défenseur n'a plus de points de vie, l'attaquant est le gagnant
        elif self.defender.points_de_vie <= 0:
            return self.attacker.nom
        # Si aucun des deux Pokemon n'est KO, il n'y a pas encore de gagnant
        else:
            return None

    # Méthode pour déterminer le perdant du combat
    def get_loser(self):
        # Si l'attaquant n'a plus de points de vie, l'attaquant est le perdant
        if self.attacker.points_de_vie <= 0:
            return self.attacker.nom
        # Si le défenseur n'a plus de points de vie, le défenseur est le perdant
        elif self.defender.points_de_vie <= 0:
            return self.defender.nom
        # Si aucun des deux Pokemon n'est KO, il n'y a pas encore de perdant
        else:
            return None

    # Méthode pour obtenir la puissance d'attaque de l'adversaire
    def get_opponent_attack_power(self):
        # Calcule le multiplicateur de dégâts en fonction des types de l'attaquant et du défenseur
        damage_multiplier = self.get_damage_multiplier(self.attacker.type, self.defender.type)
        # Retourne la puissance d'attaque de l'adversaire, multipliée par le multiplicateur de dégâts
        return self.defender.puissance_attaque * damage_multiplier
