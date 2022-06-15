class AbstractClass:
    
	def __new__(cls, *arg, **kwarg):
		return "Ошибка: нельзя создавать объекты абстрактного класса"

