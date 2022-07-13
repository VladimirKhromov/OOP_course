import random


class EmailValidator:

	_list_chars = ['_', '.', '@', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
	's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	def __new__(self):
		pass

	@staticmethod
	def __is_email_str(email):
		return isinstance(email, str)

	@classmethod
	def check_email(cls, email):
		if not cls.__is_email_str(email):
			return False

		for ch in email:
			if ch not in cls._list_chars:
				return False

		split_mail = email.split("@")

		checklist = []		

		checklist.append(len(split_mail) == 2)
		checklist.append(len(split_mail[0]) <= 100)
		checklist.append(len(split_mail[1]) <= 50)
		checklist.append(split_mail[1].count(".") >= 1)
		checklist.append(email.count("..") < 1)

		return all(checklist)

	@classmethod
	def get_random_email(cls):
		
		length = random.randint(2,100)

		name_email = []

		for _ in range(length):
			name_email.append(random.choice(cls._list_chars[3:]))

		return "".join(name_email) + "@gmail.com"


res = EmailValidator.check_email("sc_lib@list.ru") # True
print
res = EmailValidator.check_email("sc_lib@list_ru") # False