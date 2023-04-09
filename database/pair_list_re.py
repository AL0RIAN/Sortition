from database.main_data import sth_list
from copy import copy

CHECK = 1
def winner_of_pair_later(data):
    global CHECK
    pair_of_athletes = 0  # Auxiliary variable, in order to go through the entire list of pairs.
    first_list = []  # Auxiliary list for the function to work.
    second_list = []  # Auxiliary list for the function to work.
    third_list = []  # Auxiliary list for the function to work.
    fourth_list = []
    fifth_list = []
    for gender in range(len(data)):
        for age_group in range(5):
            for weight_group in range(len(data[gender][age_group])):
                if len(data[gender][age_group][weight_group]) == 0:
                    break
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
Maybe it's will be a auxiliary function to a winner_of_pair_later.
'''
# def cheking_on_cross():
'''
Making pair from main dictionary.
'''
def winner_of_pair_first(data):
    global CHECK
    first_list = []  # Auxiliary list for the function to work.
    second_list = []  # Auxiliary list for the function to work.
    third_list = []  # Auxiliary list for the function to work.
    fourth_list = []  # Auxiliary list for the function to work.
    fifth_list = []  # Auxiliary list for the function to work.
    for gender in data:
        for age_group in data[gender]:
            for weight_group in data[gender][age_group]:
                for athletes in data[gender][age_group][weight_group]:
                    first_list.append(athletes[0])
                    first_list.append(athletes[1])
                    second_list.append(copy(first_list))
                    first_list.clear()
                third_list.append(copy(second_list))
                second_list.clear()
            fourth_list.append(copy(third_list))
            third_list.clear()
        fifth_list.append(copy(fourth_list))
        fourth_list.clear()
    return fifth_list


'''
Deleting "-" from data for pair_list.
'''
def deleting_cross(data_list):
    for gender in data_list:
        for age_group in gender:
            for weight_group in age_group:
                for athlete_pair in weight_group:
                    if athlete_pair[0] == "-" or athlete_pair[1] == "-":
                        athlete_pair.clear()
                        continue
                    if athlete_pair[0] == "-" and athlete_pair[1] == "-":
                        athlete_pair.clear()
                        continue

changing_list = winner_of_pair_first(sth_list)
changing_list = winner_of_pair_later(changing_list)
changing_list = winner_of_pair_later(changing_list)
changing_list = winner_of_pair_later(changing_list)
deleting_cross(changing_list)
print(changing_list)
