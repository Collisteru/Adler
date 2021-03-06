# SETUP.PY



# This file is at the top of the hierarchy. It does not import any internal libraries.

import random
import time

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox
import tkinter.simpledialog
from tkinter import scrolledtext


currRow = 0


"""
Precondition: Sourcefile of the correct format title|tag1,tag2|100.0
Postcondition format: {{title, {tag1, tag2, tag3}}... } This is stored in sourcebooklist
Postcondition: List of Book objects corresponding to the 
"""
def parse_source(SOURCE):
    with open(SOURCE, 'r+') as src:
        lines = src.readlines()
        lineList = [line for line in lines]
        bookList = []
        # Parse each line in the file for all the information that must be passed to the book constructor: titles, tags, attributes, and others.
        for line in lineList:
            attrList = [attr for attr in line.split('|')]
            # Process Tags into their own sublist
            tagList = []
            try:
                for tag in attrList[1].split(','): # Tags are their own list in the second slot of attrList
                    tagList.append(tag)
                attrList[1] = tagList;
                bookList.append(attrList)
            except:
                pass
                # Consider adding a crash function for really bad exceptions
            attrList[2] = float(attrList[2].strip())
    return bookList

"""
We undo the operation of parse_source, "unwinding" each book back into a consistuent string we can save it in
sourceBookList is the master list of books that the program manages
"""
def write_source(SOURCE, sourceBookList):
    with open(SOURCE, 'r+') as src:
        for book in sourceBookList: # Consider replacing with writelines
            # Make the taglist
            tagString = ""
            for tag in book[1]:
                if(book[1][-1] != tag):
                    tagString = tagString + tag + ","
                else:
                    tagString = tagString + tag
            try:
                line = book[0] + "|" + tagString + "|" + str(book[2])
                src.write(line)
                src.write('\n')
            except: 
                print("Could not save {0}".format(str(book))) # Defeats stripping exceptions for malformed lines. This is a debugging tool.

def on_closing(root, sourceBookList, SOURCE):
    write_source(SOURCE, sourceBookList)
