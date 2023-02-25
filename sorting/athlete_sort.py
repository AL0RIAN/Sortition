__all__ = ["Grid"]

from sorting.athlete import *
from IO.parser import *


class Grid:
    ATHLETE_LIST = [[16, 1],
                    [9, 8],
                    [5, 12],
                    [13, 4],
                    [3, 14],
                    [11, 6],
                    [7, 10],
                    [15, 2]]

    @staticmethod
    def packaging(data):
        current = 1
        for athlete in data["participants"][5]["data"]:
            for i in range(8):
                for j in range(2):
                    if current == Grid.ATHLETE_LIST[i][j]:
                        Grid.ATHLETE_LIST[i][j] = Athlete(name=athlete["name"], birthday=athlete["birthday"],
                                                          gender=athlete["gender"], weight=athlete["weight"])
                        break
            current += 1

        for member in Grid.ATHLETE_LIST:
            if type(member[0]) == int:
                member[0] = Athlete(name="-", birthday="-", gender="-", weight="-")
            if type(member[1]) == int:
                member[1] = Athlete(name="-", birthday="-", gender="-", weight="-")

        return Grid.ATHLETE_LIST


parser_data = Parser(file_name="Попередня Запоріжжя.docx").result()
print(parser_data)
Grid.packaging(parser_data)
for athlete in Grid.ATHLETE_LIST:
    print(f"{athlete[0].name} x {athlete[1].name}")
