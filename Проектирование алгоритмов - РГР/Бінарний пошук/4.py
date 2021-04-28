
def search(arr, l, h):
    mid = (l + h) // 2

    if h < l:
        return arr[0]

    if h == l:
        return arr[l]

    if mid < h and arr[mid+1] < arr[mid]:
        return arr[mid+1]

    if mid > l and arr[mid-1] > arr[mid]:
        return arr[mid]

    if arr[h] > arr[mid]:
        return search(arr, l, mid-1)
    return search(arr, mid+1, h)


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(search(nums, 0, len(nums)-1))

    nums = [4, 5, 6, 7, 0, 1, 2]
    print(search(nums, 0, len(nums)-1))

    nums = [0, 1, 2, 3, 4]
    print(search(nums, 0, len(nums)-1))
