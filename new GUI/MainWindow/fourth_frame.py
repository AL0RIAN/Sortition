import tkinter as tk
from sorting.tournaments_list import TREE
from sorting.tournaments_list import TRIPLE_SUPP

class FourthElement(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#DCF4FF", width=550, height=540)
        self.grid(row=0, column=1, rowspan=3)

    def get_tree(self, gender, age, weight):
        for child in self.winfo_children():
            child.destroy()

        if not TREE[0][gender][age][weight]:
            for child in self.winfo_children():
                child.destroy()
            self.grid_rowconfigure(0, minsize=180)
            self.grid_rowconfigure(1, minsize=180)
            self.grid_rowconfigure(2, minsize=180)
            self.grid_columnconfigure(0, minsize=183)
            self.grid_columnconfigure(1, minsize=183)
            self.grid_columnconfigure(2, minsize=183)
            for i in range(3, 16):
                self.grid_rowconfigure(i, minsize=0)

            for i in range(3):
                athlete1 = tk.Label(self, text=TREE[i + 1][gender][age][weight][0]["name"],
                                    bg="#DCF4FF")
                athlete2 = tk.Label(self, text=TREE[i + 1][gender][age][weight][1]["name"],
                                    bg="#DCF4FF")
                if TRIPLE_SUPP[i + 1][gender][age][weight][0]['score'] \
                        > TRIPLE_SUPP[i + 1][gender][age][weight][1]["score"]:
                    athlete1.config(fg='green')
                    athlete2.config(fg='red')
                elif TRIPLE_SUPP[i + 1][gender][age][weight][0]['score'] \
                        == TRIPLE_SUPP[i + 1][gender][age][weight][1]["score"]:
                    pass
                else:
                    athlete2.config(fg='green')
                    athlete1.config(fg='red')

                athlete1.grid(column=i, row=0, sticky='wens')
                athlete2.grid(column=i, row=2, sticky='wens')

            vs_label1 = tk.Label(self, text='Проти', bg="#DCF4FF")
            vs_label2 = tk.Label(self, text='Проти', bg="#DCF4FF")
            vs_label3 = tk.Label(self, text='Проти', bg="#DCF4FF")
            vs_label1.grid(column=0, row=1, sticky='wens')
            vs_label2.grid(column=1, row=1, sticky='wens')
            vs_label3.grid(column=2, row=1, sticky='wens')
        else:
            for i in range(16):
                if i % 2 == 0:
                    flag = 0
                else:
                    flag = 1
                self.grid_rowconfigure(i, minsize=33)
                self.grid_columnconfigure(i, minsize=137)
                try:
                    athlete = tk.Label(self, text=TREE[0][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
                except TypeError:
                    athlete = tk.Label(self, text=TREE[0][gender][age][weight][i//2][flag], bg="#DCF4FF")
                athlete.grid(column=0, row=i)
            '''
            2 step
            '''
            for i in range(8):
                if i % 2 == 0:
                    flag = 0
                else:
                    flag = 1
                try:
                    athlete = tk.Label(self, text=TREE[1][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
                except TypeError:
                    athlete = tk.Label(self, text=TREE[1][gender][age][weight][i//2][flag], bg="#DCF4FF")
                athlete.grid(column=1, row=2 * i, rowspan=2)
            '''
            3 step
            '''
            for i in range(4):
                if i % 2 == 0:
                    flag = 0
                else:
                    flag = 1
                try:
                    athlete = tk.Label(self, text=TREE[2][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
                except TypeError:
                    athlete = tk.Label(self, text=TREE[2][gender][age][weight][i//2][flag], bg="#DCF4FF")
                athlete.grid(column=2, row=4 * i, rowspan=4)
            '''
            4 step
            '''
            for i in range(2):
                if i % 2 == 0:
                    flag = 0
                else:
                    flag = 1
                try:
                    athlete = tk.Label(self, text=TREE[3][gender][age][weight][i//2][flag]["name"], bg="#DCF4FF")
                except TypeError:
                    athlete = tk.Label(self, text=TREE[3][gender][age][weight][i//2][flag], bg="#DCF4FF")
                athlete.grid(column=3, row=8 * i, rowspan=8)