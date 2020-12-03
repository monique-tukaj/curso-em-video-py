'''Crie um programa que leia um numero inteiro e mostre
na tela se ele e PAR ou Impar'''

number = int(input('Digite um numero para saber se este é PAR ou IMPAR: '))
if number % 2 == 0:
    print('O numero {} é PAR.'.format(number))
else:
    print('O numero {} é IMPAR.'.format(number))
