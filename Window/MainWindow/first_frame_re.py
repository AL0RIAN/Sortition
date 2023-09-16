import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from Window.MainWindow.tracking import COUNT


class FirstElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.grid(row=0, column=0)
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, minsize=50)
        self.grid_rowconfigure(2, minsize=50)
        self.grid_columnconfigure(0, minsize=125)
        self.grid_columnconfigure(1, minsize=125)
        self.grid_rowconfigure(3, minsize=60)

        self.woman_choices = tk.IntVar()
        self.man_choices = tk.IntVar()

        self.woman_button = tk.Checkbutton(self, text="Ж", variable=self.woman_choices)
        self.man_button = tk.Checkbutton(self, text="М", variable=self.man_choices)

        self.age_choice_menu = tk.Label(self, bg='#a9c799', text='Вік')
        self.weight_choice_menu = tk.Label(self, bg='#a9c799', text='Вага')
        self.age_option_describe = tk.Label(self, bg='#a9c799', text='Вікова категорія')
        self.weight_option_describe = tk.Label(self, bg='#a9c799', text='Вагова категорія')
        self.next_tree = tk.Button(self, text='Наступне дерево')

        self.man_button.grid(row=0, column=0)
        self.woman_button.grid(row=0, column=1)
        self.age_choice_menu.grid(row=1, column=0)
        self.age_option_describe.grid(row=1, column=1, sticky='wens')
        self.weight_choice_menu.grid(row=2, column=0)
        self.weight_option_describe.grid(row=2, column=1, sticky='wens')
        self.next_tree.grid(row=3, sticky='wens', columnspan=2)

    def actual_tree(self):
        if PAIR_LIST[COUNT.value][0]['gender'] == 'Ж':
            print(1)
            self.woman_choices.set(1)
            self.man_choices.set(0)
        else:
            print(1)
            self.man_choices.set(1)
            self.woman_choices.set(0)
        self.actual_age()
        self.weight_choice_menu.config(text=PAIR_LIST[COUNT.value][0]['weight'])

    def actual_age(self):
        self.age_choice_menu.config(text=PAIR_LIST[COUNT.value][0]['birthday'])