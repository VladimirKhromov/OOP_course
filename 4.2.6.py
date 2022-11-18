class Tuple(tuple):

	def __add__(self, object):
		object = tuple(object)
		return Tuple(super().__add__(object))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t, type(t))   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t, type(t)) 