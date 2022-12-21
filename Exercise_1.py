# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

n = int(input('Input list size: '))

my_list = []

for i in range(n):
    my_list.append(int(input('Input number: ')))
print(f'my_list = {my_list}')

total = 0

for i in range(1, len(my_list), 2):
     total += my_list[i]
print(f'Sum = {total}')     