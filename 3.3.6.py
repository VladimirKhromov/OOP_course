class LinkedList :
	def __init__(self):
		self.head = None # ссылка на первый объект связного списка (если список пуст, то head = None)
		self.tail = None # ссылка на последний объект связного списка (если список пуст, то tail = None)


	def add_obj(self, obj):
		if self.head is None:
			self.head = obj
			self.tail = obj
		else:
			prev_obj = self.tail
			prev_obj.next = obj
			self.tail = obj
			self.tail.prev = prev_obj


	def remove_obj(self, indx):
		# удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); 
		# Индекс отсчитывается с нуля.
		obj = self.head 
		for _ in range(0, indx):
			obj = obj.next

		p, n = obj.prev, obj.next

		if p:
			p.next = n

		if n:
			n.prev = p  

		if self.head == obj:
			self.head = n

		if self.tail == obj:
			self.tail = p



	def __len__(self):
		""" возвращает число объектов в связном списке """
		if self.head is None:
			return 0
		len_index = 1
		obj = self.head
		while obj.next:
			len_index += 1
			obj = obj.next
		return len_index

	def __call__(self, indx):
		""" 
		возвращает строку __data, 
		хранящуюся в объекте класса ObjList, 
		расположенного под индексом indx (в связном списке) 
		"""
		obj = self.head 
		for _ in range(0, indx):
			obj = obj.next

		return obj.data


class ObjList:
	def __init__(self, data = ""):
		self.__data = data  
		self.__prev = None
		self.__next = None


	def __str__(self):
		return f"объект ObjList с данными {self.__data}"

	@property
	def prev(self):
		return self.__prev

	@prev.setter
	def prev(self, new):
		self.__prev = new

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, new):
		self.__next = new

	@property
	def data(self):
		return self.__data




## TEST ##

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))

n = len(linked_lst)  # n = 3

s = linked_lst(1) # s = Balakirev


## TEST 2 ##

ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"