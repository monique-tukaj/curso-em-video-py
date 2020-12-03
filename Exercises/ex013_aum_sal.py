#Faca um algoritmo que leia o salario de um funcionario e mostre seu novo
#salario, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$ '))
nsalario = (salario * 0.15) + salario
print('Com aumento de 15% o novo salário será de R${:.2f}.'.format(nsalario))