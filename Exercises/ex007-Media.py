#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua media.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media >= 5:
    print('Parabéns, você foi aprovado! Média final {}.'.format(media))
else:
    print('Infelizmente você foi reprovado, estude mais! Média final {}.'.format(media))
