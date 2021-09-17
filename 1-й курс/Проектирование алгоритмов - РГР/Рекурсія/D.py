
def func(n):
    if n == 1:
        print('YES')
    elif n > 1 and n < 2:
        print('N0')
    else:
        func(n / 2)


if __name__ == "__main__":
    func(1)
    func(2)
    func(3)
    func(64)
    func(127)
    func(128)
