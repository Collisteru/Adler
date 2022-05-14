# !/usr/bin/python3
import tkinter as tk
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



        # SETTING UP THE MAIN BOOK LIST BOX AND ITS SCROLL BAR


        # SET UP THE FRAME THAT WILL CONTAIN THE BOOKLIST AND THE SCROLLBAR

        booklistframe = tk.Frame(root, bg="blue", height=300, width=(WIDTH)) # Trying to add the scrollbar and the canvas to a parent frame
        booklistframe.place(x=((1/16)*WIDTH),y=40)

        # CREATE SCROLLBAR IN THE BOOKLISTFRAME


        scrollbar = tk.Scrollbar(booklistframe, orient="vertical") 
#        scrollbar.place(x = 400-16, y = 4) 
        scrollbar.pack(side="left",fill="both", expand="true")

        booklistbox = tk.Listbox(booklistframe, width = 40, height = 13, yscrollcommand = scrollbar.set) # TODO: Consider hardcoding width or making it variable based on a larger root value 


        # POPULATING BOOKISTBOX WITH ITEMS FROM SOURCEBOOKLIST

        for index, book in enumerate(sourceBookList):
            booklistbox.insert(tkinter.END, book.strip()) 


#        booklistbox.place(x = 0, y = 0) # Place the booklistbox int he top right corner of the booklistframe
        booklistbox.pack(side="left")

        booklistbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = booklistbox.yview)

        # ADD BOOK BUTTON AND FUNCTIONS

        B = tk.Button(root, text="Add Book", command = lambda: MainWindow.addBookPrompt(self, root, booklistbox)) # Note that we only list the addBook function (no parantheses), we do not actually invoke it by listing the name with parantheses.
        B.place(x = 60, y = 300)

    def addBookPrompt(self, root, booklistbox): # The function that the add book button activates. It gets a new book from the user and passes it to addBook
        newBook = tk.simpledialog.askstring( "AddBookPrompt", "Which book would you like to add?")
        MainWindow.addBook(self, newBook, booklistbox)

    def addBook(self, newBook, booklistbox):
        booklistbox.insert(tkinter.END, newBook) 
        sourceBookList.append(newBook)




class Book:
    def __init__(self, title, tags):
        self.title = title
        for tag in tags:
            self.tags.append(tag)
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


# Set tkinter root

root = tk.Tk()

# Set source of book information

# At the moment souceBookList is just a list of bare strings representing the titels
sourceBookList = parse_source(SOURCE) # Parse_source is the function that introduces he extra characters

# Create book objects and add them to the bookArr array based on sourceBookList
bookArr = []
for item in sourceBookList:
    bookArr.append(Book(item, []))


# Draw Main Window

window = MainWindow(root, sourceBookList)

# Test Book Popup

bookArr[0].infoPopup(root)

# GUI Event Loop

root.protocol("WM_DELETE_WINDOW", on_closing) # Make Sure Closing Protocol Works
root.mainloop()
