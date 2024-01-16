import json
import pygame
from pygame import*
from urllib.request import urlopen
import io

class Pokemon(pygame.sprite.Sprite):
    
    def __init__(self, data_file, index, level, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.load_from_json(data_file, index, level, x, y)

    def load_from_json(self, data_file, index, level, x, y):
        try:
            with open(data_file) as f:
                all_pokemon = json.load(f)
                self.json = all_pokemon[index]
        except Exception as e:
            print(f"Error loading Pokemon data: {e}")
            # You might want to handle the error in a different way

        self.name = self.json['name']
        self.level = level
        self.x = x
        self.y = y
        self.game = None
        self.num_potions = 3

        stats = self.json['stats']
        for stat in stats:
            if stat['stat']['name'] == 'hp':
                self.current_hp = stat['base_stat'] + self.level
                self.max_hp = stat['base_stat'] + self.level
            elif stat['stat']['name'] == 'attack':
                self.attack = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                self.defense = stat['base_stat']
            elif stat['stat']['name'] == 'speed':
                self.speed = stat['base_stat']

        self.types = [type['type']['name'] for type in self.json['types']]
        self.size = 150
        self.set_sprite('front_default')

    def set_game(self, game):
        self.game = game

    def set_sprite(self, side):
        try:
            image_path = self.json['sprites'][side]
            self.image = pygame.image.load(image_path).convert_alpha()

            scale = self.size / self.image.get_width()
            new_width = int(self.image.get_width() * scale)
            new_height = int(self.image.get_height() * scale)
            self.image = pygame.transform.scale(self.image, (new_width, new_height))
        except Exception as e:
            print(f"Error loading image for {self.name}: {e}")
            # You might want to set a default image or handle the error in another way

    def update(self):
        # Add any update logic or animations here
        pass

    def draw(self, alpha=255):
        sprite = self.image.copy()
        transparency = (255, 255, 255, alpha)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        self.game.blit(sprite, (self.x, self.y))

    def get_rect(self):

        return Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
