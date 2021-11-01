import numpy as np
from py_expression_eval import Parser

f1 = '1/sqrt(x-1)'
f2 = 'sin(x)/(x+1)'
f3 = '1/sqrt(0.5*x^2+1)'


def eval(f, x):
    return f.evaluate({'x': x})


def leftS(f, a, b, h):
    s = 0
    for x in np.arange(a, b, h):
        s += eval(f, x)
    s *= h
    return s


def rightS(f, a, b, h):
    s = 0
    for x in np.arange(a + h, b + h, h):
        s += eval(f, x)
    s *= h
    return s


def middleS(f, a, b, h):
    s = 0
    for x in np.arange(a, b, h):
        s += eval(f, x + h / 2)
    s *= h
    return s


def SimpsonS(f, a, b, h):
    s = 0
    s1 = 0
    s2 = 0
    for x in np.arange(a + h, b, h * 2):
        s1 += eval(f, x)
    for x in np.arange(a + h * 2, b - h, h * 2):
        s2 += eval(f, x)
    s = eval(f, a) + eval(f, b) + s1 * 4 + s2 * 2
    s *= h / 3
    return s


def TrapezoidS(f, a, b, h):
    s = 0
    for x in np.arange(a + h, b, h):
        s += eval(f, x)
    s += (eval(f, a) + eval(f, b)) / 2
    s *= h
    return s


def parseExpression():
    while True:
        try:
            f = Parser().parse(input('Expression: '))
            if f.variables() != ['x']:
                raise Exception()
            break
        except:
            print('Something wrong, please try again')
            continue
    return f


def calculate(f):
    print(f'\nf: {f.toString()}')
    a = float(input('a = '))
    b = float(input('b = '))
    n = float(input('n = '))
    h = (b - a) / n
    print(f'With method of left-hand rectangles S = {leftS(f, a, b, h)}')
    print(f'With method of right-hand rectangles S = {rightS(f, a, b, h)}')
    print(f'With mid-square method S = {middleS(f, a, b, h)}')
    print(f'With Simpson\'s method S = {SimpsonS(f, a, b, h)}')
    print(f'With method of trapezoids S = {TrapezoidS(f, a, b, h)}')
    print()


if __name__ == '__main__':
    while True:
        print(f'1 - {f1}\n2 - {f2}\n3 - {f3}\n4 - Input expression\n5 - Exit')
        n = input('Enter number: ')
        if (n == '1'):
            f = Parser().parse(f1)
        elif n == '2':
            f = Parser().parse(f2)
        elif n == '3':
            f = Parser().parse(f3)
        elif n == '4':
            f = parseExpression()
        elif n == '5':
            break
        else:
            print('Wrong input')
            continue

        try:
            calculate(f)
        except:
            print(
                'Something went wrong: sqrt of negative, division by zero or something else...\n')

    print('Have a nice day :)')
