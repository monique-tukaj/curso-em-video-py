'''Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores "M" ou "F". Caso este esteja errado, peça a digitação
novamente até ter um valor correto.'''



r = 'M' and 'F'
while r == 'F' or r == 'M':
    r = str(input('Type your gender? [F/M]')).upper().strip()
    if r != 'M' or r != 'F':
        print('Try one time, please. Gender not found')
    else:
        print(f'Gender {r} selected.')
print('Fim')