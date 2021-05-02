
def collect(cols, N, k):
    dp = [float('-inf') for i in range(N + 1)]
    dp[0] = cols[0]

    for i in range(N):
        for s in range(1, k + 1):
            if i + s > N:
                continue
            dp[i + s] = max(dp[i] + cols[i + s], dp[i + s])

    return dp[N]


cols = [0, 2, 15, -1, 3, -10, 20, 3]
print(collect(cols, 5, 2))

cols = [0, -1, -2, -2, 0]
print(collect(cols, 4, 3))
