
def collect(cols, N, k):
    dp = [float('-inf') for i in range(N + 1)]
    dp[0] = cols[0]

    moves = [0 for i in range(N + 1)]

    for i in range(N):
        for s in range(1, k + 1):
            if i + s > N:
                continue

            temp = dp[i + s]

            dp[i + s] = max(dp[i] + cols[i + s], dp[i + s])

            if temp != dp[i + s]:
                moves[i + s] = i

    res = []
    i = N
    while True:
        res.append(i)
        i = moves[i]
        if i == 0:
            break

    return dp[N], res[::-1]


cols = [0, 2, 15, -1, 3, -10, 20, 3]
print(collect(cols, 5, 7))

cols = [0, -1, -2, -2, 0]
print(collect(cols, 4, 3))
