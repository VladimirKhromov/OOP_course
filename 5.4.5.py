# здесь объявляйте классы
class PrimaryKeyError(Exception):
	def __init__(self, **kwargs):
		if kwargs:
			self.params = kwargs
		else:
			self.params = None