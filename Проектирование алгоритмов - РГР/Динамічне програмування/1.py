
def count(N, k):
    res = [1, 1]
    for i in range(2, N + 1):
        j = 1
        temp = 0
        while j <= k and j <= i:
            temp += res[i-j]
            j += 1
        res.append(temp)
    return res[N-1]


N = int(input('N = '))
k = int(input('k = '))
print(count(N, k))
