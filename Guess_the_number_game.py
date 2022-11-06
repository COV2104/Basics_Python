# Легкий вариант:
from random import randint
number = randint(1, 100)
while True:
    user_number = int(input('Введите число: '))
    if number == user_number:
        print('Ура! Победа!')
        break
    elif number < user_number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')

# Добавление уровня сложности:
number1 = randint(1, 100)
user_number1 = None
count = 0
levels = {1: 10, 2: 6, 3: 3}
level = int(input('выберите уровень сложности от 1 до 3: '))
max_count = levels[level]
while number1 != user_number1:
    count += 1
    print(f'Попытка № {count}')
    if count > max_count:
        print('Вы проиграли')
        break
    user_number1 = int(input('Введите число: '))
    if number1 < user_number1:
        print('Ваше число больше загаданного')
    elif number1 > user_number1:
        print('Ваше число меньше загаданного')
else:
    print('Ура! Победа!')

# Игра для нескольких игроков
number1 = randint(1, 100)
user_number1 = None
count = 0
levels = {1: 10, 2: 6, 3: 3}
level = int(input('выберите уровень сложности от 1 до 3: '))
max_count = levels[level]
user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя {i+1} игрока: ')
    users.append(user_name)
is_winner = False
winner_name = None
while not is_winner:
    count += 1
    print(f'Попытка № {count}')
    if count > max_count:
        print('Все игроки проиграли')
        break
    for user in users:
        print(f'Ход игрока {user}')
        user_number1 = int(input('Введите число: '))
        if user_number1 == number1:
            is_winner = True
            winner_name = user
            break
        elif number1 < user_number1:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print('Ура! Победа!')
    print(f'Победитель {winner_name}!')
