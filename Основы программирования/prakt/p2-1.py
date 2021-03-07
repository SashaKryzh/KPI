import math as m

x = m.log10(0.005) + 1
b = 2**x - 1

a = float(input('Введіть a: '))

Y = (x**4 - x**2 - b) / (x - b) * (x**3 - x - a) / (x - a)

print('Y =', Y)



