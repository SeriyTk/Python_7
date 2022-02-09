# x = [9, 8, 7, 6, 5]
# x.append(4)
# print(x)
# x.insert(1, 7)
# print(x)
# print(x.count(7))
# x.sort()
# print(x)
# x.reverse()
# print(x)
# y = x.pop(1)
# print(y)
# x.remove(7)
# x.clear()
# x.extend(['a','b'])
# c= x.copy()
# print(x)
# print(c)

m = [1, 2, 1, 3, 5, 'a', [1, 2]]
print(m[6])

print()
n = list(range(1, 21))
b = n[::2]
print(b)
l = []
for i in n:
    if i % 2== 0:
        l.append(i)
        n.remove(i)
else:
    print(l)
    print(n)

