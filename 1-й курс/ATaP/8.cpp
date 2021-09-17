#include <iostream>

// Мені здалося, що так буде зручніше ніж використовувати switch
std::string g_months[12] = {
	"January", "February",
	"March", "April", "May",
	"June", "July", "August",
	"September", "October", "November",
	"December"};

int main()
{
	int n, k, sum;

	printf("n = ");
	scanf("%d", &n);
	printf("k = ");
	scanf("%d", &k);

	if (n < 1 || n > 12 || k < 1 || k > 12)
	{
		printf("n <= 12 and k <= 12\n");
		return 0;
	}

	sum = n + k - 1;

	// А ось приклад використання switch
	switch (sum > 12)
	{
	case true:
		printf("Next Year!\n");
		break;
	default:
		break;
	}

	printf("%s\n", g_months[sum % 12].c_str());

	return 0;
}
