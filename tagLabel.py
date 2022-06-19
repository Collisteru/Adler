import random

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox
import tkinter.simpledialog
from tkinter import scrolledtext

from miscfuncs import *
from tagLabel import *


class tagLabel(tk.Frame):
    def __init__(self, text, parent, myRow, myColumn):
        tk.Frame.__init__(self, parent)
        HEX_COLORS = [ \
                "#79A8DA", \
                "#84E5E0", \
                "#88C192", \
                "#C3C793", \
                "#CCAA9D", \
                "#D1A5A5"  \
                ]
        color = HEX_COLORS[random.randint(0, len(HEX_COLORS) - 1)]
        t = tk.Label(parent, bg=color, text=text, font=("FreeSans", 8), fg="black", width=8, height=2)
        t.grid(row=myRow, column = myColumn)

