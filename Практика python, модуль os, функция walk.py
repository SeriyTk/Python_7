import os
spisok = []
for adress, dirs, files in os.walk('F:\Гидропоника'):
    for file in files:
        spisok.append(os.path.join(adress,file))

print(spisok)
