# MODIFYWINDOW.PY


from setup import *
from Book import *
import query

class ModifyWindow():
    newWindow = 0

    def __init__(self, Book):
        self.Book = Book
        self.newWindow = tk.Toplevel()
        self.newWindow.attributes('-topmost', 'true') # This keeps newWindow on top of all other windows in the tkinter application
        self.newWindow.title("Modify {0}".format(Book.title))
        self.newWindow.geometry("300x300")
        label = tk.Label(self.newWindow, text="You are modifying {0}.".format(Book.title))
        label.grid(row=0, column=0)

        """ These both desparately need testing! """



        # What functions should I put here to change the title of the books? 
        # BOOK MUST MAKE TITLECHANGEQUERY WHEN IT WANTS TO SET A TITLE
        changeTitle = tk.Button(self.newWindow, text="Change Title", command = lambda: Book.makeTitleQuery())
        changeTitle.grid(row=1, column=0)


        changeTags = tk.Button(self.newWindow, text="Change Tags", command = lambda: Book.setTags(self))
        changeTags.grid(row=2, column=0)

    def testFunc():
        pritn("Hello, ModifyWindow testFunc!")
