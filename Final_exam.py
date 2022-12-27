from random import randint, shuffle

class Ship:
	""" Класс для представления кораблей """
	def __init__(self, length, tp = 1, x = None, y = None):
		""" Инициализация корабля.

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
	def __init__(self, size = 10):
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

## TEST Balackirev ###
try:
	ship = Ship(2)
	ship = Ship(2, 1)
	ship = Ship(3, 2, 0, 0)

	assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
	assert ship._cells == [1, 1, 1], "неверный список _cells"
	assert ship._is_move, "неверное значение атрибута _is_move"

	ship.set_start_coords(1, 2)
	assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
	assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

	ship.move(1)
	s1 = Ship(4, 1, 0, 0)
	s2 = Ship(3, 2, 0, 0)
	s3 = Ship(3, 2, 0, 2)

	assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
	assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

	s2 = Ship(3, 2, 1, 1)
	assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

	s2 = Ship(3, 1, 8, 1)
	assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

	s2 = Ship(3, 2, 1, 5)
	assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

	s2[0] = 2
	assert s2[0] == 2, "неверно работает обращение ship[indx]"

	p = GamePole(10)
	p.init()
	for nn in range(5):
	    for s in p._ships:
	        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

	        for ship in p.get_ships():
	            if s != ship:
	                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
	    p.move_ships()
	    
	gp = p.get_pole()
	assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
	assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

	pole_size_8 = GamePole(8)
	pole_size_8.init()

except:
	print()
	print("*"*10, "\nОшибка теста")
else:
	print("Тесты пройдены")
