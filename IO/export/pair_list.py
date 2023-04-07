from sorting.athlete import *
from IO.parser import *
from copy import copy
from database.main_data import *

CHECK = 1
ALL_LIST = []

'''
The Grid class modified specifically for the list of pairs.
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
Determines the winner of the pair for the list of pairs.
P.S.
Add 2 more above the array with distribution lists by gender, as well as under the list
(distribution list by age) of distribution by weight.
'''
def winner_of_pair(list):
    global CHECK
    pair_of_athletes = 0  # Auxiliary variable, in order to go through the entire list of pairs.
    first_list = []  # Auxiliary list for the function to work.
    second_list = []  # Auxiliary list for the function to work.
    third_list = []  # Auxiliary list for the function to work.
    '''
    A cycle that goes through the list of age groups of athletes.
    '''
    for age_group in range(6):
        '''
        A cycle that goes through the list of pairs of athletes in the list of age groups.
        '''
        while pair_of_athletes < copy(len(list[age_group])):
            '''
            A cycle that goes through the list in pair.
            '''
            for index_in_pair in range(2):
                if type(list[age_group][pair_of_athletes][0]) == str or type(list[age_group][pair_of_athletes][1]) == str:
                    first_list.append(f"Победитель пары {CHECK}")
                    CHECK += 1
                    pair_of_athletes += 1
                    continue
                if list[age_group][pair_of_athletes][0].name == "-" and list[age_group][pair_of_athletes][1].name == "-":
                    first_list.append(list[age_group][pair_of_athletes][1])
                    pair_of_athletes += 1
                    continue
                if list[age_group][pair_of_athletes][0].name == "-" and list[age_group][pair_of_athletes][1].name != "-":
                    first_list.append(list[age_group][pair_of_athletes][1])
                    pair_of_athletes += 1
                    continue
                if list[age_group][pair_of_athletes][0].name != "-" and list[age_group][pair_of_athletes][1].name == "-":
                    first_list.append(list[age_group][pair_of_athletes][0])
                    pair_of_athletes += 1
                    continue
                if list[age_group][pair_of_athletes][0].name != "-" and list[age_group][pair_of_athletes][1].name != "-":
                    first_list.append(f"Победитель пары {CHECK}")
                    CHECK += 1
                    pair_of_athletes += 1
                    continue
            second_list.append(copy(first_list))
            first_list.clear()
        third_list.append(copy(second_list))
        pair_of_athletes = 0
        second_list.clear()
    return third_list
'''
Creating a list of pairs from a dictionary for easier sorting in the future.
The function fills the global variable, which will include all pairs.
'''
def create_list_of_pair(grid):
    list = []  # Auxiliary list for the function to work.
    for i in grid.ATHLETE_LIST:
        list.append(i[0])
        list.append(i[1])

        print(f"{i[0].name} x {i[1].name}")
    ALL_LIST.append(list)
'''
Removing "-" from the original list of participants. If they are on the list.
P.S.
Accidentally confused i and j, just too lazy to change.
'''
def deleting_original(list):
    i = 0
    second_list = []  # List of couples
    third_list = []  # List of couple lists
    for j in range(6):
        while i < len(list[j]):
            first_list = []  # Couple of athletes
            first_list.append(list[j][i])
            first_list.append(list[j][i + 1])
            second_list.append(first_list)
            i += 2
        i = 0
        third_list.append(copy(second_list))
        second_list = []
    return third_list

parser_data = Parser(file_name=r"C:\Users\megat\project\sortition\Попередня Запоріжжяr.docx").result()

list_of_all = []  # Initial list with all pairs received from the parser.
changing_list = []  # The list is constantly changing.
for i in range(6):
    grid = Grid(parser_data, i)
    create_list_of_pair(grid)
list_of_all = copy(ALL_LIST)
'''
Calling the functions of the distant iteration of the tournament. For TESTING.
'''
changing_list = deleting_original(list_of_all)
print(changing_list)
sth_list = winner_of_pair(changing_list)
print()
print(changing_list)
changing_list = winner_of_pair(changing_list)
print()
print(changing_list)
changing_list = winner_of_pair(changing_list)
print()
print(changing_list)