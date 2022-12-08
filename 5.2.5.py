class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


a, b = input().split()

try:
    a = int(a)
    b = int(b)
except:
    pt = Point()
else:
    pt = Point(a, b)
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")
