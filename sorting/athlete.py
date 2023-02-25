# __all__ = ["Athlete", "all"]
__all__ = ["Athlete"]


class Athlete:
    def __init__(self, name, birthday, gender, weight):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.weight = weight


# all = [[Athlete("Babodzaki", 2), Athlete("Malenia", 16)],
#        [Athlete("Radan", 4), Athlete("Godri", 2)],
#        [Athlete("Rennie", 5), Athlete("Renala", 1)],
#        [Athlete("Godwin", 2), Athlete("Tif", 9)],
#        [Athlete("Kirill", 3), Athlete("Bob", 4)],
#        [Athlete("Yarik", 2), Athlete("Rob", 9)],
#        [Athlete("Timo", 2), Athlete("Cop", 9)],
#        [Athlete("Andrey", 2), Athlete("Grob", 9)]]
