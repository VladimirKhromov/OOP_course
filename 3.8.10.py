class Cell:
    def __init__(self, value):
        self.value = value 


    def __repr__(self):
        return f"Клетка со значением {self.value}"

class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def __get_new_rowcol(self):
        self.rows = max(key[0] for key in self.cells) + 1
        self.cols = max(key[1] for key in self.cells) + 1


    def add_data(self, row, col, data):
        self.cells[(row, col)] = data
        if row > self.rows or col > self.cols:
            self.__get_new_rowcol()

    def __check_index(self, indx):
        if not (indx[0], indx[1]) in self.cells:
            raise ValueError('данные по указанным индексам отсутствуют')

    def remove_data(self, row, col):
        if not (row, col) in self.cells:
            raise IndexError('ячейка с указанными индексами не существует')
        self.cells.pop((row, col))
        if row == self.rows or col == self.cols:
            self.__get_new_rowcol()


    def __getitem__(self, item:tuple):
        self.__check_index(item)
        return self.cells[item].value

    def __setitem__ (self, item, value):
        self.cells[item] = Cell(value)
        self.__get_new_rowcol()



## TEST ##

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st.add_data(5, 1, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице

## TEST ## 

st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"

