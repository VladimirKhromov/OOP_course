class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight






class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things_list = []

    def _weight_bag_now(self):
        return sum([i.weight for i in self.things_list])

    def _check_indx(self, indx):
        if indx < 0 or indx >= len(self.things_list):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        if thing.weight + self._weight_bag_now() > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things_list.append(thing)

    def __getitem__(self, item):
        self._check_indx(item)
        return self.things_list[item]

    def __setitem__(self, item, value):
        self._check_indx(item)
        if value.weight + self._weight_bag_now() - self.things_list[item].weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things_list[item] = value

    def __delitem__(self, item):
        self._check_indx(item)
        self.things_list.pop(item) 



## test ##

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
try:
    bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
except:
    print("ОК!")
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
try:
    t = bag[4] # генерируется исключение IndexError
except:
    print("ОК!")


## test ##

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
