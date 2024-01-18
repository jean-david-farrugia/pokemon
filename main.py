import pygame
from pygame.locals import *
import time
import random
from pokemon import Pokemon
import sys

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


def display_message(message):
    pygame.draw.rect(game, white, (10, 350, 480, 140))
    pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, black)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game.blit(text, text_rect)

    pygame.display.update()

def create_button(width, heigth, left, top, text_cx, text_cy, label):
    mouse_cursor = pygame.mouse.get_pos()
    button = Rect(left, top, width, heigth)

    if button.collidepoint(mouse_cursor):
        pygame.draw.rect(game, gold, button)
    else:
        pygame.draw.rect(game, white, button)

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'{label}', True, black)
    text_rect = text.get_rect(center=(text_cx, text_cy))
    game.blit(text, text_rect)

    return button

def display_menu():
    background = pygame.image.load("background.jpg")
    background_size = (500, 500)
    background = pygame.transform.scale(background, background_size)
    while True:
        game.blit(background,(0,0))
        font = pygame.font.Font(pygame.font.get_default_font(), 32)

        play_button = create_button(200, 80, 150, 150, 250, 190, 'Play')
        quit_button = create_button(200, 80, 150, 300, 250, 340, 'Quit')

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_click = event.pos
                if play_button.collidepoint(mouse_click):
                    return True
                elif quit_button.collidepoint(mouse_click):
                    pygame.quit()
                    sys.exit()



level = 30
bulbisar = Pokemon('pokemon.json', 1, level, 25, 15)
pikachu = Pokemon('pokemon.json', 0, level, 175, 15)
salameche = Pokemon('pokemon.json', 2, level, 325, 15)
chirazard = Pokemon('pokemon.json', 3, level, 25, 200)
pokemons = [bulbisar, pikachu, salameche, chirazard]

for pokemon in pokemons:
    pokemon.set_game(game)

player_pokemon = None
rival_pokemon = None

move_button = []

game_status = 'menu'
while game_status != 'quit':

    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = 'quit'

        if event.type == MOUSEBUTTONDOWN:

            mouse_click = event.pos
        

            if game_status == 'menu':
                play_game = display_menu()
                if play_game:
                    game_status = 'select pokemon'

            if game_status == 'select pokemon':

                for i in range(len(pokemons)):

                    if pokemons[i].get_rect().collidepoint(mouse_click):
                        player_pokemon = pokemons[i]
                        rival_pokemon = pokemons[:i] + pokemons[i+1:]
                        rival_pokemon = random.choice(rival_pokemon)

                        player_pokemon.hp_x = 275
                        player_pokemon.hp_y = 250
                        rival_pokemon.hp_x = 50
                        rival_pokemon.hp_y = 50

                        game_status = 'prebattle'

            elif game_status == 'player turn':

                if fight_button.collidepoint(mouse_click):
                    game_status = 'player move'

                if potion_button.collidepoint(mouse_click):
                    
                    if player_pokemon.num_potions == 0:
                        display_message('No more potion left') 
                        time.sleep(1)
                        game_status = 'player move'  
                    else:
                        player_pokemon.use_potion()
                        display_message(f'{player_pokemon.name} used potion')
                        time.sleep(1)
                        game_status = 'rival turn'

            elif game_status == 'player move':
                    
                for i in range(len(move_button)):
                    button = move_button[i]

                    if button.collidepoint(mouse_click):
                        if i < len(player_pokemon.moves):
                            move = player_pokemon.moves[i]
                            player_pokemon.perform_attack(rival_pokemon, move)

                if rival_pokemon.current_hp == 0:
                    game_status = 'fainted'
                else:
                    game_status = 'rival turn'
            else:
                print("Invalid move index.")

    if game_status == 'select pokemon':
        game.fill(white)

        pikachu.draw()
        bulbisar.draw()
        salameche.draw()
        chirazard.draw()

        mouse_cursor = pygame.mouse.get_pos()
        for pokemon in pokemons:
            

            if pokemon.get_rect().collidepoint(mouse_cursor):
                pygame.draw.rect(game, black, pokemon.get_rect(), 2)
        
        pygame.display.update()



    if game_status == 'prebattle':
        
        game.fill(white)
        player_pokemon.draw()
        pygame.display.update()

        player_pokemon.set_moves()
        rival_pokemon.set_moves()

        player_pokemon.x = 50
        player_pokemon.y = 200
        rival_pokemon.x = 350
        rival_pokemon.y = 20

        player_pokemon.size = 100
        rival_pokemon.size = 100
        player_pokemon.set_sprite('back_default')
        rival_pokemon.set_sprite('front_default')

        game_status = 'start battle'

    if game_status == 'start battle':
    
        game.fill(white)
        rival_pokemon.draw()
        display_message(f'Rival sent out {rival_pokemon.name}!')
        time.sleep(1)
        pygame.display.update()
            
        
    
        game.fill(white)
        rival_pokemon.draw()
        player_pokemon.draw()
        display_message(f'GO {player_pokemon.name}!')
        time.sleep(1)
        pygame.display.update()
        


        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

            
        game_status = 'player turn'

        pygame.display.update()

    

    if game_status == 'player turn':

        game.fill(white)
        player_pokemon.draw()
        rival_pokemon.draw()
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        fight_button = create_button(240, 140, 10, 350, 130, 412, 'Fight')
        potion_button = create_button(240, 140, 250, 350, 370, 412, f'Use potion({player_pokemon.num_potions})' )

        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

        pygame.display.update()

    if game_status == 'player move':
        game.fill(white)
        player_pokemon.draw()
        rival_pokemon.draw()
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()
        button_width = 240
        button_height = 70

        for i in range(len(player_pokemon.moves)):
            move = player_pokemon.moves[i]
            button_width = 240
            button_height = 70
            left = 10 + i % 2 * button_width
            top = 350 + i // 2 * button_height
            text_center_x = left + 120
            text_center_y = top + 35
            button = create_button(button_width, button_height, left, top, text_center_x, text_center_y, move.name.capitalize())
            move_button.append(button)

        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

        pygame.display.update()

    if game_status == 'rival turn':
        game.fill(white)
        player_pokemon.draw()
        rival_pokemon.draw()
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        display_message('')
        time.sleep(1)

        if hasattr(rival_pokemon, 'moves') and rival_pokemon.moves:
            move = random.choice(rival_pokemon.moves)
            rival_pokemon.perform_attack(player_pokemon, move)

        if player_pokemon.current_hp == 0:
            game_status = 'fainted'
        else:
            game_status = 'player turn'

        pygame.display.update()

    if game_status == 'fainted':

        game.fill(white)
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        if rival_pokemon.current_hp == 0:
            player_pokemon.draw()
            rival_pokemon.draw()
            display_message(f'{rival_pokemon.name} as fainted!')
        else:
            display_message(f'{player_pokemon.name} as fainted!')

        for pokemon in pokemons:
            pokemon.reset_hp()

        game_status = 'game over'

    if game_status == 'game over':
        game_status = 'menu'
            

        pygame.display.update()
   
        


pygame.quit()
