from itertools import count
# функция печати разделителя


def print_sep():
    print('-'*100)


print_sep()


def show():
    print('функция')


show()


def show2():
    x = 7
    return x+10


y = show2()
z = show2() + 10
print(y)
print(z)
show()
print_sep()


def count_list(par, count=0):
    for i in par:
        count += 1
    return count


f = [1, 9, 7, 6, 3, 4, 8, 5]
print(count_list(f))
j = ['a', 'e', 'q', 'c']
print(count_list(j))
n = [5, 6, 3, 7, 8, 1, 55, 1, 2, 35]
print(count_list(n))
print_sep()


def exclusive_item(*args):
    new_list = []
    for i in args:
        for j in i:
            if j not in new_list:
                new_list.append(j)
    return new_list


x = [1, 8, 9, 2, 65, 47, 55, 55, 23, 77, 2]
f = [1, 2, 2, 8, 56, 55, 4, 5, 78, 77, 23, 2]
d = [5, 7, 8, 5, 6, 9, 3, 4, 5, 6, 2, 1, 7, 7, 7, 23, 55, 47, 6]

t = exclusive_item(x, f, d)
print(t)
print_sep()

# Пользователь вводит 3 числа. Найти минимальное число из них, максимальное число из них. Их сумму и вывести на экран.
# Использование встроенных функций
numbers = []
for i in range(3):
    number = int(input(f'Введите {i+1} число: '))
    numbers.append(number)

print(numbers)
print(f'Минимальное число = {min(numbers)}')
print(f'Максимальное число = {max(numbers)}')
print(f'{numbers[0]} + {numbers[1]} + {numbers[2]} = {sum(numbers)}')
print_sep()


# передача нескольких аргументов в функцию  по порядку
def greeting(say, *args):
    print(say, args)


greeting('Hello', 'Anna')
greeting('Hi', 'Max', 'Leo')
greeting('Nice to meet you', 'Lis', 'Max', 'Mari', 'Leo')
print_sep()

# передача нескольких аргументов в функцию по имени


def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age=20)
print_sep()

# Область видимости переменных во вложенных функциях
m = 'Меня видно везде'


def a():
    ma = 'Меня видно в b() и a() и c()'

    def b():
        print(m)
        print(ma)
        mb = 'Меня видно в c() и b(), но не видно в a()'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Меня видно только в c()'
            print(mc)
        c()
    b()


a()
print_sep()

# Передача функции параметром в другую функцию


def function():
    return 10


result = function()
print(result)

a = function   # передаем функцию в переменную
print(a())  # теперь мы можем вызвать функцию function с другим именем
print_sep()


def print_text():
    print('Работа функции из другой функции')


def to_function(parametr):  # принимает функцию как параметр
    parametr()          # вызываем параметр как функцию


# вызываем вторую функцию с параметром в виде первой функции
to_function(print_text)
print_sep()


def my_filter(numbers, function):   # создали универсальную функцию  для фильтрации чисел
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


def is_even(number):    # функция-условие, для нахождения четных чисел
    return number % 2 == 0


def is_not_even(number):    # функция-условие, для нахождения нечетных чисел
    return number % 2 != 0


def big_4(number):   # функция-условие, для нахождения чисел больше 4
    return number > 4


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)

print(my_filter(num, is_even))
print(my_filter(num, lambda number: number % 2 == 0))   # вместо функции-условия можно использовать lambda функцию
print(my_filter(num, is_not_even))
print(my_filter(num, lambda number: number % 2 != 0))   # вместо функции-условия можно использовать lambda функцию
print(my_filter(num, big_4))
print(my_filter(num, lambda number: number > 4))    # вместо функции-условия можно использовать lambda функцию
print_sep()

# функция sorted
numbers = [5,7,9,12,15,1,3,4,8,10]
print(numbers)
print(sorted(numbers))      # по возростанию
print(sorted(numbers,reverse=True))     # по убыванию