import json
import time
import math

 

class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

class Combat():
  
    TYPE_EFFECTIVENESS = {
    'water': {'water': 1, 'fire': 2, 'earth': 0.5, 'normal': 1, 'electric': 1, 'grass': 0.5},
    'fire': {'water': 0.5, 'fire': 1, 'earth': 2, 'normal': 1, 'electric': 1, 'grass': 2},
    'earth': {'water': 2, 'fire': 0.5, 'earth': 1, 'normal': 1, 'electric': 0.5, 'grass': 2},
    'normal': {'water': 0.75, 'fire': 0.75, 'earth': 0.75, 'normal': 1, 'electric': 1, 'grass': 1},
    'electric': {'water': 2, 'fire': 1, 'earth': 0.5, 'normal': 1, 'electric': 1, 'grass': 1},
    'grass': {'water': 2, 'fire': 0.5, 'earth': 2, 'normal': 1, 'electric': 1, 'grass': 1}
}

    def calculate_damage(self, opponent_type, attack_power):
        effectiveness = self.TYPE_EFFECTIVENESS[self.types[0]][opponent_type[0]]
        return attack_power * effectiveness
    
    def set_moves(self):
        self.moves = []
        for move in self.json['moves']:
            move_name = move['name']
            move_power = move['power']
            move_type = self.json['type']['name']  
            move = Move(move_name, move_power, move_type)
            self.moves.append(move)
    
    def perform_attack(self, other, move):
        from main import display_message
        display_message(f'{self.name} used {move.name}')

        time.sleep(1)

        damage = (2 * self.level + 10) / 250 * self.attack / other.defense * move.power
    
        if move.type in self.types:
            damage *= 1.5

        damage = math.floor(damage)

        other.take_damage(damage)

    def take_damage(self, damage):
        self.current_hp -= damage
    
