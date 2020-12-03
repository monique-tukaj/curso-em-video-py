'''Faca um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e ultimo nome separadamente.'''
full_name = str(input('Type your full name: ')).strip()
name_split = full_name.split()
print('Full name: {}'.format(full_name))
print('First name: {}'.format(name_split[0]))
print('Last name: {}'.format(name_split[-1]))
