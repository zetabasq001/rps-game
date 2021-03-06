#!/usr/bin/env python3
import random

"""This program plays an expansion of the game of Rock, Paper, Scissors
between two Players, and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):

    def move(self):
        response = input(f"{', '.join(Game.moves)}? >  ").lower()
        while response not in Game.moves:
            response = input("\nPlease enter one of the following:\n"
                             f"{', '.join(Game.moves)}? >  ").lower()
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

        print(f"\nPlayer 1: {one}  Player 2: {two}")

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

        print()
        if one == two:
            print(f"Players Tie Round {self.round}: {one} == {two}\n")
        elif winner:
            print(f"Player 1 Wins Round {self.round}: {one} > {two}\n")
            self.p1.score += 1
        else:
            print(f"Player 2 Wins Round {self.round}: {two} > {one}\n")
            self.p2.score += 1

        print(f"Player 1 score {self.p1.score} | "
              f"Player 2 score {self.p2.score}\n")
        print("============================================="
              "=====================")
        self.round += 1

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.beats(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Best of 7.")
        print(f"Start Game:  {', '.join(Game.moves)}, Go!")
        print("============================================="
              "=====================")

        while self.p1.score != 4 and self.p2.score != 4:
            print(f"Round {self.round}")
            self.play_round()

        if self.p1.score == 4:
            print("Player 1 Wins Best of 7!")
        else:
            print("Player 2 Wins Best of 7!")

        print()
        print(f"Player 1 score {self.p1.score} | "
              f"Player 2 score {self.p2.score}\n")
        print("Game over!\n")


if __name__ == '__main__':

    opponents = [RockPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    player_names = ["Rock", "Random", "Reflect", "Cycle"]

    response = input("Choose your Opponent "
                     f"({', '.join(player_names)})? >  ").capitalize()
    while response not in player_names:
        response = input("\nPlease enter one of the following: \n"
                         f"{', '.join(player_names)}? >  ").capitalize()
    print()

    print("------------------------------------")
    print(f"Player 2 is {response} Player")
    print("------------------------------------")
    game = Game(HumanPlayer(), opponents[player_names.index(response)])
    game.play_game()
