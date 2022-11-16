class ListInteger(list):
	@staticmethod
	def _check_arg(arg):
		if isinstance(arg, (list, tuple)):
			print("it")
			return 
		if not isinstance(arg, int):
			raise TypeError('можно передавать только целочисленные значения')		



	def __init__(self, *args):
		for arg in args:
			self._check_arg(args)
		super().__init__(*args)



	def __setitem__(self, item, value):
		pass

	def append(self, item):
		pass


s = ListInteger((1, 2, 3))