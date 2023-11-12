import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from Window.MainWindow.tracking import COUNT


class FirstElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        button_font = ('Times New Roman', 16)
        self.grid(row=0, column=0)
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, minsize=50)
        self.grid_rowconfigure(2, minsize=50)
        self.grid_columnconfigure(0, minsize=250)
        self.grid_rowconfigure(3, minsize=60)

        self.woman_choices = tk.IntVar()
        self.man_choices = tk.IntVar()

        self.gender_flag = tk.Label(self, fg='#FFFFFF', bg="#7d7373", font=button_font, text="Стать")

        self.age_choice_menu = tk.Label(self, fg='#FFFFFF', bg="#7d7373", font=button_font, text='Вік')
        self.weight_choice_menu = tk.Label(self, fg='#FFFFFF', bg="#7d7373", font=button_font, text='Вага')
        self.current_battle = tk.Label(self, text='№ Поточного спаринга', font=button_font)

        self.gender_flag.grid(row=0, column=0)
        self.age_choice_menu.grid(row=1, column=0)
        self.weight_choice_menu.grid(row=2, column=0)
        self.current_battle.grid(row=3, sticky='wens')

    def actual_tree(self):
        if PAIR_LIST[COUNT.value][0]['gender'] == 'Ж':
            self.gender_flag.config(text='Ж')
        else:
            self.gender_flag.config(text='М')
        self.actual_age()
        self.weight_choice_menu.config(text=PAIR_LIST[COUNT.value][0]['weight'])
        self.current_battle.config(text=f'Спарінг №{COUNT.value + 1}')

    def actual_age(self):
        self.age_choice_menu.config(text=PAIR_LIST[COUNT.value][0]['birthday'])