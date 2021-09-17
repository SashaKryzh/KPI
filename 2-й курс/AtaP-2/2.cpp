
#include <stdio.h>

namespace MedicineType
{
	enum type
	{
		HOSPITAL,
		CLINIC,
		AMBULATORY,
		PHARMACY,
		LABORATORY,
		URGENTCARE,
	};
}

int main(void)
{
	MedicineType::type type;
	scanf("%d", &type);
	return 0;
}