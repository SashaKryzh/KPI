
a = 5

x = float(input('Введіть x: '))

if a > 2 * x:
	print('a > 2x')
	y = (a + x**2) / a
elif a < 2 * x:
	print('a < 2x')
	y = abs(x**6 + a)**3
else:
	print('a == 2x')
	y = (x**2)**(1 / 3) * a

print('y =', y)


