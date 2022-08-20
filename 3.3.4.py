class Model:
	def __init__(self):
		self.data_base = {}


	def query(self, **kwargs):
		self.data_base.update(**kwargs)
		print(self.data_base)


	def __str__(self):
		if not self.data_base:
			return "Model"
		return "Model: " + ", ".join([f"{data} = {self.data_base[data]}" for data in self.data_base])





model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
