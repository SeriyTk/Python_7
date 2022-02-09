import os
spisok = []
for adress, dirs, files in os.walk(r'F:\Военка'):
    for file in files:
        full = os.path.join(adress, file)
        if ' .pdf' in full:
            spisok.append(full)
print(spisok)
