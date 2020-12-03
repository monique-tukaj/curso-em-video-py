'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre  uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

name = str(input('Inform your full name: ')).strip()
id = int(input('Inform your ID number: '))
velocity = float(input("Type a car's velocity: KM/H "))
if velocity > 80:
    calculation = abs(velocity - 80) * 7
    print('{} we have bad news, you have been fined. By exceeding {} km/h, the total amount of your speed ticket is R${}'.format(name, abs(velocity - 80),calculation))

else:
    print('Good news {}, you did not exceed the speed limit.'.format(name))
