
def func(n):
    if n < 1:
        return
    if n > 1:
        func(n - 1)
    print(n)


if __name__ == "__main__":
    func(1)
    print()
    func(5)
