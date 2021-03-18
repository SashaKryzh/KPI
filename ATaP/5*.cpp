#include <math.h>
#include <iostream>

int main()
{
	float a, b, c, d, y;

	printf("a, b, c, d = ");
	scanf("%f %f %f %f", &a, &b, &c, &d);

	y = abs(acos(sqrt(c / d))) + 7 * log(pow(b, a));
	printf("y = %f\n", y);

	return 0;
}

