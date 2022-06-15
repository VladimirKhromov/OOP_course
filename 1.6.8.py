class SingletonFive:
	COUNT = 5
	last_obj = None
    
	def __new__(cls, *arg, **kwarg):
		if cls.COUNT > 0:
			cls.COUNT -= 1
			cls.last_obj = super().__new__(cls)
		return cls.last_obj



	def __init__(self,name):
		self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
