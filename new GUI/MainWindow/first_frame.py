import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from sorting.tournaments_list import TREE
from fourth_frame import FourthElement


class FirstElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.grid(row=0, column=0)
        self.choices_dict = {'Ж': {}, 'М': {}}
        self.create_choices_dict()
        self.create_widgets()
        self.gender_flag = None
        self.fourth_element_instance = FourthElement(parent)
        self.woman_choices = tk.IntVar()
        self.man_choices = tk.IntVar()
        self.age_choice_menu = tk.StringVar()
        self.weight_choice_menu = tk.StringVar()
        self.woman_button = tk.Checkbutton()
        self.man_button = tk.Checkbutton()

    def create_widgets(self):
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, minsize=50)
        self.grid_rowconfigure(2, minsize=50)
        self.grid_columnconfigure(0, minsize=125)
        self.grid_columnconfigure(1, minsize=125)
        self.grid_rowconfigure(3, minsize=60)

        self.create_gender_buttons()
        self.create_age_dropdown()
        self.create_weight_dropdown()
        self.create_next_button()

    def create_gender_buttons(self):
        self.woman_button = tk.Checkbutton(self, text="Ж", variable=self.woman_choices, command=self.woman_checkbutton)
        self.man_button = tk.Checkbutton(self, text="М", variable=self.man_choices, command=self.man_checkbutton)
        self.woman_button.grid(row=0, column=0)
        self.man_button.grid(row=0, column=1)

    def create_age_dropdown(self):
        age_option_menu = tk.OptionMenu(self, self.age_choice_menu, *self.age_choices)
        age_option_describe = tk.Label(self, bg='#a9c799', text='Вікова група')
        age_option_menu.grid(row=1, column=0)
        age_option_describe.grid(row=1, column=1, sticky='wens')

    def create_weight_dropdown(self):
        weight_option_menu = tk.OptionMenu(self, self.weight_choice_menu, *self.weight_choices)
        weight_option_describe = tk.Label(self, bg='#a9c799', text='Вагова категорія')
        weight_option_menu.grid(row=2, column=0)
        weight_option_describe.grid(row=2, column=1, sticky='wens')

    def create_next_button(self):
        next_tree = tk.Button(self, text='Наступне дерево', command=self.get_selected_value)
        next_tree.grid(row=3, sticky='wens', columnspan=2)

    def woman_checkbutton(self):
        if self.woman_choices.get() == 1:
            self.man_choices.set(0)
            # Добавьте логику при выборе женского пола

    def man_checkbutton(self):
        if self.man_choices.get() == 1:
            self.woman_choices.set(0)
            # Добавьте логику при выборе мужского пола

    def get_selected_value(self):
        age_flag = self.age_choice_menu.get()
        weight_flag = self.weight_choice_menu.get()
        gender_flag = 'Ж' if self.woman_choices.get() == 1 else 'М'
        self.fourth_element_instance.get_tree(gender_flag, age_flag, weight_flag)

    def man_checkbutton(self, *args):
        if self.man_choices.get() == 1:
            self.gender_flag = 'М'
            self.woman_choices.set(0)
            new_choices = list(self.choices_dict['М'])
            self.age_choice_menu.set(new_choices[0])
            self.age_option_menu['menu'].delete(0, 'end')

            for choice in new_choices:
                self.age_option_menu['menu'].add_command(label=choice,
                                                         command=lambda new_choice=choice: self.man_age_checkbutton(
                                                             new_choice))

    def man_age_checkbutton(self, choice):
        new_choice = choice
        self.age_choice_menu.set(new_choice)
        new_choices = list(self.choices_dict['М'][self.age_choice_menu.get()])
        self.weight_choice_menu.set(new_choices[0])
        self.weight_option_menu['menu'].delete(0, 'end')

        for choice in new_choices:
            self.weight_option_menu['menu'].add_command(label=choice,
                                                        command=lambda new_choice=choice: self.weight_choice_menu.set(
                                                            new_choice))

    def woman_checkbutton(self, *args):
        if self.woman_choices.get() == 1:
            self.gender_flag = 'Ж'
            self.man_choices.set(0)
            new_choices = list(self.choices_dict['Ж'])
            self.age_choice_menu.set(new_choices[0])
            self.age_option_menu['menu'].delete(0, 'end')

            for choice in new_choices:
                self.age_option_menu['menu'].add_command(label=choice,
                                                         command=lambda new_choice=choice: self.woman_age_checkbutton(
                                                             new_choice))

    def woman_age_checkbutton(self, choice):
        new_choice = choice
        self.age_choice_menu.set(new_choice)
        new_choices = list(self.choices_dict['Ж'][self.age_choice_menu.get()])
        self.weight_choice_menu.set(new_choices[0])
        self.weight_option_menu['menu'].delete(0, 'end')

        for choice in new_choices:
            self.weight_option_menu['menu'].add_command(label=choice,
                                                        command=lambda new_choice=choice: self.weight_choice_menu.set(
                                                            new_choice))

    def get_selected_value(self):
        age_flag = self.age_choice_menu.get()
        weight_flag = self.weight_choice_menu.get()
        gender_flag = 'Ж' if self.woman_choices.get() == 1 else 'М'
        self.fourth_element_instance.get_tree(gender_flag, age_flag, weight_flag)

    def create_choices_dict(self):
        for gender in TREE[0]:
            for age in TREE[0][gender]:
                age_choices = list(TREE[0][gender].keys())
                self.choices_dict[gender][age] = {}
                for weight in TREE[0][gender][age]:
                    weight_choices = list(TREE[0][gender][age].keys())
                    self.choices_dict[gender][age][weight] = weight_choices

    def actual_tree(self):
        self.age_choice_menu.set(PAIR_LIST[self.count][0]['birthday'])
        self.weight_choice_menu.set(PAIR_LIST[self.count][0]['weight'])
        if PAIR_LIST[self.count][0]['gender'] == 'Ж':
            self.woman_choices.set(1)
            self.man_choices.set(0)
        else:
            self.man_choices.set(1)
            self.woman_choices.set(0)