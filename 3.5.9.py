class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __call__(self):
        return None

    def __new__(self):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    type_money = 'rub'
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, new_cb):
        self.__cb = new_cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    
    def get_volume(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volume(other)
        return abs(v1-v2) < 0.1

    def __lt__(self, other):
        v1, v2 = self.get_volume(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volume(other)
        return v1 <= v2

class MoneyD:
    type_money = 'dollar'
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, new_cb):
        self.__cb = new_cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    
    def get_volume(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volume(other)
        return abs(v1-v2) < 0.1

    def __lt__(self, other):
        v1, v2 = self.get_volume(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volume(other)
        return v1 <= v2

class MoneyE:
    type_money = 'euro'
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, new_cb):
        self.__cb = new_cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    
    def get_volume(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volume(other)
        return abs(v1-v2) < 0.1

    def __lt__(self, other):
        v1, v2 = self.get_volume(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volume(other)
        return v1 <= v2


## TEST ##

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")