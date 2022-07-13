class StackObj:

    def __init__(self, data):
        self.__data = data  
        self.__next = None  

    @staticmethod
    def is_correct_next(next):
        return isinstance(next,StackObj) or next is None

    @staticmethod
    def is_correct_data(data):
        return isinstance(data,str)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        if self.is_correct_data(new_data):
            self.__data = new_data

    @data.deleter
    def data(self):
        self.__data = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        if self.is_correct_next(new_next):
            self.__next = new_next


class Stack:

    def __init__(self):
        self.top = None
        self.last = None


    def push(self, obj):
        if not self.top:
            self.top = obj

        if self.last:
            self.last.next = obj

        self.last = obj

    def pop(self):
        h = self.top
        if h is None:
            return   

        while h and h.next != self.last:
            h = h.next

        if h:
            h.next = None
        last = self.last
        self.last = h  
        if self.last is None:
            self.top = None  

        return last

    def get_data(self):
        list_data = []

        if self.top is None:
            return []
        
        n = self.top
        while n is not None:
            list_data.append(n.data)
            n = n.next

        return list_data



## TEST
"""
ob1 = StackObj("данные 1")
ob2 = StackObj("данные 1")
ob1.data = "123"
print(ob1.data)
ob1.next = ob2
print(ob1.next)
"""

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(list(res))

s = Stack()
res = s.get_data()    # []
print(res)