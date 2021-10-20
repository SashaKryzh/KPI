
class Gazeta():
    name = "Газета"
    year = 2001
    pages = 25
    tyrage = 50000

    def set_name(self, n_name):
        self.name = n_name

    def set_year(self, n_year):
        self.year = n_year

    def set_pages(self, n_pages):
        self.pages = n_pages

    def set_tyrage(self, n_tyrage):
        self.tyrage = n_tyrage

    def __str__(self):
        return f"{self.name} ({self.year}): {self.pages} pages, {self.tyrage} tyrage"


obj1 = Gazeta()
print("Автоматично задані значення:")
print(obj1)
print("\nЗмінено назву:")
obj1.set_name("Київ")
print(obj1)

print("\nІнший об'єкт газети:")
obj2 = Gazeta()
obj2.set_name("Про Коронавірус")
obj2.set_year(2021)
obj2.set_pages(50)
obj2.set_tyrage(30000)
print(obj2)
