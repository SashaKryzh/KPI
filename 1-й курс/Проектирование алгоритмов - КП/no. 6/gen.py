import random

n = int(input())
array = [n] + [random.randint(-100, 100) for i in range(n)]

with open("input_{}.txt".format(n), "w") as file:
	file.write(' '.join([str(e) for e in array]))
	