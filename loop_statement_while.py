x = 0
while x < 5:
    x += 1
    print(x)

# Вывод чисел от 1 до 100
number = 1
while number <= 100:
    print(number, end=', ')
    number += 1
print('\n')

# Вывод чисел от 1 до N
number = 1
num = int(input('Введите число N: '))
while number <= num:
    print(number, end=', ')
    number += 1
print('\n')

# Вывод четных чисел от 0 до N
number = 0
num1 = int(input('Введите число N: '))
while number <= num1:
    if number % 2 == 0:
        print(number, end=', ')
    number += 1
print('\n')

# Нахождение факториала

n = int(input('Введите число для нахождения факториала : '))
count = 0
factorial = 1

while count < n:
    count += 1
    factorial *= count

else:
    print(n, '! = ', factorial)
print('\n')


c = ''
while len(c) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue
    if y == 'l':
        break
    c += y
else:
    print(c)
print('\n')

# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых.
# И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

while True:
    num = int(input('Введите число : '))
    if num <= 0 or num >= 10:
        print('Число введено неверно. Введите число от 1 до 9.')
    else:
        print('Число в квадрате = ' + str(num*num))
        break
print('\n')
