'''Refaca o desafio 009, mostrando a tabuada de um numero
 que o usuario escolher, so que agora utilizando um laco for'''

numero = int(input('Digite um numero para saber a sua tabuada: '))
print(50 * '=')
for c in range(1, 11):
    print('{} x {} = {}'.format(numero, c, (c * numero)))

print(50 * '=')