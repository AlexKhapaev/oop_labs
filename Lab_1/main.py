from roman import Roman


if __name__ == '__main__':
    roman1 = Roman("XII")
    roman2 = Roman("VIII")

    # Сложение
    result_addition = roman1 + roman2
    print(f"{roman1.roman} + {roman2.roman} = {result_addition.roman}")  # Вывод: XII + VIII = XX

    # Вычитание
    result_subtraction = roman1 - roman2
    print(f"{roman1.roman} - {roman2.roman} = {result_subtraction.roman}")  # Вывод: XII - VIII = IV

    # Умножение
    result_multiplication = roman1 * roman2
    print(f"{roman1.roman} * {roman2.roman} = {result_multiplication.roman}")  # Вывод: XII * VIII = XCIV

    # Деление
    result_division = roman1 / roman2
    print(f"{roman1.roman} / {roman2.roman} = {result_division.roman}")  # Вывод: XII / VIII = I
