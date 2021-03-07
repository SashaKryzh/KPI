
count = 0

print('Введіть послідовність:')

while True:
	n = int(input())
	if n > 0:
		count += 1
	elif n == 0:
		break
	else:
		continue

print('Кількість чисел =', count)


