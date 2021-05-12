
#include <iostream>

int decimalToOctal(int n)
{
	if (n == 0)
		return 0;
	else
		return (n % 8) + (10 * decimalToOctal(n / 8));
}

int main()
{
	int n, octal;

	std::cout << "n = ";
	std::cin >> n;
	octal = decimalToOctal(n);
	std::cout << "Octal: " << octal << std::endl;

	return 0;
}