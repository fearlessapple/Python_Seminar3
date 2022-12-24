# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

n = int(input('Input list size: '))

my_list = []

for i in range(n):
    my_list.append(float(input('Input number: ')))
print(f'my list = {my_list}')

def change_list(my_list):
    new_list = []
    for i in range(n):
        new_list.append(round(my_list[i] % 1, 2))
    return new_list
print(f'new list = {change_list(my_list)}')
print(f'diff = {round(max(change_list(my_list)) - min(change_list(my_list)), 2)}')    