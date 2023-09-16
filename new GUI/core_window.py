import tkinter as tk
from copy import copy

from sorting.tournaments_list import PAIR_LIST
from sorting.tournaments_list import TREE
from sorting.tournaments_list import TRIPLE_SUPP
from versus_window import VersusWindow

gender_flag = ''
age_flag = ''
weight_flag = ''
count = 0


'''
У нас будет 4 элемента:
1 - Это элемент где будет выбираться текущий турнир.
2 - Элемент с текущем боем.
3 - Вспомогательный элемент, где будет находиться кнопка с выходом
    из текущего турнира, смена языков и т.д..
4 - Элемент с турнирной таблицей.
'''


class MainWindow:
    def __init__(self):
        super().__init__()
        self.lottery = tk.Tk()
        self.lottery.title('Жеребкування')
        self.lottery.geometry('800x540')
        self.lottery.resizable(False, False)
        self.lottery.config(bg='#DCF4FF')

        self.first_element = FirstElement(self.lottery)
        self.second_element = SecondElement(self.lottery)
        self.third_element = ThirdElement(self.lottery)
        self.fourth_element = FourthElement(self.lottery)

    def run(self):
        self.lottery.mainloop()


'''
Functions for look actual tree in first element.
'''


def actual_tree():
    age_choice_menu.set(PAIR_LIST[count][0]['birthday'])
    weight_choice_menu.set(PAIR_LIST[count][0]['weight'])
    if PAIR_LIST[count][0]['gender'] == 'Ж':
        woman_choices.set(1)
        man_choices.set(0)
    else:
        man_choices.set(1)
        woman_choices.set(0)


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

'''
First Element, with functions of switching in OptionMenu.
'''


class FirstElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, minsize=50)
        self.grid_rowconfigure(2, minsize=50)
        self.grid_columnconfigure(0, minsize=125)
        self.grid_columnconfigure(1, minsize=125)
        self.grid_rowconfigure(3, minsize=60)

        woman_choices = tk.IntVar()
        man_choices = tk.IntVar()
        age_choices = ['10-11', '12-13', '14-15', '16-17', '18+']
        age_choice_menu = tk.StringVar()
        weight_choices = ['test', 'test', 'test', 'test', 'test']
        weight_choice_menu = tk.StringVar()

        woman_button = tk.Checkbutton(self, text="Ж", variable=woman_choices, command=woman_checkbutton)
        man_button = tk.Checkbutton(self, text="М", variable=man_choices, command=man_checkbutton)
        age_option_menu = tk.OptionMenu(self, age_choice_menu, *age_choices)
        age_option_describe = tk.Label(self, bg='#a9c799', text='Віков група')
        weight_option_menu = tk.OptionMenu(self, weight_choice_menu, *weight_choices)
        weight_option_describe = tk.Label(self, bg='#a9c799', text='Вісова група')
        next_tree = tk.Button(self, text='Наступне дерево', command=get_selected_value)

        man_button.grid(row=0, column=0)
        woman_button.grid(row=0, column=1)
        age_option_menu.grid(row=1, column=0)
        age_option_describe.grid(row=1, column=1, sticky='wens')
        weight_option_menu.grid(row=2, column=0)
        weight_option_describe.grid(row=2, column=1, sticky='wens')
        next_tree.grid(row=3, sticky='wens', columnspan=2)
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
    global age_flag
    age_flag = age_choice_menu.get()
    weight_flag = weight_choice_menu.get()
    get_tree(gender_flag, age_flag, weight_flag)


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


class SecondElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ff8282", width=250, height=180)
        self.grid(row=1, column=0)


count = -1
athlete_flag = PAIR_LIST[0][0]
count_field = 0


second_element.grid_rowconfigure(0, minsize=60)
second_element.grid_rowconfigure(1, minsize=60)
second_element.grid_rowconfigure(2, minsize=60)
second_element.grid_columnconfigure(0, minsize=250)

opponent_first = tk.Label(second_element, bg='#a9c799', text='Початок')
opponent_second = tk.Label(second_element, bg='#a9c799', text='Початок')
battle_btn = tk.Button(second_element, bg='#db928f', text='В БІЙ',
                       command=next_battle)

opponent_first.grid(column=0, row=0, sticky='wens')
battle_btn.grid(column=0, row=1, sticky='wens')
opponent_second.grid(column=0, row=2, sticky='wens')


def next_battle():
    global count
    global count_field
    try:
        count += 1
        opponent_first['text'] = PAIR_LIST[count][0]['name']
        opponent_second['text'] = PAIR_LIST[count][1]['name']

        if athlete_flag['name'] == PAIR_LIST[count][0]['name']:
            count_field += 1

        PAIR_LIST[count][0]['score'] = 0
        PAIR_LIST[count][1]['score'] = 0
        get_tree(PAIR_LIST[count][0]['gender'], PAIR_LIST[count][0]['birthday'], PAIR_LIST[count][0]['weight'])
        actual_tree()
        if not count == -1:
            versus_window = VersusWindow(PAIR_LIST[count][0], PAIR_LIST[count][1], count_field)
            versus_window.run()
    except IndexError:
        battle_btn.config(text='Кінець', state=tk.DISABLED)


'''
Third Element.
'''


class ThirdElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.grid(row=2, column=0)


third_element.grid_rowconfigure(0, minsize=30)
third_element.grid_rowconfigure(1, minsize=150)
third_element.grid_columnconfigure(0, minsize=250)

current_battle = tk.Label(third_element, text='№ Поточного спаринга')
back_button = tk.Button(third_element, bg='#db928f', text='Назад', command=previous_battle)

current_battle.grid(row=0, column=0, sticky='wens')
back_button.grid(row=1, column=0, sticky='wens')


def previous_battle():
    global count
    try:
        if count == 1:
            return
        opponent_first['text'] = PAIR_LIST[count][0]['name']
        opponent_second['text'] = PAIR_LIST[count][1]['name']
        get_tree(PAIR_LIST[count][0]['gender'], PAIR_LIST[count][0]['birthday'], PAIR_LIST[count][0]['weight'])
        count -= 1
        actual_tree()
    except IndexError:
        back_button.config(text='Кінець', state=tk.DISABLED)

'''
Fourth Element.
Usual tree
1 step
'''


class FourthElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#DCF4FF", width=550, height=540)
        self.grid(row=0, column=1, rowspan=3)


def get_tree(gender, age, weight):
    for child in fourth_element.winfo_children():
        child.destroy()

    if not TREE[0][gender][age][weight]:
        for child in fourth_element.winfo_children():
            child.destroy()
        fourth_element.grid_rowconfigure(0, minsize=180)
        fourth_element.grid_rowconfigure(1, minsize=180)
        fourth_element.grid_rowconfigure(2, minsize=180)
        fourth_element.grid_columnconfigure(0, minsize=183)
        fourth_element.grid_columnconfigure(1, minsize=183)
        fourth_element.grid_columnconfigure(2, minsize=183)
        for i in range(3, 16):
            fourth_element.grid_rowconfigure(i, minsize=0)

        for i in range(3):
            athlete1 = tk.Label(fourth_element, text=TREE[i + 1][gender][age][weight][0]["name"],
                                bg="#DCF4FF")
            athlete2 = tk.Label(fourth_element, text=TREE[i + 1][gender][age][weight][1]["name"],
                                bg="#DCF4FF")
            if TRIPLE_SUPP[i + 1][gender][age][weight][0]['score'] \
                    > TRIPLE_SUPP[i + 1][gender][age][weight][1]["score"]:
                athlete1.config(fg='green')
                athlete2.config(fg='red')
            elif TRIPLE_SUPP[i + 1][gender][age][weight][0]['score'] \
                    == TRIPLE_SUPP[i + 1][gender][age][weight][1]["score"]:
                pass
            else:
                athlete2.config(fg='green')
                athlete1.config(fg='red')

            athlete1.grid(column=i, row=0, sticky='wens')
            athlete2.grid(column=i, row=2, sticky='wens')

        vs_label1 = tk.Label(fourth_element, text='Проти', bg="#DCF4FF")
        vs_label2 = tk.Label(fourth_element, text='Проти', bg="#DCF4FF")
        vs_label3 = tk.Label(fourth_element, text='Проти', bg="#DCF4FF")
        vs_label1.grid(column=0, row=1, sticky='wens')
        vs_label2.grid(column=1, row=1, sticky='wens')
        vs_label3.grid(column=2, row=1, sticky='wens')
    else:
        for i in range(16):
            if i % 2 == 0:
                flag = 0
            else:
                flag = 1
            fourth_element.grid_rowconfigure(i, minsize=33)
            fourth_element.grid_columnconfigure(i, minsize=137)
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