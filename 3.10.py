class Cell():
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False

    def __repr__(self):
        show = ("-", "X", "O")
        return str(self.value)


class TicTacToe():
    SIZE = 3
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def init(self):
        """инициализация игры (очистка игрового поля, возможно, еще какие-либо действия)"""
        self.pole = [[Cell() for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.__human_win = self.__comp_win = self.__draw = False

    def __init__(self):
        self.init()


    @property
    def is_human_win(self):
        value = False
        ar = [[i.value for i in a] for a in self.pole]
        for i in ar:
            if i[0] == i[1] == i[2] == 1:
                value = True
                break  
        for i in range(3):
            if ar[0][i] == ar[1][i] == ar[2][i] == 1:
                value = True
                break 
        if not value:
            if ar[0][0] == ar[1][1] == ar[2][2] == 1 or ar[0][2] == ar[1][1] == ar[2][0] == 1:
                value = True

        self.__human_win = value
        self.__comp_win = self.__draw = False
        return self.__human_win

    @property
    def is_computer_win(self):
        value = False
        ar = [[i.value for i in a] for a in self.pole]
        for i in ar:
            if i[0] == i[1] == i[2] == 2:
                value = True
                break  
        for i in range(3):
            if ar[0][i] == ar[1][i] == ar[2][i] == 2:
                value = True
                break 
        if not value:
            if ar[0][0] == ar[1][1] == ar[2][2] == 2 or ar[0][2] == ar[1][1] == ar[2][0] == 2:
                value = True

        self.__comp_win = value
        self.__human_win = self.__draw = False
        return self.__comp_win

    @property
    def is_draw(self):
        return self.__draw




    def __check_index(self, *indx):
        index_range = tuple(range(self.SIZE))
        for i in indx:
            if i not in index_range:
                raise IndexError('некорректно указанные индексы')

    def __getitem__(self, key):
        i, j = key[0], key[1]
        self.__check_index(i, j)    
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = key[0], key[1]
        self.__check_index(i, j)    
        self.pole[i][j].value = value



    def show(self):
        """отображение текущего состояния игрового поля (как именно - на свое усмотрение)"""
        #for i in self.pole:
            #print(i)
        pass

    def human_go(self):
        """реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик)"""
        pass

    def computer_go(self):
        """реализация хода компьютера (ставит случайным образом нолик в свободную клетку)"""
        pass

    def __bool__(self):
        if any([self.is_human_win, self.is_computer_win, self.is_draw]):
            return False
        return True

## TEST ##

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"