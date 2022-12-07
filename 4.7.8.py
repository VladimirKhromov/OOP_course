class Note:
	_available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

	def __init__(self, name, ton = 0):
		self.name = name
		self.ton = ton


	def __setattr__(self, key, value):
		if key == "_name" and value not in self._available_values:
			raise ValueError('недопустимое значение аргумента')
		if key == "_ton" and value not in (-1, 0, 1):
			raise ValueError('недопустимое значение аргумента')
		object.__setattr__(self, key, value)


class Notes:
	__instance = None
	_available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си') 
	__slots__ = (
				"_do",
				"_re",
				"_mi",
				"_fa",
				"_solt",
				"_la",
				"_si",
				)

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def __del__(self):
		Notes.__instance = None

	def __init__(self):
		for k, v in zip(self.__slots__, self._available_values):
			setattr(self, k, Note(v))


	@staticmethod
	def _check_index(index):
		if index not in range(0,7):
			raise IndexError('недопустимый индекс')

	def __getitem__(self, index):
		self._check_index(index)
		return getattr(self, self.__slots__[index])



notes = Notes()
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
notes_name = (
			"до",
			"ре",
			"ми",
			"фа",
			"соль",
			"ля",
			"си",
			)

notes_name = (
			"do",
			"re",
			"mi",
			"fa",
			"solt",
			"la",
			"si",
			)