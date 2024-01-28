from deposit import DepositAdvisor


if __name__ == '__main__':
    # Пример использования
    advisor = DepositAdvisor()

    recommended_deposit = advisor.advise(7000, 2)
    print(f"Рекомендованный вклад: {type(recommended_deposit).__name__}")
    print(f"Ожидаемая прибыль: {recommended_deposit.calculate_profit()}")
