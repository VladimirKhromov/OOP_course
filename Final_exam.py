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
		""" установка начальных координат """
		pass

	def get_start_coords(self):
		""" Получение начальных координат корабля в виде кортежа x, y. """
		pass

	def move(self, go):
		""" Перемещение корабля в направлении его ориентации на go клеток. """
		pass

	def is_collide(self, ship):
		""" 
		Проверка на столкновение с другим кораблем ship.
		Метод возвращает True, если столкновение есть и False - в противном случае.
		"""
		pass

	def is_out_pole(self, size):
		""" 
		Проверка на выход корабля за пределы игрового поля. 
		Возвращается True, если корабль вышел из игрового поля 
		и False - в противном случае.
		"""
		pass


	def __getitem__(self, item):
		pass

	def __setitem__(self, key, item):
		pass


class GamePole:
	def __init__(self, size = 10):
		self._size = size
		self._ships = []


	def init(self):
		""" Начальная инициализация игрового поля. """
		pass


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