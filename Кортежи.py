x = (9, 8, 7, 6)
y = []
for i in range(len(x)):
    y.append(x[i] + 3)

print(y)
print(x)
t = list(x)
t[0] = 10
x = tuple(t)
print(x)
