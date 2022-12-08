class Rect:
    def __init__(self, x, y, width, height):
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if type(width) not in (int, float) or width <=0 or type(height) not in (int, float) or height <=0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        x1, y1, w1, h1 = self._x, self._y, self._width, self._height
        x2, y2, w2, h2 = rect._x, rect._y, rect._width, rect._height
        if not (y2 + h2 < y1 or y1 + h1 < y2 or x2 + w2 < x1 or x1 + w1 < x2): 
            raise TypeError('прямоугольники пересекаются')

    def __str__(self):
        return f"RECT {self._x}, {self._y}, {self._width}, {self._height}"
    def __repr__(self):
        return f"RECT {self._x}, {self._y}, {self._width}, {self._height}"

lst_rect = [
            Rect(0, 0, 5, 3),
            Rect(6, 0, 3, 5),
            Rect(3, 2, 4, 4),
            Rect(0, 8, 8, 1),
            ]

lst_not_collision = []

for rect in lst_rect:
    try:
        for second_rect in lst_rect:
            if rect is second_rect:
                continue
            rect.is_collision(second_rect)
    except:
        continue
    else:
        lst_not_collision.append(rect)





'''
for i in range(len(lst_rect)):
    for j in range(len(lst_rect)):
        if i != j:
            try:
                lst_rect[i].is_collision(lst_rect[j])
            except:
                break

        if j == len(lst_rect) - 1:
            lst_not_collision.append(lst_rect[i])
'''
print(lst_not_collision)

## TEST ##

R = Rect(0, 0, 5, 3)
try:
    R.is_collision(Rect(3, 2, 4, 4))
except:
    print('error1 ok')

R.is_collision(Rect(0, 8, 8, 1))
R.is_collision(Rect(6, 0, 3, 5))


r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"

