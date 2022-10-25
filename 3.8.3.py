class Track:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords_list = []


    def _check_coords(self, indx):
        if not isinstance(indx, int) or indx < 0  or indx >= len(self.coords_list):
            raise IndexError('некорректный индекс')

    def add_point(self, x, y, speed):
        self.coords_list.append([(x, y), speed])


    def __getitem__(self, item):
        self._check_coords(item)
        return self.coords_list[item][0], self.coords_list[item][1]


    def __setitem__(self, item, value):
        self._check_coords(item)
        self.coords_list[item][1] = value

## TEST ##

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

try:
    res = tr[3] 
except IndexError:
    print("OK")