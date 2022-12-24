# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Input your number: '))

def fib(n):
    my_list = [0]
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, f1+f2
        my_list.append(f1)
        my_list.insert(0, -f1 if i%2 else f1)
    return my_list
print(fib(n))    