class Deposit:
    def __init__(self, amount, rate, period):
        self.amount = amount  # Сумма вклада
        self.rate = rate  # Процентная ставка
        self.period = period  # Период вклада в годах

    def calculate_profit(self):
        raise NotImplementedError("Метод 'calculate_profit' должен быть реализован в подклассе")


class FixedDeposit(Deposit):
    def calculate_profit(self):
        return self.amount * self.rate * self.period / 100


class BonusDeposit(FixedDeposit):  # Наследуемся от FixedDeposit вместо Deposit
    def __init__(self, amount, rate, period, bonus_threshold, bonus_rate):
        super().__init__(amount, rate, period)
        self.bonus_threshold = bonus_threshold
        self.bonus_rate = bonus_rate

    def calculate_profit(self):
        profit = super().calculate_profit()  # Используем реализацию из FixedDeposit
        if self.amount > self.bonus_threshold:
            return profit + (profit * self.bonus_rate / 100)
        return profit


class CapitalizationDeposit(Deposit):
    def calculate_profit(self):
        return self.amount * ((1 + self.rate / 100) ** self.period - 1)


class DepositAdvisor:
    def advise(self, amount, period):
        # Логика для выбора типа вклада
        if amount < 10000:
            # Меньше 10000 - срочный вклад
            return FixedDeposit(amount, 5, period)
        elif amount < 20000:
            # Между 10000 и 20000 - бонусный вклад
            return BonusDeposit(amount, 4, period, 15000, 10)
        else:
            # Более 20000 - вклад с капитализацией
            return CapitalizationDeposit(amount, 3, period)
