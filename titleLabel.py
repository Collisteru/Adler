import random

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox
import tkinter.simpledialog
from tkinter import scrolledtext

from miscfuncs import *
from tagLabel import *

class titleLabel(tk.Frame):
    # Todo: replace this with actual popup function
    def testFunc(self, event, label):
        print("testing...")

    # Why aren't these working?
    def on_enter(self, event, label):
        label.config(background= "#9c9c9c")

    def on_leave(self, event, label):
        label.config(background="gray")

    def __init__(self, text, parent, myRow):
        tk.Frame.__init__(self, parent)
        t = tk.Label(parent, bg="gray", text=text, font=("FreeSerif", 15), anchor="w", fg="black", width=15, height=2)
        a = 5;
        # Really, clicking on a label should activate the function to bring up the book info popup
        # (Why do we have to list t twice? Why is the first parameter ignored?
        t.bind("<Button-1>", lambda e:self.testFunc(t, t))
        t.bind('<Enter>', lambda e:self.on_enter(t, t))
        t.bind('<Leave>', lambda e:self.on_leave(t, t))
        t.grid(row = myRow, column = 0)
