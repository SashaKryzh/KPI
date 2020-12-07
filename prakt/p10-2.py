
import random

def squareMatrix(n):
	""" Returns square matrix of size n with random elements (1, 5) """
	return [[random.randint(1, 5) for j in range(n)] for i in range(n)]

def printMatrix(matrix):
	""" Prints matrix """
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

def minElementRow(matrix, n):
    """ Returns index of min element in row n """
    return matrix[n].index(min(matrix[n]))

def rotateRowByN(matrix, rowIndex, n):
	"""
	Rotates row IN-PLACE.
	matrix : matrix
	rowIndex : row to be rotated
	n : steps to rotate
	"""
	rotateSteps = n % len(matrix[rowIndex])
	row = matrix[rowIndex]
	matrix[rowIndex] = row[rotateSteps:] + row[:rotateSteps]

matrix = squareMatrix(3)  # Random matrix of size 3
printMatrix(matrix)

rrow = 1
minColIndex = minElementRow(matrix, rrow)  # Column index of min element in row
print('Index of min element in {} row is {}; min = {}'.format(
    rrow + 1, minColIndex, matrix[rrow][minColIndex]))

matrix_c = [row[:] for row in matrix]
# Rotate row by min element in row
rotateRowByN(matrix_c, rrow, matrix_c[rrow][minColIndex])
printMatrix(matrix_c)


