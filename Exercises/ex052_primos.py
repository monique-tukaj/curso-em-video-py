'''Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
Primo: Maior do que um e divisivel por um e por ele mesmo.'''

print('Verificando se um número é primo!')
numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='') #Se for divisivel pinta de amarelo
        tot += 1
    else:
        print('\033[31m', end='') #Se nao for divisivel ira pintar de vermelho
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(numero, tot))
if tot == 2:
    print('E por isso ele e PRIMO!')
else:
    print('E por isso ele NAO e PRIMO')


