import tkinter as tk
from sorting.tournaments_list import PAIR_LIST


'''
У нас будет 4 элемента:
1 - Это элемент где будет выбираться текущий турнир.
2 - Элемент с текущем боем.
3 - Вспомогательный элемент, где будет находиться кнопка с выходом
    из текущего турнира, смена языков и т.д..
4 - Элемент с турнирной таблицей.
'''


lottery = tk.Tk()
lottery.title('Жеребкування')
lottery.geometry('800x540')
lottery.resizable(False, False)
lottery.config(bg='#DCF4FF')

first_element = tk.Frame(lottery, bg="#7d7373", width=250, height=180)
second_element = tk.Frame(lottery, bg="#ff8282", width=250, height=180)
third_element = tk.Frame(lottery, bg="#7d7373", width=250, height=180)
fourth_element = tk.Frame(lottery, bg="#DCF4FF", width=550, height=540)

first_element.grid(row=0, column=0)
second_element.grid(row=1, column=0)
third_element.grid(row=2, column=0)
fourth_element.grid(row=0, column=1, rowspan=3)

'''
First Element.
'''

'''
Second Element.
'''

count = 0

def next_battle():
    global count
    count += 1
    opponent_first['text'] = PAIR_LIST[count][0]['name']
    opponent_second['text'] = PAIR_LIST[count][1]['name']


second_element.grid_rowconfigure(0, minsize=60)
second_element.grid_rowconfigure(1, minsize=60)
second_element.grid_rowconfigure(2, minsize=60)
second_element.grid_columnconfigure(0, minsize=250)

opponent_first = tk.Label(second_element, bg='#a9c799', text=PAIR_LIST[count][0]['name'])
opponent_second = tk.Label(second_element, bg='#a9c799', text=PAIR_LIST[count][1]['name'])
battle_btn = tk.Button(second_element, bg='#db928f', text='В БІЙ',
                       command=next_battle)

opponent_first.grid(column=0, row=0, sticky='wens')
battle_btn.grid(column=0, row=1, sticky='wens')
opponent_second.grid(column=0, row=2, sticky='wens')


'''
Third Element.
'''

'''
Fourth Element.
'''


lottery.mainloop()


#AGREEEEE