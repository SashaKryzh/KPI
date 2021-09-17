
#include <iostream>

void printBits(unsigned int x)
{
	int MASK = 1 << (8 * sizeof(unsigned int) - 1);
	for (int i = 1; i <= 32; i++)
	{
		printf("%c", x & MASK ? '1' : '0');
		x <<= 1;
		if (i % 8 == 0)
			printf(" ");
	}
	printf("\n");
}

void function(unsigned int &x, unsigned int n, unsigned int p)
{
	while (n > 0) {
		x &= ~(1 << (p + n - 1));
		n--;
	}
}

int main()
{
	unsigned int x, n, p;

	printf("x = ");
	scanf("%u", &x);
	printf("n = ");
	scanf("%u", &n);
	printf("p = ");
	scanf("%u", &p);

	if (x < 0 || n < 0 || p < 0)
	{
		printf("Error\n");
		return 0;
	}

	if (p + n > 32)
	{
		printf("Error\n");
		return 0;
	}

	printBits(x);
	function(x, n, p);
	printBits(x);

	return 0;
}
