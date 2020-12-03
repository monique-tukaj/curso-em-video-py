'''Faca um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e
 o menor peso lidos'''

numbers = []
for num in range(1, 6):
    weight = float(input(f'User number {num} type your weight: '))
    numbers.append(weight)
print(f'The smallest and the largest weight are {min(numbers)} KG and {max(numbers)} KG.')

