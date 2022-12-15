class DateError(Exception):
	pass


class DateString:
	def __init__(self, date_string):
		self.date_string = date_string
		try:
			self.date_string = [int(i) for i in self.date_string.split(".")]
		except:
			raise DateError
		self.check_date(self.date_string)

	def check_date(self, lst):
		if len(lst) != 3 or lst[0] <= 0 or lst[1] <= 0 or lst[0] > 31 or lst[1] > 12:
			raise DateError


	def __str__(self):
		d, m, y = self.date_string[0], self.date_string[1], self.date_string[2] 
		return f"{d:02}.{m:02}.{y}"





date_string = "26.5.2022"
try:
	date = DateString(date_string)
	print(date) # date - объект класса DateString
except DateError:
	print("Неверный формат даты")
