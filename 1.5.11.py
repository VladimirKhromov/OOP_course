from random import shuffle
from copy import deepcopy


class Cell:
	def __init__(self, around_mines, mine):
		self.around_mines = around_mines
		self.mine = mine
		self.fl_open = False

class GamePole:
	def __init__(self, N, M):
		self.N = N
		self.M = M
		self.init()  


	def init(self):
		A = [1 if i < self.M else 0 for i in range(self.N**2)]
		shuffle(A)
		self.pole = [A[i*self.N:(i+1)*self.N] for i in range(self.N)]


		for i in self.pole:
			print(i)
		self.get_number_mines_pole()
		

	def get_number_mines_pole(self):
		mines = deepcopy(self.pole)

		print('***')
		# добавляем строки и столбцы с 0
		mines.insert(0,[0 for _ in range(self.N)])
		mines.append([0 for _ in range(self.N)])
		for i in mines:
			i.insert(0,0)
			i.append(0)

		for i in mines:
			print(i)
		print('***')
		result = []
		for i in range(1,len(mines)-1):
			for j in range(1,i-1):
				row = [sum(mines[i-1][j-1:j+1],sum(mines[i][j-1:j+1],mines[i+1][j-1:j+1]) )]

				result.append(row)

		print(result)



	def show(self):
		pass



pl = GamePole(10,12)
