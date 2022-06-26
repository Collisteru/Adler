import random
import time
import re

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox as mb
import tkinter.simpledialog
from tkinter import scrolledtext


class CloseWindowException(Exception):
    pass

# Precondition: Opens a new window with the question given and a place to input an answer, as well as an "OK" button and a "Cancel" button. 
# * origin is the Book that created the query
# Postcondition: Throws a CloseWindowException if the user closes the window by pressing Cancel. Asks again if the user inputs a blank answer or an answer with only punctuation marks. Otherwise, returns the value of the user's answer.
class query():
    def __init__(self, title, question, origin):
        self.origin = origin
        self.fieldInput="___"
        self.newTitleFlag=False # Prevents us from getting the title too early
        newWindow = tk.Tk()
        newWindow.title(title)
        newWindow.geometry("400x300")
        newWindow.attributes('-topmost', 'true')
        entryBox = tk.Entry(newWindow)
        entryBox.grid(row=0, column=0)
        okayButton = tk.Button(newWindow, text="Ok", bg="green", command= lambda:self.queryOK(root=newWindow, field=entryBox))
        cancelButton = tk.Button(newWindow, text="Cancel", bg="red", command= lambda:self.queryCancel(root=newWindow))
        okayButton.grid(row=1, column=0)
        cancelButton.grid(row=1, column=1)

    # Unfortunatey this relies on calling Book APIs so this function isn't fully general
    # TODO Make query more fully general and then have a child bookQuery function whose queryOK method specifically calls Book methods
    def queryOK(self, root, field):
        # Checks if user's response is correct, if not it passes control back to newWindow
        # If so, it closes newWindow
        newFieldInput = field.get()
        notalphanum = re.compile("\W")
        if(newFieldInput == "" or (notalphanum.match(newFieldInput) != None)):
            warning = tk.messagebox.showwarning(title="Invalid Input", message="Careful! Don't input empty strings or strings that contain non-alphanumeric characters.")
            root.lower()
            return False 
        else:
            root.destroy()
            self.setFieldInput(newFieldInput=newFieldInput)
            self.fieldInput = newFieldInput

            # CALL TO BOOK API GOES HERE
            # origin not specified
            self.origin.setTitle(self.fieldInput)
            # Just in case :D
            return self.fieldInput

    def queryCancel(self, root):
        root.destroy()
        return CloseWindowException

    def printFieldInput(self):
        print(query.fieldInput)

    def getFieldInput(self):
        # What if getFieldInput returns a different self.fieldInput because WE'RE INPUTTING A DIFFERENT SELF?
        return self.fieldInput

    def setFieldInput(self, newFieldInput):
        self.fieldInput = newFieldInput


