a = {1,2,3,'a','c',(1,2)}
b = set()
print(a)
z = {1,2,3,4,5}
x= {3,4,5,6,7}
z.add(8)
z.discard(9)
z.remove(8)
z.update(x)
y = z.union(x)
print(z)
print(y)