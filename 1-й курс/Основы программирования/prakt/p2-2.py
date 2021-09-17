
N = int(input('N: '))
array = list(map(int, input("array: ").strip().split()))[:N]

max_index = 0
i = 1

while i < N:
	max_index = i if array[i] > array[max_index] else max_index
	i += 1

print('max_index =', max_index)
print('max =', array[max_index])

