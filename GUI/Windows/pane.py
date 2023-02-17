from tkinter import *


class NavigationWindow(PanedWindow):
    def __init__(self, master=None, cnf={}, **kwargs):
        Widget.__init__(self, master, "panedwindow", cnf, kwargs)


