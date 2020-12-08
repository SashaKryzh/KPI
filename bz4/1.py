
def foo(n):
    digits = []
    is_negative = False

    if n == 0:
        digits.append(0)
    elif n < 0:
        is_negative = True
        n = abs(n)

    while n != 0:
        digits.append(n % 10)
        n //= 10

    if is_negative:
        digits.append('-')

    print(*digits, sep=', ', end='; ')
    print('Number of digits = {}'.format(len(digits) - is_negative))


n = int(input())
foo(n)
