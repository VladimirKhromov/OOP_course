class NewList:
	def __init__(self, lst = None):
		self.__lst = lst[:] if lst and isinstance(lst, list) else []

	def get_list(self):
		return self.__lst



	def __sub__(self, other):
		if isinstance(other, list):
			sub_list = other[:]
		elif isinstance(other, NewList):
			sub_list = other.get_list()[:]
		else:
			raise TypeError("Неверный тип данных")

		return NewList(self.__diff_list(self.__lst, sub_list))


	@staticmethod
	def __diff_list(lst1, lst2):
		if len(lst2) == 0:
			return lst1
		sub = lst2[:]
		return [x for x in lst1 if not NewList.__is_elem(x, sub)]

	@staticmethod
	def __is_elem(x, sub):
		res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
		if res:
			sub.remove(x)
		return res

	def __rsub__(self, other):	
		if not isinstance(other, list):
			raise TypeError("Неверный тип данных")
		return NewList(self.__diff_list(other, self.__lst))







lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print ("первый пример [-4, 6, 10, 11, 15, False]", res_1)

lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]

print ("Второй пример [1, 2, 3] ", res_2)
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print ("Третий пример [4.5]", res_3)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print ("Четвертый пример [1, 2]", res_4)
