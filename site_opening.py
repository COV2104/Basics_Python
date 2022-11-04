import os

website = input('Введите сайт: ')

if 'https://' in website:
    os.system('start ' + website)
    print('if')
elif 'www.' in website:
    website = 'https://' + website
    os.system('start ' + website)
    print('elif')
else:
    website = 'https://www.' + website
    os.system('start ' + website)
    print('else')

