class LinkedList:

	def __init__(self):
		self.__datalist = []

	def add_obj(self, obj):
		self.__datalist.append(obj)


	def remove_obj(self):
		if self.__datalist:
			self.__datalist.pop()


	def get_data(self):
		return [data.get_data() for data in self.__datalist]




class ObjList:

	def __init__(self, data):
		self.__next = None  
		self.__prev = None
		self.__data = data



## TEST
