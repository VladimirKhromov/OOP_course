from dataclasses import dataclass, field

# class Vector3D 
@dataclass
class V3D:
	x: int
	y: int
	z: int
	length: float = field(init=False)
	# field имеет параметры
	# 	init - не входит в инициализатор, используется для получения в post_init
	#	repr - отображает ли в описании (True по умолчанию)
	#	compare - учитывается ли при сравнении (True по умолчанию)

	def __post_init__(self):
		self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

v = V3D(1, 2, 3)
print(v)  # show x, y, z and length