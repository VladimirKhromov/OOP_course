
class VideoRating:
	def __init__(self):
		self.__rating = 0

	def __check_value(self, value):
		if value not in (0, 1, 2, 3, 4, 5):
			raise ValueError('неверное присваиваемое значение')

	@property
	def rating(self):
		return self.__rating

	@rating.setter
	def rating(self, value):
		self.__check_value(value)
		self.__rating = value

class VideoItem:
	def __init__(self, title, descr, path):
		self.title = title  
		self.descr = descr
		self.path = path
		self.rating = VideoRating()

## TEST ##



v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
try:
	v.rating.rating = 6  # ValueError
except ValueError:
	print("VE ok")