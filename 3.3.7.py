class Complex:
	def __init__(self, real, img):
		self.__real = self.check_number(real)
		self.__img = self.check_number(img)


	@staticmethod
	def check_number(number):
		if isinstance(number,(int, float)):
			return number
		raise ValueError("Неверный тип данных.")


	@property
	def real(self):
		return self.__real

	@real.setter
	def real(self, number):
		self.__real = self.check_number(number)
	
	@property
	def img(self):
		return self.__img

	@img.setter
	def img(self, number):
		self.__img = self.check_number(number)


	def __abs__(self):
		return (self.__real**2 + self.__img**2)**0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4

c_abs = abs(cmp)