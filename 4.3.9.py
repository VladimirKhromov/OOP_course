class StringDigit(str):

	def _check_str(self, st):
		if not st.isdigit():
			raise ValueError("в строке должны быть только цифры")

	def __init__(self, st = ""):
		self._check_str(st)
		str.__init__(st)

	def __add__(self, other):
		self._check_str(other)
		return StringDigit(self.__str__() + other)

	def __radd__(self, other):
		self._check_str(other)
		return StringDigit(other + self.__str__())

## TEST ## 

s = StringDigit("123")
sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
print(sd)	
sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
    
try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
