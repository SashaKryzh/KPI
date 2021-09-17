#include <iostream>

int main()
{
	float radius, x, y;

	std::cout << "Circle radius = ";
	std::cin >> radius;

	std::cout << "x = ";
	std::cin >> x;

	std::cout << "y = ";
	std::cin >> y;

	if (y <= -x)
	{
		if (sqrt(pow(x, 2) + pow(y, 2)) <= radius)
		{
			std::cout << "Yes" << std::endl;
			return 0;
		}
	}

	std::cout << "No" << std::endl;

	return 0;
}
