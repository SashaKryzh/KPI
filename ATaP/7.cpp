#include <iostream>

bool isUnderLine(int x, int y)
{
	return y <= -x;
}

bool isInCircle(int radius, int x, int y)
{
	return sqrt(pow(x, 2) + pow(y, 2)) <= radius;
}

int main()
{
	float radius, x, y;

	std::cout << "Circle radius = ";
	std::cin >> radius;

	std::cout << "x = ";
	std::cin >> x;

	std::cout << "y = ";
	std::cin >> y;

	if (isUnderLine(x, y) && isInCircle(radius, x, y))
	{
		std::cout << "Yes" << std::endl;
	}
	else
	{
		std::cout << "No" << std::endl;
	}

	return 0;
}
