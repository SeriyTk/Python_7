def decor(arg):
    def wrapper():
        try:
            h = arg()
        except Exception:
            print('Повторите ввод')
            h = arg()
        return h
    return wrapper

@decor  # make = decor(make)
def make():
    enter = float(input('Введите число: '))
    return enter
@decor
def make2():
    enter = float(input('Введите число снова: '))
    return enter

make()
make2()