# объявление словаря
# my_dikt = {key1:val1,key2:val2,key3:val3}

friend = {'name': 'Kate', 'age': 27}
print(friend)
print(friend['name'])   # получение значения по ключу
# добавление значения по ключу (словарь[ключ] = значение)
friend['has_car'] = True
print(friend)
friend['surname'] = 'Selizneva'
print(friend)
del friend['surname']   # удаление элемента по ключу
print(friend)
'name' in friend    # можно применять оператор in

# варианты перебора словаря
# по ключам
for key in friend.keys():
    print(key, ' - ', friend[key])

# по значениям
for val in friend.values():
    print(val)

# по парам ключ + значение
for item in friend.items():
    print(item)

for key,val in friend.items():
    print(key,'-',val)    
