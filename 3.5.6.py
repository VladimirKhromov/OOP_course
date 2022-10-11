stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __repr__(self):
        return f'{self.lst_words}'

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)

    def get_str(self):
        return " ".join(self.lst_words)





lst_text = []
for st in stich:
    for ch in "–?!,.;":
        st = st.replace(ch, "")
    
    lst_text.append(StringText(st.split()))

print(lst_text)

lst_text_sorted = lst_text[:]
lst_text_sorted = sorted(lst_text_sorted,reverse=True)

lst_text_sorted = [obj.get_str() for obj in lst_text_sorted]


print(lst_text_sorted)
    