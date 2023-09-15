from IO.parser import *
from datetime import date
from datetime import datetime
from random import shuffle
from copy import copy


# Declaring Dictionaries.
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
            "48": [],  # 48-
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
            "27": [],  # 27-
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
            "2000": []  # 70+
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
    "Ж": {
        "10": "10-11",
        "12": "12-13",
        "14": "14-15",
        "16": "16-17",
        "18": "18+"
    },
    "М": {
        "10": "10-11",
        "12": "12-13",
        "14": "14-15",
        "16": "16-17",
        "18": "18+"
    }
}

weight_count = {
    "Ж": {
        "10": {
            "27": "27-",
            "30": "27-30",
            "33": "30-33",
            "36": "33-36",
            "39": "36-39",
            "42": "39-42",
            "45": "42-45",
            "48": "45-48",
            "2000": "48+"
        },  # 10-11
        "12": {
            "30": "30-",
            "33": "30-33",
            "36": "33-36",
            "39": "36-39",
            "42": "39-42",
            "45": "42-45",
            "48": "45-48",
            "52": "48-52",
            "2000": "52+"
        },  # 12-13
        "14": {
            "39": "39-",
            "42": "39-42",
            "45": "42-45",
            "48": "45-48",
            "52": "48-52",
            "56": "52-55",
            "2000": "56+"
        },  # 14-15
        "16": {
            "44": "44-",
            "48": "44-48",
            "52": "48-52",
            "56": "52-56",
            "60": "56-60",
            "2000": "60+"
        },  # 16-17
        "18": {
            "48": "48-",
            "52": "48-52",
            "56": "52-56",
            "60": "56-60",
            "65": "60-65",
            "70": "65-70",
            "75": "70-75",
            "2000": "75+"
        }  # 18+
    },
    "М": {
        "10": {
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
        "12": {
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
        "14": {
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
        "16": {
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
        "18": {
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

ATHLETE_LIST_THIRD = {
    "Ж": {
        "10": {
        },
        "12": {
        },
        "14": {
        },
        "16": {
        },
        "18": {
        }
    },
    "М": {
        "10": {
        },
        "12": {
        },
        "14": {
        },
        "16": {
        },
        "18": {
        }
    }
}
# Program code.


# Adding participants to the desired section of the main dictionary (data)
def packaging(data, index):
    for athlete in data["participants"][index]["data"]:
        age = calculate_group_of_age(athlete)
        weight = calculate_group_of_weight(athlete, age)
        ATHLETES_DISTRIBUTION[athlete["gender"]][age][weight].append(athlete)
    return ATHLETES_DISTRIBUTION


# Calculation of the participant's age.
def calculate_age(athlete):
    today = date.today()
    date_format = "%d.%m.%y"
    date_born = datetime.strptime(athlete["birthday"], date_format)
    today_date = today.year - date_born.year - ((today.month, today.day) < (date_born.month, date_born.day))
    if today_date > 18:
        today_date = 18
    return today_date


# Calculation the weight group to which the participant belongs.
def calculate_group_of_weight(athlete, age):
    for weight in ATHLETES_DISTRIBUTION[athlete["gender"]][age]:
        if float(athlete["weight"]) <= float(weight):
            return weight
        continue


# Calculation the age group to which the participant belongs.
def calculate_group_of_age(athlete):
    for groups in ATHLETES_DISTRIBUTION[athlete["gender"]]:
        if calculate_age(athlete) <= int(groups):
            return groups
        continue


# Randomization of the list of participants in the tournament.
def shuffle_tournament(data):
    for gender in data:
        for age in data[gender]:
            for weight in data[gender][age].values():
                shuffle(weight)


# Changes the keys of age categories for the distribution of participants to the names of
# categories approved in the regulations.
def change_to_normal_name_in_age(data):
    for gender in data:
        for age in copy(data[gender]):
            data[gender][age_count[gender][age]] = data[gender].pop(age)


# Changes the keys of weight categories for the distribution of participants to the names of
# categories approved in the regulations.
def change_to_normal_name_in_weight(data):
    for gender in data:
        for age in data[gender]:
            for weight in copy(data[gender][age]):
                data[gender][age][weight_count[gender][age][weight]] = data[gender][age].pop(weight)


# Converting a dictionary containing a list of participants in the competition into a dictionary containing
# the location of participants in the tournament grid.
def to_actual_data(data):
    for gender in data:
        for age in copy(data[gender]):
            for weight in copy(data[gender][age]):
                adding_is_circle_trinity(data[gender][age][weight])
                '''
                Deleting empty part of main dictionary.
                '''
                if len(data[gender][age][weight]) <= 1:
                    data[gender][age].pop(weight)
                    continue

                '''
                Deleting part of main dictionary with third participant of main dictionary.
                And adding they to special dict.
                '''
                if len(data[gender][age][weight]) == 3:
                    ATHLETE_LIST_THIRD[gender][age][weight] = copy(data[gender][age][weight])
                    data[gender][age][weight] = []
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
    '''
    Deleting empty part of main dictionary.
    '''
    for gender in data:
        for age in copy(data[gender]):
            if len(data[gender][age]) == 0:
                data[gender].pop(age)
    '''
    Deleting part of main dictionary with third participant of main dictionary.
    And adding they to special dict.
    '''
    for gender in ATHLETE_LIST_THIRD:
        for age in copy(ATHLETE_LIST_THIRD[gender]):
            if len(ATHLETE_LIST_THIRD[gender][age]) == 0:
                ATHLETE_LIST_THIRD[gender].pop(age)


'''
Add flag of triple and score for battle.
'''


def adding_is_circle_trinity(athletes):
    for people in athletes:
        people["is_circle_trinity"] = False
        people["score"] = 0


# A function that does distribute the participants in a dictionary and parsed information.
def parcing():
    data = Parser(file_name=r"C:\Users\megat\project\sortition\Попередня Запоріжжя reborn.docx").result()
    full_list = []
    for categories in range(len(data["participants"])):
        full_list = packaging(data, categories)
    return full_list


# Execution of all program functions, for further use of the main date.
def normalization():
    parser_data = parcing()
    shuffle_tournament(parser_data)
    to_actual_data(parser_data)
    change_to_normal_name_in_weight(parser_data)
    change_to_normal_name_in_age(parser_data)
    change_to_normal_name_in_weight(ATHLETE_LIST_THIRD)
    change_to_normal_name_in_age(ATHLETE_LIST_THIRD)
    return parser_data