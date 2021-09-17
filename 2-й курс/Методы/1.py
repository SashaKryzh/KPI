import math


def first(x, X):
    return abs(x - X) / X


print('sqrt(n1) = x1 ~ X1')
n1 = float(input('Input n1 = '))
X1 = math.sqrt(n1)
x1 = float(input('Input x1 = sqrt(n1) = '))
dx1 = first(x1, X1)
print('dx1={}'.format(dx1))

print('n2/N2 = x2 ~ X2')
n2 = float(input('Input n2 = '))
N2 = float(input('Input N2 = '))
X2 = n2 / N2
x2 = float(input('Input x2 = n2/N2 = '))
dx2 = first(x2, X2)
print('dx2={}'.format(dx2))

if dx1 < dx2:
    print("sqrt({}) is more accurate".format(n1))
else:
    print("{}/{} is more accurate".format(n2, N2))
