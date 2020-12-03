'''Escreva um programa para aprovar o emprestimo bancario
para a compra de uma casa. O programa vai perguntar o valor da casa,
 o salario do comprador e em quantos anos ele vai pagar,

 Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30%
 do salario ou entao o emprestimo sera negado.'''

house_price = float(input('Insert the house"s price:R$ '))
income = float(input('Insert your monthly income: '))
year = int(input('How many year do you want to pay it: '))

monthly_instalment = house_price / (year * 12) #Here the house price was divided by the years and later divided by 12 to get the monthly payment.

if monthly_instalment >= income * 0.30:
    print('Considering an income of R$ {:.2f}, unfortunately the loan has been DENIED.'.format(income))

else:
    print('The monthly instalment is R$ {:.2f}. Considering an income of R$ {:.2f}, your loan has been APPROVED.'.format(monthly_instalment, income))