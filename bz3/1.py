
matrix = []
size = None

while True:
    string = input()
    if string == 'end':
        break
    row = [int(n) for n in string.split()]
    if size == None:
        size = len(row)
    elif len(row) != size:
        raise Exception('Wrong len(row)')
    matrix.append(row)

if len(matrix) != size:
    raise Exception('Wrong len(matrix)')

output = [row[:] for row in matrix]

for i in range(size):
    for j in range(size):
        s = 0
        s += matrix[(i - 1 + size) % size][j]
        s += matrix[(i + 1) % size][j]
        s += matrix[i][(j - 1 + size) % size]
        s += matrix[i][(j + 1) % size]
        output[i][j] = s

for row in output:
    print(' '.join(['{}'.format(n) for n in row]))
