from abc import ABC, abstractmethod

class Clothes(ABC):
    instances = []

    def __init__(self, param):
        self.param = param
        Clothes.instances.append((self))

    @abstractmethod
    def cloth_consumption(self):
        pass

    def __del__(self):
        if self in Clothes.instances:
            Clothes.instances.remove(self)

class Coat(Clothes):
    @property
    def cloth_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)

class Costume(Clothes):
    @property
    def cloth_consumption(self):
        return round((self.param * 2 + 0.3) / 100, 2)

coat1 = Coat(50)
costume1 = Costume(170)
costume2 = Costume(230)


total_cloth_consumption = 0
for wear in Clothes.instances:
    total_cloth_consumption += wear.cloth_consumption
print(f"total fabric consumption: {total_cloth_consumption}")

