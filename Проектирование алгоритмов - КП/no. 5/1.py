import argparse


# Завдання 1
def linearSearch(where, what):
    for i in where:
        if i == what:
            return i
    return None


# Завдання 2
def binirySearch(where, what):
    left, right, mid = 0, len(where) - 1, None
    while left <= right:
        mid = (left + right) // 2
        if where[mid] > what:
            right = mid - 1
        elif where[mid] < what:
            left = left + 1
        else:
            return where[mid]
    return None


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-l', '--linear', action='store_true')
group.add_argument('-b', '--biniry', action='store_true')
args = parser.parse_args()

search = linearSearch if args.linear else binirySearch

print('Вхідні дані:')

N, K = [int(item) for item in input().split()]
assert N > 0
assert K < 1000000

a1 = [number for number in [
    int(item) for item in input().split()] if abs(number) <= 1000000000]
a2 = [number for number in [
    int(item) for item in input().split()] if abs(number) <= 1000000000]
assert len(a1) == N
assert len(a2) == K

a1.sort()

print('Вихідні дані:')

for i in a2:
    if search(a1, i) is not None:
        print('YES')
    else:
        print('NO')
