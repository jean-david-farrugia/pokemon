class Pokemon:
    def __init__(self, name, hp, level, attack_power, defense, type, evolution_level=None, evolution_name=None):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack_power = attack_power
        self.defense = defense
        self.type = type
        self.evolution_level = evolution_level
        self.evolution_name = evolution_name

    def evolve(self):
        if self.evolution_level is not None and self.level >= self.evolution_level:
            print(f"{self.name} est en train d'évoluer !")
            self.name = self.evolution_name
            self.attack_power += 10  # Increase stats upon evolution
            self.defense += 10
            print(f"Félicitations ! Votre {self.name} a évolué !")
        else:
            print(f"{self.name} n'est pas encore prêt à évoluer.")
