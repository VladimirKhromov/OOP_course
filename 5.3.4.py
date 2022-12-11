class ValidatorString:
	def __init__(self, min_length, max_length, chars = ""):
		self.min_length = min_length
		self.max_length = max_length
		self.chars = chars

	def is_valid(self, string):
		if not isinstance(string, str) or not (self.min_length <= len(string) <= self.max_length ):
			raise ValueError('недопустимая строка')
		if self.chars != "" and not any([ch in string for ch in self.chars]):
			raise ValueError('недопустимая строка')

class LoginForm:
	def __init__(self, login_validator, password_validator):
		self.login_validator = login_validator
		self.password_validator = password_validator


	def form(self, request):
		if "login" not in request or "password" not in request:
			raise TypeError('в запросе отсутствует логин или пароль')

		login = request["login"]
		password = request["password"]
		self.login_validator.is_valid(login)
		self.password_validator.is_valid(password)
		self._login = login
		self._password = password

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = 'sergey', 'balakirev!'

try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
