
def func():
    n = int(input())
    if n > 0:
        m = int(input())
        print(' ', n)
        if m > 0:
            func()


if __name__ == "__main__":
    func()
