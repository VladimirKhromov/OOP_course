class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = self.j = 0

    def __iter__(self):
        self.i = self.j = 0
        return self

    def __next__(self):
        i, j = self.i, self.j
        self.j += 1
        if self.j > self.i:
            self.i += 1
            self.j = 0  

        if i >= len(self.lst):
            raise StopIteration

        return self.lst[i][j]



## test ##

lst = [['x00'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32', 'x33']]


it = TriangleListIterator(lst)
for x in it:
    print(x)