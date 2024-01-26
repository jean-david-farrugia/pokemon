import pygame
import json


class Pokedex:
    
    def __init__(self, pokemon_data_file, rival_data_file):
        self.pokemon_data_file = pokemon_data_file
        self.rival_data_file = rival_data_file

    def update_rival_data(self, defeated_rival_name, new_sprite_path):
        try:
            with open(self.rival_data_file) as rival_file:
                rival_data = json.load(rival_file)

            rival_names = [pokemon['name'] for pokemon in rival_data]
            if defeated_rival_name not in rival_names:
                new_rival_data = {
                    "name": defeated_rival_name,
                    "sprites": {
                        "front_default": new_sprite_path
                    }
                }
                rival_data.append(new_rival_data)

            with open(self.rival_data_file, 'w') as updated_rival_file:
                json.dump(rival_data, updated_rival_file, indent=2)

            print(f"Rival data updated for {defeated_rival_name}.")
        except Exception as e:
            print(f"Error updating rival data: {e}")


    def display(self, game):
        with open(self.rival_data_file) as rival_file:
            rival_data = json.load(rival_file)
        for i, pokemon in enumerate(rival_data):
            sprite_path = pokemon['sprites']['front_default']
            sprite_image = pygame.image.load(sprite_path)

            new_size = (150, 150)

            sprite_image = pygame.transform.scale(sprite_image, new_size)

            sprite_rect = sprite_image.get_rect()
            sprite_rect.x = 10 + i * 100  
            sprite_rect.y = 30
            game.blit(sprite_image, sprite_rect)

            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render(pokemon['name'], True, (0, 0, 0))
            text_rect = text.get_rect(center=(sprite_rect.centerx, sprite_rect.bottom + 20))
            game.blit(text, text_rect)
