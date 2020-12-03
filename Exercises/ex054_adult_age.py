'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda nao atingiram a maior idade (21) e quantos ja sao maiores.'''

import datetime  # importing this module enable to define the current year

year = datetime.date.today().year  # current year from this computer.
count_minor = 0
count_higher = 0
for x in range(1, 8):
    birth_year = int(input('What year the person {} born: '.format(x)))
    if birth_year > (year - 21):
        count_minor = count_minor + 1  # the "count" (line 6) starts with zero and this line of code will count 1 everytime the condition will be full filled.
    else:
        count_higher = count_higher + 1
print(f'In a group of 7 people, {count_higher} did achieve the adult age. ')
print(f'In a group of 7 people, {count_minor} did not achieve the adult age.')
