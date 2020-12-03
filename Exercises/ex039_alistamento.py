from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Voce tem que se alistar imediatamente.')

elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alitados ha {} anos.'.format(saldo))