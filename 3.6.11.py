class Triangle:
    def __init__(self, a, b, c):
        self.a = self.chech_value(a)
        self.b = self.chech_value(b)
        self.c = self.chech_value(c)
        self.is_triangle(self.a, self.b, self.c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


    @staticmethod
    def chech_value(value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return value

    @staticmethod
    def is_triangle(a, b, c):
        if not (a < (b + c) and b < (a + c) and c < (a + b)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")



    def __len__(self):
        return int(self.a + self.b + self.c)


    def tr(self):
        p = len(self)/2
        a, b, c = self.a, self.b, self.c
        return (p * (p-a) * (p-b) * (p-c))**0.5

    def __call__(self):
        return self.tr()


## TEST ##

tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"