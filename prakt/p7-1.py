import random

m = int(input('m: '))
k = None

while k is None or k < 3 or k > 10:
	k = int(input('k: '))

for i in range(m):
	if i != 0 and i % k == 0:
		print()
	print(random.randint(-11, 111), end=' ')
	
print()

