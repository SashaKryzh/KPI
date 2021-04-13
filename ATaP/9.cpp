#include <math.h>
#include <iostream>

float function(float x)
{
	return sqrt(abs(x + 3)) + 5.6 * x;
}

int main()
{
	float x;

	for (float t = 0; t <= 5; t += 0.25)
	{
		if (t <= 0.5)
			x = t + 8;
		else if (0.5 < t && t <= 1)
			x = sin(t);
		else
			x = log(t) + 2;
		printf("t = %f  :  y = %f\n", t, function(x));
	}
	
	return 0;
}