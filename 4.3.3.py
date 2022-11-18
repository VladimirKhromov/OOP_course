
class Book:
	def __init__(self, title, author, pages, year):
		self.title = title  
		self.author = author
		self.pages = pages
		self.year = year  

class DigitBook(Book):
	def __init__(self, title, author, pages, year, size, frm):
		super().__init__(title, author, pages, year)
		self.size = size
		self.frm = frm  


book1 = Book('Евгений Онегин', 'Пушкин', 666, 1830)
book2 = DigitBook('Борис Годунов ', 'Пушкин', 777, 1825, 1024, 'fb2')

data = lambda obj: [print(f'{key:6} --> {value}') for key, value in obj.__dict__.items()]

data(book1); print('*' * 33); data(book2)