
import random

def printMatrix(matrix):
	for row in matrix:
		print(' '.join([str(e) for e in row]))

n = int(input('Введіть n: '))
m = int(input('Введіть m: '))
a = int(input('Введіть a: '))
b = None
while b is None or a >= b:
    b = int(input('Введіть b: '))

matrix = [[random.randint(a, b) for j in range(m)] for i in range(n)]

print('m: {}, n: {}, a: {}, b: {}'.format(m, n, a, b))
printMatrix(matrix)

column_sum = [sum(e) for e in (zip(*matrix))]

print('Сума стовпців:')
print(column_sum)

