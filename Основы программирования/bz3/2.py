import math


def f(x):
    return math.sin(x) / x


n = int(input())
hashtable = {}

for _ in range(n):
    x = int(input())
    try:
        y = hashtable[x]
    except:
        y = f(x)
        hashtable[x] = y
    print('{} -> {}'.format(x, y))
