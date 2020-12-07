
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if max([a1, a2, b1, b2]) > 100:
    raise Exception('Wrong number')

if a1 > a2:
    a1, a2 = a2, a1
if b1 > b2:
    b1, b2 = b2, b1

a = set(range(a1, a2 + 1))
b = set(range(b1, b2 + 1))

print(len(a.intersection(b)))
