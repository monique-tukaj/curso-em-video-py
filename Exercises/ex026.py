'''Faca um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posicao ela aparece a primeira vez
- Em que posicao ela aparece a ultima vez'''

phrase = str(input('Type a phrase: ')).upper().strip()
print(phrase.capitalize())
print('- Letters "A" in the phrase: {}'.format(phrase.count('A')))
print('- First letter "A" position: {}'.format(phrase.find('A')))
print('- Last letter "A" position: {}'.format(phrase.rfind('A')))