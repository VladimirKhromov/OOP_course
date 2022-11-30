from abc import ABC, abstractmethod

class StackInterface(ABC):
	@abstractmethod
	def push_back(self):
		pass

	@abstractmethod
	def pop_back(self):
		pass

class StackObj:
	def __init__(self, data):
		self._data = data
		self._next = None
		self._prev = None

class Stack(StackInterface):
	def __init__(self):
		self._top = None
		self._last = None

	def push_back(self, obj):
		if not isinstance(obj, StackObj):
			raise TypeError("В стек можно передовать только объект класса StackObj")
		if not self._top:
			self._top = obj
			self._last = obj
		else:
			self._last._next = obj
			prev = self._last
			self._last = obj
			obj._prev = prev

	def pop_back(self):
		res = self._last
		self._last = res._prev
		if res._prev:
			self._last._next = None
		if res == self._top:
			self._top = None
		return res

## TEST ##

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)


## TEST 2 ##

assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
