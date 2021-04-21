#include <iostream>

int main()
{
	int x, y, k;

	printf("k = ");
	scanf("%d", &k);

	for (x = 1; x <= 30; x++)
	{
		for (y = x; y <= 30; y++)
		{
			if (x * x + y * y == k * k)
			{
				printf("%d^2 + %d^2 = %d^2;  ", x, y, k);
			}
		}
	}
	printf("\n");

	return 0;
}