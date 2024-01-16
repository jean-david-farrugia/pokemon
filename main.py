import pygame
from pygame.locals import *
import time
import math
import random
import requests
from pokemon import Pokemon

pygame.init()



game_width = 500
game_height = 500
size = (game_width, game_height)
game = pygame.display.set_mode(size)
pygame.display.set_caption('pokemon')


black = (0,0,0)
gold = (218,165,32)
grey = (200,200,200)
green = (0,200,0)
red = (200,0,0)
white = (255, 255, 255)

level = 30
bulbasaur = Pokemon('jsonpokedex.json', 1, level, 25, 150)
pikachu = Pokemon('jsonpokedex.json', 0, level, 175, 150)
salameche = Pokemon('jsonpokedex.json', 2, level, 325, 150)
pokemons = [bulbasaur, pikachu, salameche]

for pokemon in pokemons:
    pokemon.set_game(game)

player_pokemon = None
rival_pokemon = None


game_status = 'select pokemon'
while game_status != 'quit':

    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = 'quit'

        if event.type == MOUSEBUTTONDOWN:

            mouse_click = event.pos

            if game_status == 'select pokemon':

                for i in range(len(pokemons)):

                    if pokemons[i].get_rect().collidepoint(mouse_click):

                        player_pokemon = pokemons[i]
                        rival_pokemon = pokemons[(i + 1) % len(pokemons)]

                        rival_pokemon.level = int(rival_pokemon * .75)

                        player_pokemon.hp_x = 275
                        player_pokemon.hp_y = 250
                        rival_pokemon.hp_x = 50
                        rival_pokemon.hp_y = 50

                        game_status = 'prebattle'




    if game_status == 'select pokemon':
        game.fill(white)

        bulbasaur.draw()
        pikachu.draw()
        salameche.draw()

        mouse_cursor = pygame.mouse.get_pos()
        for pokemon in pokemons:

            if pokemon.get_rect().collidepoint(mouse_cursor):
                pygame.draw.rect(game, black, pokemon.get_rect(), 2)
        
        pygame.display.update()

pygame.quit()