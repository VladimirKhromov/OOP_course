class WordString:
	def __init__(self, st = ""):
		self.st = st


	@property
	def string(self):
		return self.st

	@string.setter
	def string(self, st):
		self.st = st


	def __len__(self):
		return len(self.st.split())


	def __call__(self, indx):
		lst = self.st.split()
		return lst[indx]


## TEST ##


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
