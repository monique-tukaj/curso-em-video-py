'''Crie um programa que faca o computador
jogar jokenpo com voce.'''

from random import choice
import emoji

print(emoji.emojize("Let's play JOKENPO :fist:, :hand:, :+1:", use_aliases=True))

print('=' * 40)
user = str(input('Choose "Rock", "Paper" or "Scissors": ')).strip().isupper()
list_1 = ['ROCK', 'SCISSORS', 'PAPER']
computer = choice(list_1)

if user == computer:
    print("DRAW, let's play again!")

elif computer == 'ROCK' and user == 'SCISSORS':
    print(emoji.emojize(':x: I won :stuck_out_tongue_winking_eye:! Try again.', use_aliases=True))

elif computer == 'SCISSORS' and user == 'PAPER':
    print(emoji.emojize(':x: I won :stuck_out_tongue_winking_eye:! Try again.', use_aliases=True))

elif computer == 'PAPEL' and user == 'PEDRA':
    print(emoji.emojize(':x: I won :stuck_out_tongue_winking_eye:! Try again.', use_aliases=True))

else:
    print(emoji.emojize('CONGRATS! You won :tada:', use_aliases=True))