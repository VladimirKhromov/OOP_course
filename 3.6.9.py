class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year


    def __hash__(self):
        return hash((self.author.lower(), self.name.lower()))


lst = """Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021"""


lst_bs = []
lst_in = lst.split("\n")
for s in lst_in:
    name, author, year = s.split(";")
    lst_bs.append(BookStudy(name, author, year))

book_dict = {}
for book in lst_bs:
    hash_book = hash(book)
    if hash_book not in book_dict:
        book_dict[hash_book] = 1
    else:
       book_dict[hash_book] += 1
       
unique_books = len(book_dict.values())
print(unique_books) 


