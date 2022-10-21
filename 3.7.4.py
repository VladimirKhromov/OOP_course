class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score


    def __bool__(self):
        return True if int(self.score) > 0 else False

    def __repr__(self):
        return f"объект {self.name}"




inr = """Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0"""

lst_in = inr.split("\n")


players = [Player(*x.split("; ")) for x in lst_in]
players_filtered = list(filter(bool, players))
print(lst_in, players, players_filtered, sep="\n")