class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView

class ShopGenericView:
	def __str__(self):
		for key, value in self.__dict__.items():
			print(f'{key}: {value}')
		return ' '
	def __repr__(self):
		for key, value in self.__dict__.items():
			print(f'{key}: {value}')
		return ' '

class ShopUserView:
	def __str__(self):
		for key, value in self.__dict__.items():
			if key !="_id":
				print(f'{key}: {value}')
		return ' '
	def __repr__(self):
		for key, value in self.__dict__.items():
			if key !="_id":
				print(f'{key}: {value}')
		return ' '

class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)