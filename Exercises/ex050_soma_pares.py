'''Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar , desconsidere-o. '''

s = 0
for a in range(1, 7):
    num = int(input('Digite o {} numero inteiro: '.format(a)))
    if num % 2 == 0:
        s += num
print('O somatorio dos numeros pares é {}.'.format(s))