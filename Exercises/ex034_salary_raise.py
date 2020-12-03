'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.
Para salarios superiors a R$1250, calcule um aumento de 10% e, para os inferiores um aumentos de 15%'''

name = input('Inform your name: ')
salary = float(input('Inform your salary: '))
if salary > 1250:
    print('Hello, {}. Good news, you will obtain 10% raise in your salary. The new income now is R${:.2f}.'.format(name, salary * 0.10 + salary))

else:
    print('Hello, {}. Good news, you will obtain 15% raise in your salary. The new income now is R${:.2f}.'.format(name, salary * 0.15 + salary))