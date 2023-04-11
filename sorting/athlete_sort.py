__all__ = ["grids", "parser_data"]

from sorting.athlete import *
from IO.parser import *


class Grid:
    def __init__(self, data, index):
        self.ATHLETE_LIST = [[16, 1],
                             [9, 8],
                             [5, 12],
                             [13, 4],
                             [3, 14],
                             [11, 6],
                             [7, 10],
                             [15, 2]]
        self.packaging(data, index)

    def packaging(self, data, index):
        current = 1
        for athlete in data["participants"][index]["data"]:
            for i in range(8):
                for j in range(2):
                    if current == self.ATHLETE_LIST[i][j]:
                        data = {"name": athlete["name"],
                                "birthday": athlete["birthday"],
                                "gender": athlete["gender"],
                                "weight": athlete["weight"]}
                        self.ATHLETE_LIST[i][j] = Athlete(data)
                        break
            current += 1

        for pair in self.ATHLETE_LIST:
            data = {"name": "-", "birthday": "-", "gender": "-", "weight": "-"}
            if type(pair[0]) == int:
                pair[0] = Athlete(data)
            if type(pair[1]) == int:
                pair[1] = Athlete(data)

        return self.ATHLETE_LIST


parser_data = Parser(file_name=r"Попередня Запоріжжя.docx").result()
print(parser_data)
# Grid.packaging(parser_data)
grids = [Grid(parser_data, 5), Grid(parser_data, 4), Grid(parser_data, 3)]
