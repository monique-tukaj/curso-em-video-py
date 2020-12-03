'''Faca um programa que leia um numero  de 0 a 9999
e mostre na tela cada um dos digitos separados.
Ex.
Numero: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

number = int(input('Type a number up to 999: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print('Number: {}'.format(number))
print('Unit: {}'.format(u))
print('Ten: {}'.format(d))
print('Hundred: {}'.format(c))
print('Thousands: {}'.format(m))