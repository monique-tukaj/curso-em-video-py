'''Crie um programa que leia o nome de uma cidade e diga
se ela comeca ou nao com o nome "SANTO".'''

city = input('Type a citys name: ').strip().upper() #The method upper is used to turn the input into upper letters.
x = city.split()
first_word = x[0] #After splitting the input typed, this line return the first word.
print(f"The city's name starts with Santo? \nAnswer: {'SANTO' in first_word}")