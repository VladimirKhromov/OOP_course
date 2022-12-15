class Box:
	def __init__(self, name, max_weight):
		self._name = name
		self._max_weight = max_weight
		self._things = []


	def add_thing(self, obj):
		if sum([item[1] for item in self._things]) + obj[1]> self._max_weight:
			raise ValueError('превышен суммарный вес вещей')
		self._things.append(obj)


class BoxDefender:
	def __init__(self, box):
		self.box = box
		self._things = box._things[:]

	def __enter__(self):
		return self.box

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type:
			self.box._things = self._things
		return False

b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2
        
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"