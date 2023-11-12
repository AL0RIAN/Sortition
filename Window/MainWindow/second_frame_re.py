import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from Window.MainWindow.tracking import COUNT
from Window.MainWindow.fourth_frame import FourthElement
from Window.versus_window import VersusWindow


class SecondElement(tk.Frame):
    # def __init__(self, parent, age_option, weight_option):
    def __init__(self, parent, first_frame_instance):
        super().__init__(parent, bg="#ff8282", width=250, height=180)
        self.button_font = ('Times New Roman', 14)
        self.grid(row=1, column=0)
        self.create_widgets()
        self.athlete_flag = PAIR_LIST[0][0]
        self.count_field = 0
        self.first_frame = first_frame_instance
        self.fourth_element_instance = FourthElement(parent)
        self.lottery = parent

    def create_widgets(self):
        self.grid_rowconfigure(0, minsize=60)
        self.grid_rowconfigure(1, minsize=60)
        self.grid_rowconfigure(2, minsize=60)
        self.grid_columnconfigure(0, minsize=250)

        self.opponent_first = tk.Label(self, bg='#a9c799', text='Початок', font=self.button_font)
        self.battle_btn = tk.Button(self, bg='#db928f', text='В БІЙ',
                                    font=self.button_font, command=lambda: self.next_battle(COUNT))
        self.opponent_second = tk.Label(self, bg='#a9c799', text='Початок', font=self.button_font)

        self.opponent_first.grid(column=0, row=0, sticky='wens')
        self.battle_btn.grid(column=0, row=1, sticky='wens')
        self.opponent_second.grid(column=0, row=2, sticky='wens')

    def next_battle(self, count):
        try:
            with count.lock:
                count.value += 1
            self.opponent_first['text'] = PAIR_LIST[count.value][0]['name']
            self.opponent_second['text'] = PAIR_LIST[count.value][1]['name']
            PAIR_LIST[count.value][0]['score'] = 0
            PAIR_LIST[count.value][1]['score'] = 0
            self.fourth_element_instance.get_tree(PAIR_LIST[count.value][0]['gender'],
                                                  PAIR_LIST[count.value][0]['birthday'],
                                                  PAIR_LIST[count.value][0]['weight'])

            if self.athlete_flag['name'] == PAIR_LIST[count.value][0]['name']:
                self.count_field += 1
            if not count.value == -1:
                versus_window = VersusWindow(PAIR_LIST[count.value][0], PAIR_LIST[count.value][1], self.count_field)
                versus_window.run()
        except IndexError:
            self.battle_btn.config(text='Кінець', state=tk.DISABLED)
        finally:
            try:
                self.first_frame.actual_tree()
            except Exception as e:
                print(f"Exception occurred: {e}")