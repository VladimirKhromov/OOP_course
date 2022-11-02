class IterColumn:
    def __init__(self, lst, colomn):
        self.lst = lst
        self.colomn = colomn
        


    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        i = self.i
        self.i += 1

        if i >= len(self.lst):
            raise StopIteration

        return self.lst[i][self.colomn]



## test ##

lst = [['x00', 'x01', 'x02', 'x03'], ['x10', 'x11', 'x12', 'x13'], ['x20', 'x21', 'x22', 'x23'],
       ['x30', 'x31', 'x32', 'x33']]


it = IterColumn(lst, 1)
for x in it:
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
print(x)
