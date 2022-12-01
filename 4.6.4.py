class Digit:
	def __init__(self, value):
		if isinstance(value,(int,float)):
			self.value = value
		else:
			raise TypeError('значение не соответствует типу объекта')



class Integer(Digit):
	def __init__(self, value):
		super().__init__(value)
		if not isinstance(value,int):
			raise TypeError('значение не соответствует типу объекта')
		self.value = value



class Float(Digit):
	def __init__(self, value):
		super().__init__(value)
		if not isinstance(value,float):
			raise TypeError('значение не соответствует типу объекта')
		self.value = value





class Positive(Digit):
	def __init__(self, value):
		self._check_value(value)
		self.value = value

	def _check_value(self,value):
		if not isinstance(value,(int,float)) or value < 0:
			raise TypeError('значение не соответствует типу объекта')



class Negative(Digit):
	def __init__(self, value):
		self._check_value(value)
		self.value = value

	def _check_value(self,value):
		if not isinstance(value,(int,float)) or value > 0:
			raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
	def __init__(self, value):
		super().__init__(value)


class FloatPositive(Positive, Float):
	def __init__(self, value):
		Positive.__init__(self, value)
		Float.__init__(self, value)
		


digits = [PrimeNumber(1),PrimeNumber(2),PrimeNumber(3),FloatPositive(1.2),
          FloatPositive(3.6),FloatPositive(2345.6),FloatPositive(1.2345),FloatPositive(0.5555)]

lst_positive  = list(filter(lambda x:isinstance(x,Positive), digits))
lst_float = list(filter(lambda x:isinstance(x,Float), digits))

print(lst_positive, lst_float)

try:
	a = FloatPositive(-1.5)
except TypeError:
	print("01 OK")


try:
	a = Digit("str")
except TypeError:
	print("02 DIGIT OK")

try:
	a = Integer(1.5)
except TypeError:
	print("03 INT OK")

try:
	a = Float(1)
except TypeError:
	print("04 Float OK")

try:
	a = Positive(-11)
except TypeError:
	print("05 Positive OK")

try:
	a = Negative(11)
except TypeError:
	print("06 Negative OK")


try:
	a = PrimeNumber(11.2)
except TypeError:
	print("07-1 PrimeNumber Integer  OK")

try:
	a = PrimeNumber(-11)
except TypeError:
	print("07-2 PrimeNumber Positive  OK")


try:
	a = FloatPositive(11)
except TypeError:
	print("08-1 PrimeNumber Float   OK")

try:
	a = FloatPositive(-11.5)
except TypeError:
	print("08-2 PrimeNumber Positive  OK")