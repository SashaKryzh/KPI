
import math as m

n = 14 + 10
sum = 0

for i in range(1, n + 1):
	sum += 2**(-m.sqrt(i)) / m.sqrt(i)

print(sum)

