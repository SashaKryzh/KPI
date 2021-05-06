
def minJumps(row):
    dp = [float('inf') for i in range(len(row))]
    dp[0] = 0

    for i in range(len(row) - 1):
        for jump in range(1, row[i] + 1):
            if i + jump >= len(row):
                continue
            dp[i + jump] = min(dp[i + jump], dp[i] + 1)

    return dp[-1]


row = [2, 3, 1, 1, 4]
print(minJumps(row))

row = [1, 2, 4, 2, 5, 1]
print(minJumps(row))

row = [2, 1, 3, 1, 5]
print(minJumps(row))
