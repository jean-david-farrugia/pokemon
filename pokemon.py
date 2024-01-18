import json
import pygame
from pygame import*
import math
import time
from combat import Combat


green = (0,200,0)
red = (200,0,0)
black = (0,0,0)

class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

class Pokemon(pygame.sprite.Sprite, Combat):
    
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

    def use_potion(self):
        if self.num_potions > 0:

            self.current_hp += 30
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp

            self.num_potions -= 1


    def reset_hp(self):
        self.current_hp = self.max_hp

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

    def update(self):
        pass

    def draw(self, alpha=255):
        sprite = self.image.copy()
        transparency = (255, 255, 255, alpha)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        self.game.blit(sprite, (self.x, self.y))


    def draw_hp (self):
        bar_scale = 200 // self.max_hp
        for i in range(self.max_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(self.game, red, bar)

        for i in range(int(self.current_hp)):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(self.game, green, bar)

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, black)
        text_rect = text.get_rect()
        text_rect.x = self.hp_x
        text_rect.y = self.hp_y + 30
        self.game.blit(text, text_rect)



    def get_rect(self):

        return Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
