class Circle:
	def __init__(self, x, y, radius):
		self.__x = self.check_atribute(x)
		self.__y = self.check_atribute(y)  
		self.__radius = self.check_atribute(radius)

	@staticmethod
	def check_atribute(value):
		if not (isinstance(value,(int, float))):
			raise TypeError("Неверный тип присваиваемых данных.")	 
		return value


	def __setattr__(self, key, value):
		if key == 'radius':
			if not (isinstance(value,(int, float))):
				raise TypeError("Неверный тип присваиваемых данных.")
			elif value < 0:
				return
		if key in ('x', 'y'):
			if not (isinstance(value,(int, float))):
				raise TypeError("Неверный тип присваиваемых данных.")
		object.__setattr__(self, key, value)

	def __getattr__(self, item):
		return False

	@property
	def x(self):
		return self.__x  

	@x.setter
	def x(self, value):
		self.__x = value

	@property
	def y(self):
		return self.__y  

	@y.setter
	def y(self, value):
		self.__y = value

	@property
	def radius(self):
		return self.__radius 

	@radius.setter
	def radius(self, value):
		self.__radius = value


## TEST ##


circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует


assert type(Circle.x) == property and type(Circle.y) == property and type(Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, '7', 22)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = '20'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
    
cr.y = 7.8
cr.radius = 10.6