d1 = {}
d2 = dict()
d3 = dict.fromkeys('1')

price = dict(мясо=3, хлеб=2, картофель=1, вода=0.5)


def buy():
    pay = 0
    while True:
        enter = input('Что покупаем? ')
        if enter == 'end':
            break
        pay += price[enter]
    return pay


print(buy())
