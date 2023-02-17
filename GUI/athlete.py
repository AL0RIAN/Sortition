__all__ = ["Athlete", "all"]


class Athlete:
    def __init__(self, name, power, index):
        self.name = name
        self.power = power
        self.index = index


all = [[Athlete("Babodzaki", 3, 16), Athlete("Malenia", 4, 1)],
       [Athlete("Radan", 4, 9), Athlete("Godri", 2, 8)],
       [Athlete("Rennie", 5, 5), Athlete("Renala", 1, 12)],
       [Athlete("Godwin", 2, 13), Athlete("Tif", 9, 4)],
       [Athlete("Kirill", 3, 3), Athlete("Bob", 4, 14)],
       [Athlete("Yarik", 2, 11), Athlete("Rob", 9, 6)],
       [Athlete("Timo", 2, 7), Athlete("Cop", 9, 10)],
       [Athlete("Andrey", 2, 15), Athlete("Grob", 9, 2)]]
