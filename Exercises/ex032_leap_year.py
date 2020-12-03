'''Faca um program que leia um ano qualquer e mostre se ele e bissexto.'''
from datetime import date
year = int(input('What year do you want to analyse? Input 0 to analyse the current year:  '))
if year == 0: #to return the analyse based in the current year, the user need to include 0
    year = date.today().year #to return the current year identified in the cumputer
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #all the conditions to identify a leap year.
    print('The year {} is a leap year.'.format(year))
else:
    print('The year {} is not a leap year.'.format(year))

