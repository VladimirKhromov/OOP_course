class Box:
    def __init__(self):
        self.things = []


    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        listself = self.things[:]
        listother = other.things[:]
        if len(listself) != len(listother):
            return False
        res = [x for x in listself if x in listother]
        return len(res) == len(listself)


class Thing:
    def __init__(self, name, mass):
        self.name = name 
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass



