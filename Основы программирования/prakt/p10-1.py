
def func1(a, b):
	"""
	Return 2 variables:
	first = a + b
	second = a - c
	"""
	return a + b, a - b

a = 5
b = 10

print('a: {}, b: {}'.format(a, b))
print(func1.__doc__)
a, b = func1(a, b)
print('a: {}, b: {}'.format(a, b))

