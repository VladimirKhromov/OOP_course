class ItemAttrs:

	def __getitem__(self, item):
		keys = list(self.__dict__)
		return self.__dict__[keys[item]]
	def __setitem__(self, key, value):
		keys = list(self.__dict__)
		self.__dict__[keys[key]] = value



class Point(ItemAttrs):
	def __init__(self, x, y):
		self.x = x 
		self.y = y  


## TEST ##

pt = Point(1, 2.5)
print(pt.__dict__)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10

print(pt.__dict__)