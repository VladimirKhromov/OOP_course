class Singleton:
	__instance = None
	__instance_base = None

	def __new__(cls, *args, **kwargs):
		if cls == Singleton:
			if cls.__instance_base is None:
				cls.__instance_base = super().__new__(cls)
			return	cls.__instance_base
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
	
		return cls.__instance




class Game(Singleton):
	def __init__(self, name):
		if 'name' not in self.__dict__:
			self.name = name


g = Game("123")
g2 = Game("456")
print(id(g), id(g2))
print(g.name, g2.name)