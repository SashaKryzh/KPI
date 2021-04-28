
def search_help(arr, low, high, x, position='f'):
    '''
        position: f - first or l - last
    '''

    if high >= low:
        mid = (high + low) // 2

        if position == 'f' and arr[mid] == x and (mid == 0 or x > arr[mid-1]):
            return mid

        if position == 'l' and arr[mid] == x and (mid == high or x < arr[mid+1]):
            return mid

        if (position == 'f' and arr[mid] >= x) or (position == 'l' and arr[mid] > x):
            return search_help(arr, low, mid - 1, x, position=position)
        else:
            return search_help(arr, mid + 1, high, x, position=position)

    else:
        return -1


def search(arr, low, high, x):
    return (search_help(arr, 0, len(arr)-1, x, 'f'), search_help(arr, 0, len(arr)-1, x, 'l'))


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    print(search(nums, 0, len(nums)-1, 8))

    nums = [5, 7, 7, 8, 8, 10]
    print(search(nums, 0, len(nums)-1, 6))

    nums = [5, 7, 8, 8, 10]
    print(search(nums, 0, len(nums)-1, 5))
