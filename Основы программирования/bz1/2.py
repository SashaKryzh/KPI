
def digits_sum(str):
	return sum([int(c) for c in str])

ticket = input()

first = ticket[:3]
last = ticket[3:]

if digits_sum(first) == digits_sum(last):
	print('Счастливый')
else:
	print('Обычный')

	