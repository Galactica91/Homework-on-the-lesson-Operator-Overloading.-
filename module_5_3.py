class House:
    houses_history = []
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
        House.houses_history.append(self.name)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __len__(self):
        print(self.numbers_of_floors)

    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __str__(self):
        print(f' Название {self.name}, Количество этажей {self.numbers_of_floors}')

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors and self.name == other.name

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors and self.name != other.name

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.numbers_of_floors + other)

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.numbers_of_floors + other)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.numbers_of_floors += other
            return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('Акация', 20)

print(h1 < h2)
print(h1 > h2)
print(h1 == h2)
print(h1 != h2)
print(h1 >= h2)
print()
h1 = h1 + 10
h1.__str__()
h1 += 10
h1.__str__()
h2 = 10 + h2
h2.__str__()

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)