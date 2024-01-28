# Определение базового класса Транспортное_средство
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        # Вызывается исключение, если метод не был реализован в подклассе
        raise NotImplementedError("Метод 'move' должен быть реализован в подклассе")


# Подкласс для водных транспортных средств
class WaterVehicle(Vehicle):
    def move(self):
        return f"{self.name} двигается по воде"


# Подкласс для колесных транспортных средств
class WheeledVehicle(Vehicle):
    def move(self):
        return f"{self.name} двигается по дороге"


# Подкласс для автомобилей
class Car(WheeledVehicle):
    def __init__(self, name, brand):
        super().__init__(name)
        self.__brand = brand  # Приватный атрибут, марка автомобиля

    def move(self):
        return f"Автомобиль {self.__brand} ({self.name}) движется по дороге"
