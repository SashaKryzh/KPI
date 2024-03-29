
#include <stdio.h>

namespace MedicineType
{
	enum type
	{
		HOSPITAL = 0,
		CLINIC,
		AMBULATORY,
		PHARMACY,
		LABORATORY,
		URGENTCARE,
		ERROR,
	};
}

int main(void)
{
	MedicineType::type type;
	
	unsigned short shType;
	printf("HOSPITAL - 0\nCLINIC - 1\nAMBULATORY - 2\nPHARMACY - 3\nLABORATORY - 4\nURGENTCARE - 5\n\nSelect type: ");
	scanf("%hu", &shType);
	type = shType < MedicineType::ERROR ? (MedicineType::type)shType : MedicineType::ERROR;
	
	const char *s;
	switch (type)
	{
	default:
		s = "ERROR";
		break;
	case MedicineType::HOSPITAL:
		s = "HOSPITAL";
		break;
	case MedicineType::CLINIC:
		s = "CLINIC";
		break;
	case MedicineType::AMBULATORY:
		s = "AMBULATORY";
		break;
	case MedicineType::PHARMACY:
		s = "PHARMACY";
		break;
	case MedicineType::LABORATORY:
		s = "LABORATORY";
		break;
	case MedicineType::URGENTCARE:
		s = "URGENTCARE";
		break;
	}

	printf("%s\n", s);

	return 0;
}