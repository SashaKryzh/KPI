
import sys


def median_of_three(A, p, r):
    mid = (p + r - 1) // 2
    a = A[p]
    b = A[mid]
    c = A[r - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, r - 1
    if b <= c <= a:
        return c, r - 1
    return a, p


def partition(A, p, r, isUseMedian=False):
    counter = 0
    i = p - 1
    if isUseMedian:
        pivot, pidx = median_of_three(A, p, r)
        A[r], A[pidx] = A[pidx], A[r]
    else:
        pivot = A[r]
    for j in range(p, r):
        counter += 1
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1, counter


def quicksort(A, p, r, pivot='l'):
    ''' pivot = l, f, m '''
    counter = 0

    if len(A) == 1:
        return A

    if p < r:
        if pivot == 'l':
            pi, counter = partition(A, p, r)
        elif pivot == 'f':
            A[p], A[r] = A[r], A[p]
            pi, counter = partition(A, p, r)
        else:
            pi, counter = partition(A, p, r, isUseMedian=True)

        counter += quicksort(A, p, pi - 1, pivot=pivot)
        counter += quicksort(A, pi + 1, r, pivot=pivot)

    return counter


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as file:
        array = [int(e) for e in file.readline().split(' ')]

    print('Initial array:')
    print(array)

    a1, a2, a3 = array[:], array[:], array[:]

    count = quicksort(a1, 0, len(array) - 1, pivot='l')
    print('Quicksorted (last) array (count = {}):'.format(count))
    print(a1)

    count = quicksort(a2, 0, len(array) - 1, pivot='f')
    print('Quicksorted (first) array (count = {}):'.format(count))
    print(a2)

    count = quicksort(a3, 0, len(array) - 1, pivot='m')
    print('Quicksorted (median) array (count = {}):'.format(count))
    print(a3)
