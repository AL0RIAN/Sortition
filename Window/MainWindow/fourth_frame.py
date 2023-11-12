import tkinter as tk
from sorting.tournaments_list import TREE
from sorting.tournaments_list import TRIPLE_SUPP


class FourthElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#DCF4FF", width=550, height=540)
        self.grid(row=0, column=1, rowspan=3)
        self.button_font = ('Times New Roman', 10)

    def make_column(self, gender, age, weight, number_cycle, number_field, n_column):
        for i in range(number_cycle):
            flag = 0 if i % 2 == 0 else 1
            try:
                athlete = tk.Label(self, text=TREE[n_column][gender][age][weight][i // 2][flag]["name"],
                                   font=self.button_font, bg="#DCF4FF")
            except TypeError:
                athlete = tk.Label(self, text=TREE[n_column][gender][age][weight][i // 2][flag],
                                   font=self.button_font, bg="#DCF4FF")
            athlete.grid(column=n_column, row=i * number_field, rowspan=number_field)

    def get_tree(self, gender, age, weight):
        for child in self.winfo_children():
            child.destroy()

        for i in range(16):
            athlete_label = tk.Label(self, text="", bg="#DCF4FF")
            athlete_label.grid(column=0, row=i)
            self.grid_rowconfigure(i, minsize=33)
            self.grid_columnconfigure(i, minsize=137)

        if TREE[0][gender][age][weight]:
            '''
            1 step
            '''
            self.make_column(gender, age, weight, 16, 1, 0)
            '''
            2 step
            '''
            self.make_column(gender, age, weight, 8, 2, 1)
            '''
            3 step
            '''
            self.make_column(gender, age, weight, 4, 4, 2)
            '''
            4 step
            '''
            self.make_column(gender, age, weight, 2, 8, 3)
        else:
            for i in range(3):
                self.grid_rowconfigure(i, minsize=40)
                self.grid_columnconfigure(i, minsize=137)
                athlete1 = tk.Label(self, text=TREE[i + 1][gender][age][weight][0]["name"], bg="#DCF4FF",
                                    font=self.button_font)
                athlete2 = tk.Label(self, text=TREE[i + 1][gender][age][weight][1]["name"], bg="#DCF4FF",
                                    font=self.button_font)
                if TRIPLE_SUPP[i + 1][gender][age][weight][0]['score'] > TRIPLE_SUPP[i + 1][gender][age][weight][1][
                    "score"]:
                    athlete1.config(fg='green')
                    athlete2.config(fg='red')
                elif TRIPLE_SUPP[i + 1][gender][age][weight][0]['score'] == TRIPLE_SUPP[i + 1][gender][age][weight][1][
                    "score"]:
                    pass
                else:
                    athlete2.config(fg='green')
                    athlete1.config(fg='red')

                athlete1.place(x=i * 183, y=0, width=183, height=180)
                athlete2.place(x=i * 183, y=360, width=183, height=180)

                vs_label = tk.Label(self, text='Проти', bg="#DCF4FF", font=("Times New Roman", 20))
                vs_label.place(x=i * 183, y=180, width=183, height=180)