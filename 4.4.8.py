class Aircraft:
	def __init__(self, model, mass, speed, top):
		self.model = model  
		self.mass = mass 
		self.speed = speed
		self.top = top

	@staticmethod
	def _check_str(value):
		if not isinstance(value,str):
			raise TypeError('неверный тип аргумента')

	@staticmethod
	def _check_int(value):
		if not isinstance(value,int) or value <= 0:
			raise TypeError('неверный тип аргумента')

	@staticmethod
	def _check_number(value):
		if not isinstance(value,(int, float)) or value <= 0:
			raise TypeError('неверный тип аргумента')

	@staticmethod
	def _check_dict(value):
		if not isinstance(value,dict):
			raise TypeError('неверный тип аргумента')

	# model
	@property
	def model(self):
		return self._model

	@model.setter
	def model(self, new_value):
		self._check_str(new_value)
		self._model = new_value

	#mass
	@property
	def mass(self):
		return self._mass

	@mass.setter
	def mass(self, new_value):
		self._check_number(new_value)
		self._mass = new_value

	#speed
	@property
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, new_value):
		self._check_number(new_value)
		self._speed = new_value

	#top
	@property
	def top(self):
		return self._model

	@top.setter
	def top(self, new_value):
		self._check_number(new_value)
		self._top = new_value


class PassengerAircraft(Aircraft):
	def __init__(self, model, mass, speed, top, chairs):
		super().__init__(model, mass, speed, top)
		self.chairs = chairs

	#chairs
	@property
	def chairs(self):
		return self._chairs

	@chairs.setter
	def chairs(self, new_value):
		self._check_int(new_value)
		self._chairs = new_value


class WarPlane(Aircraft):
	def __init__(self, model, mass, speed, top, weapons:dict):
		super().__init__(model, mass, speed, top)
		self.weapons = weapons

	#weapons
	@property
	def weapons(self):
		return self._weapons

	@weapons.setter
	def weapons(self, new_value):
		self._check_dict(new_value)
		self._weapons = new_value





planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80.1),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

