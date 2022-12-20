from random import randint

class Ship:
	""" Класс для представления кораблей """
	def __init__(self, length, tp = 1, x = None, y = None):
		self._length = length
		self._tp = tp 
		self._x = x
		self._y = y
		self._is_move = True
		self._cells = [1] * self._length

	def set_start_coords(self, x, y):
		""" Установка начальных координат. """
		self._x = х
		self._y = y

	def get_start_coords(self):
		""" Получение начальных координат корабля в виде кортежа x, y. """
		return self._x, self._y
	
	def get_course(self):
		""" Возвращает координату движения коробля. """
		if self._tp == 1:
			return self._x
		elif self._tp == 2:
			return self._y
		else:
			raise ValueError("Неверное значение положения коробля")

	def move(self, go):
		""" Перемещение корабля в направлении его ориентации на go клеток. """
		if self._is_move:
			mv = self.get_course()
			mv += go


	def coords_ship_info(self):
		""" Возвращает кортеж координат, на котором находится корабль, а также его окружение"""
		if self._tp == 1:
			coords_x = [self._x + i for i in range(-1, self._length) if 0 <= self._x + i]
			coords_y = [self._y + i for i in (-1, 0, 1) if 0 <= self._y + i]
		elif self._tp == 2:
			coords_x = [self._x + i for i in (-1, 0, 1) if 0 <= self._x + i]
			coords_y = [self._y + i for i in range(-1, self._length) if 0 <= self._y + i]

		result = [(i, j) for i in coords_x for j in coords_y]
		return tuple(result)


	def is_collide(self, ship):
		""" 
		Проверка на столкновение с другим кораблем ship.
		Метод возвращает True, если столкновение есть и False - в противном случае.
		"""
		this_ship = self.coords_ship_info()
		other_ship = ship.coords_ship_info()
		general = (set(this_ship) & set(other_ship))
		return True if general else False			 

	def is_out_pole(self, size):
		""" 
		Проверка на выход корабля за пределы игрового поля. 
		Возвращается True, если корабль вышел из игрового поля 
		и False - в противном случае.
		"""
		if self._x is None or self._y is None or not (0 <= self._x < size) or not (0 <= self._x < size) or \
				self.get_course() + self._length > size:
			return False
		return True 

	def __repr__(self):
		return f"Ship coords {self._x} {self._y} and length {self._length}\n"

	def __getitem__(self, indx):
		if 0 <= indx < self._length:
			return self._cells[indx]

	def __setitem__(self, key, item):
		if 0 <= indx < self._length and key in (0, 1, 2):
			self._cells[indx] = key


class GamePole:
	def __init__(self, size = 10):
		self._size = size
		self._ships = []


	def init(self):
		""" Начальная инициализация игрового поля. """
		self._ships.clear()
		for i in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1):
			self._ships.append(Ship(i, tp=randint(1,2)))


	def get_ships(self):
		return self._ships

	def move_ships(self):
		"""
		Gеремещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад)
		в направлении ориентации корабля; если перемещение в выбранную сторону невозможно 
		(другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, 
		иначе (если перемещения невозможны), оставаться на месте.
		"""
		pass

	def show(self):
		"""
		Отображение игрового поля в консоли.
		Корабли отображаются значениями из коллекции _cells каждого корабля, вода - значением 0.
		"""
		pass

	def get_pole(self):
		"""
		Получение текущего игрового поля в виде двумерного кортежа размером size x size элементов.
		"""
		pass

## TEST ##

ship = Ship(4, 1, 2, 5)
ship2 = Ship(1, 1, 6, 6)
print(ship.coords_ship_info())
print(ship2.coords_ship_info())
print(ship.is_collide(ship2))

"""
pole = GamePole()
pole.init()
print(pole.get_ships())
"""