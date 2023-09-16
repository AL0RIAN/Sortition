import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from first_frame import FirstElement
from fourth_frame import FourthElement
from  import VersusWindow


class SecondElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ff8282", width=250, height=180)
        self.grid(row=1, column=0)
        self.count = -1
        self.athlete_flag = PAIR_LIST[0][0]
        self.count_field = 0
        self.first_frame = FirstElement(parent)
        self.fourth_element_instance = FourthElement(parent)

        self.grid_rowconfigure(0, minsize=60)
        self.grid_rowconfigure(1, minsize=60)
        self.grid_rowconfigure(2, minsize=60)
        self.grid_columnconfigure(0, minsize=250)

        self.opponent_first = tk.Label(self, bg='#a9c799', text='Початок')
        self.opponent_second = tk.Label(self, bg='#a9c799', text='Початок')
        self.battle_btn = tk.Button(self, bg='#db928f', text='В БІЙ', command=self.next_battle)

        self.opponent_first.grid(column=0, row=0, sticky='wens')
        self.battle_btn.grid(column=0, row=1, sticky='wens')
        self.opponent_second.grid(column=0, row=2, sticky='wens')

    def next_battle(self):
        try:
            self.count += 1
            self.opponent_first['text'] = PAIR_LIST[self.count][0]['name']
            self.opponent_second['text'] = PAIR_LIST[self.count][1]['name']

            if self.athlete_flag['name'] == PAIR_LIST[self.count][0]['name']:
                self.count_field += 1

            PAIR_LIST[self.count][0]['score'] = 0
            PAIR_LIST[self.count][1]['score'] = 0
            self.fourth_element_instance.get_tree(PAIR_LIST[self.count][0]['gender'],
                                                  PAIR_LIST[self.count][0]['birthday'],
                                                  PAIR_LIST[self.count][0]['weight'])
            self.first_frame.actual_tree()
            if not self.count == -1:
                versus_window = VersusWindow(PAIR_LIST[self.count][0], PAIR_LIST[self.count][1], self.count_field)
                versus_window.run()
        except IndexError:
            self.battle_btn.config(text='Кінець', state=tk.DISABLED)