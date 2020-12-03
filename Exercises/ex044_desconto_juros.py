'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preco normal e condicao de paagamento:

- a vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% de juros

Adicionar opcao de pergunta dentro do if com input da quantidade
de parcelas.
acrescentar valores de parcela e desconto.'''



print('=' * 15 + ' MONALISA FASHION ' + '=' * 15)
item_price = float(input('Insert the total shopping: R$ '))
print('=' * 48)
print('PAYMENT METHODS')
print('[ 0 ] - Cash')
print('[ 1 ] - Debit')
print('[ 2 ] - 2x Credit Card')
print('[ 3 ] - 3x or more Credit Card')
print('=' * 48)

payment_m = int(input('Insert the payment: '))
if payment_m == 0:
    print('Payment method selected: CASH. The total payment is R${:.2f}.'.format(item_price - (item_price * 0.10)))
elif payment_m == 1:
    print('Payment method selected: DEBIT. The total payment is R${:.2f}.'.format(item_price - (item_price * 0.05)))
elif payment_m == 2:
    print('Payment method selected: CREDIT CARD. The total payment is R${:.2f}.'.format(item_price))
elif payment_m == 3:
    print('Payment method selected: CREDIT CARD 3x or more. The total payment is R${:.2f}.'.format(item_price + (item_price * 0.20)))
else:
    total = payment_m
    print('INVALID PAYMENT METHOD. TRY AGAIN.')
