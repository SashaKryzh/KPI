
N = int(input())

if N <= 0:
    raise Exception('Число ненатуральне')

n = N
res = []
i = 2

while i * i < n:
    if n % i == 0:
        res.append(i)
        n //= i
    else:
        i += 1
if n > 1:
    res.append(n)

print('{} = '.format(N), end='')
print(*res, sep=' * ')
