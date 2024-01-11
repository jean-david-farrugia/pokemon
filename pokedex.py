import json

class Pokedex:
    # Initialisation de la classe Pokedex
    def __init__(self, filename="jsonpokedex.json"):
        self.filename = filename  # Nom du fichier contenant le Pokedex
        self.pokedex = self.load_pokedex()  # Charge le Pokedex à partir du fichier

    # Méthode pour charger le Pokedex à partir du fichier
    def load_pokedex(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)  # Charge le Pokedex à partir du fichier JSON
        except FileNotFoundError:
            return {}  # Si le fichier n'existe pas, retourne un Pokedex vide

    # Méthode pour sauvegarder le Pokedex dans le fichier
    def save_pokedex(self):
        with open(self.filename, "w") as file:
            json.dump(self.pokedex, file)  # Sauvegarde le Pokedex dans le fichier JSON

    # Méthode pour enregistrer un Pokemon dans le Pokedex
    def register_pokemon(self, pokemon):
        if pokemon.name not in self.pokedex:  # Vérifie si le Pokemon n'est pas déjà dans le Pokedex
            # Ajoute le Pokemon au Pokedex
            self.pokedex[pokemon.name] = {
                "name": pokemon.name,
                "hp": pokemon.hp,
                "level": pokemon.level,
                "attack_power": pokemon.attack_power,
                "defense": pokemon.defense,
                "type": pokemon.type
            }
            print(f"{pokemon.name} a été ajouté à votre Pokédex!")  # Affiche un message de confirmation
            self.save_pokedex()  # Sauvegarde le Pokedex
        else:
            print(f"{pokemon.name} est déjà dans votre Pokédex.")  # Affiche un message si le Pokemon est déjà dans le Pokedex

    # Méthode pour afficher le Pokedex
    def display_pokedex(self):
        for pokemon in self.pokedex.values():  # Parcourt tous les Pokemon dans le Pokedex
            print(pokemon)  # Affiche les informations du Pokemon
