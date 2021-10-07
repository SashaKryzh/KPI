
#include <iostream>

int **createMatrix(int &rows, int &cols)
{
	printf("Enter matrix size 'rows cols': ");
	scanf("%d %d", &rows, &cols);
	if (rows <= 0 or cols <= 0)
	{
		printf("Wrong size\n");
		exit(0);
	}
	int **m = new int *[rows];
	std::srand(std::time(0));
	for (int i = 0; i < rows; i++)
	{
		m[i] = new int[cols];
		for (int j = 0; j < cols; j++)
			m[i][j] = std::rand() % 20 - 10;
	}
	return m;
}

void printMatrix(const int **matrix, const int rows, const int cols)
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
			printf("%4d", matrix[i][j]);
		printf("\n");
	}
}

void calculate11(const int **matrix, const int rows)
{
	int product = 0;
	for (int i = 0; i < rows; i++)
	{
		if (matrix[i][0] < 0 && matrix[i][0] % 2 == 0)
			product = product == 0 ? matrix[i][0] : product * matrix[i][0];
	}
	printf("Answear: %d\n", product);
}

int main(void)
{
	int rows, cols;
	int **matrix = createMatrix(rows, cols);
	printMatrix((const int **)matrix, rows, cols);
	calculate11((const int **)matrix, rows);
	for (int i = 0; i < rows; i++)
		delete[] matrix[i];
	delete[] matrix;
	return 0;
}