import tkinter as tk
from functools import partial
from sorting.tournaments_list import PAIR_LIST
from Window.MainWindow.tracking import COUNT
from Window.MainWindow.first_frame_re import FirstElement
from Window.MainWindow.fourth_frame import FourthElement
import traceback


class ThirdElement(tk.Frame):
    def __init__(self, parent, opponent_first, opponent_second, first_frame_instance):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.button_font = ('Times New Roman', 20)
        self.grid(row=2, column=0)
        self.create_widgets()
        self.opponent_first = opponent_first
        self.opponent_second = opponent_second
        self.first_frame = first_frame_instance
        self.fourth_element_instance = FourthElement(parent)

    def create_widgets(self):
        self.grid_rowconfigure(0, minsize=180)
        self.grid_columnconfigure(0, minsize=250)

        self.back_button = tk.Button(self, bg='#db928f', text='Назад',
                                     font=self.button_font, command=partial(self.previous_battle, COUNT))

        self.back_button.grid(row=0, column=0, sticky='wens')

    # def previous_battle(self, count):
    #     try:
    #         if count.value == 0:
    #             return
    #         with count.lock:
    #             count.value -= 1
    #         self.opponent_first['text'] = PAIR_LIST[count.value][0]['name']
    #         self.opponent_second['text'] = PAIR_LIST[count.value][1]['name']
    #         self.fourth_element_instance.get_tree(PAIR_LIST[count.value][0]['gender'],
    #                                               PAIR_LIST[count.value][0]['birthday'],
    #                                               PAIR_LIST[count.value][0]['weight'])
    #         self.first_frame.actual_tree()
    #     except IndexError:
    #         self.back_button.config(text='Кінець', state=tk.DISABLED)
    def previous_battle(self, count):
        try:
            if count.value == 0:
                return
            with count.lock:
                count.value -= 1
            self.opponent_first['text'] = PAIR_LIST[count.value][0]['name']
            self.opponent_second['text'] = PAIR_LIST[count.value][1]['name']
            self.fourth_element_instance.get_tree(PAIR_LIST[count.value][0]['gender'],
                                                  PAIR_LIST[count.value][0]['birthday'],
                                                  PAIR_LIST[count.value][0]['weight'])
            self.first_frame.actual_tree()
        except IndexError:
            self.back_button.config(text='Кінець', state=tk.DISABLED)
        except Exception as e:
            print(f"Unexpected error in previous_battle: {e}")
            traceback.print_exc()
