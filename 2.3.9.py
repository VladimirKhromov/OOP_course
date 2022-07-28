class SuperShop:

	def __init__(self, name):
		self.name = name
		self.goods = []

	def add_product(self, product):
		self.goods.append(product)

	def remove_product(self, product):
		if product in self.goods:
			self.goods.remove(product)


class StringValue:

	def __init__(self, min_length = 2, max_length = 50):
		self.min_length = min_length
		self.max_length = max_length

	def valid_str(self, value):
		return isinstance(value,str) and self.min_length <= len(value) <= self.max_length

	def __set_name__(self, owner, name):
		self.name = "_" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value):
		if self.valid_str(value):
			return setattr(instance,self.name, value)


class PriceValue :

	def __init__(self, max_value = 10000):
		self.max_value = max_value

	def valid_price(self, value):
		return isinstance(value,(float, int)) and 0 <= value <= self.max_value

	def __set_name__(self, owner, name):
		self.name = "_" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value):
		if self.valid_price(value):
			return setattr(instance, self.name, value)


class Product:
	name = StringValue()
	price = PriceValue()

	def __init__(self, name, price):
		self.name = name
		self.price = price


## TEST ##

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
t = Product("Курс по Python ООП", 2000)
shop.add_product(t)
shop.remove_product(t)
for p in shop.goods:
    print(f"{p.name}: {p.price}")


shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
print(t)
shop.remove_product(t)
assert len(shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')


t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"

