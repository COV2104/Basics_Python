x = input('Введите число: ')
r = int(x) + 5
print(r)

y = input('Введите число: ')
b = float(y) + 10
print(b)

a = float(input('Введите число: '))
b = float(input('Введите число: '))
result = a+b
print('Сумма а + b = '+ str(result))
print(str(a)+' + '+str(b)+' = '+ str(result))

# 1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и
# выведите результат на экран.

a = int(input('Введите число: '))
print(a,' + 2 = ',a+2)


ale = 71
age = int(input('Введите ваш возраст: '))

after20 = age + 20
print('Через 20 лет вам будет ',after20,' лет')

alive = ale - age
print('По статистике вам осталось жить ',alive)

count = 144000000
all_alive = count * ale
print('Среднее время жизни всех людей ',all_alive)

live_part = age/ale
print('Часть прожитой жизни ',live_part)
