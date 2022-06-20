class Application:

	def __init__(self, name, blocked = False):
		self.name = name
		self.blocked = blocked



class AppStore:
	application = []


	def add_application(self, app): # добавление нового приложения app в магазин;
		self.application.append(app)

	def remove_application(self, app): # удаление приложения app из магазина;
		while app in self.application:
			 self.application.remove(app)

	def block_application(self, app): # блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
		indx = self.application.index(app)
		self.application[indx].blocked = True

	def total_apps(self): # возвращает общее число приложений в магазине.
		return len(self.application)
