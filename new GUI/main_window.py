import tkinter as tk
from sorting.tournaments_list import PAIR_LIST
from sorting.tournaments_list import TREE


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
    try:
        opponent_first['text'] = PAIR_LIST[count][0]['name']
        opponent_second['text'] = PAIR_LIST[count][1]['name']
    except TypeError:
        opponent_first['text'] = PAIR_LIST[count][0]
        opponent_second['text'] = PAIR_LIST[count][1]
    except IndexError:
        battle_btn.config(text='Кінець', state=tk.DISABLED)


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
Usual tree
1 step
'''


for i in range(16):
    if i % 2 == 0:
        flag = 0
    else:
        flag = 1
    fourth_element.grid_rowconfigure(i, minsize=33)
    fourth_element.grid_columnconfigure(i, minsize=136)
    try:
        athlete = tk.Label(fourth_element, text=TREE[0]['М']['18+']['48-'][i//2][flag]["name"], bg="#DCF4FF")
    except TypeError:
        athlete = tk.Label(fourth_element, text=TREE[0]['М']['18+']['48-'][i//2][flag], bg="#DCF4FF")
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
        athlete = tk.Label(fourth_element, text=TREE[1]['М']['18+']['48-'][i//2][flag]["name"], bg="#DCF4FF")
    except TypeError:
        athlete = tk.Label(fourth_element, text=TREE[1]['М']['18+']['48-'][i//2][flag], bg="#DCF4FF")
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
        athlete = tk.Label(fourth_element, text=TREE[2]['М']['18+']['48-'][i//2][flag]["name"], bg="#DCF4FF")
    except TypeError:
        athlete = tk.Label(fourth_element, text=TREE[2]['М']['18+']['48-'][i//2][flag], bg="#DCF4FF")
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
        athlete = tk.Label(fourth_element, text=TREE[3]['М']['18+']['48-'][i//2][flag]["name"], bg="#DCF4FF")
    except TypeError:
        athlete = tk.Label(fourth_element, text=TREE[3]['М']['18+']['48-'][i//2][flag], bg="#DCF4FF")
    athlete.grid(column=3, row=8 * i, rowspan=8)

'''
Troika
'''

lottery.mainloop()


#AGREEEEE