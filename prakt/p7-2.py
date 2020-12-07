import random

n = int(input('Введіть n: '))

a = int(input('Введіть a: '))
b = None
while b is None or b <= a:
	b = int(input('Введіть b: '))

array = [random.randint(a, b) for i in range(n)]

print('n: ', n, ', a: ', a, ', b: ', b, sep='')
print(array)

max_index = 0
positive_sum = None
calc_positive_sum = False

for i, n in enumerate(array):
	if abs(n) > abs(array[max_index]):
		max_index = i
	if calc_positive_sum:
		positive_sum = n if positive_sum is None else positive_sum + n
	if n > 0:
		calc_positive_sum = True

print('Номер максимального за модулем:', max_index)
print('Сума після першого додатнього:', positive_sum)

