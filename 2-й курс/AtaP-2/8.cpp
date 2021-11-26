#include <stdio.h>
#include <iostream>

struct Client
{
	int id;
	char surname[31];
	char firstname[31];
	char fathersname[31];
	short discount;

	Client(int id, const char *surname, const char *firstname, const char *fathersname, int discount) : id(id), discount(discount)
	{
		memmove(this->surname, surname, 30);
		memmove(this->firstname, firstname, 30);
		memmove(this->fathersname, fathersname, 30);
	}
};

void swapClients(Client &a, Client &b)
{
	Client temp = a;
	a = b;
	b = temp;
}

int partition(Client clients[], int low, int high)
{
	Client &pivot = clients[high];
	int i = (low - 1);

	for (int j = low; j <= high - 1; j++)
	{
		if (clients[j].id < pivot.id)
		{
			i++;
			swapClients(clients[i], clients[j]);
		}
	}
	swapClients(clients[i + 1], clients[high]);
	return (i + 1);
}

void quickSortClientsById(Client clients[], int low, int high)
{
	if (low < high)
	{
		int pi = partition(clients, low, high);
		quickSortClientsById(clients, low, pi - 1);
		quickSortClientsById(clients, pi + 1, high);
	}
}

void showClientsWithDiscount(Client *clients, int size, short discount)
{
	bool empty = true;
	for (int i = 0; i < size; i++)
	{
		Client &c = clients[i];
		if (c.discount == discount)
		{
			if (empty)
			{
				printf("%5s %30s %30s %30s %10s\n", "id", "Surname", "Firstname", "Fathersname", "Discount");
				empty = false;
			}
			printf("%5d %30s %30s %30s %9d%c\n", c.id, c.surname, c.firstname, c.fathersname, c.discount, '%');
		}
	}
	if (empty)
		printf("Empty\n");
}

int main(void)
{
	Client clients[] = {
		Client(1, "Pusharov", "Oleksii", "Alexander", 15),
		Client(49, "Kalapun", "Ostap", "Andriovych", 25),
		Client(2, "Michenko", "Zina", "Genadiivna", 5),
		Client(42, "Kryzhanovskyi", "Alexander", "Oleksiyovych", 10),
		Client(11, "Shevchenko", "Denys", "Petrovich", 10),
		Client(5, "Kozybunska", "Olga", "Alexandrovna", 20),
		Client(7, "Lytvynets", "Vadym", "Illych", 10),
		Client(32, "Lasheko", "Oleg", "Ostapovich", 10),
	};
	int size = sizeof(clients) / sizeof(Client);
	quickSortClientsById(clients, 0, size - 1);
	showClientsWithDiscount(clients, size, 10);
	return 0;
}