class Thing:
	def __init__(self, name, price, weight):
		self.name = name
		self.price = price
		self.weight = weight



class DictShop(dict):

	def __setitem__(self, item, value):
		