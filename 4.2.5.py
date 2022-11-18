class Element:
	def __init__(self, name:str, weight:float, old:int):
		self.name = name  
		self.weight = weight  
		self.old = old

	def __repr__(self):
		return f"{self.name} {self.weight} {self.old}"

class Protists:
	pass

class Plants(Protists):
	pass

class Animals(Protists):
	pass

class Mosses(Plants):
	pass

class Flowering(Plants):
	pass

class Worms(Animals):
	pass

class Mammals(Animals):
	pass

class Human(Mammals):
	pass

class Monkeys(Mammals):
	pass

# Elements

class Monkey(Monkeys, Element):
	pass

class Person (Human, Element):
	pass

class Flower(Flowering, Element):
	pass

class Worm (Worms, Element):
	pass


lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),  
			Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),  
			Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),  
			Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]



lst_animals = [object for object in lst_objs if isinstance(object, Animals)]
lst_plants = [object for object in lst_objs if isinstance(object, Plants)]
lst_mammals = [object for object in lst_objs if isinstance(object, Mammals)]
print(lst_animals, lst_plants, lst_mammals)