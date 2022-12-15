# Exception

class CellException(Exception):
	pass

class CellIntegerException(CellException):
	pass

class CellFloatException(CellException):
	pass

class CellStringException(CellException):
	pass

# Program

class CellInteger:
	def __init__(self, min_value, max_value):
		self._min_value = min_value
		self._max_value = max_value
		self.__value = None

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		if not self._min_value <= new_value <= self._max_value:
			raise CellIntegerException('значение выходит за допустимый диапазон')
		self.__value = new_value

class CellFloat:
	def __init__(self, min_value, max_value):
		self._min_value = min_value
		self._max_value = max_value
		self.__value = None

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		if not self._min_value <= new_value <= self._max_value:
			raise CellFloatException('значение выходит за допустимый диапазон')
		self.__value = new_value

class CellString:
	def __init__(self, min_length, max_length):
		self._min_length = min_length
		self._max_length = max_length
		self.__value = None

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		if not self._min_length <= len(new_value) <= self._max_length:
			raise CellStringException('длина строки выходит за допустимый диапазон')
		self.__value = new_value

class TupleData:
	def __init__(self, *cells):
		self.cells = cells


	def __getitem__(self, item):
		if not 0 < item < len(self.cells):
			raise IndexError
		return self.cells[item]


	def __setitem__(self, item, value):
		if not 0 <= item < len(self.cells):
			raise IndexError
		self.cells[item].value = value

	def __len__(self):
		return len(self.cells)

	def __iter__(self):
		self.value_row = 0
		return self
 
	def __next__(self):
		if self.value_row < len(self):
			result = self.cells[self.value_row]
			self.value_row += 1
			return result.value
		else:
			raise StopIteration



## 
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

## 

t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"


cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

    
cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

    
cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(CellStringException, CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"