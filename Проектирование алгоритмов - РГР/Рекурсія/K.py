
def func():
    n = int(input())
    if n > 0:
        if n % 2 == 1:
            print(' ', n)
        func()


if __name__ == "__main__":
    func()
