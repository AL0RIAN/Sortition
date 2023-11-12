import tkinter as tk
from Window.MainWindow.first_frame_re import FirstElement
from Window.MainWindow.second_frame_re import SecondElement
from Window.MainWindow.third_frame import ThirdElement
from Window.MainWindow.fourth_frame import FourthElement


class MainWindow:
    def __init__(self):
        super().__init__()
        self.lottery = tk.Tk()
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

    def run(self):
        self.lottery.mainloop()


# test = MainWindow()
# test.run()