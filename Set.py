# множества не содержат повторяющихся элементов
city = ['Moscow', 'Paris', 'Seul', 'Moscow', 'Paris', 'Las Vegas']
print(city)
cities = set(city)  # выводит список из уникальных значений
print(cities)
cities.add('Burma')  # добавление элемента
print(cities)
cities.remove('Moscow')  # удаление элемента
print(cities)
print(len(cities))
print('Seul' in cities)  # проверяет есть ли элемент в множестве

for city in cities:
    print(city, end=' ')
print('\n')

# семейная пара собирается в отпуск
# каждый из супругов взял с собой вещи
# Макс взял эти вещи:
max_things = {'Телефон', 'Рубашка', 'Бритва', 'Шорты'}
# Кейт взяла эти вещи:
kate_things = {'Телефон', 'Помада', 'Шорты', 'Сумочка'}
# Какие вещи взяли супруги?
print(max_things | kate_things)
# Какие вещи повторяются?
print(max_things & kate_things)
# Какие вещи взял Макс, но не взяла Кейт?
print(max_things-kate_things)
# Какие вещи взяла Кейт, но не взял Макс?
print(kate_things-max_things)
