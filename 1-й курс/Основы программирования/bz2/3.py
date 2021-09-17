
numbers = [int(input()) for i in range(3)]
strings = [str(n) for n in numbers]
sums = [sum([int(c) for c in n if c.isdigit()]) for n in strings]
print(numbers[sums.index(max(sums))])

