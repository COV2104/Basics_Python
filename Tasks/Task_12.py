# Задача 12: Напишите программу, которая будет принимать на вход два числа и выводить,
# является ли второе число кратным первому. Если второе число не кратно числу первому,
# то программа выводит остаток от деления.
# 34, 5 -> не кратно, остаток 4
# 16, 4 -> кратн

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 % num2 == 0:
    print('Второе число является кратным первому')
else:
    print('Второе число не является кратным первому, остаток от деления = ', num1 % num2)