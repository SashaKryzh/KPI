import math


def rec_func(x, e, __p_x=1, __fact=0, __n=0):
	if __fact == 0:
		return 1 + rec_func(x, e, __fact=1, __n=1)

	__p_x = __p_x * x
	__fact = __fact * __n
	value = __p_x / __fact

	if abs(value) > e:
		return value + rec_func(x, e, __p_x=__p_x, __fact=__fact, __n=__n+1)
	else:
		return value

def iter_func(x, e):
	result = 1
	
	p_x = x
	value = math.inf
	fact = 1
	count = 1

	while abs(value) > e:
		count += 1

		value = p_x / fact
		result += value
		
		p_x *= x
		fact *= count
	
	return result


x = int(input('x: '))
e = float(input('e: '))

print(' Standart = {}'.format(math.exp(x)))
print('Recursion = {}'.format(rec_func(x, e)))
print('Iteration = {}'.format(iter_func(x, e)))


