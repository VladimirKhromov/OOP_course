class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0  # 1 for X and 2 for O


    def __bool__(self):
        return self.is_free


    def __repr__(self):
        if self.value == 0 :
            return "-"
        return "X" if self.value == 1 else "O"



class TicTacToe:


    def clear(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.pole[1][1].value = 0

    def _check_index(self, indx):
        if isinstance(indx, int):
            if indx not in (0, 1, 2):
                raise IndexError('неверный индекс клетки')

    def __init__(self):
        self.clear()

    def __getitem__(self, item):
        r, c = item[0], item[1]
        self._check_index(r)
        self._check_index(c)

        if isinstance(r, slice):
            return tuple(self.pole[x][c].value for x in range(3))
        if isinstance(c, slice):
            return tuple(self.pole[r][x].value for x in range(3))

        return self.pole[r][c].value

    def __setitem__(self, item, key):
        r, c = item[0], item[1]
        self._check_index(r)
        self._check_index(c)
        if self.pole[r][c].value == 0:
            self.pole[r][c].value = key
        else:
            raise ValueError('клетка уже занята')



## TEST ##

g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"


