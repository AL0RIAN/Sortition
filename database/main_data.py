'''
The description how will work the start of "Жеребьёвка"

1 - Tournament participants will be added one by one to the list, a variable is also added, with saving
its number is on the list, because we will need to remember it.
2 - Later we will use method shuffle() to it array, and than I say early, we shall remember number of
athlete in array from parser witch will showed in tournament tree in the program.
3 - Then we add athletes from parser to athletes_list and in the future we will use that array.
4 - Later we take that array for make pair_list. ( It will separate peace of program (. )
5 - And later... We will output pair_list (We should to remake it)
6 - The program will able to start )
'''
ATHLETES_DISTRIBUTION = {
    "Ж": {
        "10": {
            "27": [],  # 27-
            "30": [],  # 27-30
            "33": [],  # 30-33
            "36": [],  # 33-36
            "39": [],  # 36-39
            "42": [],  # 39-42
            "45": [],  # 42-45
            "48": [],  # 45-48
            "2000": []  # 48+
        },  # 10-11
        "12": {
            "30": [],  # 30-
            "33": [],
            "36": [],
            "39": [],
            "42": [],
            "45": [],
            "48": [],
            "52": [],
            "2000": []  # 52+
        },  # 12-13
        "14": {
            "39": [],  # 39-
            "42": [],
            "45": [],
            "48": [],
            "52": [],
            "56": [],
            "2000": []  # 56+
        },  # 14-15
        "16": {
            "44": [],  # 44-
            "48": [],
            "52": [],
            "56": [],
            "60": [],
            "2000": []  # 60+
        },  # 16-17
        "18": {
            "48-": [],  # 48-
            "52": [],
            "56": [],
            "60": [],
            "65": [],
            "70": [],
            "75": [],
            "2000": []  # 75+
        }  # 18+
    },
    "М": {
        "10": {
            "27": [],  #27-
            "30": [],
            "33": [],
            "36": [],
            "39": [],
            "42": [],
            "45": [],
            "48": [],
            "52": [],
            "56": [],
            "2000": []  # 56+
        },  # 10-11
        "12": {
            "30": [],  # 30-
            "33": [],
            "36": [],
            "39": [],
            "42": [],
            "45": [],
            "48": [],
            "52": [],
            "56": [],
            "60": [],
            "2000": []  # 60+
        },  # 12-13
        "14": {
            "39": [],  # 39-
            "42": [],
            "45": [],
            "48": [],
            "52": [],
            "56": [],
            "60": [],
            "65": [],
            "70": [],
            "2000": []  #70+
        },  # 14-15
        "16": {
            "48": [],  # 48-
            "52": [],
            "56": [],
            "60": [],
            "65": [],
            "70": [],
            "75": [],
            "80": [],
            "2000": []  # 80+
        },  # 16-17
        "18": {
            "48": [],  # 48-
            "52": [],
            "56": [],
            "60": [],
            "65": [],
            "70": [],
            "75": [],
            "80": [],
            "85": [],
            "90": [],
            "2000": []  # 90+
        }  # 18+
    }
}

age_count = {
    10: "10-11",
    12: "12-13",
    14: "14-15",
    16: "16-17",
    18: "18+"
}

weight_count = {
    "Ж": {
        10: {
            27: "27-",
            30: "27-30",
            33: "30-33",
            36: "33-36",
            39: "36-39",
            42: "39-42",
            45: "42-45",
            48: "45-48",
            2000: "48+"
        },  # 10-11
        12: {
            30: "30-",
            33: "30-33",
            36: "33-36",
            39: "36-39",
            42: "39-42",
            45: "42-45",
            48: "45-48",
            52: "48-52",
            2000: "52+"
        },  # 12-13
        14: {
            39: "39-",
            42: "39-42",
            45: "42-45",
            48: "45-48",
            52: "48-52",
            56: "52-55",
            2000: "56+"
        },  # 14-15
        16: {
            44: "44-",
            48: "44-48",
            52: "48-52",
            56: "52-56",
            60: "56-60",
            2000: "60+"
        },  # 16-17
        18: {
            48: "48-",
            52: "48-52",
            56: "52-56",
            60: "56-60",
            65: "60-65",
            70: "65-70",
            75: "70-75",
            2000: "75+"
        }  # 18+
    },
    "М": {
        10: {
            "27": "27-",
            "30": "27-30",
            "33": "30-33",
            "36": "33-36",
            "39": "36-39",
            "42": "39-42",
            "45": "42-45",
            "48": "45-48",
            "52": "48-52",
            "56": "52-56",
            "2000": "56+"
        },  # 10-11
        12: {
            "30": "30-",
            "33": "30-33",
            "36": "33-36",
            "39": "36-39",
            "42": "39-42",
            "45": "42-45",
            "48": "45-48",
            "52": "48-52",
            "56": "52-56",
            "60": "56-60",
            "2000": "60+"
        },  # 12-13
        14: {
            "39": "39-",
            "42": "39-42",
            "45": "42-45",
            "48": "45-48",
            "52": "48-52",
            "56": "52-56",
            "60": "56-60",
            "65": "60-65",
            "70": "65-70",
            "2000": "70+"
        },  # 14-15
        16: {
            "48": "48-",
            "52": "48-52",
            "56": "52-56",
            "60": "56-60",
            "65": "60-65",
            "70": "65-70",
            "75": "70-75",
            "80": "75-80",
            "2000": "80+"
        },  # 16-17
        18: {
            "48": "48-",
            "52": "48-52",
            "56": "52-56",
            "60": "56-60",
            "65": "60-65",
            "70": "65-70",
            "75": "70-75",
            "80": "75-80",
            "85": "80-85",
            "90": "85-90",
            "2000": "90+"
        }  # 18+
    }
}

ATHLETE_LIST = [[16, 1],
                [9, 8],
                [5, 12],
                [13, 4],
                [3, 14],
                [11, 6],
                [7, 10],
                [15, 2]]

ATHLETE_LIST_KEYS = {
    16: 1,
    1: 2,
    9: 3,
    8: 4,
    5: 5,
    12: 6,
    13: 7,
    4: 8,
    3: 9,
    14: 10,
    11: 11,
    6: 12,
    7: 13,
    10: 14,
    15: 15,
    2: 16
}

ATHLETE_LIST_KEYS_re = {
    16: "-",
    1: "-",
    9: "-",
    8: "-",
    5: "-",
    12: "-",
    13: "-",
    4: "-",
    3: "-",
    14: "-",
    11: "-",
    6: "-",
    7: "-",
    10: "-",
    15: "-",
    2: "-"
}

from sorting.athlete import *
from IO.parser import *
from datetime import date
from datetime import datetime
from random import shuffle
from copy import copy


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
        # self.packaging(data, index)

def packaging(data, index):
    for athlete in data["participants"][index]["data"]:
        age = calculate_group_of_age(athlete)
        weight = calculate_group_of_weight(athlete, age)
        ATHLETES_DISTRIBUTION[athlete["gender"]][age][weight].append(athlete)
    return ATHLETES_DISTRIBUTION

def calculate_age(athlete):
    today = date.today()
    date_format = "%d.%m.%y"
    date_born = datetime.strptime(athlete["birthday"], date_format)
    return today.year - date_born.year - ((today.month, today.day) < (date_born.month, date_born.day))

def calculate_group_of_weight(athlete, age):
    for weight in ATHLETES_DISTRIBUTION[athlete["gender"]][age]:
        if float(athlete["weight"]) <= float(weight):
            return weight
        continue
def calculate_group_of_age(athlete):
    for groups in ATHLETES_DISTRIBUTION[athlete["gender"]]:
        if calculate_age(athlete) <= int(groups):
            return groups
        continue

def shuffle_tournament(data):
    for gender in data:
        for age in data[gender]:
            for weight in data[gender][age].values():
                shuffle(weight)

def to_actual_data(data):
    for gender in data:
        for age in data[gender]:
            for weight in data[gender][age]:
                if len(data[gender][age][weight]) <= 1:
                    data[gender][age][weight].clear()
                    continue
                flag_dict = ATHLETE_LIST_KEYS_re.copy()
                for index in range(len(data[gender][age][weight])):
                    flag_dict[index + 1] = data[gender][age][weight][index]
                flag_list = []
                data[gender][age][weight].clear()
                for athlete in flag_dict.values():
                    flag_list.append(athlete)
                    if len(flag_list) == 2:
                        data[gender][age][weight].append(flag_list)
                        flag_list = []

parser_data = Parser(file_name=r"C:\Users\megat\project\sortition\Попередня Запоріжжяr.docx").result()
# print(parser_data)

sth_list = packaging(parser_data, 1)
sth_list = packaging(parser_data, 2)
sth_list = packaging(parser_data, 3)

shuffle_tournament(sth_list)
to_actual_data(sth_list)
'''
Testing calculate_group_of_age.
'''
# for groups in athletes_distribution["Ж"]:
#     if calculate_age(parser_data["participants"][1]["data"][1]) <= int(groups):
#         print(groups)
#     continue
# print(calculate_age(parser_data["participants"][1]["data"][1]))

'''
Testing calculate_group_of_weight.
'''
# for weight in athletes_distribution["М"]["18+"]:
#     if float(parser_data["participants"][1]["data"][1]["weight"]) <= float(weight):
#         print(weight)
#         break
