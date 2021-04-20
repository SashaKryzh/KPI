
def func(A, B):
    print(A, end=" ")
    if A < B:
        func(A + 1, B)
    elif A > B:
        func(A - 1, B)
    else:
        print()


if __name__ == "__main__":
    func(0, 0)
    func(10, -10)
    func(-10, 10)

    A = int(input('A = '))
    B = int(input('B = '))
    func(A, B)
