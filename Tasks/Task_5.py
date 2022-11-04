# Задача 5. Напишите программу, которая на вход принимает одно число (N), а на выходе показывает
# все целые числа в промежутке от -N до N.
# 4 -> "-4, -3, -2, -1, 0, 1, 2, 3, 4"

num = int(input('Введите число: '))
if num > 0:
    num = num
else:
    num = num*-1

startnum = -num
while startnum <= num:
    print(startnum, end='  ')
    startnum += 1
print('\n')
