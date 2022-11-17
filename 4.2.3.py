class ListInteger(list):
	
	def _check_arg(self, arg):
		if isinstance(arg, (list, tuple)):
			for i in arg:
				self._check_arg(i)
				return 
		if not isinstance(arg, int):
			raise TypeError('можно передавать только целочисленные значения')		

	def __init__(self, *args):
		for arg in args:
			self._check_arg(args)
		super().__init__(*args)

	def __setitem__(self, item, value):
		self._check_arg(value)
		super().__setitem__(item, value)

	def append(self, *item):
		self._check_arg(item)
		super().append(*item)

## TEST ##

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
try:
	s[0] = 10.5
except TypeError:
	print("TE - ok!")