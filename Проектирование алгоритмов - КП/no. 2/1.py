

def rec_sum(n):
	if n > 1:
		return (n + 1) / (2 * n + 5) + rec_sum(n - 1)
	else:
		return 2 / 7


n = int(input())
print('S = {}'.format(rec_sum(n)))



