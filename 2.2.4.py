class Car:

    def __init__(self, model = None):
        self.__model = model

    @staticmethod
    def is_correct_model_name(name):
        if isinstance(name, str) and len(name) >= 2 and len(name) <= 100:
            return True

        return False

    @property
    def model(self):
        return self.__model


    @model.setter
    def model(self, new_model):
        if self.is_correct_model_name(new_model):
            self.__model = new_model


