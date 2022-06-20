import re  
from string import ascii_lowercase, digits



class CardCheck:
	CHARS_FOR_NAME = ascii_lowercase.upper() + digits

	@staticmethod
	def check_card_number_old(number):
		match = re.fullmatch(r'(\d{4})(?:-\d{4}){3}', number)
		if match != None:
			return True  
		return False   

	@staticmethod
	def check_card_number(number):
		if not isinstance(number, str):
			return False
		spl_number = number.split("-")
		if len(spl_number) == 4 and all(map(lambda x: x.isdigit(), spl_number)):
			return True
		return False



	@classmethod
	def check_name(cls, name):
		if type(name) != str:
			return False
		s = name.split()
		if len(s) !=2:
			return False
		set_chars = set(cls.CHARS_FOR_NAME)
		return all(map(lambda x: set(x) < set_chars, s))

