class LineTo:
	def __init__(self, x, y):
		self.x = x  
		self.y = y  


class PathLines:
	def __init__(self, *lines):
		self.LIST_LINE = []
		if lines:
			for line in lines:
				self.LIST_LINE.append(line)

	def get_path(self):
		return self.LIST_LINE

	def add_line(self, line):
		self.LIST_LINE.append(line)

	def get_length(self):
		result = 0
		if len(self.LIST_LINE) == 0:
			return 0
		for indx in range(len(self.LIST_LINE)):
			if indx == 0:
				result += (self.LIST_LINE[indx].x**2 + self.LIST_LINE[indx].y**2)**0.5
			else:
				result += (((self.LIST_LINE[indx].x-self.LIST_LINE[indx-1].x)**2) + 
					((self.LIST_LINE[indx].y-self.LIST_LINE[indx-1].y)**2))**0.5
		return result


## TEST 
p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []