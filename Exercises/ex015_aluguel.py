#Escreva um programa que pergunte a quantidade de
# Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kilometros foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
v_aluguel = 60 * dias
v_km = km * 0.15

print('Com aluguel de {} dias e {:.0f} km rodados, o valor total a pagar sera de R${:.2f}'.format(dias, km, (v_aluguel + v_km)))