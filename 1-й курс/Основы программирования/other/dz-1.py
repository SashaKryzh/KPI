
def printNumber(n, recursion=False):
	if n < 0:
		n = -n
		print('-', end=' ')
	if n == 0 and recursion:
		return
	printNumber(n // 10, recursion=True)
	print(n % 10, end=' ')

number = int(input('Введіть число: '))
printNumber(number)
print()

