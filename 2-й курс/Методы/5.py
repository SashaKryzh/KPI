import numpy as np


# 3x^4+2x^3+x^2+x-5
def f(x): return 3*pow(x, 4) + 2*pow(x, 3) + pow(x, 2) + x - 5


# 12x^3+6x^2+2x+1
def df(x): return 12*pow(x, 3) + 6*pow(x, 2) + 2*x + 1


def Newton():
    a = float(input('a = '))
    b = float(input('b = '))
    e = float(input('e = '))

    a, b = min(a, b), max(a, b)
    i = 0
    print('Koreni:')
    for x in np.arange(a, b, e):
        y1 = f(x)
        y2 = f(x+e)
        if (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0):
            i += 1
            while True:
                x1 = x
                x2 = x1 - f(x1)/df(x1)
                q = np.fabs(x1 - x2)
                if (q < e):
                    print(f'x{i}={x1}')
                    break


def Bisection():
    a = float(input('a = '))
    b = float(input('b = '))
    e = float(input('e = '))

    a, b = min(a, b), max(a, b)
    p1 = a
    p2 = b
    p = (p1 + p2)/2
    if f(p1)*f(p2) > 0:
        print('Na zadanom intervali koreniv nema')
        return

    while True:
        if f(p1)*f(p) < 0:
            p2 = p
            p = (p1 + p2)/2
        else:
            p1 = p
            p = (p1 + p2)/2
        c = np.fabs((p1-p2)/2)
        if np.fabs(c <= 2*e):
            break

    print(f'Koren rivnjannja x={p}')


def main():
    while True:
        print('Menu')
        print('1 - Newton')
        print('2 - Bisection')
        print('0 - Exit')

        choice = input('Enter number: ')
        if (choice == '1'):
            Newton()
        elif (choice == '2'):
            Bisection()
        elif (choice == '0'):
            break
        else:
            print('Wrong input')

        print()

    print('Have a nice day :)')


if __name__ == '__main__':
    main()
