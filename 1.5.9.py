class Cart:
	goods = []

	def add(self, gd):
		self.goods.append(gd)

	def remove(self, indx):
		self.goods.pop(indx)

	def get_list(self):
		return [f"{i.name}: {i.price}" for i in self.goods]


class Table:
	def __init__(self, name, price):
		self.name = name  
		self.price = price


class TV:
	def __init__(self, name, price):
		self.name = name  
		self.price = price


class Notebook:
	def __init__(self, name, price):
		self.name = name  
		self.price = price

class Cup:
	def __init__(self, name, price):
		self.name = name  
		self.price = price


cart = Cart()
cart.add(TV("Телевизор 1", 20000))
cart.add(TV("Телевизор 2", 35000))
cart.add(Table("Стол", 2000))
cart.add(Notebook("Ноутбук 1", 55000))
cart.add(Notebook("Ноутбук 2", 75000))
cart.add(Cup("Кружка", 200))


cart.remove(0)