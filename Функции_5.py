import math

PI = math.pi


def radius():
    n = float(input('Диаметр цилиндра в см: '))
    return n / 2


def height():
    return float(input('Высота цилиндра в см: '))


def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    return s * h



print(f'Объем цилиндра {volume():.2f} см3.')

def massa(g):
    n = float(input('Удельный вес цилиндра г\см3: '))
    return g * n / 1000
print(f'Вес цилиндра в килограммах {massa(volume()):.2f}.')
