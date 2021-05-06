
def func(n):
    l = [[0, 0, 0] for i in range(n+1)]
    l[1] = [1, 1, 0]

    for i in range(2, n + 1):
        l[i][0] = l[i-1][0] + l[i-1][1] + l[i-1][2]
        l[i][1] = l[i-1][0]
        l[i][2] = l[i-1][1]

    return l[n][0] + l[n][1] + l[n][2]


print(func(int(input('N = '))))
