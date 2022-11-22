class Furniture:
	def __init__(self, name, weight):

		self.name = name
		self.weight = weight

	@staticmethod
	def __verify_name(name):
		if not isinstance(name, str):
			raise TypeError('название должно быть строкой')

	@staticmethod
	def __verify_weight(weight):
		if not isinstance(weight, (int, float)) or weight <= 0:
			raise TypeError('вес должен быть положительным числом')

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, new_name):
		self.__verify_name(new_name)
		self._name = new_name

	@property
	def weight(self):
		return self._weight

	@weight.setter
	def weight(self, new_weight):
		self.__verify_weight(new_weight)
		self._weight = new_weight

	def get_attrs(self):
		return tuple(self.__dict__.values())


class Closet(Furniture):
	def __init__(self, name, weight, tp, doors):
		super().__init__(name, weight)
		self._tp = tp
		self._doors = doors

class Chair(Furniture):
	def __init__(self, name, weight, height):
		super().__init__(name, weight)
		self._height = height

class Table(Furniture):
	def __init__(self, name, weight, height, square):
		super().__init__(name, weight)
		self._height = height
		self._square = square

## TEST ##

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())