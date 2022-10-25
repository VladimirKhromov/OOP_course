class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, item):
        if not isinstance(item, int) or item > len(self.__dict__):
            raise IndexError('неверный индекс поля')
        key_lst = [key for key in self.__dict__.keys()]
        return self.__dict__[key_lst[item]]

    def __setitem__(self, item, value):
        if not isinstance(item, int) or item > len(self.__dict__):
            raise IndexError('неверный индекс поля')
        key_lst = [key for key in self.__dict__.keys()]
        self.__dict__[key_lst[item]] = value




r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r[0])
print(r.__dict__)
