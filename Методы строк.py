s = 'Строка текста.'
print("Стр" in s)
print("Стрq" in s)
print(s.upper())
print(s.lower())
path = 'C:/Users/Desktop/s.py'
path1 = path.replace('/', '\\')
print(path1)

r = path1.split('\\')
print(r)
print(r[-1])

with open(r'G:\text1.txt', encoding='utf-8') as file_text:
    r = file_text.read()
    list_znk = ['(',')','"','\n']
    for i in list_znk:
        r = r.replace(i, ' ')
    print(r)
    r2 = r.split()
    print(r2)
    new_text = ' '.join(r2)
    print(new_text)
