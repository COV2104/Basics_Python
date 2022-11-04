from ast import For


array = [1, 5, 7, 8, 12, 15, 23]
print(array)
print('array[4] = ', array[4])  # выдаст элемент под индексом 4
print('длина массива = ', len(array))  # выдаст длину массива
print('последний элемент в массиве = ', array[-1])  # выдаст последний элемент в массиве
print('\n')

# массив состоящий из массивов:
l = [[1, 3, 5], ['a', 'n', 'd'], [1, 6, 9]]
print(l)
print('элемент массива ', l[2])
print('длина массива ', len(l))
print('обращение к элементу вложенного массива ', l[2][1])
l[0], l[1] = l[1], l[0]
print(l)
print('\n')

m = list(input('Введите элементы: '))   
print(m)
print('\n')

n = list(range(10))
print(n)
print('\n')

# массив в котором не будет восьмерки
k = list(range(10))
s = []  # пустой список в который мы будем добавлять значения
for i in k:
    if i == 8:
        continue
    s += [i]
else:
    print(s, end=' ')
print('\n')

# методы списка
massiv = [1, 3, 9, 25, 45, 9, 21, 22, 9, 10]  # объявляем и заполняем массив
print(massiv)
massiv.append(23)   # добавляет элемент в конец списка
print(massiv)
del massiv[5]
print(massiv)
massiv.insert(5, 8) # вставляет элемент по указанному индексу
print(massiv)
print(massiv.count(9))  # позволяет посмотреть сколько одинаковых элементов в списке (9-значение элемента)
massiv.sort()   # сортирует список по возростанию
print(massiv)
massiv.reverse()    # переварачивает массив в обратную сторону
print(massiv)
y = massiv.pop(3)   # удаляет элемент из списка (в скобках индекс удаляемого элемента, 
                    # если скобки пустые удаляется последний элемент), можно записать удаленный элемент в переменную
print(y)
print(massiv)
massiv.remove(9)    # удаляет элемент из списка по его значению (9-значение элемента)
print(massiv)
massiv.clear()  # полностью очищает список
print(massiv)
massiv.extend([3, 6, 9, 4, 5, 78, 12, 36, 11, 10])  # в конец списка добавляет значения из другого списка
print(massiv)
newarray = massiv.copy()    # копирует все данные из другого списка
print(newarray)
print('\n')

x = list(range(1, 21))
b = x.copy()
x1 = []

for i in x:
    if i % 2 == 0:
        x1.append(i)
        x.remove(i)
else:
    print(x)
    print(x1)
print (b)
print('\n')

# оператор in позволяет проверить есть элемент в всписе или нет
city = ['Milan', 'Moscow', 'Paris', 'Rom']
if 'Moscow' in city:
    print('есть')
print('\n')

# Программа winners, интерактивное награждение победителей
print('Соревнование по Python')
count = int(input('Введите количество участников: '))
i = count
members = []
while i >0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i-=1 
print('В соревновании участвовали: ',sorted(members)) 
members.reverse()
result = members[:3]
print('Победители: {}. Поздравляем!'.format(result)) 
print('\n')
