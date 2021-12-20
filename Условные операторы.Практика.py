import os
import time
while True:
    site = input('Название сайта: ')
    if site == 'завершить':
        break
    time.sleep(5)
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
