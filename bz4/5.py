
def minmax(a, b, c=None):
    nums = list(filter(lambda n: n is not None, [a, b, c]))
    return min(nums), max(nums)


def test(a, b, c=None):
    mi, ma = minmax(a, b, c)
    print('min: {}, max: {}'.format(mi, ma))


test(0, 0)
test(25, -12)
test(-10, -12)

print('---')

test(50, 12, 23)
test(12, 0, 34)
test(-123, 0, -12)
