from ast import For


array = [1, 5, 7, 8, 12, 15, 23]
print(array)
print('array[4] = ', array[4])  # выдаст элемент под индексом 4
print('длина массива = ', len(array))  # выдаст длину массива
print('последний элемент в массиве = ', array[-1])  # выдаст последний элемент в массиве

# массив состоящий из массивов:
l = [[1, 3, 5], ['a', 'n', 'd'], [1, 6, 9]]
print(l)
print('элемент массива ', l[2])
print('длина массива ', len(l))
print('обращение к элементу вложенного массива ', l[2][1])
l[0], l[1] = l[1], l[0]
print(l)


m = list(input('Введите элементы: '))
print(m)


n = list(range(10))
print(n)

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


massiv = [1, 3, 9, 25, 45, 9, 21, 22, 9, 10]
print(massiv)
massiv.append(23)
print(massiv)
massiv.insert(5, 8)
print(massiv)
print(massiv.count(9))
massiv.sort()
print(massiv)
massiv.reverse()
print(massiv)
y = massiv.pop(3)
print(y)
print(massiv)
massiv.remove(9)
print(massiv)
massiv.clear()
print(massiv)
massiv.extend([3, 6, 9, 4, 5, 78, 12, 36, 11, 10])
print(massiv)
newarray = massiv.copy()
print(newarray)


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