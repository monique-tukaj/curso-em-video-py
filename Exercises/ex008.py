#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Digite um valor em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print('Você digitou {} metros, este valor convertido em centimetros é igual a {} e em milimetros {}.'.format(medida, centimetros, milimetros))