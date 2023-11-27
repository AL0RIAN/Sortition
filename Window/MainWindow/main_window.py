import tkinter as tk
import sys
from Window.MainWindow.first_frame_re import FirstElement
from Window.MainWindow.second_frame_re import SecondElement
from Window.MainWindow.third_frame import ThirdElement
from Window.MainWindow.fourth_frame import FourthElement


class MainWindow:
    def __init__(self):
        super().__init__()
        self.lottery = tk.Toplevel()
        self.lottery.title('Жеребкування')
        self.lottery.geometry('800x540')
        self.lottery.resizable(False, False)
        self.lottery.config(bg='#DCF4FF')

        self.first_element = FirstElement(self.lottery)
        # self.second_element = SecondElement(self.lottery, self.first_element.age_choice_menu,
        #                                     self.first_element.weight_choice_menu)
        self.second_element = SecondElement(self.lottery, self.first_element)
        self.third_element = ThirdElement(self.lottery, self.second_element.opponent_first,
                                          self.second_element.opponent_second, self.first_element)
        self.fourth_element = FourthElement(self.lottery)

        self.lottery.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.lottery.mainloop()

    def on_closing(self):
        self.lottery.destroy()
        sys.exit(0)

# test = MainWindow()
# test.run()