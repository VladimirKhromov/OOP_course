class Router:

	def __init__(self):
		"""
		И одно обязательное локальное свойство (могут быть и другие свойства):
		buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
		"""
		self.buffer = []
		self.links = {}

	def link(self, server):
		"""
		link(server) - для присоединения сервера server (объекта класса Server) к роутеру 
		(для простоты, каждый сервер соединен только с одним роутером)
		"""
		ip = server.get_ip()
		self.links[ip] = server
		server.router = self

	def unlink(self, server):
		"""
		unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера
		"""
		server.router = None

	def send_data(self):
		"""
		send_data() - для отправки всех пакетов	(объектов класса Data) из буфера роутера 
		соответствующим серверам (после отправки буфер должен очищаться)
		"""
		for d in self.buffer:
			self.links.get(d.ip).buffer.append(d)

		self.buffer.clear()


class Server:
	IP = 1

	"""
	buffer - список принятых пакетов (объекты класса Data, изначально пустой);
	ip - IP-адрес текущего сервера.
	"""

	def __init__(self):
		self.buffer = []
		self.ip = Server.IP  
		Server.IP += 1
		self.router = None

	def send_data(self, data):
		"""
		send_data(data) - для отправки информационного пакета data (объекта класса Data) 
		с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере 
		- локальном свойстве buffer)
		"""
		self.router.buffer.append(data)

	def get_data(self):
		"""
		get_data() - возвращает список принятых пакетов (если ничего принято не было, 
		то возвращается пустой список) и очищает входной буфер.
		"""
		result = self.buffer.copy()
		self.buffer.clear()
		return result


	def get_ip(self):
		"""
		get_ip() - возвращает свой IP-адрес.
		"""
		return self.ip		


class Data:
	
	def __init__(self, data:str, ip):
		self.data = data  
		self.ip = ip


## test ##

router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from, msg_lst_to)

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"