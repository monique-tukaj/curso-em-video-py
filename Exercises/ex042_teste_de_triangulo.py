'''
EQUILATERO - todos os lados iguais
ISOSCELES - dois lados iguais
ESCALENO - todos os lados diferentes
'''

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #Cada um dos lados deve ser menor que a soma dos outros dois.
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO! ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO.')
    elif r1 != r2 != r3 != r1: #Na diferenca todos os numeros devem ser testados, pois no fim o primeiro diferente pode ser igual ao ultimo
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR UM TRIANGULO.')
