import math


def first(x, X):
    return abs(x - X) / X


def fn_sqrt():
    # print('sqrt(n1) = x1 ~ X1')
    n1 = float(input('Input n1 = '))
    X1 = math.sqrt(n1)
    x1 = float(input('Input x1 = sqrt(n1) = '))
    dx1 = first(x1, X1)
    print('dx1={}'.format(dx1))
    return dx1, (n1,)


def fn_div():
    # print('n2/N2 = x2 ~ X2')
    n2 = float(input('Input n2 = '))
    N2 = float(input('Input N2 = '))
    X2 = n2 / N2
    x2 = float(input('Input x2 = n2/N2 = '))
    dx2 = first(x2, X2)
    print('dx2={}'.format(dx2))
    return dx2, (n2, N2)


def select():
    print('1: sqrt(n1) = x1 ~ X1\n2: n2/N2    = x2 ~ X2')
    while True:
        i = input('Your choice: ')
        if i == '1' or i == '2':
            return i


def show_result(inputs):
    if len(inputs) == 1:
        print("sqrt({}) is more accurate".format(inputs[0]))
    else:
        print("{}/{} is more accurate".format(inputs[0], inputs[1]))


dx1, inputs1 = fn_sqrt() if select() == '1' else fn_div()
dx2, inputs2 = fn_sqrt() if select() == '1' else fn_div()

if dx1 < dx2:
    show_result(inputs1)
else:
    show_result(inputs2)
