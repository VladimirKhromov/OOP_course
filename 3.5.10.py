class Body:
    def __init__(self, name, ro, volume):
        self.name = name  
        self.ro = ro
        self.volume = volume
        self.mass = self.ro * self.volume


    def __eq__(self, other):
        r = other.mass if isinstance(other, Body) else other
        return self.mass == r


    def __lt__(self, other):
        r = other.mass if isinstance(other, Body) else other
        return self.mass < r

    def __le__(self, other):
        r = other.mass if isinstance(other, Body) else other
        return self.mass <= r   


## TEST ##

body1 = Body("sdf",7, 1)
body2 = Body("sdf2",5, 1)

print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(body1 < 10)     # True, если масса тела body1 меньше 10
print(body2 == 5)     # True, если масса тела body2 равна 5