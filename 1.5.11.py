from random import shuffle, randint

class Cell:
	def __init__(self, around_mines=0, mine=False):
		self.around_mines = around_mines
		self.mine = mine
		self.fl_open = False

class GamePole:
	def __init__(self, N, M):
		self._n = N
		self._m = M
		self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
		self.init()  



	def init(self):
		m = 0
		while m < self._m:
			i = randint(0, self._n-1)
			j = randint(0, self._n-1)
			mine = self.pole[i][j].mine
			if not mine:
				mine = True
				m += 1  

		indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
	
		for x in range(self._n):
			for y in range(self._n):
				if not self.pole[x][y].mine:
					mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self._n and 0 <= y+j < self._n))
					self.pole[x][y].around_mines = mines



	def show(self):
		for row in self.pole:
			print(*map(lambda x: "#" if not x.fl_open else x.around_mines if not x.mine else "*", row))

pole_game = GamePole(10,12)

## TEST ##
pole_game.show()


assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')

Cell.__doc__

N = 10
M = 10

def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k+i, l+j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n
            
for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            assert pole_game.pole[i][j].around_mines == get_around_mines(i, j), f"неверное число мин вокруг клетки с индексами {i, j}"