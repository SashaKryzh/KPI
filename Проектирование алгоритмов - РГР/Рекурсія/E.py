
def func(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + func(n // 10)


if __name__ == "__main__":
    print(func(10))
    print(func(-123))
    print(func(0))
    print(func(-12521634))
