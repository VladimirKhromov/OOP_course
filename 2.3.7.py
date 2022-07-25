class FloatValue:


	def __set_name__(self, owner, name):
		self.name = f"_{name}"

	@staticmethod
	def check_float(value):
		if not isinstance(value, float):
			raise TypeError("Присваивать можно только вещественный тип данных.")

	def __get__(self, instance, owner):
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		self.check_float(value)
		instance.__dict__[self.name] = value	


class Cell:

	value = FloatValue()


	def __init__(self, value = 0.0):
		self.value = value


class TableSheet:

	def __init__(self, N, M):
		self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)

n = 1.0

for i in range(5):
	for j in range(3):
		table.cells[i][j].value = n  
		n += 1
