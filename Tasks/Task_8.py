# Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 8 -> 2, 4, 6, 8

num = int(input('Введите число: '))
num_even = 1

while num_even <= num:
    if num_even % 2 == 0:
        print(num_even, end='  ')
    num_even += 1
print('\n')
