#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random


class Player:

    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    
    def move(self):
        return "rock"
    

class RandomPlayer(Player):

    def move(self):
        return random.choice(Game.moves)


class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.memory = []

    def move(self):
        if self.memory == []:
            return random.choice(Game.moves)
        else:
            return self.memory.pop()
        
    def learn(self, my_move, their_move):
        self.memory.append(their_move)
        

class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.memory = -1

    def move(self):
        if self.memory == -1:
            self.memory = random.randint(0, 2)
            return Game.moves[self.memory]
        else:
            return Game.moves[self.memory]

    def learn(self, my_move, previous_move):
        self.memory = (self.memory + 1) % len(Game.moves)
        
        
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    moves = ['rock', 'paper', 'scissors']

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(CyclePlayer(), ReflectPlayer())
    game.play_game()
