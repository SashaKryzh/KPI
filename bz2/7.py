
count = int(input())
sums = sum(range(1, count + 1))

for i in range(count - 1):
	card = int(input())
	if card > count:
		raise ValueError('Impossible card')
	sums -= card

print(sums)

