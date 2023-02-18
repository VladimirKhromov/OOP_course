from dataclasses import dataclass, field
from typing import Any


@dataclass
class Goods:
	current_uid = 0  

	uid: int = field(init=False)
	price: Any = None
	weight: Any = None

	def __post_init__(self):
		print("Goods: post_init")  # чтобы убедится, что post init вызван
		Goods.current_uid += 1
		self.uid = Goods.current_uid


@dataclass
class Book(Goods):
	title: str = ""
	author: str = ""
	price: float = 0
	weight: int | float = 0

	def __post_init__(self):
		print("Book: post_init")
		super().__post_init__()
		# при наследовении метод init дочернего класса ищет и вызывает метод __post_init__,
		# и если его нет в дочернем классе, он ищет его в родительском.
		# если метод __post_init__ определен и в родительском и в дочернем,
		# то будет вызван только в дочернем.
		# Явное указание вызова через super() позволит вызвать метод __post_init__
		# как в дочернем, так и в родительском классах
		


book = Book(1000, 100, "Python ООП", "Балакирев С.М.")
print(book) # видим что сначала вызван post init у дочернего, потом у родительского класса