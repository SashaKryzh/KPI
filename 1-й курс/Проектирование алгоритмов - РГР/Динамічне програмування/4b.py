
def knapsack(W, val, wt):
    dp = [[0 for x in range(W + 1)] for x in range(len(val) + 1)]

    for i in range(len(val) + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1]
                               + dp[i-1][w-wt[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[len(val)][W]


W = 6
values = [26, 20, 50, 30]
weights = [2, 2, 5, 3]
print(knapsack(W, values, weights))

W = 4
weights = [1, 1, 2, 2]
values = [1, 2, 4, 5]
print(knapsack(W, values, weights))

W = 8
weights = [2, 3, 3, 4, 5, 6, 7]
values = [3, 5, 9, 2, 12, 2, 4]
print(knapsack(W, values, weights))
