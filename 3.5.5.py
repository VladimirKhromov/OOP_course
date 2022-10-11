class Dimensions:
	MIN_DIMENSION = 10
	MAX_DIMENSION = 10000


	def __init__(self, a, b, c):
		self.__a = a  
		self.__b = b  
		self.__c = c  


	@classmethod
	def verified_size(cls, size):
		return isinstance(size, (int, float)) and cls.MIN_DIMENSION <= size <= cls.MAX_DIMENSION


	@property
	def a(self):
		return self.__a

	@a.setter
	def a(self, new_a):
		if self.verified_size(new_a):
			self.__a = new_a

	@property
	def b(self):
		return self.__b

	@b.setter
	def b(self, new_b):
		if self.verified_size(new_b):
			self.__b = new_b

	@property
	def c(self):
		return self.__c

	@c.setter
	def c(self, new_c):
		if self.verified_size(new_c):
			self.__c = new_c

	def get_abc(self):
		return self.__a, self.__b, self.__c

	def get_full_size(self):
		return self.__a * self.__b * self.__c


	def __le__(self, other):
		return self.get_full_size() <= other.get_full_size()

	def __lt__(self, other):
		return self.get_full_size() < other.get_full_size()

	def __repr__(self):
		return f'{self.__a} * {self.__b} * {self.__c}'

class ShopItem:

	def __init__(self, name, price, dim):
		self.name = name  
		self.price = price
		self.dim = dim

	def __repr__(self):
		return f'товар {self.name} стоимостью {self.price} и габаритами {self.dim}'


lst_shop = [ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = lst_shop[:]
lst_shop_sorted.sort(key = lambda x: x.dim.get_full_size())



## TEST ##

assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"