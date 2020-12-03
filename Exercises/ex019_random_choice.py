#Um profrssor quer sortear um dos seus alunos para apagar o quadro.
#faca um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = str(input('Digite o primeiro nome: '))
aluno2 = str(input('Digite o segundo nome: '))
aluno3 = str(input('Digite o terceiro nome: '))
aluno4 = str(input('Digite o terceiro nome: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))



