'''Desenvolva um programa que pergunte a distancia
de uma viagem em km. Calcule o preco da passagem
cobrando R$0.50 por km para viagens de ate 200 km e R$0.45 para
viagens mais longas.'''

distance = float(input('Type the distance in Km: '))
if distance <= 200:
    print('Considering a travel of {:.0f} Km the total price will be R${:.2f}.'.format(distance, (0.50 * distance)))

else:
    print('Considering a travel of {:.0f} Km the total price will be R${:.2f}.'.format(distance, (0.45 * distance)))