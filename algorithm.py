import math
import random


class Athlete:
    '''
    Maybe it's temporary, but now it's the main class, which
    representing the athlete.
    '''
    def __init__(self, n, age, weight, score):
        self.n = n
        self.age = age
        self.weight = weight
        self.score = score

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"{self.n}"

def sorter(list_main:list) -> list:
    '''
    Use sorter to sort general list of athletes
    by weight group.
    :param list_main: general list of athletes that we get after output from the file
    :return: two-dimensional list of athletes in where each nested list contains athletes of the same weight group
    '''
    list_return = []   # list which will return for further work with it
    for i in range(len(list_of_age)):
        list_of_w = []   # built-in list filled in by students of the same weight group
        for j in range(len(list_main)):
            if list_of_age[i - 1] < int(list_main[j].age) < list_of_age[i]:
                list_of_w.append(list_main[j])
        list_return.append(list_of_w)
    return list_return
def randomizer(list_main:list, element:list, save_list:list):
    '''
    Use randomize to sort athletes of the
    same weight group in their first fight.
    :param list_main: the main list that we will sort
    :param element: a helper list that use to get the correct output
    :param save_list: a list in which enter our athletes in a random order
    '''
    list_spare = list_main.copy()   # use a copy of the main list in order not to change it
    index = 0

    for i in range(math.ceil(len(list_main) / 2)):
        Kira = random.choice(list_spare)   # first opponent
        del list_spare[list_spare.index(Kira)]
        L = random.choice(list_spare)   # second opponent
        del list_spare[list_spare.index(L)]

        element[index] = Kira       # most adding athletes in the
        save_list.append(Kira)  # correct order to the sorted list
        element[index + 2] = L
        save_list.append(L)
        index += 4

        if len(list_spare) == 1:               # if there is only one athlete left on the list
            save_list.append(list_spare[0])
            break
def next_iteration(element:list, list:list, dividers:list):
    '''
    Use next iteration to output the next
    steps of the tournament tree.
    :param element: a helper list that use to get the correct output
    :param list: the main list that we will change
    :param dividers: list of dividers
    '''
    flag = len(list)   # length of inputting list, because list is changes
    for i in range(flag // 2):   # we leave in the list of winners of the last round
        if i == len(list):
            break
        if list[i].score > list[i + 1].score:
            list.pop(int(i + 1))
        else:
            list.pop(int(i))

    divider = 0   # the divider will be used to determine the stage of tournament tree
    for i in range(len(element)):   # definition divider for stage of tournament tree
        if type(element[i]) == int:
            for j in range(len(dividers)):
                if element[i] % dividers[j] == 0:
                    divider = dividers[j]
                    break
            break

    index = 0
    for i in range(len(element)):   # adding athletes definite position in the list
        if type(element[i]) == int:
            if element[i] % divider == 0:
                element[i] = list[index]
                index += 1
            if index == len(list):
                break



if __name__ == '__main__':
    list_of_age = [27, 30, 33, 36, 39, 42, 45, 48, 52, 56]

    list = []
    first = Athlete("Babodzaki", 38, 70, 3)
    second = Athlete("Malenia", 37, 56, 4)
    third = Athlete("Radan", 37, 100, 4)
    fourth = Athlete("Godri", 38, 74, 2)
    fifth = Athlete("Rennie", 37, 25, 5)
    sixth = Athlete("Renala", 37, 60, 1)
    seventh = Athlete("Godwin", 37, 80, 2)
    eighth = Athlete("Tif", 37, 54, 9)

    list.append(first)
    list.append(second)
    list.append(third)
    list.append(fourth)
    list.append(fifth)
    list.append(sixth)
    list.append(seventh)
    list.append(eighth)

    list_sorted = sorter(list)

    element = [2, 9, 10, 25, 30, 33, 40, 49, 62, 63, 64, 65, 92, 93, 94]   # static list needed for the correct output
                                                                           # of the tournament tree
    escape = [0, 9, 0, 18, 0, 9, 0, 27, 0, 9, 0, 18, 0, 9, 0]   # temporary auxiliary list
    dividers = [2, 3, 5, 7]   # static array to define the stage in the tournament grid
    save = []
    randomizer(list_sorted[4], element, save)

    next_iteration(element, save, dividers)
    next_iteration(element, save, dividers)
    next_iteration(element, save, dividers)

    for i in range(15):   # temporary output to the console
        for j in range(escape[i]):
            print(" ", end='')
        if type(element[i]) == int:
            print('')
            continue
        print(element[i])