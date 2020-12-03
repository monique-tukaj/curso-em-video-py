'''Faca um programa que leia tres numeros e mostre qual
e o maior e qual e o menor.'''

a = int(input('Type a number: '))
b = int(input('Type another number: '))
c = int(input('Type one more number: '))
# Verificando quem e o menor
menor = a  # considera o valor "a" como sendo o menor. Se este numero nao for o menor, imediatamente e substituido pelo menor.
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}.'.format(menor))

# Verificando quem e o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado e {}.'.format(maior))
