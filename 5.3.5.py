class Test:
	def __init__(self, descr):
		self._check_descr(descr)
		self.descr = descr

	def _check_descr(self, descr):
		if type(descr) != str or not (10 <= len(descr) <= 10000):
			raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

	def run(self):
		raise NotImplementedError


class TestAnsDigit(Test):
	def __init__(self, descr, ans_digit, max_error_digit = 0.01):
		if max_error_digit < 0 :
			raise ValueError('недопустимые значения аргументов теста')


		super().__init__(descr)
		self.ans_digit = ans_digit
		self.max_error_digit = max_error_digit



	def run(self):
		ans = float(input())
		max_value = self.ans_digit + self.max_error_digit
		min_value = self.ans_digit - self.max_error_digit
		return min_value <= ans <= max_value

tad = TestAnsDigit("Это тестовый прогон значений", 5)
tad.run()


## TEST ##

try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

    
try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False