
def search_peak(arr, low, high):
    if high >= low:
        mid = (high + low) // 2

        if (mid == 0 or arr[mid-1] < arr[mid]) and (mid == high or arr[mid+1] < arr[mid]):
            return mid

        elif mid != 0 and arr[mid-1] > arr[mid]:
            return search_peak(arr, low, mid - 1)

        else:
            return search_peak(arr, mid + 1, high)

    else:
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(search_peak(nums, 0, len(nums)-1))

    nums = [1, 2, 1, 3, 5, 6, 4]
    print(search_peak(nums, 0, len(nums)-1))
