class Viber:
	dict_messages = []

	@classmethod
	def add_message(cls, msg):
		cls.dict_messages.append(msg)


	@classmethod
	def remove_message(cls, msg):
		if msg in cls.dict_messages:
			cls.dict_messages.remove(msg)
	
	@classmethod
	def set_like(cls, msg):
		msg.fl_like = not msg.fl_like

	@classmethod
	def show_last_message(cls, number):
		for n in range(-number, 0):
			print(cls.dict_messages[n].text)

	@classmethod
	def total_messages(cls):
		return len(dict_messages)

class Message:
	def __init__(self, text):
		self.text = text  
		self.fl_like = False


msg = Message("Всем привет!")
Viber.add_message(msg)

Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
