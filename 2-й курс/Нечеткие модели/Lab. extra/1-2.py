
class Gazeta():
    def __init__(self, name="Газета", year=2001, pages=25, tyrage=50000):
        self.name = name
        self.year = year
        self.pages = pages
        self.tyrage = tyrage

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_pages(self, pages):
        self.pages = pages

    def set_tyrage(self, tyrage):
        self.tyrage = tyrage

    def __str__(self):
        return f"{self.name} ({self.year}): {self.pages} pages, {self.tyrage} tyrage"


obj1 = Gazeta()
print("Автоматично задані значення:")
print(obj1)
print("\nЗмінено назву:")
obj1.set_name("Київ")
print(obj1)

print("\nІнший об'єкт газети (через init):")
obj2 = Gazeta("Про Коронавірус", 2021, 50, 30000)
print(obj2)
