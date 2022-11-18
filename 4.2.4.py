class Thing:
	def __init__(self, name, price, weight):
		self.name = name
		self.price = price
		self.weight = weight


	def __hash__(self):
		return hash((self.name.lower(), self.price, self.weight))




class DictShop(dict):

	def __init__(self, things = None):
		things = {} if things == None else things
		if not isinstance(things, dict):
			raise TypeError('аргумент должен быть словарем')
		if not all(isinstance(key, Thing) for key in things):
			raise TypeError('ключами могут быть только объекты класса Thing')

		super().__init__(things)

	def __setitem__(self, item, value):
		if not isistence(item, Thing):
			raise TypeError('ключами могут быть только объекты класса Thing')
		super().__setitem__(item, value)


dict_things = DictShop() 
