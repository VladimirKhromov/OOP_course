# Attention! не доделано!

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
	name_class = "DialogWindows"
	def __init__(self, name):
		self.name = name  

class DialogLinux:
	name_class = "DialogLinux"
	def __init__(self, name):
		self.name = name  

class Dialog:
	def __new__(cls, *args, **kwarg):
		if TYPE_OS == 1:
			ret = DialogWindows.__new__(cls)
		else:
			ret = DialogLinux.__new__(cls)

		ret.name = args[0]
		return ret

	def __init__(self, name):
		self.name = name  


dlg = Dialog("Строка")		

print(dlg, dlg.__dict__)