# !/usr/bin/python3
# TODO: FINISH GRAPHICAL EXPRESSION OF BOOK OBJECT: Title and many tag labels and a button that brings up the book modify screen. Then, turn bookistbox into a scrollable canvas with instances of that object inside

import random

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from tkinter import messagebox
import tkinter.simpledialog
from tkinter import scrolledtext

TESTSOURCE = "./source2.txt"
SOURCE = "./source.txt"
HEIGHT = 600
WIDTH = 400


# We only have one column of books, so we can make currRow global
currRow = 0


# Precondition: Sourcefile of the correct format title|tag1,tag2|100.0
# Postcondition format: {{title, {tag1, tag2, tag3}}... } This is stored in sourcebooklist
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
                # Consider adding a crash function for really bad exceptions
                print("Exception found; malformed attrList? See below: ")
                print(attrList)
            attrList[2] = float(attrList[2].strip())
    return bookList

# We undo the operation of parse_source, "unwinding" each book back into a consistuent string we can save it in
def write_source(SOURCE):
    with open(SOURCE, 'r+') as src:
        for book in sourceBookList: # Consider replacing with writelines
            # Make the taglist
            tagString = ""
            for tag in book[1]:
                if(book[1][-1] != tag):
                    tagString = tagString + tag + ","
                else:
                    tagString = tagString + tag
            # TODO: THERE IS AN ERROR AROUND HERE SOMEWHERE RELATED TO WRITING BOOKS IN THE FILE WHEN WE'VE ADDED A NEW BOOK. YOUR TOP PRIORITY IS TO FIGURE THIS OUT.
            try:
                line = book[0] + "|" + tagString + "|" + str(book[2])
                src.write(line)
                src.write('\n')
            except: 
                print("Could not save {0}".format(str(book))) # Defeats stripping exceptions for malformed lines. This is a debugging tool.
def on_closing():
    write_source(SOURCE)
    root.destroy()



# Based on
#   https://web.archive.org/web/20170514022131id_/http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame
#   https://stackoverflow.com/questions/47850849/how-to-convert-this-example-from-python2-to-python3
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

        # Number to track most recently used row

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

    # self: The calling object
    # bookstr: the title of the book to insert
    # taglist: a list of strings represeting the list of tags
    # Depracated now I think?
    def insert(self, bookStr, tagList):
        pass
        # print("self.currRow: ", self.currRow)
        # self.currRow += 1
        # newBook = Book(self.interior, bookStr, tagList, self.currRow) 

class MainWindow:
    def __init__(self, master, sourceBookList):
        self.master = master
        master.title("Adler")
        master.geometry('{1}x{0}+{1}+{0}'.format(WIDTH,HEIGHT))

        # Add Label

        self.label = tk.Label(master, text="The Book Management Program", fg="blue", bg="#c0c2ae")
        self.label.place(x=(WIDTH/2), y = 0)

        # Add Main Booklist from initial list given in instructor

        booklistLabel = tk.Label(root, text = "Main Reading List")

        # TEST OUR ABILITY TO PACK A WIDGET INTO ROOT

#        testFrame = tk.Frame(root, bg='blue', height=100, width=100)
#        testFrame.place(anchor="center", x = 100, y = 100)

        # SET UP THE FRAME THAT WILL CONTAIN THE BOOKLIST AND THE SCROLLBAR

        booklistframe = ScrollableFrame(root) # Trying to add the scrollbar and the canvas to a parent frame
        booklistframe.place(anchor="nw",x = 4, y = 20) 

        # Create book objects in the debugWindow and add them to the bookArr array and booklistframe
        for index, item in enumerate(sourceBookList):
            title = item[0]
            tagList = item[1]
            rating = item[2]
            newBook = Book(booklistframe.interior, title, tagList, index+1, rating) 


        # ADD BOOK BUTTON AND FUNCTIONS

        B = tk.Button(root, text="Add Book", command = lambda: MainWindow.addBookPrompt(self, root, booklistframe)) # Note that we only list the addBook function (no parantheses), we do not actually invoke it by listing the name with parantheses.
        B.place(x = 60, y = 300)

    # Creates a dialogue exchange to collect information to construct a new book
    # Passes this information to addBook
    def addBookPrompt(self, root, booklistframe): # The function that the add book button activates. It gets a new book from the user and passes it to addBook
        newBook = tk.simpledialog.askstring( "AddBookPrompt", "Which book would you like to add?")
        tags = tk.simpledialog.askstring("AddBookPrompt", "Which tags would you like your new book to have? If none, leave this blank. Separate them with commas.")
        while(True):
            try:
                rating = tk.simpledialog.askstring("AddBookPrompt", "Which rating would you like the book to have? Please express this as a decimal number.")
                rating = float(rating)
                break
            except:
                self.inputErr()
        tagList = MainWindow.parse_tags(tags)
        MainWindow.addBook(self, newBook, tagList, booklistframe, rating)

    # Precondition: a string of the form "tag1,tag2,tag3"
    # Postcondition: a list of the form [tag1, tag2, tag3]
    def parse_tags(tags):
        tagList = tags.strip().split(',')
        for tag in tagList:
            tag = tag.strip()
        return tagList 

    #Precondition:
    #   NewBookName is a string representing the name of the new book
    #   tags is a list of strings representing the tags the book should have
    #   booklistframe is the scrollable frame that the book should appear in
    #   rating is a double ranging from 0 to 100 representing the book's quality
    #Poscondition:
    #   This function adds a string to sourceBookList that looks like this:
    #   ['title', ['tag1','tag2','tag3'], 100.0]

    def addBook(self, newBookName, tags, booklistframe, rating):
        newBook = Book(booklistframe.interior, newBookName, tags, 0, rating) 
        attrList = []
        attrList.append(newBookName) # Append title
        attrList.append(tags)
        attrList.append(rating) # Append rating
        sourceBookList.append(attrList)

    # Shows the user a popup window explaining that they made an input error
    def inputErr(self):
        tk.messagebox.showerror("Wrong input.", "Wrong input format. Try Again.")

# Class representing the book as it appears in booklistframe.
class Book(tk.Frame):
    # parent: parent in which to pack
    # title: the title of the book
    # tags: a list of strings representing the book's tags
    # index: the number of the book to be inserted
    def __init__(self, parent, title, tags, index, rating):
        self.title = title
        global currRow # Make sure to declare currRow as global within the class
        currRow += 1;
        if(index == 0):
            index = currRow
        for tagIndex, tag in enumerate(tags):
            self.tags.append(tag)
            self.tagLabel = tagLabel(tag, parent, index, tagIndex + 1)
        tk.Frame.__init__(self, parent)

        # Arrange layout

        self.titleLabel = titleLabel(title, parent, index)

    title = ''
    tags = []

    def printBook(self):
        print("{0} has the following tags: ".format(self.title))
        for tag in self.tags:
            print(tag)

    def addTag(self, tag):
        self.tags.append(tag)

    # Pass in the top level in the window hierarchy as root
    def infoPopup(self, root):
        newWindow = tk.Toplevel()
        newWindow.attributes('-topmost', 'true') # This keeps newWindow on top of all other windows in the tkinter application
        newWindow.title("Modify {0}".format(self.title))
        newWindow.geometry("200x200")
        tk.Label(newWindow, text="You are modifying {0}.".format(self.title))
        newWindow.grab_set()


class titleLabel(tk.Frame):
    def __init__(self, text, parent, myRow):
        tk.Frame.__init__(self, parent)
        t = tk.Label(parent, bg="gray", text=text, font=("FreeSerif", 15), anchor="w", fg="black", width=10, height=2)
        t.grid(row = myRow, column = 0)

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

# Create a debugWindow

def debugWindow():
    # Create a debugging Winow

    debugWindow = tk.Toplevel()
    debugWindow.attributes('-topmost', 'true') 
    debugWindow.title("Debug Window")
    debugWindow.geometry("200x200")

bookArr = []

root = tk.Tk() # Set tkinter root

# Format: {{title, {tag1, tag2, tag3}}... } This is stored in sourcebooklist
sourceBookList = parse_source(SOURCE) # Parse_source is the function that introduces the extra characters

window = MainWindow(root, sourceBookList) # Draw Main Window

# GUI Event Loop

root.protocol("WM_DELETE_WINDOW", on_closing) # Closing Protocol
root.mainloop()
