
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        arr = [self.fio, self.job, self.old, self.salary, self.year_job]
        if item < 0 or item > 4:
            raise IndexError('неверный индекс')
        return arr[item]



## test ##
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)

for v in pers:
    print(v)

asss = iter(pers)
print(next(asss))
print(next(asss))
print(next(asss))
print(next(asss))