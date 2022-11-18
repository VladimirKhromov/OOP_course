
class IteratorAttrs:

	def __iter__(self):
		for attr in self.__dict__.items():
			yield attr


class SmartPhone(IteratorAttrs):
	def __init__(self, model, size, memory):
		self.model = model  
		self.size = size
		self.memory = memory


## TEST ## 

exemple = SmartPhone("saf", 1232, 16)
for attr, value in exemple:
    print(attr, value)