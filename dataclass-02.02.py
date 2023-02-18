from dataclasses import dataclass, field, InitVar

# class Vector3D 
@dataclass(init=True, repr=True, eq=True, order=False, frozen=False)
# параметры декоратора dataclass
# init - для разрешения создавать инициализатор. (по умолчанию True)
# False используется если текущий класс - родительский
#
# repr - создание магического метода repr (по умолчанию True).
#
# eq - создание магического метода eq (по умолчанию True).
# важно что при False, магический метод не создается а наследуется от родителя.
# Значит сравнение будет тоже возможно, но по умолчанию проверяется что это один и тотже объект.
#
# order - позволяет сравнивать на >, >=, <, <=, и определяет соответсвующие маг. методы. 
# (по умолчанию False). при значении order=True - параметр eq тоже должен быть True
# также при включенном параметре нельзя прописывать свои собственные магические методы
#
# frozen - запрещает изменение атрибутов экземпляра класса после создания(по умолчанию False)


class V3D:
	x: int
	y: int
	z: int
	calc_len: InitVar[bool] = True  # new parm
	# InitVar use parm in post_init 
	length: float = field(init=False, default=0)


	def __post_init__(self, calc_len: bool):
		if calc_len:
			self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

v_1 = V3D(1, 2, 3)
v_2 = V3D(1, 2, 3, False)
print(v_1)  
print(v_2) 