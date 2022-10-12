# здесь объявляйте класс


text = input()   # эту строчку не менять

# здесь создавайте объекты класса и обрабатывайте строку text

class Morph:
    def __init__(self, *words):
        self.words = list(map(lambda x: x.strip(".,!?:;").lower(), words))

    def add_word(self, word):
        if word.lower() not in self.words:
            self.words.append(word.lower())

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return other.lower() in self.words


dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
            Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
            Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
            Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),   
            Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]


words = map(lambda x: x.strip(".,!?:;").lower(), text.split())

print(sum(word == morph for word in words for morph in dict_words))