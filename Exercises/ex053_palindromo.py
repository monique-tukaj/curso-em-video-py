'''Crie um programa que leia uma frase qualquer e diga se ela e um polindrogomo.
desconsiderando os espacos - Frase de frente para tras e de tras para frente sao a mesma coisa. '''

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()  # Separou a frase
junto = ''.join(palavras)  # Junto a frase sem espacos
inverso = junto[::-1]  # Do inicio ao fim de tras para frente.
print('O inverso de {} e {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')
