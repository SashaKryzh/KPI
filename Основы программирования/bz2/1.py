
while True:
	n = int(input())
	if n < 0:
		raise ValueError('Number is not positive')

	if n == 0:
		break
	elif n % 2 == 0 and n % 3 != 0:
		print('two')
	elif n % 2 != 0 and n % 3 == 0:
		print('three')
	elif n % 2 == 0 and n % 3 == 0:
		print('six')
	else:
		print('none')
	
print('Finish')

