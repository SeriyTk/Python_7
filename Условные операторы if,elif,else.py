print(4 == 4)
print(4 == 5)
x = -3
if x == 0:
    print('if')
elif x > 0:
    print('elif')
else:
    print('else')

print()
x = "5"
if x == 0:
    x = 1
    print('x был равен 0.')
elif type(x) == int or type(x) == float:
    print('x допустимое значение.')
else:
    print("Другой тип данных.")
    x = 1

print(100/x)
