#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos euros ela pode comprar.
#cotacao atual

valor = float(input('Digite a quantidade de dinheiro que deseja trocar em euro: R$'))
conversao = valor / 6.26
print('Com R$ {:.2f} poderá comprar €{:.2f}.'.format(valor, conversao))

#pesquisar demais moedas e tentar construir um site de conversao de moedas.