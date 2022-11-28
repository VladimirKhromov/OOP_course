from abc import ABC, abstractmethod

class Model(ABC):

	@abstractmethod
	def get_pk(self):
		pass

	def get_info(self):
		return "Базовый класс Model"

class ModelForm(Model):
	ID = 0

	@classmethod
	def __get_id(cls):
		cls.ID += 1
		return cls.ID


	def __init__(self, login, password):
		self._login = login
		self._password = password
		self._id = self.__get_id()

	def get_pk(self):
		return self._id


## TEST ##

form = ModelForm("Логин", "Пароль")
assert form.get_pk() == 1, "ID"
assert form.get_info() == 'Базовый класс Model', "get_info"
print(form.get_pk())