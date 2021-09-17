
def func():
    n = int(input())
    if n > 0:
        return max(n, func())
    else:
        return -1


if __name__ == "__main__":
    print('max: {}'.format(func()))
