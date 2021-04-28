
def search(arr, l, h, key):
    if l <= h:
        mid = (l + h) // 2

        if arr[mid] == key:
            return mid

        # If arr[l...mid] is sorted
        if arr[l] <= arr[mid]:
            if key >= arr[l] and key <= arr[mid]:
                return search(arr, l, mid-1, key)
            return search(arr, mid + 1, h, key)

        # If arr[l..mid] is not sorted, then arr[mid... r] must be sorted
        if key >= arr[mid] and key <= arr[h]:
            return search(a, mid + 1, h, key)
        return search(arr, l, mid-1, key)

    else:
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    n = int(input())
    print(search(nums, 0, len(nums)-1, n))
