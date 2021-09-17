import math as m

a = 10
b = 23
c = 2

x = int(input('Введите x: '))

y = m.pow(a * m.sqrt(b) - c * m.sqrt(x), 2) * (5.6 / (a + b + c))

print('y =', round(y, 10))