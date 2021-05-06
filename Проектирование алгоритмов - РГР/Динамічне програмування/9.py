
def checkIsland(mat, i, j, N):
    if i < 0 or i == N or j < 0 or j == N or mat[i][j] == 0:
        return 0

    mat[i][j] = 0

    return 1 + checkIsland(mat, i + 1, j, N) \
        + checkIsland(mat, i - 1, j, N) \
        + checkIsland(mat, i, j + 1, N) \
        + checkIsland(mat, i, j - 1, N)


def func(matrix):
    mat = [line[:] for line in matrix]
    N = len(mat)

    max_area = 0
    count = 0

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                area = checkIsland(mat, i, j, N)
                max_area = max(max_area, area)
                count += 1

    return max_area, count


mat = [[0, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 1, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 1, 1, 0],
       [0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 0]]

print(func(mat))
