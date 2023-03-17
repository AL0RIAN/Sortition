from sorting.athlete import *
from IO.parser import *
from copy import copy

CHECK = 1
ALL_LIST = []

'''
Решить проблему с переопределением ATHLETE_LIST
'''

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
                        self.ATHLETE_LIST[i][j] = Athlete(name=athlete["name"], birthday=athlete["birthday"],
                                                          gender=athlete["gender"], weight=athlete["weight"])
                        break
            current += 1

        for pair in self.ATHLETE_LIST:
            if type(pair[0]) == int:
                pair[0] = Athlete(name="-", birthday="-", gender="-", weight="-")
            if type(pair[1]) == int:
                pair[1] = Athlete(name="-", birthday="-", gender="-", weight="-")

        return self.ATHLETE_LIST


'''
Определяет победителя из пары.
'''
def winner_of_pair(list):
    global CHECK
    i = 0
    new_list = []
    new_second_list = []
    new_third_list = []
    for x in range(6):
        while i < copy(len(list[x])):
            for j in range(2):
                if type(list[x][i][0]) == str or type(list[x][i][1]) == str:
                    new_list.append(f"Победитель пары {CHECK}")
                    CHECK += 1
                    i += 1
                    continue
                if list[x][i][0].name == "-" and list[x][i][1].name == "-":
                    new_list.append(list[x][i][1])
                    i += 1
                    continue
                if list[x][i][0].name == "-" and list[x][i][1].name != "-":
                    new_list.append(list[x][i][1])
                    i += 1
                    continue
                if list[x][i][0].name != "-" and list[x][i][1].name == "-":
                    new_list.append(list[x][i][0])
                    i += 1
                    continue
                if list[x][i][0].name != "-" and list[x][i][1].name != "-":
                    new_list.append(f"Победитель пары {CHECK}")
                    CHECK += 1
                    i += 1
                    continue
            new_second_list.append(copy(new_list))
            new_list.clear()
        new_third_list.append(copy(new_second_list))
        i = 0
        new_second_list.clear()
    return new_third_list
'''
ДОРАБОТАТЬ
Создание всего списка пар.
'''
def create_list_of_pair(grid):
    list = []
    for i in grid.ATHLETE_LIST:
        list.append(i[0])
        list.append(i[1])

        print(f"{i[0].name} x {i[1].name}")
    ALL_LIST.append(list)
'''
Удаление "-" из изначального списка участников.
(разбиение основного списка на пары)
'''
def deleting_original(list):
    i = 0
    new_list = []
    third_new_list = []
    for j in range(6):
        while i < len(list[j]):
            second_new_list = []
            second_new_list.append(list[j][i])
            second_new_list.append(list[j][i + 1])
            new_list.append(second_new_list)
            i += 2
        i = 0
        third_new_list.append(copy(new_list))
        new_list = []
    return third_new_list

parser_data = Parser(file_name="Попередня Запоріжжя.docx").result()

sth_list = []
all_list = []
for i in range(6):
    grid = Grid(parser_data, i)
    create_list_of_pair(grid)
all_list = copy(ALL_LIST)
'''
Вызов срабатывания функций дальней итерации турнира
-----------------------------------------------------------
'''
sth_list = deleting_original(all_list)
print(sth_list)
sth_list = winner_of_pair(sth_list)
print()
print(sth_list)
sth_list = winner_of_pair(sth_list)
print()
print(sth_list)
sth_list = winner_of_pair(sth_list)
print()
print(sth_list)
'''
-----------------------------------------------------------
'''