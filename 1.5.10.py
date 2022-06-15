class ListObject:

	def __init__(self, data, next_obj = None):
		self.data = data 
		self.next_obj = next_obj

	def link(self, obj):
		self.next_obj = obj.data


lst_in = ["234", "345","56565"]


head_obj = ListObject(lst_in[0])
head_obj1 = ListObject(lst_in[1])

head_obj.link(head_obj1)

head_obj2 = ListObject(lst_in[2])

head_obj.link(head_obj1)