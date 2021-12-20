m = [1, 2, 1, 3, 5, 'a', [1, 2]]
print(m[6])

print()
n = list(range(10))
l = []
for i in n:
    if i == 8:
        continue
    l += [i]
else:
    print(l)
