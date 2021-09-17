import timeit
import sys


def MergeSort(arr):
    if len(arr) == 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    MergeSort(left)
    MergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


filename = sys.argv[1]
with open(filename) as file:
    elements = [int(e) for e in file.readline().split(' ')]

array = elements[1:]
assert len(array) == elements[0]

test_array = array[:]

print('Initial array:')
print(array)
MergeSort(array)
print('Sorted array:')
print(array)

t = timeit.Timer(lambda: MergeSort(test_array))
print(t.repeat(5, 1000))