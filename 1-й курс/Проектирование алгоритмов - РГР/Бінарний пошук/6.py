
def search(arr, low, high, x, k):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left: left + k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(search(nums, 0, len(nums)-1, 5, 3))

    nums = [1, 2, 3, 4, 5]
    print(search(nums, 0, len(nums)-1, 1, 4))
