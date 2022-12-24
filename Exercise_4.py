# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Input your number: '))

my_list = []

while n != 0:
    n1 = n % 2
    my_list.insert(0, n1)
    n = n // 2
print(*my_list, sep='')
