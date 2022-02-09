import os
while True:
    site = input("Введите название сайта: ")
    if site == 'завершить':
        print("Программа завершена.")
        break
    if 'https://' in site:
        os.system('start ' + site)
        print('if')
    elif 'www.' in site:
        site = 'https://' + site
        os.system('start ' + site)
        print('elif')
    else:
        site = 'https://www.' + site
        os.system(f'start {site}')
        print('else')


