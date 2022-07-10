class Point:
	def __init__(self, x, y):
		self.__x = x  
		self.__y = y  

	def get_coords(self):
		return self.__x, self.__y




class Rectangle:
	
	def __init__(self, *args):
		if len(args) == 4:
			self.__sp = Point(args[0], args[1])
			self.__ep = Point(args[2], args[3])
		elif len(args) == 2:
			if all([isinstance(args[0], Point),isinstance(args[1], Point)]):
				self.__sp = args[0]
				self.__ep = args[1]
		else:
			raise ValueError



	def set_coords(self, sp, ep):
		self.__sp = sp
		self.__ep = ep  

	def get_coords(self):
		return self.__sp, self.__ep


	def draw(self):
		print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(0, 0, 20, 34)




## TEST
rect.draw()

pt1 = Point(7, 8)
pt2 = Point(40, 50)

rectangle = Rectangle(1,2,3,4)
sp, ep = rectangle.get_coords()
print(sp, ep)



rectangle = Rectangle(pt1,pt2)
sp, ep = rectangle.get_coords()
rectangle.draw()