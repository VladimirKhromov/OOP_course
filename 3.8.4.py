""" Если кратко, то вам самим надо создать список из объектов класса Integer в Array, 
в классе Integer просто один локальный атрибут, изначально равен 0 и свойства property 
для его изменения и получения. 
Далее все операции со списком из объектов проводите в необходимых магических методах класса Array, 
результат вывода это обычные цифры из  лок.атрибута Integer , 0  либо другая цифра отличная от 0 
если в каком либо объекте списка мы меняем значение.
"""



class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise ValueError('должно быть целое число')
        self.__value = new_value

    def __repr__(self):
        return str(self.__value)

class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length  # максимальное количество элементов в массиве
        self.__cell = cell  # ссылка на класс, описывающий отдельный элемент этого массива 
        self.__array = [self.__cell() for _ in range(self.__max_length)]


    def __chech_value(self, value):
        if not isinstance(value, int) or value < 0 or value > self.__max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')


    def __repr__(self):
        return ' '.join([str(i) for i in self.__array])
        return " ".join(map(str, self.__array))


    def __getitem__(self, item):
        self.__chech_value(item)
        return self.__array[item].value


    def __setitem__(self, item, value):
        self.__chech_value(item)
        self.__array[item].value = value



## TEST ##
ar_int = Array(10, cell=Integer)
print(ar_int[3])

ar_int[1] = 10
print(ar_int[1])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел

try:
    ar_int[10] = 1 # должно генерироваться исключение IndexError
except IndexError:
    print("IndexError ok!")

try:
    ar_int[1] = 10.5 # должно генерироваться исключение ValueError
except ValueError:
    print("ValueError ok!")

