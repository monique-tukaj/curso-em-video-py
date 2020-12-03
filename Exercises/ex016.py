#crie um programa que leia um numero Real qualquer e mostre na tela
# a sua porcao Inteira.
#ex. Digite um numero: 6.127 o numero 6.127 tem a parte inteira 6.

'''from math import trunc
num = float(input('Type any real number: '))
integer = trunc(num)
print('For the number {} its integer is {}.'.format(num, integer))'''

numero = float(input('Digite um valor: '))
print(f'O valor digitado foi {numero} e a sua parte inteira e {int(numero)}.')