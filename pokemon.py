class Pokemon:
    # Initialisation de la classe Pokemon
    def __init__(self, name, hp, level, attack_power, defense, type, evolution_level=None, evolution_name=None):
        self.name = name  # Nom du Pokemon
        self.hp = hp  # Points de vie du Pokemon
        self.level = level  # Niveau du Pokemon
        self.attack_power = attack_power  # Puissance d'attaque du Pokemon
        self.defense = defense  # Défense du Pokemon
        self.type = type  # Type du Pokemon (par exemple, Feu, Eau, Plante, etc.)
        self.evolution_level = evolution_level  # Niveau auquel le Pokemon évolue
        self.evolution_name = evolution_name  # Nom de l'évolution du Pokemon

    # Méthode pour faire évoluer le Pokemon
    def evolve(self):
        # Vérifie si le Pokemon a un niveau d'évolution et si son niveau actuel est suffisant pour évoluer
        if self.evolution_level is not None and self.level >= self.evolution_level:
            print(f"{self.name} est en train d'évoluer !")
            self.name = self.evolution_name  # Change le nom du Pokemon pour son évolution
            self.attack_power += 10  # Augmente la puissance d'attaque du Pokemon lors de l'évolution
            self.defense += 10  # Augmente la défense du Pokemon lors de l'évolution
            print(f"Félicitations ! Votre {self.name} a évolué !")
        else:
            # Si le Pokemon n'est pas prêt à évoluer, affiche un message
            print(f"{self.name} n'est pas encore prêt à évoluer.")
