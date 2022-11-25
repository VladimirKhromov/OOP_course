class ShopInterface:
	def get_id(self):
		raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):
	ID = 0

	@classmethod
	def _get_id(cls):
		result = cls.ID
		cls.ID += 1
		return result

	def __init__(self, name, weight, price):
		self._name = name
		self._weight = weight
		self._price = price
		self._id = self._get_id()

	def get_id(self):
		return self._id

	def get_info(self):
		return self._name, self._weight, self._price, self._id


## TEST ##

item1 = ShopItem("Колбаса", 1, 300)
item2 = ShopItem("Молоток", 50, 3000)
print(item1.get_info())
print(item2.get_info())