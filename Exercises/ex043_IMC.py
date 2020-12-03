'''Desenvolva uma logica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida'''

weight = float(input('Insert your weight: (KG) '))
height = float(input('insert your height in: (m) '))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print('Dear user, your BMI is {:.2f}. Becareful, you are UNDERWEIGHT.'.format(bmi))
elif 18.5 <= bmi < 25:
    print('Dear user, your Body Mass index is {:.1f}. You have NORMAL weight.'.format(bmi))
elif 25 <= bmi < 30:
    print('Dear user, your Body Mass Index is {:.1f}. Your are OVERWEIGHT.'.format(bmi))
elif 30 <= bmi < 40:
    print('Dear user, your Body Mass Index is {:.1f}. Please, contact a doctor, you have OBESITY.'.format(bmi))
else:
    print('Dead user, your Body Mass Index is {:.1f}. Please, contact a doctor, you have MORBID OBESITY.'.format(bmi))
