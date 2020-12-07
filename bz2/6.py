
for i in range(1000, 10000):
	if sum([int(c) for c in str(i)]) == 15:
		print(i)

	