
def func(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return func(m - 1, 1)
    elif m > 0 and n > 0:
        return func(m - 1, func(m, n - 1))


if __name__ == "__main__":
    print(func(0, 0))
    print(func(2, 1))
    print(func(3, 2))
