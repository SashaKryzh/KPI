
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

isyes = sum([n > 0 for n in [a, b, c]]) == 1

if isyes:
	print('YES')
else:
	print('NO')

	