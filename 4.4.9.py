def class_log(log_lst):
	def log_method(cls):
		methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
		for k, v in methods.items():
			setattr(cls, k, log_method_decotator(v))
		return cls

	def log_method_decotator(func):
		def wrapper(*args, **kwargs):
			log_lst.append(func.__name__)
			return func(*args, **kwargs)
		return wrapper
	return log_method



vector_log = []   


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value



## TEST ##

v = Vector(1, 2, 3)
v[0] = 10
assert vector_log == ['__init__', '__setitem__'], "не то"