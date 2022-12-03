class Money:
    @staticmethod
    def _check_value(value):
        if not isinstance(value,(int,float)):
            raise TypeError('сумма должна быть числом')


    def __init__(self, value):
        self.money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._check_value(value)
        self._money = value


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)


    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)       




class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"



## TEST ##

m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
try:
    m = m1 + m2  # TypeError
except TypeError:
    print("TypeError OK")