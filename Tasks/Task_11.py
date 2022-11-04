# Задача 11: Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.
# 456 -> 46
from random import randint, randrange
number = randint(100, 999)
number1 = int(number/100)
number3 = int(number % 10)
newnumber = number1*10+number3
print('Случайное трехзначное число: ', number)
print('Число с удаленной второй цифрой: ', newnumber)
