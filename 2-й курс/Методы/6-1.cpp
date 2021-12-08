#include <cmath>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	float a, b, h, n;
	float X[100], Y[100], F[100];
	cout << " ZDR. Metod Eilera z utochnenyam:" << endl;
	cout << " y'=x+cos(y/3)" << endl
		 << endl;
	cout << " Vvedit promigok [a;b]:" << endl;
	cout << " a=";
	cin >> a;
	cout << " b=";
	cin >> b;
	cout << " Krok h=";
	cin >> h;
	cout << " Pochatkova umova: y(" << a << ")=";
	cin >> Y[0];
	X[0] = a;
	n = (b - a) / h;
	cout << endl
		 << " Tablytsya znachenʹ:" << endl;
	for (int i = 0; i <= n; i++)
	{
		X[i + 1] = X[i] + h;
		Y[i + 1] = Y[i] + h / 2 * (X[i] + cos(Y[i] / 3) + X[i + 1] + cos(Y[i] + h * (X[i] + cos(Y[i] / 3))));
		cout << " " << X[i] << '\t' << Y[i] << endl;
	}
	return 0;
}