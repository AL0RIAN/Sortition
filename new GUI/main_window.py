import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from sorting.tournaments_list import TREE

gender_flag = ''
age_flag = ''
weight_flag = ''


'''
У нас будет 4 элемента:
1 - Это элемент где будет выбираться текущий турнир.
2 - Элемент с текущем боем.
3 - Вспомогательный элемент, где будет находиться кнопка с выходом
    из текущего турнира, смена языков и т.д..
4 - Элемент с турнирной таблицей.
'''


lottery = tk.Tk()
lottery.title('Жеребкування')
lottery.geometry('800x540')
lottery.resizable(False, False)
lottery.config(bg='#DCF4FF')

first_element = tk.Frame(lottery, bg="#7d7373", width=250, height=180)
second_element = tk.Frame(lottery, bg="#ff8282", width=250, height=180)
third_element = tk.Frame(lottery, bg="#7d7373", width=250, height=180)
fourth_element = tk.Frame(lottery, bg="#DCF4FF", width=550, height=540)

first_element.grid(row=0, column=0)
second_element.grid(row=1, column=0)
third_element.grid(row=2, column=0)
fourth_element.grid(row=0, column=1, rowspan=3)

'''
Crete dictionary for first element(dictionary with categories of tournament trees).
'''

choices_dict = {'Ж': {}, 'М': {}}
for gender in TREE[0]:
    for age in TREE[0][gender]:
        choices = list(TREE[0][gender].keys())
        for weight in TREE[0][gender][age]:
            choices = list(TREE[0][gender][age].keys())
            choices_dict[gender][age] = choices
print(choices_dict)

'''
First Element, with functions of switching in OptionMenu.
'''


def man_checkbutton(*args):
    if man_choices.get() == 1:
        global gender_flag
        gender_flag = 'М'
        woman_choices.set(0)
        new_choices = list(choices_dict['М'])
        age_choice_menu.set(new_choices[0])
        age_option_menu['menu'].delete(0, 'end')

        for choice in new_choices:
            age_option_menu['menu'].add_command(label=choice,
                                                command=lambda new_choice=choice: man_age_checkbutton(new_choice))


def man_age_checkbutton(choice):
    global age_flag
    age_flag = age_choice_menu.get()
    new_choice = choice
    age_choice_menu.set(new_choice)
    new_choices = list(choices_dict['М'][age_choice_menu.get()])
    weight_choice_menu.set(new_choices[0])
    weight_option_menu['menu'].delete(0, 'end')

    for choice in new_choices:
        weight_option_menu['menu'].add_command(label=choice,
                                               command=lambda new_choice=choice: weight_choice_menu.set(new_choice))


def woman_checkbutton(*args):
    if woman_choices.get() == 1:
        global gender_flag
        gender_flag = 'Ж'
        man_choices.set(0)
        new_choices = list(choices_dict['Ж'])
        age_choice_menu.set(new_choices[0])
        age_option_menu['menu'].delete(0, 'end')

        for choice in new_choices:
            age_option_menu['menu'].add_command(label=choice,
                                                command=lambda new_choice=choice: woman_age_checkbutton(new_choice))

def woman_age_checkbutton(choice):
    global age_flag
    age_flag = age_choice_menu.get()
    new_choice = choice
    age_choice_menu.set(new_choice)
    new_choices = list(choices_dict['Ж'][age_choice_menu.get()])
    weight_choice_menu.set(new_choices[0])
    weight_option_menu['menu'].delete(0, 'end')

    for choice in new_choices:
        weight_option_menu['menu'].add_command(label=choice,
                                               command=lambda new_choice=choice: weight_choice_menu.set(new_choice))


def get_selected_value():
    global weight_flag
    weight_flag = weight_choice_menu.get()
    get_tree(gender_flag, age_flag, weight_flag)



# def woman_checkbutton():
#     if woman_choices.get() == 1:
#         man_choices.set(0)
#         new_choices = list(choices_dict['Ж'])
#         age_choice_menu.set(new_choices[0])
#         age_option_menu['menu'].delete(0, 'end')
#         for choice in new_choices:
#             age_option_menu['menu'].add_command(label=choice,
#                                                 command=woman_age_checkbutton(choice))
#
#
# def woman_age_checkbutton(choice):
#     if woman_choices.get() == 1:
#         new_choice = choice
#         age_choice_menu.set(new_choice)
#         new_choices = list(choices_dict['Ж'][age_choice_menu.get()])
#         # Очищаем старые опции во втором OptionMenu
#         weight_choice_menu.set(new_choices[0])
#         weight_option_menu['menu'].delete(0, 'end')
#
#         for choice in new_choices:
#             weight_option_menu['menu'].add_command(label=choice,
#                                                    command=lambda new_choice=choice: weight_choice_menu.set(
#                                                         new_choice))


first_element.grid_rowconfigure(0, minsize=40)
first_element.grid_rowconfigure(1, minsize=50)
first_element.grid_rowconfigure(2, minsize=50)
first_element.grid_columnconfigure(0, minsize=125)
first_element.grid_columnconfigure(1, minsize=125)
first_element.grid_rowconfigure(3, minsize=60)

woman_choices = tk.IntVar()
man_choices = tk.IntVar()
age_choices = ['10-11', '12-13', '14-15', '16-17', '18+']
age_choice_menu = tk.StringVar()
weight_choices = ['test', 'test', 'test', 'test', 'test']
weight_choice_menu = tk.StringVar()

woman_button = tk.Checkbutton(first_element, text="Ж", variable=woman_choices, command=woman_checkbutton)
man_button = tk.Checkbutton(first_element, text="М", variable=man_choices, command=man_checkbutton)
age_option_menu = tk.OptionMenu(first_element, age_choice_menu, *age_choices)
age_option_describe = tk.Label(first_element, bg='#a9c799', text='Віков група')
weight_option_menu = tk.OptionMenu(first_element, weight_choice_menu, *weight_choices)
weight_option_describe = tk.Label(first_element, bg='#a9c799', text='Вісова група')
next_tree = tk.Button(first_element, text='Наступне дерево', command=get_selected_value)


man_button.grid(row=0, column=0)
woman_button.grid(row=0, column=1)
age_option_menu.grid(row=1, column=0)
age_option_describe.grid(row=1, column=1, sticky='wens')
weight_option_menu.grid(row=2, column=0)
weight_option_describe.grid(row=2, column=1, sticky='wens')
next_tree.grid(row=3, sticky='wens', columnspan=2)


'''
Second Element.
'''

count = 0


def next_battle():
    global count
    count += 1
    try:
        opponent_first['text'] = PAIR_LIST[count][0]['name']
        opponent_second['text'] = PAIR_LIST[count][1]['name']
    except TypeError:
        opponent_first['text'] = PAIR_LIST[count][0]
        opponent_second['text'] = PAIR_LIST[count][1]
    except IndexError:
        battle_btn.config(text='Кінець', state=tk.DISABLED)


second_element.grid_rowconfigure(0, minsize=60)
second_element.grid_rowconfigure(1, minsize=60)
second_element.grid_rowconfigure(2, minsize=60)
second_element.grid_columnconfigure(0, minsize=250)

opponent_first = tk.Label(second_element, bg='#a9c799', text=PAIR_LIST[count][0]['name'])
opponent_second = tk.Label(second_element, bg='#a9c799', text=PAIR_LIST[count][1]['name'])
battle_btn = tk.Button(second_element, bg='#db928f', text='В БІЙ',
                       command=next_battle)

opponent_first.grid(column=0, row=0, sticky='wens')
battle_btn.grid(column=0, row=1, sticky='wens')
opponent_second.grid(column=0, row=2, sticky='wens')


'''
Third Element.
'''


third_element.grid_rowconfigure(0, minsize=30)
third_element.grid_rowconfigure(1, minsize=150)
third_element.grid_columnconfigure(0, minsize=250)

current_battle = tk.Label(third_element, text='№ Поточного спаринга')
back_button = tk.Button(third_element, bg='#db928f', text='Назад')

current_battle.grid(row=0, column=0, sticky='wens')
back_button.grid(row=1, column=0, sticky='wens')

'''
Fourth Element.
Usual tree
1 step
'''


def get_tree(gender, age, weight):
    for i in range(16):
        if i % 2 == 0:
            flag = 0
        else:
            flag = 1
        fourth_element.grid_rowconfigure(i, minsize=33)
        fourth_element.grid_columnconfigure(i, minsize=136)
        try:
            athlete = tk.Label(fourth_element, text=TREE[0][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
        except TypeError:
            athlete = tk.Label(fourth_element, text=TREE[0][gender][age][weight][i//2][flag], bg="#DCF4FF")
        athlete.grid(column=0, row=i)
    '''
    2 step
    '''
    for i in range(8):
        if i % 2 == 0:
            flag = 0
        else:
            flag = 1
        try:
            athlete = tk.Label(fourth_element, text=TREE[1][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
        except TypeError:
            athlete = tk.Label(fourth_element, text=TREE[1][gender][age][weight][i//2][flag], bg="#DCF4FF")
        athlete.grid(column=1, row=2 * i, rowspan=2)
    '''
    3 step
    '''
    for i in range(4):
        if i % 2 == 0:
            flag = 0
        else:
            flag = 1
        try:
            athlete = tk.Label(fourth_element, text=TREE[2][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
        except TypeError:
            athlete = tk.Label(fourth_element, text=TREE[2][gender][age][weight][i//2][flag], bg="#DCF4FF")
        athlete.grid(column=2, row=4 * i, rowspan=4)
    '''
    4 step
    '''
    for i in range(2):
        if i % 2 == 0:
            flag = 0
        else:
            flag = 1
        try:
            athlete = tk.Label(fourth_element, text=TREE[3][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
        except TypeError:
            athlete = tk.Label(fourth_element, text=TREE[3][gender][age][weight][i//2][flag], bg="#DCF4FF")
        athlete.grid(column=3, row=8 * i, rowspan=8)

'''
Troika
'''


lottery.mainloop()


#AGREEEEE