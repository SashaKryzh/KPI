import string

digits = string.digits + string.ascii_uppercase

def int2base(n, base, recursion=False):
	if n == 0 and recursion:
		return
	int2base(n // base, base, recursion=True)
	print(digits[n % base], end=' ')

num = int(input('Введіть число: '))
base = int(input('Система числення: '))

int2base(num, base)
print()

