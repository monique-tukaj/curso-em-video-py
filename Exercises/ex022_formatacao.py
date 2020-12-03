'''Crie um programa que leia o nome completo de
uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras no total (sem considerar espacos)
- Quantas letras tem o primeiro nome'''

name = input('Type your full name: ').strip()
total = name.split()  # The method split is used in order to separate the words
total2 = ''.join(total)  # The method join is used to connect the words back without space
print('Uppercase: {}'.format(name.upper()))
print('Lowercase: {}'.format(name.lower()))
print('Total letters: {}'.format(len(total2)))
print('Total letters: {}'.format(len(name) - name.count(' ')))
print('Total letter first name: {}'.format(name.find(' ')))
