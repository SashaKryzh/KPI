import math as m

a = 1000
b = float(input('Введите b: '))

y = (m.pow(a + b, 3) - (m.pow(a, 3) + 3 * m.pow(a, 2) * b)) / (3 * a * m.pow(b, 2) + m.pow(b, 3))

print('y =', round(y, 10))



