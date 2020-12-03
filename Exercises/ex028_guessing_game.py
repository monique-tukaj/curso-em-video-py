'''Escreva um programa que faca o computador "pensar" em um numero
inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero
escolhido pelo computador.
O programa deve escrever se o computador ganhou ou perdeu'''

from random import randint
from time import sleep
print('-=-' * 20)
print('Lets play a guessing game.')
number = int(input('Try to guess what did I think. Type a number from 0 to 5:'))
print('PROCESSING..')
sleep(3) #Used to delay the result display to make the game more interactive.

computer_choice = randint(0, 5) #faz o computador pensar em um numeroclea
if number == computer_choice:
    print('You got it right! The number is {}.'.format(computer_choice))
else:
    print('WRONG! The number is {}. Try again.'.format(computer_choice))

question = str(input('Do you wanna play again? ')).strip().upper()
while question == 'YES':
    print('=' * 25)
    number = int(input('Type a number from 0 to 5: '))
    computer_choice = randint(0, 5)
    if number == computer_choice:
        print('You got it right! The number is {}.'.format(computer_choice))
    else:
        print('WRONG! The number is {}. Try again.'.format(computer_choice))

else:
    print('END')