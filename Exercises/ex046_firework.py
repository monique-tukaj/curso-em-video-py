'''Faca um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artificio,
indo de 10 ate 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep

import emoji
from emoji import emojize
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize('FELIZ ANO NOVO!! :fireworks:', use_aliases=True))