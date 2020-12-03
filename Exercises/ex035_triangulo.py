'''Desenvolva um programa que leia o comprimeiro de tres retas e diga ao usuarios
se elas podem ou nao formar um triangulo'''
print('-=' * 20)
print('Analisador de triangulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #cada reta precisa ser menor do que a soma dos demais lados.
    print('Os segmentos acima podem formar triangulo! ')

else:
    print('O segmento acima nao podem formar um triangulo.')
