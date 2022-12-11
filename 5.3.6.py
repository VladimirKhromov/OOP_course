# здесь объявляйте класс
class TupleLimit(tuple):
	def __new__(cls, lst, max_length):
		inctance = super().__new__(cls, lst)
		inctance.max_length = max_length
		if len(lst) > max_length:
			raise ValueError('число элементов коллекции превышает заданный предел')
		return inctance

	def __str__(self):
		return ' '.join(map(str, self))

	def __repr__(self):
		return ' '.join(map(str, self))


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса

try:
	tl = TupleLimit(digits, 5)
	print(tl)
except ValueError as e:
	print(e)
