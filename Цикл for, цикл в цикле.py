x = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
y = input('Введите строку: \n')
for i in x:
    count = 0
    for j in y:
        if j == i:
            count += 1
    if count > 0:
        print(f'Букв {i} было {count}.')
