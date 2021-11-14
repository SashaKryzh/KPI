#include <stdio.h>
#include <iostream>
#include <filesystem>

bool file_exists(const char *filename)
{
	FILE *f = fopen(filename, "r");
	if (f == NULL)
		return false;
	fclose(f);
	return true;
}

bool create_random_file()
{
	char newname[100];
	std::cout << "Enter new filename: ";
	std::cin.getline(newname, 100);
	if (file_exists(newname))
	{
		std::cout << "File already exists" << std::endl;
		return false;
	}
	FILE *f = fopen(newname, "wb");
	srand(time(0));
	for (int i = 0; i < 10; i++)
		fputc(rand() % 10, f);
	fclose(f);
	return true;
}

bool file_rename(const char *oldname)
{
	char newname[100];
	std::cout << "Enter new filename: ";
	std::cin.ignore();
	std::cin.getline(newname, 100);
	return rename(oldname, newname);
}

bool show_file(const char *filename)
{
	FILE *f = fopen(filename, "rb");
	if (f == NULL)
	{
		std::cout << "Error opening file: " << filename << std::endl;
		return false;
	}
	std::cout << filename << ": ";
	char c[2];
	while (fgets(c, 2, f) != NULL)
		std::cout << static_cast<int>(*c) << " ";
	std::cout << std::endl;
	fclose(f);
	return true;
}

bool process(const char *filename_1, const char *filename_2)
{
	if (file_exists(filename_2))
	{
		std::cout << filename_2 << " already exists.\n1 - rename\n* - continue\nEnter number: ";
		int choice;
		std::cin >> choice;
		if (choice == 1 && file_rename(filename_2))
		{
			std::cout << "Error renaming file" << std::endl;
			return false;
		}
	}
	FILE *f1 = fopen(filename_1, "rb");
	FILE *f2 = fopen(filename_2, "wb");
	fseek(f1, 0, SEEK_END);
	int size = ftell(f1);
	fseek(f1, 0, SEEK_SET);
	char *f1_data = new char[size];
	fread(f1_data, sizeof(char), size, f1);
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if (i != j && f1_data[i] == f1_data[j])
			{
				fputc(f1_data[i], f2);
				break;
			}
		}
	}
	delete[] f1_data;
	fclose(f1);
	fclose(f2);
	return true;
}

int main(int ac, char *av[])
{
	if (ac == 1)
	{
		create_random_file();
	}
	else if (ac == 3)
	{
		const char *f1 = av[1];
		const char *f2 = av[2];
		show_file(f1) && process(f1, f2) && show_file(f2);
	}
	return 0;
}