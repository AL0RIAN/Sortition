__all__ = ["Athlete", "all"]


class Athlete:
    def __init__(self, name, power):
        self.name = name
        self.power = power


all = [[Athlete("Babodzaki", 3), Athlete("Malenia", 4)], [Athlete("Radan", 4), Athlete("Godri", 2)], [Athlete("Rennie", 5),
       Athlete("Renala", 1)], [Athlete("Godwin", 2), Athlete("Tif", 9)]]
