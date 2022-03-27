while True:
    try:
        enter = float(input('Введите число: '))
        break
    except ValueError:
        print("Это не число.")
