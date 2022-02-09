x = 5


def foo():
    x = 100
    return foo2(x)



def foo2(param):
    print(param)


foo()