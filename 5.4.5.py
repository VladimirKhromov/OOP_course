# здесь объявляйте классы
class PrimaryKeyError(Exception):
	def __init__(self, **kwargs):
		if 'id' not in kwargs and 'pk' not in kwargs:
			self.params = None
		else:
			self.params = [(key, values) for key, values in tuple(kwargs.items())]



	def __str__(self):
		if not self.params:
			return "Первичный ключ должен быть целым неотрицательным числом"
		else:
			return f"Значение первичного ключа {self.params[0][0]} = {self.params[0][1]} недопустимо"


try:
	raise PrimaryKeyError(id = -10.5)
except PrimaryKeyError as e:
	print(e)
