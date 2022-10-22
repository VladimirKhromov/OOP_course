class Ellipse:
    def __init__(self, *args):
        if len(args) >= 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __len__(self):
        return len(self.__dict__)

    def get_coords(self):
        if bool(self):
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')

x1, y1, x2, y2 = 0, 1, 2, 3
el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)

lst_geom = [Ellipse(), Ellipse(), Ellipse(1,2,3,4), Ellipse(10,20,30,40)]

for item in lst_geom:
    if item:
        item.get_coords()