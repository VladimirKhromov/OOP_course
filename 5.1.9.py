class Triangle:
    def __init__(self, a, b ,c):
        self._a = self._check_side(a)
        self._b = self._check_side(b)
        self._c = self._check_side(c)
        self._is_triangle() 

    @staticmethod
    def _check_side(side):
        if not isinstance(side, (int, float)) or side <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        return side

    def _is_triangle(self):
        a, b, c = self._a, self._b, self._c
        if a + b < c or a + c < b or b + c < a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for i in input_data:
    try: 
        t = Triangle(i[0], i[1], i[2])
    except:
        continue
    lst_tr.append(t)
print(lst_tr)