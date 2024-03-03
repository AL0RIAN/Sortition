import tkinter as tk
from sorting.tournaments_list import TRIPLE_SUPP
import shared_triple_supp

supporting_tree = {}

'''
Создание окна боя.
'''


class VersusWindow:
    def __init__(self, first_athlete, second_athlete, count):
        self.versus = tk.Tk()
        self.versus.title('Бій')
        self.versus.geometry('600x390')
        self.versus.resizable(False, False)
        self.versus.config(bg='#DCF4FF')
        self.first_athlete = first_athlete
        self.second_athlete = second_athlete
        self.count = count
        self.is_open = True

        self.versus.grid_columnconfigure(0, minsize=200)
        self.versus.grid_columnconfigure(1, minsize=200)
        self.versus.grid_columnconfigure(2, minsize=200)

        self.create_widgets()

    # Создание и размещение виджетов
    def create_widgets(self):
        label1 = tk.Label(self.versus, text=self.first_athlete['name'])
        label2 = tk.Label(self.versus, text="Проти")
        label3 = tk.Label(self.versus, text=self.second_athlete['name'])

        score1 = tk.Label(self.versus, text=self.first_athlete['score'])
        score2 = tk.Label(self.versus, text=self.second_athlete['score'])

        add1 = tk.Button(self.versus, text="Добавить", command=lambda: self.adding(1, score1))
        add2 = tk.Button(self.versus, text="Добавить", command=lambda: self.adding(2, score2))

        warning1 = tk.Button(self.versus, text="Предупреждение")
        warning2 = tk.Button(self.versus, text="Предупреждение")

        note1 = tk.Button(self.versus, text="Замечание")
        note2 = tk.Button(self.versus, text="Замечание")

        border1 = tk.Button(self.versus, text="Граница")
        border2 = tk.Button(self.versus, text="Граница")

        define = tk.Button(self.versus, text="Определить", command=self.close)

        # Размещение виджетов на сетке
        label1.grid(row=0, column=0)
        label2.grid(row=0, column=1)
        label3.grid(row=0, column=2)

        score1.grid(row=1, column=0)
        score2.grid(row=1, column=2)

        add1.grid(row=2, column=0)
        add2.grid(row=2, column=2)

        warning1.grid(row=3, column=0)
        warning2.grid(row=3, column=2)

        note1.grid(row=4, column=0)
        note2.grid(row=4, column=2)

        border1.grid(row=5, column=0)
        border2.grid(row=5, column=2)

        define.grid(row=6, column=1)

    # def run(self):
    #     while self.is_open:
    #         self.versus.update()
    #     self.versus.mainloop()

    def run(self):
        while self.is_open:
            self.versus.update()

    def close(self):
        TRIPLE_SUPP = shared_triple_supp.read_variable()
        self.is_open = False
        gender_flag = self.first_athlete['gender']
        birthday_flag = self.first_athlete['birthday']
        weight_flag = self.first_athlete['weight']
        print(TRIPLE_SUPP)
        if self.first_athlete['is_circle_trinity'] == 1:
            if self.first_athlete['score'] > self.second_athlete['score']:
                TRIPLE_SUPP[self.count][gender_flag][birthday_flag][weight_flag][0]['score']\
                    = self.first_athlete['score']
                shared_triple_supp.write_variable(TRIPLE_SUPP)
            else:
                TRIPLE_SUPP[self.count][gender_flag][birthday_flag][weight_flag][1]['score']\
                    = self.second_athlete['score']
                shared_triple_supp.write_variable(TRIPLE_SUPP)
        self.versus.destroy()

    def adding(self, button_number, score):
        if button_number == 1:
            self.first_athlete['score'] += 1
            score.config(text=self.first_athlete['score'])
        elif button_number == 2:
            self.second_athlete['score'] += 1
            score.config(text=self.second_athlete['score'])

