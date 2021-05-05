
def king_min(a, b):
    m = min(a, b)
    return m, a != m


def king(mat):
    m, n = len(mat), len(mat[0])

    dp = [[float('inf') for j in range(n)] for i in range(m)]
    dp[0][0] = mat[0][0]

    moves = [[0 for j in range(n)] for i in range(m)]

    for i in range(m - 1):
        for j in range(n - 1):
            # down
            if i + 1 < m:
                dp[i+1][j], c = king_min(dp[i+1][j], dp[i][j] + mat[i+1][j])
                if c:
                    moves[i+1][j] = (i, j)

            # right
            if j + 1 < n:
                dp[i][j+1], c = king_min(dp[i][j+1], dp[i][j] + mat[i][j+1])
                if c:
                    moves[i][j+1] = (i, j)

            # diagonal
            if i + 1 < m and j + 1 < n:
                dp[i+1][j+1], c = king_min(dp[i+1]
                                           [j+1], dp[i][j] + mat[i+1][j+1])
                if c:
                    moves[i+1][j+1] = (i, j)

    res = []
    cell = (m-1, n-1)
    while True:
        res.insert(0, cell)
        cell = moves[cell[0]][cell[1]]
        if cell[0] == 0 and cell[1] == 0:
            break

    return dp[m-1][n-1], res


mat = [[0, 1, 1, 3, 2],
       [1, 2, 1, 3, 2],
       [6, 1, 5, 3, 2],
       [10, 6, 1, 3, 2]]
print(king(mat))
