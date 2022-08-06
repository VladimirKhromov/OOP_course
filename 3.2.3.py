from random import randint

class RandomPassword:

	def __init__(self, psw_chars, min_length, max_length):
		self.psw_chars = psw_chars
		self.min_length = min_length
		self.max_length = max_length



	def __call__(self):
		len_psw_chars = len(self.psw_chars)
		len_password = randint(self.min_length, self.max_length)
		return "".join([self.psw_chars[randint(0,len_psw_chars-1)] for _ in range(len_password)])



min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]

print(lst_pass)