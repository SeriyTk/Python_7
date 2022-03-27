price = dict(мясо=3, хлеб=2, картофель=1, вода=0.5)
new_price = dict()
for i in price:
    new_price[i] = round(price[i] * 0.85, 2)

    print(i, price[i])

print(price)
print(new_price)

x= price.items()
print(x)

for key, value in price.items():
    print(key)
    print(value)