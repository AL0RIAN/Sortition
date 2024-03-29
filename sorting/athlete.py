# __all__ = ["Athlete", "all"]
__all__ = ["Athlete"]

import json
from typing import Dict


class Athlete:
    def __init__(self, args: dict):
        self.name = args["name"]
        self.birthday = args["birthday"]
        self.gender = args["gender"]
        self.weight = args["weight"]
        self.category = args["category"]
        self.is_sanda = args["is_sanda"]
        self.is_cinda = args["is_cinda"]
        self.is_tuishou = args["is_tuishou"]
        self.is_vinchun = args["is_vinchun"]
        self.region = args["region"]
        self.club = args["club"]
        self.trainer = args["trainer"]
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

# all = [[Athlete("Babodzaki", 2), Athlete("Malenia", 16)],
#        [Athlete("Radan", 4), Athlete("Godri", 2)],
#        [Athlete("Rennie", 5), Athlete("Renala", 1)],
#        [Athlete("Godwin", 2), Athlete("Tif", 9)],
#        [Athlete("Kirill", 3), Athlete("Bob", 4)],
#        [Athlete("Yarik", 2), Athlete("Rob", 9)],
#        [Athlete("Timo", 2), Athlete("Cop", 9)],
#        [Athlete("Andrey", 2), Athlete("Grob", 9)]]
