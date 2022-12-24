# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = int(input('Input list size: '))

my_list = []

for i in range(n):
    my_list.append(int(input('Input number: ')))
print(f'my list = {my_list}')

def my_list_multi(my_list):
    my_multi_list = []
    for i in range((n+1)//2):
        my_multi_list.append(my_list[i] * my_list[len(my_list)-1-i])
    return my_multi_list
print(f'my multi list = {my_list_multi(my_list)}')  
