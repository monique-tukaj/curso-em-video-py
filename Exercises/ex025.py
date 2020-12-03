'''Crie um programa que leia o nome de uma pessoa e se
ela tem "SILVA" no nome.'''
name = str(input('Type your full name: ')).title() #in the end I added title to modify the first letter of each word to upper letter.
print('Does {} has "Silva" on its name? \nAnswer: {}'.format(name,'Silva' in name))