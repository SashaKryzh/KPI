

def func(w):
    if len(w) == 0 or len(w) == 1:
        return True
    else:
        if w[0] == w[-1]:
            if len(w) == 2:
                return True
            else:
                return func(w[1:-1])
        else:
            return False


def run_func(w):
    print('YES' if func(w) else 'NO')


if __name__ == "__main__":
    run_func('')
    run_func('func')
    run_func('abcddcba')
    run_func('abcddcb')
    run_func('abcdcba')
