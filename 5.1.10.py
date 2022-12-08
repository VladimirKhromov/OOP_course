class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value


    def __call__(self, value):
        if not isinstance(value, float) or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value


    def __call__(self, value):
        if not isinstance(value, int) or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    result = []
    for i in lst:
        for val in validators:
            try:
                val(i)
            except ValueError:
                continue
            if i not in result:
                result.append(i)
    return result


## TEST ##

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])
print(lst_out)