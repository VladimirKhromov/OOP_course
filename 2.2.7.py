class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x = 0, y = 0):
        if self.is_correct_coords(x):
            self.__x = x
        else:
            self.__x = 0       

        if self.is_correct_coords(y):
            self.__y = y
        else:
            self.__y = 0

    @classmethod
    def is_correct_coords(cls, value):
        return isinstance(value, (int,float)) and value >= cls.MIN_COORD and value <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x  


    @x.setter
    def x(self, value):
        if self.is_correct_coords(value):
            self.__x = value
    @property
    def y(self):
        return self.__y  


    @y.setter
    def y(self, value):
        if self.is_correct_coords(value):
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x*vector.x + vector.y*vector.y



v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
print(v1.__dict__)
v2 = RadiusVector2D(1,100)       # радиус-вектор с координатами (1; 0)
print(v2.__dict__)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
v3.x = 1000
v3.y = 1025
print(v3.__dict__)
r = RadiusVector2D.norm2(v2)
print(r)