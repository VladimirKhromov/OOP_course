class Clock:
	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def get_time(self):
		return self.seconds + self.minutes * 60 + self.hours * 3600


class DeltaClock:
	def __init__(self, clock1, clock2):
		self.clock1 = clock1
		self.clock2 = clock2


	def __str__(self):
		result = self.clock1.get_time() - self.clock2.get_time()
		if result > 0:
			h = result//3600
			m = (result - h*3600)//60
			s = (result - h*3600)%60
			return f"{h:02}: {m:02}: {s:02}"
		return 0

	def __len__(self):
		result = self.clock1.get_time() - self.clock2.get_time()
		return result if result >= 0 else 0


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)