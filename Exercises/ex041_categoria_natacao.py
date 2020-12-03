'''A confederacao nacional de natacao precisa de um programa
que leia o nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- ate 9 anos: MIRIM
- ate 14 anos: INFANTIL
- ate 19 anos: JUNIOR
- ate 20 anos: SENIOR
- acima: MASTER'''

import datetime
print("Let's analyse what category you are qualified to in the swimming team.")
birth_year = int(input('Insert your birth year: '))
year = datetime.date.today().year

if year - birth_year <= 9:
    print('Your category is BABY.')
elif year - birth_year <= 14:
    print('Your category is INFANT.')
elif year - birth_year <= 19:
    print('Your category is JUNIOR.')
elif year - birth_year <= 25:
    print('Your category is SENIOR.')
else:
    print('Your category is MASTER.')
