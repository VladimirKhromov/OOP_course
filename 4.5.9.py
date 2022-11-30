class PointTrack:
	def _check_coords(self, *args):
		if not all([isinstance(x,(int, float)) for x in args]):
			raise TypeError('координаты должны быть числами')

	def __init__(self, x, y):
		self._check_coords(x,y)
		self.x = x 
		self.y = y

	def __str__(self):
		return f"PointTrack: {self.x}, {self.y}"


class Track:

	def __init__(self, *args):
		if len(args) == 2:
			self.__points = [PointTrack(args[0],args[1])]
		else:
			self.__points = list(args)

	@property
	def points(self):
		return tuple(self.__points)


	def add_back(self, pt):
		self.__points.append(pt)

	def add_front(self, pt):
		self.__points.insert(0, pt)

	def pop_back(self):
		self.__points.pop()

	def pop_front(self):
		self.__points.pop(0)




tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)