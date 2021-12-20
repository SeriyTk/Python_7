x = 0
while x < 5:
    x += 1
    print(x, end=' ')

print()
a = int(input())
count = 0
b = 1
while count < a:
    count += 1
    b *= count
print(b)
print('------------------------------')
n = ' '
while len(n) < 5:
    y = input('Ввести данные: ')
    n += y
else:
    print(n)
