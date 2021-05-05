
def king(mat):
    m, n = len(mat), len(mat[0])

    dp = [[float('inf') for j in range(n)] for i in range(m)]
    dp[0][0] = mat[0][0]

    for i in range(m - 1):
        for j in range(n - 1):
            # down
            if i + 1 < m:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + mat[i+1][j])

            # right
            if j + 1 < n:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + mat[i][j+1])

            # diagonal
            if i + 1 < m and j + 1 < n:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + mat[i+1][j+1])

    return dp[m-1][n-1]


mat = [[0, 1, 1, 3, 2],
       [1, 2, 1, 3, 2],
       [6, 1, 5, 3, 2],
       [10, 6, 1, 3, 2]]
print(king(mat))
