class Dimensions:
    def __init__(self, a, b, c):
        self.a = self.chech_value(a)
        self.b = self.chech_value(b)
        self.c = self.chech_value(c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


    @staticmethod
    def chech_value(value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return value


s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"


lst_dims = []  
for i in s_inp.split(';'):  
    lst_dims.append(Dimensions(*map(float, i.split())))

lst_dims.sort(key= lambda x: hash(x))