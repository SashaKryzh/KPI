#include <iostream>

void randArray(int *arr, const int size)
{
	for (int i = 0; i < size; i++)
		arr[i] = rand() % 51;
}

int **createMatrix(const int size)
{
	srand(time(0));
	int **matrix = new int *[size];
	for (int i = 0; i < size; i++)
	{
		matrix[i] = new int[size];
		randArray(matrix[i], size);
	}
	return matrix;
}

void printMatrix(const int **matrix, const int rows, const int cols)
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
			printf("%3d", matrix[i][j]);
		printf("\n");
	}
}

void shellSort(int *arr, const int size)
{
	for (int s = size / 2; s > 0; s /= 2)
	{
		for (int i = s; i < size; ++i)
		{
			for (int j = i - s; j >= 0 && arr[j] < arr[j + s]; j -= s)
			{
				int temp = arr[j];
				arr[j] = arr[j + s];
				arr[j + s] = temp;
			}
		}
	}
}

void shellSortTime(int *arr, const int size)
{
	int start = clock();
	shellSort(arr, size);
	int end = clock();
	std::cout << "Array of " << size << " elements was sorted in " << end - start << " ms" << std::endl;
}

void sortMatrix(int **matrix, const int size)
{
	int *temp = new int[size];
	for (int row = 0; row < size; row++)
	{
		for (int i = 0; i < size; i++)
			temp[i] = matrix[i][row];
		shellSort(temp, size);
		for (int i = 0; i < size; i++)
			matrix[i][row] = temp[i];
	}
	delete[] temp;
}

int main(void)
{
	int n;
	std::cout << "Enter matrix size (10 by subject): ";
	std::cin >> n;
	if (n <= 0)
		n = 10;

	std::cout << "Initial matrix:" << std::endl;
	int **matrix = createMatrix(n);
	printMatrix((const int **)matrix, n, n);

	std::cout << "\nSorted matrix:" << std::endl;
	sortMatrix(matrix, n);
	printMatrix((const int **)matrix, n, n);

	for (int i = 0; i < n; i++)
		delete[] matrix[i];
	delete[] matrix;

	std::cout << "\n--- Time tests ---" << std::endl;

	int t1[100];
	randArray(t1, 100);
	shellSortTime(t1, 100);

	int t2[500];
	randArray(t2, 500);
	shellSortTime(t2, 500);

	int t3[1000];
	randArray(t3, 1000);
	shellSortTime(t3, 1000);

	int t4[5000];
	randArray(t4, 5000);
	shellSortTime(t4, 5000);

	return 0;
}