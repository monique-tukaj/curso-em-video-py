'''Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- se ele ainda vai se alistar ao servico militar.
- Se e a hora de se alistar.
- Se ja passou do tempo do alistamento.
Seu programa tambem devera mostrar quanto tempo
falta ou passou do prazo
Base ano atual do sistema'''

import datetime
from time import sleep
name = str(input('Insert your full name: ')).strip()
birth_year = int(input('Insert your birth year: '))

print("Hello, {} let's analyse the year you should enroll into the military service:  ".format(name))
print('PROGRESS...')
sleep(3)

year = datetime.date.today().year
if birth_year < year - 18:
    print('Dear {}, the time to enroll into the military service has passed.'.format(name))
    time = (birth_year + 18)
    print('The correct year to enlist it was {}.'.format(time))

elif birth_year == year - 18:
    print('Dead {}, is time to enlist into the military service.'.format(name))

else:
    time = abs((birth_year + 18) - year)
    print('Dear {}, is not yet time to enlist into the military service.\nYou still have {} years until then.'.format(name, time))

