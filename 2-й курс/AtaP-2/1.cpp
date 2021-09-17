// SOURCE

// #include <conio.h>
// #include <iostream>
// using namespace std;

// void main()
// {
// 	int n = 20;
// 	int factorial = 1;

// 	// n! = 1*2*3...*n
// 	for (int i = 1; i <= n; i++)
// 		factorial *= i;

// 	cout << "The factorial of " << n << " is " << factorial << endl;

// 	getch();
// }

// FIXED

#include <iostream>
using namespace std;

int main()
{
	int n = 20;
	long factorial = 1; // Замінюємо на long, щоб уникнути Overflow

	for (int i = 1; i <= n; i++)
		factorial *= i; // Overflow змінної на 17-му кроці 

	cout << "The Factorial of " << n << " is " << factorial << endl;

	// MacOS не має conio.h 
	// https://stackoverflow.com/questions/8792317/where-is-the-conio-h-header-file-on-linux-why-cant-i-find-conio-h
	getchar();
}
