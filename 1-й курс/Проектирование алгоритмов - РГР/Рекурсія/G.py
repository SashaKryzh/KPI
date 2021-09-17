
def func(n):
    if n < 10:
        return str(n)
    else:
        return func(n // 10) + ' ' + str(n % 10)


if __name__ == "__main__":
    print(func(5))
    print(func(17))
    print(func(12521634))
