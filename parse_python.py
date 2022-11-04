import os
import time

spisok = []
for adress, dirs, files in os.walk('C:\\Users\Пользователь\Desktop\пример'):
    spisok.append(adress)
print(spisok)


spisok = []
for adress, dirs, files in os.walk('C:\\Users\Пользователь\Desktop\пример'):
    for file in files:
        spisok.append(os.path.join(adress, file))
print(spisok)


spisok = []
for adress, dirs, files in os.walk('C:\\Users\Пользователь\Desktop\пример'):
    for file in files:
        full = os.path.join(adress, file)
        if ('.txt') in full:
            spisok.append(full)
print(spisok)


spisok = []
for adress, dirs, files in os.walk('C:\\Users\Пользователь\Desktop\пример'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)
print(spisok)
