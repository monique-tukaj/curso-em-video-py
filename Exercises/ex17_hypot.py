#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(x, y)
print('Com um cateto oposto de {:.2f} e um cateto adjacente de {:.2f} obtem-se uma hipotenusa de {:.2f}.'.format(x, y, hipotenusa))


'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hypotenusa = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hypotenusa))'''

