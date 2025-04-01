from HangMan.hangman import hangman_game
from TwoZeroFourEight import two_zero_four_eight_game

print("Which game do you want to play? ")
print("1. Hangman (guess a word) \n2. 2048")
game = int(input(""))
while game <= 0 or game > 2:
    game = int(input("Wrong input. Must be between 1 and 2. "))
games = [hangman_game, two_zero_four_eight_game]
games[game-1]()