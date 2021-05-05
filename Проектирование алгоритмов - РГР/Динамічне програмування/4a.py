
def unboundedKnapsack(W, val, wt):
    dp = [0 for i in range(W + 1)]

    for i in range(W + 1):
        for j in range(len(val)):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[W]


W = 6
values = [26, 20, 50, 30]
weights = [2, 2, 5, 3]
print(unboundedKnapsack(W, values, weights))

W = 4
weights = [1, 1, 2, 2]
values = [1, 2, 4, 5]
print(unboundedKnapsack(W, values, weights))

W = 8
weights = [2, 3, 3, 4, 5, 6, 7]
values = [3, 5, 9, 2, 12, 2, 4]
print(unboundedKnapsack(W, values, weights))
