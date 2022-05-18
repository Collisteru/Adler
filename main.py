# !/usr/bin/python3
# TODO: FINISH GRAPHICAL EXPRESSION OF BOOK OBJECT: Titel and many tag labels and a button that brings up the book modify screen. Then, turn bookistbox into a scrollable canvas with instances o that object inside

import functools # From random StackExcahnge post; is it really a good idea, though?
import random

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox
import tkinter.simpledialog
from tkinter import scrolledtext

   

SOURCE = "./source.txt"
HEIGHT = 600
WIDTH = 400

def parse_source(SOURCE):
    with open(SOURCE, 'r+') as src:
        lines = src.readlines()
        outputList = [line for line in lines]
    return outputList


def write_source(SOURCE):
    with open(SOURCE, 'r+') as src:
        for book in sourceBookList: # Consider replacing with writelines
            try:
                book = str(book.strip())
                src.write(book)
                src.write('\n')
            except: # Defeats stripping exceptions for malformed lines. This is a debugging tool.
                print("Could not save ", {0}, ".".format(str(book)))
def on_closing():
    write_source(SOURCE)
    root.destroy()



# Based on
#   https://web.archive.org/web/20170514022131id_/http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

class ScrollableFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=LEFT, expand=FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
        anchor=NW)

        # Add Border
        ttk.Style().configure(self, highlightbackground="blue", highlightthickness=2)

# Track changes to the canvas and frame width and sync them,
# also updating the scrollbar.
    def _configure_interior(event):
    # Update the scrollbars to match the size of the inner frame.
        size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
        canvas.config(scrollregion="0 0 %s %s" % size)
        if interior.winfo_reqwidth() != canvas.winfo_width():
        # Update the canvas's width to fit the inner frame.
            canvas.config(width=interior.winfo_reqwidth())
            interior.bind('<Configure>', _configure_interior)

    def _configure_canvas(event):
        if interior.winfo_reqwidth() != canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            canvas.bind('<Configure>', _configure_canvas)

    def insert(self, child):
        child.pack()

class MainWindow:

    masterList = []

    def __init__(self, master, sourceBookList):
        self.master = master
        master.title("Adler")
        master.geometry('{1}x{0}+{1}+{0}'.format(WIDTH,HEIGHT))

        # Add Label

        self.label = tk.Label(master, text="The Book Management Program", fg="blue", bg="#c0c2ae")
        self.label.place(x=(WIDTH/2), y = 0)

        # Add Main Booklist from initial list given in instructor

        booklistLabel = tk.Label(root, text = "Main Reading List")



        # SET UP THE FRAME THAT WILL CONTAIN THE BOOKLIST AND THE SCROLLBAR

        booklistframe = ScrollableFrame(root, height=300, width=(WIDTH)) # Trying to add the scrollbar and the canvas to a parent frame
        booklistframe.place(x=((1/16)*WIDTH),y=40)

        # CREATE SCROLLBAR IN THE BOOKLISTFRAME

#        scrollbar = tk.Scrollbar(booklistframe, orient="vertical") 
#        scrollbar.place(x = 400-16, y = 4) 
#        scrollbar.pack(side="left",fill="both", expand="true")


        # Disable booklistframe
#         booklistframe = tk.Listbox(booklistframe, width = 40, height = 13, yscrollcommand = scrollbar.set) # TODO: Consider hardcoding width or making it variable based on a larger root value 

        # Create book objects in the debugWindow and add them to the bookArr array.
        bookArr = []
        for item in sourceBookList:
            bookArr.append(Book(booklistframe, item, ["tag1", "tag2"]))


        # CREATE BOOKLIST CANVAS, POPULATE IT WITH BUTTONS

        for index, book in enumerate(bookArr):
            print(type(book))
            booklistframe.insert(book)

        
        booklistframe.place(x = 0, y = 0) # Place the booklistframe int he top right corner of the booklistframe
        booklistframe.pack(side="left")

#         booklistframe.config(yscrollcommand = scrollbar.set)
#         scrollbar.config(command = booklistframe.yview)

        # ADD BOOK BUTTON AND FUNCTIONS

        B = tk.Button(root, text="Add Book", command = lambda: MainWindow.addBookPrompt(self, root, booklistframe)) # Note that we only list the addBook function (no parantheses), we do not actually invoke it by listing the name with parantheses.
        B.place(x = 60, y = 300)

    def addBookPrompt(self, root, booklistframe): # The function that the add book button activates. It gets a new book from the user and passes it to addBook
        newBook = tk.simpledialog.askstring( "AddBookPrompt", "Which book would you like to add?")
        MainWindow.addBook(self, newBook, booklistframe)

    def addBook(self, newBook, booklistframe):
        booklistframe.insert(newBook) 
        sourceBookList.append(newBook)


class Book(tk.Frame):
    def __init__(self, parent, title, tags):
        self.title = title
        for tag in tags:
            self.tags.append(tag)
        tk.Frame.__init__(self, parent)
        # Arrange layout

#        self.titleLabel = tk.Label(parent, self.title)
        self.tagLabel = tagLabel(title, parent) 
        self.tagLabel.pack()

    title = ''
    tags = []

    def printBook(self):
        print("{0} has the following tags: ".format(self.title))
        for tag in self.tags:
            print(tag)

    def addTag(self, tag):
        self.tags.append(tag)
        print("appended tag {0} to {1}".format(tag, self.title))

    # Pass in the top level in the window hierarchy as root
    def infoPopup(self, root):
        print("inside infoPopup!")
        newWindow = tk.Toplevel()
        newWindow.attributes('-topmost', 'true') # This keeps newWindow on top of all other windows in the tkinter application
        newWindow.title("Modify {0}".format(self.title))
        newWindow.geometry("200x200")
        tk.Label(newWindow, text="You are modifying {0}.".format(self.title))
        newWindow.grab_set()

class tagLabel(tk.Frame):
    def __init__(self, text, parent):
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
        t = tk.Label(parent, bg=color, text=text, font=("FreeSans", 17), fg="black", width=8, height=2)
        t.pack()

# Create a debugWindow

def debugWindow():
    # Create a debugging Winow

    debugWindow = tk.Toplevel()
    debugWindow.attributes('-topmost', 'true') 
    debugWindow.title("Debug Window")
    debugWindow.geometry("200x200")


# Set tkinter root

root = tk.Tk()

# Set source of book information

# At the moment souceBookList is just a list of bare strings representing the titels
sourceBookList = parse_source(SOURCE) # Parse_source is the function that introduces he extra characters


# Test Book objects by packign them into debugWindow


# Draw Main Window

window = MainWindow(root, sourceBookList)

# Test Book Popup

# bookArr[0].infoPopup(root)

# GUI Event Loop

root.protocol("WM_DELETE_WINDOW", on_closing) # Make Sure Closing Protocol Works
root.mainloop()
