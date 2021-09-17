
def func(road):
    res = 0

    for l in range(1, max(road)):
        i = 0
        while i < len(road) - 1:

            if road[i] >= l and road[i+1] < l:

                count = 0
                while i < len(road) - 1 and road[i+1] < l:
                    count += 1
                    i += 1

                if i < len(road) - 1 and road[i+1] >= l:
                    res += count

            i += 1

    return res


print(func([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(func([2, 0, 0, 1, 0, 3, 0, 1, 0]))
