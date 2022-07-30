class Book:
	def __init__(self, title = "", author = "", pages = 0, year = 0):
		self.title = title  
		self.author = author
		self.pages = pages
		self.year = year  

	def __setattr__(self, key, value):
		if key == "title" or key == "author":
			if not isinstance(value, str):
				raise TypeError("Неверный тип присваиваемых данных.")
		if key == "pages" or key == "year":
			if not isinstance(value, int):
				raise TypeError("Неверный тип присваиваемых данных.")
		object.__setattr__(self, key, value)



book = Book("Python ООП","Сергей Балакирев", 123, 2022)
