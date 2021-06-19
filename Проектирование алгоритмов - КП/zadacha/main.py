
def Solve(arr):
    global N

    ans = [[] for _ in range(N)]
    given = []

    m = N
    i = 0
    while i < N:
        while arr[0] != m:
            given.append(arr.pop(0))
            i += 1

        ans[i].append(arr.pop(0))
        given.sort(reverse=True)
        while True:
            if len(given) and given[0] == ans[i][-1] - 1:
                ans[i].append(given.pop(0))
            else:
                m = ans[i][-1] - 1
                break

        i += 1

    return ans


N = int(input())
arr = list(map(int, input().split()))

out_ = Solve(arr)
for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
