class Roman:
    # Словарь, который связывает римские цифры с их арабскими значениями.
    roman_numerals = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    def __init__(self, roman):
        # Инициализируем объект римским числом и преобразуем его в арабское значение.
        self.roman = roman
        self.arabic = Roman.to_arabic(roman)

    @staticmethod
    def to_arabic(roman):
        # Статический метод, который преобразует римское число в арабское.
        arabic = 0
        i = 0
        while i < len(roman):
            if i+1 < len(roman) and roman[i:i+2] in Roman.roman_numerals:
                arabic += Roman.roman_numerals[roman[i:i+2]]
                i += 2
            else:
                arabic += Roman.roman_numerals[roman[i]]
                i += 1
        return arabic

    @staticmethod
    def to_roman(arabic):
        # Статический метод, который преобразует арабское число в римское.
        roman = ''
        for r, a in Roman.roman_numerals.items():
            while arabic >= a:
                roman += r
                arabic -= a
        return roman

    def __add__(self, other):
        # Метод для операции сложения (+).
        return Roman(Roman.to_roman(self.arabic + other.arabic))

    def __sub__(self, other):
        # Метод для операции вычитания (-).
        return Roman(Roman.to_roman(self.arabic - other.arabic))

    def __mul__(self, other):
        # Метод для операции умножения (*).
        return Roman(Roman.to_roman(self.arabic * other.arabic))

    def __truediv__(self, other):
        # Метод для операции деления (/).
        return Roman(Roman.to_roman(self.arabic // other.arabic))
