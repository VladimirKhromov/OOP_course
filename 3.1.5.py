class Shop:
	def __init__(self, name):
		self.name = name  
		self.goods = []

	def add_product(self, product):
		self.goods.append(product)

	def remove_product(self, product):
		self.goods.remove(product)


class Product:
	ID = 1

	@classmethod
	def give_id(cls):
		result = cls.ID
		cls.ID += 1
		return result

	def __init__(self, name, weight, price):
		self.id = self.give_id()
		self.name = name  
		self.weight = weight
		self.price = price
		

	def __setattr__(self, key, value):
		if key == "name":
			if not isinstance(value, str):
				raise TypeError("Неверный тип присваиваемых данных.")
		if key in ('weight','price'):
			if isinstance(value,(int, float)) and value < 0:
				raise TypeError("Неверный тип присваиваемых данных.")
		if key == "id":
			if not isinstance(value, int):
				raise TypeError("Неверный тип присваиваемых данных.")
		object.__setattr__(self, key, value)

	def __delattr__(self, item):
		if item == "id":
			raise AttributeError("Атрибут id удалять запрещено.")
		object.__delattr__(self, item)





shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")







