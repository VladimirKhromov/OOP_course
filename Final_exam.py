from random import randint, shuffle

class Ship:
	""" Класс для представления кораблей """
	def __init__(self, length, tp = 1, x = None, y = None):
		""" 
		Инициализация корабля.

		Значения: 
		x, y - координаты начала расположения корабля (целые числа);
		length - длина корабля (число палуб);
		tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная);
		is_move - может ли корабль совершать движения.
		"""
		self._length = length
		self._tp = tp 
		self._x = x
		self._y = y
		self._is_move = True
		self._cells = [1] * self._length

	def set_start_coords(self, x, y):
		""" Установка начальных координат. """
		self._x, self._y = x, y

	def get_start_coords(self):
		""" Получение начальных координат корабля в виде кортежа x, y. """
		return self._x, self._y	

	def _check_coords(self):
		if self._x is None or self._y is None:
			raise ValueError("Для получения кортежа координат коробля нужно задать начальные значения")

	def get_ship_coords(self):
		""" Возвращает кортеж координат корабля. """
		self._check_coords() # проверяем установленны ли начальные координаты
		# Создаем лист коорданат х и y
		if self._tp == 1:
			x = [self._x + i for i in range(0, self._length)]
			y = [self._y] * self._length
		elif self._tp == 2:
			x = [self._x] * self._length
			y = [self._y + i for i in range(0, self._length)] 
		else:
			raise ValueError("Неверно задано расположение корабля")
		# Создаем кортеж координат из координат х и y
		coords = tuple(zip(x,y))
		return coords

	def get_ship_coords_with_pole(self):
		""" Возвращает кортеж координат, на котором находится корабль, а также его окружение. """
		self._check_coords() # проверяем установленны ли начальные координаты
		# Создаем лист коорданат х и y
		if self._tp == 1:
			x = [self._x + i for i in range(-1, self._length + 1) if self._x + i >= 0]
			y = [self._y + i for i in (-1, 0, 1) if self._y + i >= 0]
		elif self._tp == 2:
			x = [self._x + i for i in (-1, 0, 1) if self._x + i >= 0]
			y = [self._y + i for i in range(-1, self._length + 1) if self._y + i >= 0]
		else:
			raise ValueError("Неверно задано расположение корабля")
		# Создаем кортеж координат из координат х и y
		coords = tuple([(i, j) for i in x for j in y])
		return coords

	def move(self, go):
		""" Перемещение корабля в направлении его ориентации на go клеток. """
		if self._is_move:
			if self._tp == 1:
				self._x += go
			elif self._tp == 2:
				self._y += go

	def is_collide(self, ship):
		""" 
		Проверка на столкновение с другим кораблем ship.
		Метод возвращает True, если столкновение есть и False - в противном случае.
		"""
		main_ship = self.get_ship_coords_with_pole()
		other_ship = ship.get_ship_coords()
		lst_general_coords = (set(main_ship) & set(other_ship))
		if lst_general_coords:
			return True
		return False

	def is_out_pole(self, size):
		""" 
		Проверка на выход корабля за пределы игрового поля. 
		Возвращается True, если корабль вышел из игрового поля 
		и False - в противном случае.
		"""
		self._check_coords()
		for x, y in self.get_ship_coords():
			if x < 0 or x > size - 1 or y < 0 or y > size - 1:
				return True
		return False

	def __repr__(self):
		return f"Ship coor:{self._x}-{self._y}, tp:{self._tp}, len:{self._length}\n"

	def __getitem__(self, indx):
		if 0 <= indx < self._length:
			return self._cells[indx]

	def __setitem__(self, indx, value):
			self._cells[indx] = value


class GamePole:
	""" Класс для работы с игровым полем. """
	def __init__(self, size = 10):
		""" 
		Инициализация поля. 

		Значения: 
		_size - Размер игрового поля.
		_ships - Список кораблей на поле. """
		self._size = size
		self._ships = []


	def init(self):
		""" Начальная инициализация игрового поля. """
		# Создаем список кораблей
		self._ships.clear()
		for i in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1):
			self._ships.append(Ship(i, tp=randint(1, 2)))

		# Расставляем координаты кораблей и проверяем на столкновение и выход за поле.
		other_ships = []
		for ship in self._ships:
			while True:
				# Задаем координаты
				x = randint(0, self._size-1)
				y = randint(0, self._size-1)
				ship.set_start_coords(x, y)
				if ship.is_out_pole(self._size):
					continue

				# Проверяем на столкновение
				result = []
				for other_ship in other_ships:
					result.append(ship.is_collide(other_ship))
				if any(result):
					continue
				other_ships.append(ship)
				break

	def get_ships(self):
		return self._ships
	def move_ships(self):
		"""
		Перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад)
		в направлении ориентации корабля; если перемещение в выбранную сторону невозможно 
		(другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, 
		иначе (если перемещения невозможны), оставаться на месте.
		"""
		move_list = [1, -1]
		shuffle(move_list)
		for ship in self._ships:
			if not ship._is_move:
				continue

			origin_coords = ship.get_start_coords()
			ship.move(move_list[0])

			result = [ship.is_collide(other_ship) for other_ship in self._ships if ship != other_ship]
			if not any(result) and not ship.is_out_pole(self._size):
				continue

			ship.set_start_coords(*origin_coords)
			ship.move(move_list[1])

			result = [ship.is_collide(other_ship) for other_ship in self._ships if ship != other_ship]
			if not any(result) and not ship.is_out_pole(self._size):
				continue

			ship.set_start_coords(*origin_coords)

	def show(self):
		"""
		Отображение игрового поля в консоли.
		Корабли отображаются значениями из коллекции _cells каждого корабля, вода - значением 0.
		"""

		for row in self.get_pole():
			for i in row:
				print(i, end=' ')
			print()


	def get_pole(self):
		"""
		Получение текущего игрового поля в виде двумерного кортежа размером size x size элементов.
		"""
		game_pole = [[0 for _ in range(self._size)] for _ in range(self._size)]

		for ship in self._ships:
			result = ship.get_ship_coords()
			for i in range(len(result)):
				x, y = result[i][0], result[i][1]
				game_pole[x][y] = ship._cells[i]

		gp = []
		for row in game_pole:
			gp.append(tuple(row))

		gp = tuple(gp)
		return gp


class SeaBattle:
	""" Класс управления игровым процессом. """

	def init(self):
		""" Инициализирует игровые поля. """
		self.People_pole = GamePole()
		self.People_pole.init()
		self.People_pole.show()
		print()
		self.Computer_pole = GamePole()
		self.Computer_pole.init()
		self.Computer_pole.show()
		

	def show(self):
		""" Отображает поле игрока и поле компьютера."""
		pass

	def start_game(self):
		""" """
		pass


if __name__ == "__main__":
	battle = SeaBattle()
	battle.init()
	battle.show()