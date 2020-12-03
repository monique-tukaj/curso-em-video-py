'''Crie um programa que leia duas notas de um aluno
e calcule sua media, mostrando uma mensagem no final,
de acordo com a media atingida:

- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media 7.0 ou superior: APROVADO'''


grade_1 = float(input('Insert the first grade: '))
grade_2 = float(input('Insert the second grade: '))
average = (grade_1 + grade_2) / 2
if average < 5:
    print('Dear student, the total average is {}. Study more, unfortunately you FAILED.'.format(average))

elif average >= 5 and average < 7:
    print('Dear student, the total average is {}. Study more, you need to recover.'.format(average))

elif average >= 7.0:
    print('Dear student, the total average is {}. GOOD JOB! You are APPROVED.'.format(average))
