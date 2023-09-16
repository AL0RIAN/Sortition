import tkinter as tk
from first_frame import FirstElement
from second_frame import SecondElement
from third_frame import ThirdElement
from fourth_frame import FourthElement
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