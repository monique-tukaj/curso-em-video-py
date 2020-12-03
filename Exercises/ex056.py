'''Desenvolva um programa que leia o nome, idade e seco de 4 pessoas.
No final do programa, mostre:
- A media de idade do grupo.
- Qual e o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.'''

sum_age = 0
average_age = 0
highest_age_m = 0
name_oldest_m = ''
woman_20 = 0
for person in range(1, 5):
    print(f'----- {person}ª Pessoa -----')
    user_name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender [F/M]: ')).upper().strip()
    sum_age += age
    if person == 1 and gender == 'M':
        highest_age_m = age
        name_oldest_m = user_name
    if gender == 'M' and age > highest_age_m:
        highest_age_m = age
        name_oldest_m = user_name
    if gender == 'F' and age < 20:
        woman_20 += 1
average_age = sum_age / 4
print('This group average age is {}.'.format(average_age))
print('The oldest man is {} years old and his name is {}.'.format(highest_age_m, name_oldest_m))
print('In total there are {} women with age less then 20 years old.'.format(woman_20))