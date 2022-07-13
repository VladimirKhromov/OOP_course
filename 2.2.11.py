class PhoneBook:
	LIST_PHONE = []

	def add_phone(self, phone):
		if isinstance(phone, PhoneNumber):
			self.LIST_PHONE.append(phone)

	def remove_phone(self, indx):
		self.LIST_PHONE.pop(indx)

	def get_phone_list(self):
		return self.LIST_PHONE

class PhoneNumber:

	def __init__(self, number:int, fio:str):
		self.number = self.check_number(number)
		self.fio = fio

	@staticmethod
	def check_number(number):
		if isinstance(number, int) and len(list(str(number))) == 11:
			return number
		raise ValueError("Incorrect number")

