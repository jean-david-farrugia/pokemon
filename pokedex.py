import json

class Pokedex:
    def __init__(self, filename="pokedex.json"):
        self.filename = filename
        self.pokedex = self.load_pokedex()

    def load_pokedex(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_pokedex(self):
        with open(self.filename, "w") as file:
            json.dump(self.pokedex, file)

    def register_pokemon(self, pokemon):
        if pokemon.name not in self.pokedex:
            self.pokedex[pokemon.name] = {
                "name": pokemon.name,
                "hp": pokemon.hp,
                "level": pokemon.level,
                "attack_power": pokemon.attack_power,
                "defense": pokemon.defense,
                "type": pokemon.type
            }
            print(f"{pokemon.name} a été ajouté à votre Pokédex!")
            self.save_pokedex()
        else:
            print(f"{pokemon.name} est déjà dans votre Pokédex.")

    def display_pokedex(self):
        for pokemon in self.pokedex.values():
            print(pokemon)
