# MODIFYWINDOW.PY


from setup import *


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


        print("In ModifyWindow: self.Book: ", self.Book)
        changeTitle = tk.Button(self.newWindow, text="Change Title", command = self.Book.setTitle("ButtonTitle"))
        changeTitle.grid(row=1, column=0)

        changeTags = tk.Button(self.newWindow, text="Change Tags", command = self.Book.setTags("ButtonTags"))
        changeTags.grid(row=2, column=0)
