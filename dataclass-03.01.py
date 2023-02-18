from dataclasses import dataclass, field, InitVar
from typing import Any


@dataclass
class Goods:
	uid: Any
	price: Any = None
	weight: Any = None



@dataclass
class Book(Goods):
	title: str = ""
	author: str = ""
	price: float = 0
	weight: int | float = 0

print("Cмотрим какие атрибуты будут в родительском и дочернем классе")
print(Goods.__doc__)
print(Book.__doc__)
print()

book = Book("1", "1000", '100', "Python ООП", "Балакирев С.М.")
print(book)