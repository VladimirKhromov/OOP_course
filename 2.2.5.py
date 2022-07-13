class WindowDlg:

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width    
        self.__height = height



    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height} ")


    @staticmethod
    def is_correct_width(width):
        if all([isinstance(width, int), width >=0, width <= 10000]):
            return True  
        return False


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if self.is_correct_width(new_width):
            self.__width = new_width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if self.is_correct_width(new_height):
            self.__height = new_height
            self.show()   


## TEST


wnd = WindowDlg("Title 1", 100, 50)
wnd.width = 1000
wnd.height = 3000000
assert wnd.width == 1000 and wnd.height == 50

w = WindowDlg("Title 2", 100, 200)
w.width = 10
w.height = 20
assert w.width == 10 and w.height == 20
