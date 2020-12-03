'''Escreva um programa que leia dois numeros
inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor e o maior
- O segundo valor e o maior
- Nao existe valor maior, os dois sao iguais'''

number_1 = int(input('Type a number: '))
number_2 = int(input('Type a second number: '))

if number_1 > number_2:
    print('The number {} is the greatest.'.format(number_1))

elif number_2 > number_1:
    print('The number {} is the greatest.'.format(number_2))

else:
    print('The numbers mentioned above are equal.')

