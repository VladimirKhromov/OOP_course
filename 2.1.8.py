class Line():
	def __init__(self,x1, y1, x2, y2):
		self.__x1 = x1
		self.__x2 = x2
		self.__y1 = y1
		self.__y2 = y2


	def set_coords(self, x1, y1, x2, y2):
		self.__x1 = x1
		self.__x2 = x2
		self.__y1 = y1
		self.__y2 = y2

	def get_coords(self):
		return self.__x1, self.__y1, self.__x2, self.__y2

	def draw(self):
		print(self.__x1, self.__y1, self.__x2, self.__y2)



## TEST


line = Line(0, 0, 10, 12)

print(line.get_coords())
line.draw()

line.set_coords(4, 5, 22, 15)


line.draw()