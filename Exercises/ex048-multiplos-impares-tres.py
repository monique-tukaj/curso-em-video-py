'''Faca um programa que calcule a soma entre todos os numeros
impares que sao multiplos de tres e que se encontram no intervalo
de 1 ate 500.'''

soma = 0 #Aqui o contador começa com zero para que possa acumular números depois.
cont = 0 #O mesmo ocorre com o contador aqui
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados e {}.'.format(cont, soma))


