class IntegerValue:

    @staticmethod
    def _check_int(value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self._check_int(value)
        instance.__dict__[self.name] = value


class CellInteger:
    value = IntegerValue()
    def __init__(self, start_value=0):
        self.value = start_value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)      
        
    def __int__(self):
        return self.value



class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):
        self.cells = tuple([tuple([cell() for _ in range(rows)]) for __ in range(cols)])

    def __getitem__(self, item):
        r, c = int(item[0]), int(item[1])
        return int(self.cells[r][c])

    def __setitem__(self, item, value):
        r, c = int(item[0]), int(item[1])
        self.cells[c][r].value = value



## TEST ## 

tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1

for row in tb.cells:
    for x in row:
        print(x.value, end=' ')
    print()


assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"

