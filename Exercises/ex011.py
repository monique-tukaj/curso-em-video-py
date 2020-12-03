#Faca um programa que leia a largura e a altura de uma parede em metros, calceule
# a sua area e a quantidade de tinta necessaria para pinta-la sabendo que
#cada litro de tinta pinta uma area de 2m quadrados.

largura = float(input('Insira o valor da altura: '))
altura = float(input('Insira o valor da largura:'))
area = (largura * altura)/2
print('Para pintar uma parede de dimensões {} x {} serão necessários {} litros de tinta.'.format(largura, altura, area))