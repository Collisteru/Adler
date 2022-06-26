# TITLELABEL.PY



from source import *
from tagLabel import *
# What does this module need from others, anyway?
from others import *
from ModifyWindow import *



class titleLabel(tk.Frame):
    # Todo: replace this with actual popup function
    title = ""
    row = 0

    def displayBookWindow(self, event, label, index):
        modWin = ModifyWindow(self.get_myBook(self.row))

    def on_enter(self, event, label):
        label.config(background= "#9c9c9c")

    def on_leave(self, event, label):
        label.config(background="gray")

    def setTitle(self, newTitle):
        print("Called with newTitle {0}".format(newTitle))
        self.title = newTitle

    def get_myBook(self, myRow):
        return BookList[myRow-1]

    def __init__(self, text, parent, myRow):
        tk.Frame.__init__(self, parent)
        self.title = text
        self.row = myRow
        t = tk.Label(parent, bg="gray", text=text, font=("FreeSerif", 15), anchor="w", fg="black", width=15, height=2)
        a = 5

        # Really, clicking on a label should activate the function to bring up the book info popup
        # (Why do we have to list t twice? Why is the first parameter ignored?

        t.bind("<Button-1>", lambda e:self.displayBookWindow(self.get_myBook(myRow), t, myRow))
        t.bind('<Enter>', lambda e:self.on_enter(t, t))
        t.bind('<Leave>', lambda e:self.on_leave(t, t))
        t.grid(row = myRow, column = 0)
