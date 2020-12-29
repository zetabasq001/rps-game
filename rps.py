#!/usr/bin/env python3

"""This program plays an expansion of the game of Rock, Paper, Scissors 
between two Players, and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

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


class HumanPlayer(Player):
    
    def move(self):
        response = input(f"What is your move? {Game.moves}\n")
        while response not in Game.moves:
            response = input(f"Please enter: {Game.moves}\n")
        return response


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
            self.memory = random.randint(0, len(Game.moves) - 1)
            return Game.moves[self.memory]
        else:
            return Game.moves[self.memory]

    def learn(self, my_move, previous_move):
        self.memory = (self.memory + 1) % len(Game.moves)
        
        
class Game:

    moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

    def __init__(self, p1, p2):
        self.round = 1
        self.p1 = p1
        self.p2 = p2


    def beats(self, one, two):
        
        print(f"Player 1: {one}  Player 2: {two}")

        winner = ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock') or
                (one == 'rock' and two == 'lizard') or
                (one == 'lizard' and two == 'spock') or
                (one == 'spock' and two == 'scissors') or
                (one == 'scissors' and two == 'lizard') or
                (one == 'lizard' and two == 'paper') or
                (one == 'paper' and two == 'spock') or
                (one == 'spock' and two == 'rock'))

        if one == two:
            print(f"Players Tie Round {self.round}: {one} == {two}\n")
        elif winner:
            print(f"Player 1 Wins Round {self.round}: {one} > {two}\n")
            self.p1.score += 1
        else:
            print(f"Player 2 Wins Round {self.round}: {two} > {one}\n")
            self.p2.score += 1

        print(f"Player 1 score {self.p1.score} | Player 2 score {self.p2.score}\n")
        print("==================================================================")
        self.round += 1

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.beats(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print("Game start!")
        print("Best of 7.")
        print("==================================================================")
       
        while self.p1.score != 4 and self.p2.score != 4:
            print(f"Round {self.round}")
            self.play_round()
        
        if self.p1.score == 4:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
