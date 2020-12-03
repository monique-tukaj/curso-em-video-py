'''Desenvolva um programa que leia o primeiro termos e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressao. Pesquisar sobre progressao aritmetica.'''

print('=' * 50)
frase = '10 TERMOS DE UMA PA'
print(frase.center(50,' '))
print('=' * 50)

termo = int(input('Primeiro Termo: '))
razao = int(input('Digite a razao: '))
decimo = termo + (10 - 1) * razao #Enesimo termo de uma PA, para encontrar o decimo termo da PA.

for c in range(termo, decimo + razao, razao):
    print(c, end=' ⮕ ')
print('Acabou', end=' ')
