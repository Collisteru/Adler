import random
import time
import re

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox as mb
import tkinter.simpledialog
from tkinter import scrolledtext



# Precondition: Opens a new window with the question given and a place to input an answer, as well as an "OK" button and a "Cancel" button.
# Postcondition: Throws a CloseWindowException if the user closes the window by pressing Cancel. Asks again if the user inputs a blank answer or an answer with only punctuation marks. Otherwise, returns the value of the user's answer.
class query():
    def __init__(self, title, question):
        self.fieldInput = "___"
        newWindow = tk.Tk()
        newWindow.title(title)
        newWindow.geometry("400x300")
        newWindow.attributes('-topmost', 'true')
        entryBox = tk.Entry(newWindow)
        entryBox.grid(row=0, column=0)
        okayButton = tk.Button(newWindow, text="Ok", bg="green", command= lambda:query.queryOK(self=query, root=newWindow, field=entryBox))
        cancelButton = tk.Button(newWindow, text="Cancel", bg="red", command= lambda:query.queryCancel(newWindow))
        okayButton.grid(row=1, column=0)
        cancelButton.grid(row=1, column=1)

    def queryOK(self, root, field):
        # Checks if user's response is correct, if not it passes control back to newWindow
        # If so, it closes newWindow
        fieldInput = field.get()
        notalphanum = re.compile("\W")
        if(fieldInput == "" or (notalphanum.match(fieldInput) != None)):
            warning = tk.messagebox.showwarning(title="Invalid Input", message="Careful! Don't input empty strings or strings that contain non-alphanumeric characters.")
            root.lower()
            return False 
        else:
            root.destroy()
            # It's interesting that "self" isn't brought to be a parameter of the function by the higher query scope... very strange.
            query.setFieldInput(self=query, newFieldInput=fieldInput)
            return fieldInput

    def queryCancel(self, root):
        root.destroy()
        return CloseWindowException

    def printFieldInput(self):
        print(query.fieldInput)

    def getFieldInput(self):
        return self.fieldInput

    def setFieldInput(self, newFieldInput):
        self.fieldInput = newFieldInput

    class CloseWindowException(Exception):
        pass
