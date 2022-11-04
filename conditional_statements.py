from random import randint
x = randint(-10,10)
if x == 0:
    print('x = 0')
elif x > 0:
    print('x > 0')
else:
    print('x < 0')


a = randint(-10,10)
if a > 0:
    a += 2
print('a = ',a)


y = randint(-10,10)

if y == 0:
    y = 1
    print('x был равен нулю')
elif type(y) == type(5) or type(y) == type(5.5):
    print('x допустимое значение')
else:
    y = 1
    print('x недопустимое значение')

print('100 / '+str(y)+' = '+str(100/y))

# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

print('Медицинская анкета:')
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
age = int(input('Введите свой возраст: '))
weight = int(input('Введите свой вес: '))
health_status = ''
if age < 30:
    if weight > 50 and weight < 120:
        health_status = 'Вы в хорошем состоянии'
    else:    
        health_status = 'Вам требуется заняться собой'
elif age >= 30 and age <= 40:
    if weight < 50 or weight > 120:
        health_status = 'Вам требуется заняться собой'
    else:
        health_status = 'Вы в хорошем состоянии. Продолжайте следить за собой'    
else:
    if weight < 50 or weight > 120: 
        health_status = 'Вам необходим врачебный осмотр'  
    else:
        health_status = 'Вы в хорошем состоянии. Продолжайте следить за собой'         

print(name,' ',surname,', возраст - ',age,', вес - ',weight,' кг. ',health_status)
