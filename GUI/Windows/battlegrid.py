__all__ = ["BattleGrid"]

import tkinter as tk


class BattleGrid:
    def __init__(self, master):
        self.frame = tk.Frame(master=master)
        self.frame.config(width=300, height=300)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        frame1 = tk.Frame(self.frame, width=300, height=150, background="green")
        frame2 = tk.Frame(self.frame, width=300, height=150, background="blue")

        frame1.pack(fill=tk.X)
        frame2.pack(fill=tk.X)

        tk.Button(master=frame2, text="1").pack(side=tk.LEFT)
        tk.Button(master=frame2, text="2").pack(side=tk.RIGHT)

