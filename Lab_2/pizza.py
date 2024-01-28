# Определение класса Pizza
class Pizza:
    # Конструктор класса Pizza
    def __init__(self, dough, sauce, topping, price):
        self.dough = dough  # Тип теста
        self.sauce = sauce  # Соус
        self.topping = topping  # Начинка
        self.price = price  # Цена

    # Метод для представления объекта в виде строки
    def __str__(self):
        return f"{self.dough} тесто, {self.sauce} соус, {self.topping} начинка. Цена: {self.price}"

    # Метод для подготовки пиццы
    def prepare(self):
        return "Подготовка пиццы."

    # Метод для запекания пиццы
    def bake(self):
        return "Печка пиццы."

    # Метод для разрезания пиццы
    def cut(self):
        return "Разрезание пиццы."

    # Метод для упаковки пиццы
    def package(self):
        return "Упаковка пиццы."


# Подклассы пиццы
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Толстое", "Томатный", "Пепперони", 8.5)


class BarbecuePizza(Pizza):
    def __init__(self):
        super().__init__("Тонкое", "BBQ", "Курица", 9.5)


class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__("Тонкое", "Томатный", "Морепродукты", 10.5)


# Класс для заказа
class Order:
    def __init__(self):
        self.ordered_pizzas = []  # Список заказанных пицц

    # Метод для добавления пиццы в заказ
    def add_pizza(self, pizza):
        self.ordered_pizzas.append(pizza)

    # Метод для подсчета общей стоимости заказа
    def calculate_total(self):
        return sum(pizza.price for pizza in self.ordered_pizzas)


# Класс для терминала оформления заказов
class Terminal:
    def __init__(self):
        self.menu = {
            1: PepperoniPizza(),
            2: BarbecuePizza(),
            3: SeafoodPizza()
        }  # Меню доступных пицц

    # Метод для отображения меню
    def display_menu(self):
        for number, pizza in self.menu.items():
            print(f"{number}: {pizza}")

    # Метод для создания заказа
    def create_order(self):
        new_order = Order()  # Создание нового заказа
        while True:
            self.display_menu()
            choice = input("Выберите номер пиццы для добавления в заказ (готово или отмена для завершения): ")
            if choice.lower() == 'готово':
                break
            if int(choice) in self.menu:
                new_order.add_pizza(self.menu[int(choice)])
                print(f"Добавлена {self.menu[int(choice)].__class__.__name__} в ваш заказ.\n")
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.\n")
        return new_order

    # Метод для оформления заказа и оплаты
    def checkout(self, order):
        total = order.calculate_total()
        print(f"Ваш итог: ${total:.2f}")
        received_payment = float(input("Введите сумму оплаты: "))
        if received_payment >= total:
            print("Платеж принят. Спасибо!")
            change = received_payment - total
            if change > 0:
                print(f"Ваша сдача: ${change:.2f}")
            print("Подготовка вашего заказа...")
            for pizza in order.ordered_pizzas:
                print(pizza.prepare())
                print(pizza.bake())
                print(pizza.cut())
                print(pizza.package())
        else:
            print("Недостаточная оплата. Транзакция отменена.")


# Пример использования
terminal = Terminal()  # Создание терминала
order = terminal.create_order()  # Создание заказа
terminal.checkout(order)  # Оформление заказа
