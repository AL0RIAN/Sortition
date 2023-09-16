import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from first_frame import FirstElement
from fourth_frame import FourthElement


class ThirdElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.grid(row=2, column=0)
        self.create_widgets()
        self.opponent_first = {}
        self.opponent_second = {}
        self.first_frame = FirstElement(parent)
        self.fourth_element_instance = FourthElement(parent)

    def create_widgets(self):
        self.grid_rowconfigure(0, minsize=30)
        self.grid_rowconfigure(1, minsize=150)
        self.grid_columnconfigure(0, minsize=250)

        self.current_battle = tk.Label(self, text='№ Поточного спаринга')
        self.back_button = tk.Button(self, bg='#db928f', text='Назад', command=self.previous_battle)

        self.current_battle.grid(row=0, column=0, sticky='wens')
        self.back_button.grid(row=1, column=0, sticky='wens')

    def previous_battle(self):
        global count
        try:
            if count == 0:
                return
            count -= 1
            self.opponent_first['text'] = PAIR_LIST[count][0]['name']
            self.opponent_second['text'] = PAIR_LIST[count][1]['name']
            self.fourth_element_instance.get_tree(PAIR_LIST[count][0]['gender'],
                                                  PAIR_LIST[count][0]['birthday'],
                                                  PAIR_LIST[count][0]['weight'])
            self.first_frame.actual_tree()
        except IndexError:
            self.back_button.config(text='Кінець', state=tk.DISABLED)