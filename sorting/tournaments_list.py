from sorting.main_dicts import normalization
from sorting.main_dicts import ATHLETE_LIST_THIRD
from copy import copy
from copy import deepcopy

# Declaration of global variables
CHECK = 1  # For a regular tournament bracket.
CHECK_third = -1  # For a tournament bracket of 3 participants.
CHECK_delete = 0  # To keep track of the index of the element we are removing.
TREE = []  # Will be using in GUI.
PAIR_LIST = []  # Will be using in pair_list.
'''
main_dict = {
    "Ж": {
        "10-11": {
            "27-": [],
            "27-30": [],
            "30-33": [],
            "33-36": [],
            "36-39": [],
            "39-42": [],
            "42-45": [],
            "45-48": [],
            "48+": []
        },  # 10-11
        "12-13": {
            "30-": [],
            "30-33": [],
            "33-36": [],
            "36-39": [],
            "39-42": [],
            "42-45": [],
            "45-48": [],
            "48-52": [],
            "52+": []
        },  # 12-13
        "14-15": {
            "39-": [],
            "39-42": [],
            "42-45": [],
            "45-48": [],
            "48-52": [],
            "52-55": [],
            "56+": []
        },  # 14-15
        "16-17": {
            "44-": [],
            "44-48": [],
            "48-52": [],
            "52-56": [],
            "56-60": [],
            "60+": []
        },  # 16-17
        "18+": {
            "48-": [],
            "48-52": [],
            "52-56": [],
            "56-60": [],
            "60-65": [],
            "65-70": [],
            "70-75": [],
            "75+": []
        }  # 18+
    },
    "М": {
        "10-11": {
            "27-": [],
            "27-30": [],
            "30-33": [],
            "33-36": [],
            "36-39": [],
            "39-42": [],
            "42-45": [],
            "45-48": [],
            "48-52": [],
            "52-56": [],
            "56+": []
        },  # 10-11
        "12-13": {
            "30-": [],
            "30-33": [],
            "33-36": [],
            "36-39": [],
            "39-42": [],
            "42-45": [],
            "45-48": [],
            "48-52": [],
            "52-56": [],
            "56-60": [],
            "60+": []
        },  # 12-13
        "14-15": {
            "39-": [],
            "39-42": [],
            "42-45": [],
            "45-48": [],
            "48-52": [],
            "52-56": [],
            "56-60": [],
            "60-65": [],
            "65-70": [],
            "70+": []
        },  # 14-15
        "16-17": {
            "48-": [],
            "48-52": [],
            "52-56": [],
            "56-60": [],
            "60-65": [],
            "65-70": [],
            "70-75": [],
            "75-80": [],
            "80+": []
        },  # 16-17
        "18+": {
            "48-": [],
            "48-52": [],
            "52-56": [],
            "56-60": [],
            "60-65": [],
            "65-70": [],
            "70-75": [],
            "75-80": [],
            "80-85": [],
            "85-90": [],
            "90+": []
        }  # 18+
    }
}
'''
# Program code.

# For lists.
# Creating a list of pairs for further iterations of the tournament.
'''
def winner_of_pair_later(data):
    global CHECK
    pair_of_athletes = 0  # Auxiliary variable, in order to go through the entire list of pairs.
    first_list = []  # Auxiliary list for the function to work.
    second_list = []  # Auxiliary list for the function to work.
    third_list = []  # Auxiliary list for the function to work.
    fourth_list = []
    fifth_list = []

    for gender in data:
        for age_group in data[gender]:
            for weight_group in data[gender][age_group]:
                if len(data[gender][age_group][weight_group]) == 0:
                    continue
                while pair_of_athletes < copy(len(data[gender][age_group][weight_group])):
                    for index_in_pair in range(2):
                        if data[gender][age_group][weight_group][pair_of_athletes][0] == "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] == "-":
                            first_list.append(data[gender][age_group][weight_group][pair_of_athletes][1])
                            pair_of_athletes += 1
                            continue
                        if data[gender][age_group][weight_group][pair_of_athletes][0] == "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] != "-":
                            first_list.append(data[gender][age_group][weight_group][pair_of_athletes][1])
                            pair_of_athletes += 1
                            continue
                        if data[gender][age_group][weight_group][pair_of_athletes][0] != "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] == "-":
                            first_list.append(data[gender][age_group][weight_group][pair_of_athletes][0])
                            pair_of_athletes += 1
                            continue
                        if data[gender][age_group][weight_group][pair_of_athletes][0] != "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] != "-":
                            first_list.append(f"Победитель пары {CHECK}")
                            CHECK += 1
                            pair_of_athletes += 1
                            continue
                        if type(data[gender][age_group][weight_group][pair_of_athletes][0]) == str and\
                                type(data[gender][age_group][weight_group][pair_of_athletes][0]) == str:
                            first_list.append(f"Победитель пары {CHECK}")
                            CHECK += 1
                            pair_of_athletes += 1
                            continue
                    second_list.append(copy(first_list))
                    first_list.clear()
                third_list.append(copy(second_list))
                pair_of_athletes = 0
                second_list.clear()
            fourth_list.append(copy(third_list))
            third_list.clear()
        fifth_list.append(copy(fourth_list))
        fourth_list.clear()
    return fifth_list
'''


# For main Dictionary.
# Creating a list of pairs for further iterations of the tournament.
def winner_of_pair_later(data):
    global CHECK
    pair_of_athletes = 0  # Auxiliary variable, in order to go through the entire list of pairs.
    first_list = []  # Auxiliary list for the function to work.
    second_list = []  # Auxiliary list for the function to work.

    for gender in data:
        for age_group in data[gender]:
            for weight_group in data[gender][age_group]:
                if len(data[gender][age_group][weight_group]) == 0:
                    continue
                while pair_of_athletes < copy(len(data[gender][age_group][weight_group])):
                    for index_in_pair in range(2):
                        if data[gender][age_group][weight_group][pair_of_athletes][0] == "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] == "-":
                            first_list.append(data[gender][age_group][weight_group][pair_of_athletes][1])
                            pair_of_athletes += 1
                            continue
                        if data[gender][age_group][weight_group][pair_of_athletes][0] == "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] != "-":
                            first_list.append(data[gender][age_group][weight_group][pair_of_athletes][1])
                            pair_of_athletes += 1
                            continue
                        if data[gender][age_group][weight_group][pair_of_athletes][0] != "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] == "-":
                            first_list.append(data[gender][age_group][weight_group][pair_of_athletes][0])
                            pair_of_athletes += 1
                            continue
                        if data[gender][age_group][weight_group][pair_of_athletes][0] != "-" and\
                                data[gender][age_group][weight_group][pair_of_athletes][1] != "-":
                            first_list.append(f"Победитель пары {CHECK}")
                            CHECK += 1
                            pair_of_athletes += 1
                            continue
                        if type(data[gender][age_group][weight_group][pair_of_athletes][0]) == str and\
                                type(data[gender][age_group][weight_group][pair_of_athletes][0]) == str:
                            first_list.append(f"Победитель пары {CHECK}")
                            CHECK += 1
                            pair_of_athletes += 1
                            continue
                    second_list.append(copy(first_list))
                    first_list.clear()
                data[gender][age_group].update({str(weight_group): list(copy(second_list))})
                pair_of_athletes = 0
                second_list.clear()


# A decorator to count how many times the function has been called. (Function should be called 3 times.)
def decorator_for_third(func):
    def wrapper(*args, **kwargs):
        global CHECK_third
        CHECK_third += 1
        result = func(*args, **kwargs)
        return result
    return wrapper


# Determining the list of pairs from the list where 3 participants.
@decorator_for_third
def winner_of_pair_in_third(data_third):
    copy_of_data = deepcopy(data_third)
    new_data = {}
    for gender in copy_of_data:
        for age in copy_of_data[gender]:
            for weight in copy_of_data[gender][age]:
                if CHECK_third == 0:
                    new_data[gender] = copy_of_data[gender]
                    new_data[gender][age][weight].pop(2)
                if CHECK_third == 1:
                    new_data[gender] = copy_of_data[gender]
                    new_data[gender][age][weight].pop(1)
                if CHECK_third == 2:
                    new_data[gender] = copy_of_data[gender]
                    new_data[gender][age][weight].pop(0)
    return new_data


# Determining the list of pairs from the general list of the tournament participant.
def winner_of_pair_first(data):
    first_list = []  # Auxiliary list for the function to work.
    second_list = []  # Auxiliary list for the function to work.
    third_list = {}  # Converted to dictionary
    fourth_list = {}  # Converted to dictionary
    fifth_list = {}  # Converted to dictionary
    for gender in data:
        for age_group in data[gender]:
            for weight_group in data[gender][age_group]:
                for athletes in data[gender][age_group][weight_group]:
                    first_list.append(athletes[0])
                    first_list.append(athletes[1])
                    second_list.append(copy(first_list))
                    first_list.clear()
                third_list[weight_group] = copy(second_list)  # Convert to dictionary with key `weight_group`
                second_list.clear()
            fourth_list[age_group] = copy(third_list)  # Convert to dictionary with key `age_group`
            third_list.clear()
        fifth_list[gender] = copy(fourth_list)  # Convert to dictionary with key `gender`
        fourth_list.clear()
    return fifth_list


# Deleting "-" from data.
def deleting_cross(data):
    for gender in data:
        for age_group in data[gender]:
            for weight_group in data[gender][age_group]:
                for athlete_pair in data[gender][age_group][weight_group]:
                    for index_in_pair in athlete_pair:
                        if athlete_pair[0] == "-" or athlete_pair[1] == "-":
                            athlete_pair.clear()
                            continue
                        if athlete_pair[0] == "-" and athlete_pair[1] == "-":
                            athlete_pair.clear()
                            continue
                        '''
                        Changing the values of athletes in PAIR_LIST for 
                        more convenient use of this list together with TREE.
                        '''
                        if type(index_in_pair) == dict:
                            index_in_pair["birthday"] = age_group
                            index_in_pair["weight"] = weight_group
    return data


# List creation function for outputting a list of pairs. And creating list for GUI.
def make_pair_list():
    global TREE
    pair_list = []  # Future list for pair_list.
    tree_with_cross = []  # Future list for tree.
    normal_dict = winner_of_pair_first(normalization())
    dict_wit_cross = deepcopy(normal_dict)
    normal_dict_re = deleting_cross(deepcopy(normal_dict))
    pair_list.append(deepcopy(normal_dict_re))
    tree_with_cross.append(deepcopy(dict_wit_cross))
    '''
    Because there are only 4 iterations in the tournament.
    '''
    for i in range(3):
        winner_of_pair_later(normal_dict)
        dict_wit_cross = deepcopy(normal_dict)
        normal_dict_re = deleting_cross(deepcopy(normal_dict))
        troika_dict = winner_of_pair_in_third(ATHLETE_LIST_THIRD)
        '''
        Merging dictionaries into 1.
        '''
        for gender in troika_dict:
            for age_group in troika_dict[gender]:
                for weight_group in troika_dict[gender][age_group]:
                    dict_wit_cross[gender][age_group][weight_group] = deepcopy(troika_dict[gender][age_group][weight_group])
                    '''
                    Changing the values of athletes in PAIR_LIST for 
                    more convenient use of this list together with TREE.
                    '''
                    for index in range(len(troika_dict[gender][age_group][weight_group])):
                        troika_dict[gender][age_group][weight_group][index]["birthday"] = age_group
                        troika_dict[gender][age_group][weight_group][index]["weight"] = weight_group
                    normal_dict_re[gender][age_group][weight_group] = troika_dict[gender][age_group][weight_group]
        pair_list.append(deepcopy(normal_dict_re))
        tree_with_cross.append(dict_wit_cross)
    TREE = tree_with_cross
    return pair_list


# The function of deleting empty elements, for more convenient and faster passage through the list of pairs.
def pair_list_cleaner(pair_list):
    global CHECK_delete
    '''
    PLEASE DON'T ASK HOW IT WORKS. IF IT WORKS, DO NOT TOUCH!!!!
    '''
    check_list = []
    for tournament_iterations in copy(pair_list):
        for gender in copy(tournament_iterations):
            for age_group in copy(tournament_iterations[gender]):
                for weight_group in copy(tournament_iterations[gender][age_group]):
                    for item in deepcopy(tournament_iterations[gender][age_group][weight_group]):
                        '''
                        Creating a complete list of couples.
                        '''
                        if len(item) != 0:
                            if type(item) == list:
                                for items in tournament_iterations[gender][age_group][weight_group]:
                                    check_list.append(items)
                                    continue
                                continue
                            check_list.append(tournament_iterations[gender][age_group][weight_group])
                        break
    '''
    Old code, with the old view of the list of pairs, if you need to restore it, 
    then you need to delete everything before the last comment.
    '''
    #                     if len(item) == 0:
    #                         tournament_iterations[gender][age_group][weight_group].remove(item)
    #                 if len(tournament_iterations[gender][age_group][weight_group]) == 0:
    #                     tournament_iterations[gender][age_group].pop(weight_group)
    #             if len(tournament_iterations[gender][age_group]) == 0:
    #                 tournament_iterations[gender].pop(age_group)
    #         if len(tournament_iterations[gender]) == 0:
    #             tournament_iterations.pop(gender)
    # for tournament_iterations in copy(range(len(pair_list))):
    #     if len(pair_list[CHECK_delete]) == 0:
    #         pair_list.pop(CHECK_delete)
    #         continue
    #     CHECK_delete += 1
    return check_list


sth_list = make_pair_list()
PAIR_LIST = pair_list_cleaner(sth_list)
print(TREE)
print(PAIR_LIST)
# Rasfuma









# AGREEE
