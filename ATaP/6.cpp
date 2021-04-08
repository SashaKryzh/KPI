#include <iostream>

bool inputValue(char label)
{
	bool value;
	std::cin.clear();
	std::cout << label << " = ";
	std::cin >> value;
	return value;
}

int main()
{
	bool x, y, z, f;

	x = inputValue('x');
	y = inputValue('y');
	z = inputValue('z');

	f = x || !y && z || x && !y && !z || !(y && z);
	std::cout << f << std::endl;

	return 0;
}
