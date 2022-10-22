from random import randint


class GamePole:
    __instance = None

    def __init__(self, N, M, total_mines):
        self.N = N # (N строк и M столбцов)
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = None #TODO!

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
 
        return cls.__instance

    @property
    def pole(self):
        return self.__pole_cells

    def count_mine(self, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k+i, l+j
                if ii < 0 or ii > self.N-1 or jj < 0 or jj > self.M-1:
                    continue
                if self.pole[ii][jj].is_mine:
                    n += 1
                    
        return n



    def init_pole(self):
        """для инициализации начального состояния игрового поля,
        (расставляет мины и делает все клетки закрытыми)"""
        N, M = self.N, self.M # (N строк и M столбцов)
        # Получим координаты мин. 
        mines_coords = []
        while len(mines_coords) < self.total_mines:
            mine_coord = randint(0,(N*M)-1)
            if mine_coord not in mines_coords:
                mines_coords.append(mine_coord)
        mines_coords.sort() 
        # Создадим поле и расставим объекты класса Cell

        pole = [Cell() for _ in range(M*N)]
        for coord in mines_coords:
            pole[coord].is_mine = True
        self.__pole_cells = []
        for i in range(N):
            self.__pole_cells.append(pole[i*M:i*M+M])


        #Считаем мины вокруг клеток
        for i in range(0,self.N):
            for j in range(0, self.M):
                self.__pole_cells[i][j].number = self.count_mine(i, j)

        
    def open_cell(self, i, j):
        if not (0 <= i <= self.N or 0 <= j <= self.M):
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        """открывает ячейку с индексами (i, j); 
        нумерация индексов начинается с нуля; 
        метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True"""
        self.__pole_cells[i][j].is_open = True 

    def show_pole(self):
        """отображает игровое поле в консоли 
        (как именно сделать - на ваше усмотрение, этот метод - домашнее задание)"""
        for i in self.__pole_cells:
            print(i)

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False


    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if value not in (True, False):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not (isinstance(value, int) and 0 <= value <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if value not in (True, False):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value       

    def __bool__(self):
        return not self.__is_open


    def __repr__(self):
        if  self.__is_mine:
            return '*'
        else:
            return str(self.__number)





















##TEST ##

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)

assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.show_pole()
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k+i, l+j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1
                
    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"