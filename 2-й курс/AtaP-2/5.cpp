#include <iostream>
#include <string.h>

void processLine(char *s)
{
	for (int i = 0; s[i] != '\0'; i++)
	{
		if (!isdigit(s[i]))
			s[i] = '-';
	}
}

int main(void)
{
	char s[100];
	std::cout << "Enter string:\n";
	std::cin.getline(s, 100);
	processLine(s);
	std::cout << s << std::endl;
	return 0;
}