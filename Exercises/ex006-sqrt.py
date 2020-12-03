#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
from math import sqrt
n1 = int(input('Digite um numero: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = sqrt(n1)
print('O numero digitado é {}.\n O dobro deste é {}, o seu triplo é {} e a raiz quadrada é {:.2f}.'.format(n1, dobro, triplo, raiz))