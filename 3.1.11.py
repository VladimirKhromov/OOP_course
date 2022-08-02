import time

class Mechanical:
	_not_change_atribute = ""

	def __init__(self, date):
		self.date = date
		self._not_change_atribute = "date"

	def __setattr__(self, key, value):
		if key != self._not_change_atribute:
			object.__setattr__(self, key, value)


class Aragon:
	_not_change_atribute = ""

	def __init__(self, date):
		self.date = date
		self._not_change_atribute = "date"

	def __setattr__(self, key, value):
		if key != self._not_change_atribute:
			object.__setattr__(self, key, value)


class Calcium:
	_not_change_atribute = ""

	def __init__(self, date):
		self.date = date
		self._not_change_atribute = "date"

	def __setattr__(self, key, value):
		if key != self._not_change_atribute:
			object.__setattr__(self, key, value)


class GeyserClassic :
	MAX_DATE_FILTER = 100

	SLOTS_FILTER = {0:Mechanical, 1:Aragon, 2:Calcium}


	def __init__(self):
		self.slots = [False for _ in range(3)]

	def add_filter(self, slot_num, filtr):
		if slot_num not in (1,2,3):
			raise ValueError("Неверный слот")
		if self.slots[slot_num-1] is False:
			if isinstance(filtr, self.SLOTS_FILTER[slot_num-1]):
				self.slots[slot_num-1] = filtr

	def remove_filter(self, slot_num):
		self.slots[slot_num-1] = False


	def get_filters(self):
		sl = self.slots
		return sl[0], sl[1], sl[2]

	def water_on(self):
		if not all(self.slots):
			return False

		for slot in self.slots:
			print(slot.date)
			if not (0 <= (time.time() - slot.date) <= self.MAX_DATE_FILTER):
				return False


		return True

## TEST ##

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))



assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"

