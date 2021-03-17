#include <math.h>
#include <iostream>

int main()
{
	float a = 5.1,
		  b = 1.2,
		  c = -0.3,
		  d = -3.1,
		  y;

	y = abs(acos(sqrt(c / d))) + 7 * log(pow(b, a));
	std::cout << "y = " << y << std::endl;

	return 0;
}

