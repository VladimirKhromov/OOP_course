class Vertex:
	def __init__(self):
		self._links = []

	@property
	def links(self):
		return self._links

class Link:
	def __init__(self, v1, v2, dist = 1):
		self._v1 = v1
		self._v2 = v2
		self._dist = dist


	@property
	def v1(self):
		return self._v1

	@property
	def v2(self):
		return self._v2

	@property
	def dist(self):
		return self._dist

	@dist.setter
	def dist(self, new_dist):
		self._dist = new_dist

class Station(Vertex):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return f'{self.name}'

class LinkMetro(Link):
	def __init__(self, v1, v2, dist):
		super().__init__(v1, v2, dist)

class LinkedGraph:
	def __init__(self):
		self._links = []
		self._vertex = []

	def add_vertex(self, v):
		if v not in self._vertex:
			self._vertex.append(v)


	def add_link(self, link):
		if link not in self._links:
			self._links.append(link)


	def find_path(self, start_v, stop_v):
		"""
		возвращает список из вершин кратчайшего маршрута и 
		список из связей этого же маршрута в виде кортежа
		([вершины кратчайшего пути], [связи между вершинами])
		"""
		pass

