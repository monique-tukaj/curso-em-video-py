#faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com
#5% de desconto.

price = float(input('Type the product"s price: R$'))
valor_final = (price * 0.05) - price
print('O valor total a ser pago com 5% de desconto é {:.2f}.'.format(abs(valor_final)))