
def func(n):
	if n > 0:
		return '{} {}'.format(n % 10, func(n // 10))
	else:
		return ''


if __name__ == "__main__":
	print(func(5))
	print(func(17))
	print(func(12521634))
