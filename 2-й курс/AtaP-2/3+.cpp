
#include <iostream>
#include <math.h>

int main(void)
{
	float a, b;
	scanf("%f%f", &a, &b);
	double c;
	std::cin >> c;
	printf("%f\n", powf((a + b) * c, 1.0 / 7));
	return 0;
}