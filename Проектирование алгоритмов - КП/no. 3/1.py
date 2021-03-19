

def digits(number):
    i = 0
    while number > 0:
        number //= 10
        i += 1
    return i


def karatsuba(X, Y):
    global ad_plus_bc_count

    if X < 10 or Y < 10:
        return X * Y

    n = digits(max(X, Y))
    m = n // 2

    m2 = pow(10, m)
    Xl, Xr = X // m2, X % m2
    Yl, Yr = Y // m2, Y % m2

    ac = karatsuba(Xl, Yl)
    bd = karatsuba(Xr, Yr)
    ad_plus_bc = karatsuba((Xl + Xr), (Yl + Yr)) - ac - bd

    if ad_plus_bc in ad_plus_bc_count:
        ad_plus_bc_count[ad_plus_bc] += 1
    else:
        ad_plus_bc_count[ad_plus_bc] = 1

    return ac * 10**(2*m) + (ad_plus_bc * 10**m) + bd


ad_plus_bc_count = {}

X = int(input('X = '))
Y = int(input('Y = '))

print('Karatsuba: {}'.format(int(karatsuba(X, Y))))
print('Python:    {}'.format(X * Y))
for item in ad_plus_bc_count:
    print('\tad + bc = {} repeats {} times'.format(item, ad_plus_bc_count[item]))

