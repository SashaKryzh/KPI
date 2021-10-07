
#include <iostream>

void minmaxIndex(int arr[], int size, int &minIndex, int &maxIndex)
{
	minIndex = 0;
	int min = INT_MAX;
	maxIndex = 0;
	int max = INT_MIN;

	for (int i = 0; i < size; ++i)
	{
		if (arr[i] < min)
		{
			min = arr[i];
			minIndex = i;
		}
		if (arr[i] > max)
		{
			max = arr[i];
			maxIndex = i;
		}
	}
}

void printArray(int arr[], int size)
{
	std::cout << "Your array: ";
	for (int i = 0; i < size; ++i)
		std::cout << arr[i] << " ";
	std::cout << std::endl;
}

void inputArray(int arr[], int &size)
{
	std::cout << "Enter " << size << " numbers seperated by a new line:" << std::endl;
	for (int i = 0; i < size; ++i)
		std::cin >> arr[i];
}

int calculateProduct(int arr[], int minIndex, int maxIndex)
{
	if (maxIndex < minIndex)
	{
		int tmp = minIndex;
		minIndex = maxIndex;
		maxIndex = tmp;
	}

	minIndex++;
	int product = 0;
	while (minIndex < maxIndex)
	{
		product = product == 0 ? arr[minIndex] : product * arr[minIndex];
		minIndex++;
	}

	return product;
}

int main()
{
	int arr[10];
	int size = 10;
	inputArray(arr, size);

	int minIndex = 0, maxIndex = 0;
	minmaxIndex(arr, size, minIndex, maxIndex);

	int product = calculateProduct(arr, minIndex, maxIndex);

	printArray(arr, size);
	std::cout << "The product of numbers between min and max (" << minIndex << " and " << maxIndex << " indexes): "
			  << product << std::endl;

	return 0;
}