# Infinite loop?
# !/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog

SOURCE = "./source.txt"


def parse_source(SOURCE):
    with open(SOURCE, 'r+') as src:
        lines = src.readlines()
        outputList = [line for line in lines]
    return outputList


def write_source(SOURCE):
    with open(SOURCE, 'r+') as src:
        for book in sourceBookList: # Consider replacing with writelines
            book = str(book.strip())
            src.write(book)
            src.write('\n')

def on_closing():
    write_source(SOURCE)
    root.destroy()

class MainWindow:

    masterList = []

    def __init__(self, master, sourceBookList):
        self.master = master
        master.title("Adler")
        master.geometry('400x300+400+300')

        # Add Label

        self.label = tk.Label(master, text="The Book Management Program")
        self.label.pack(pady=10)

        # Add Main Booklist from initial list given in instructor

        booklistLabel = tk.Label(root, text = "Main Reading List")
        booklistbox = tk.Listbox(root)

        for index, book in enumerate(sourceBookList):
            booklistbox.insert(tkinter.END, book.strip()) 
        booklistbox.pack()

        # Add Button

        B = tk.Button(root, text="Add Book", command = lambda: MainWindow.addBookPrompt(self, root, booklistbox)) # Note that we only list the addBook function (no parantheses), we do not actually invoke it by listing the name with parantheses.
        B.pack()

    def addBookPrompt(self, root, booklistbox): # The function that the add book button activates. It gets a new book from the user and passes it to addBook
        newBook = tk.simpledialog.askstring( "AddBookPrompt", "Which book would you like to add?")
        MainWindow.addBook(self, newBook, booklistbox)

    def addBook(self, newBook, booklistbox):
        booklistbox.insert(tkinter.END, newBook) 
        sourceBookList.append(newBook)

class Book:
    def __init__(self, title):
        this.title = title
    tags = []

# Set tkinter root

root = tk.Tk()

# Set source of book information

sourceBookList = parse_source(SOURCE) # Parse_source is the function that introduces he extra characters


# Draw Main Window

window = MainWindow(root, sourceBookList)

# GUI Event Loop

root.protocol("WM_DELETE_WINDOW", on_closing) # Make Sure Closing Protocol Works
root.mainloop()
