
def fibonacci(N):
    if N <= 0:
        raise Exception('Wrong input')
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)


N = int(input())
print(fibonacci(N))
