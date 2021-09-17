import sys


def merge(A1, A2, dest):
    i = 0
    j = 0

    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            dest[i + j] = A1[i]
            i += 1
        else:
            dest[i + j] = A2[j]
            j += 1
    while i < len(A1):
        dest[i + j] = A1[i]
        i += 1

    while j < len(A2):
        dest[i + j] = A2[j]
        j += 1


def SortAndCountInv(A, B):
    if len(A) <= 1:
        return 0

    mid = len(A) // 2
    A1 = A[:mid]
    A2 = A[mid:]
    B1 = B[:mid]
    B2 = B[mid:]

    if len(A1) >= 1 and len(B2) >= 1:
        ans = SortAndCountInv(A1, B1) + SortAndCountInv(A2, B2)
    else:
        A.sort()
        B.sort()
        ans = 0

    index_A = index_B = 0
    for k in range(len(A) + len(B)):
        if A1[index_A] <= B2[index_B]:
            index_A += 1

            if index_A == len(A1):
                merge(A1, A2, A)
                merge(B1, B2, B)
                return ans

        else:
            index_B += 1
            ans += len(A1) - index_A

            if index_B == len(B2):
                merge(A1, A2, A)
                merge(B1, B2, B)
                return ans


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as file:
        matrix = [[int(e) for e in line.split(' ')] for line in file]

    user_1 = int(input('user 1 = '))
    A = matrix[user_1 - 1]
    user_2 = int(input('user 2 = '))
    B = matrix[user_2 - 1]

    print()
    print("Initial")
    print("A:", A)
    print("B:", B)

    print()
    print("Sorted")
    print("A:", A)
    print("B:", B)

    print()
    invs = SortAndCountInv(A, B)
    print("Inversions:", invs)
