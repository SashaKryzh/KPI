
def sqrt_binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid]**2 <= x and (mid >= high or arr[mid+1]**2 > x):
            return mid

        elif arr[mid]**2 > x:
            return sqrt_binary_search(arr, low, mid - 1, x)

        else:
            return sqrt_binary_search(arr, mid + 1, high, x)

    else:
        return -1


def sqrt(x):
    return sqrt_binary_search(list(range(0, (x // 2) + 1)), 0, x // 2, x)


if __name__ == '__main__':
    x = int(input())
    print(sqrt(x))
