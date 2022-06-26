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
        self.title = newTitle
        self.t.config(text=newTitle) # Actually change titleLabel representation

    def get_myBook(self, myRow):
        return BookList[myRow-1]

    def __init__(self, text, parent, myRow):
        tk.Frame.__init__(self, parent)
        self.title = text
        self.row = myRow
        self.t = tk.Label(parent, bg="gray", text=text, font=("FreeSerif", 15), anchor="w", fg="black", width=15, height=2)

        # Really, clicking on a label should activate the function to bring up the book info popup
        # (Why do we have to list t twice? Why is the first parameter ignored?

        self.t.bind("<Button-1>", lambda e:self.displayBookWindow(self.get_myBook(myRow), self.t, myRow))
        self.t.bind('<Enter>', lambda e:self.on_enter(self.t, self.t))
        self.t.bind('<Leave>', lambda e:self.on_leave(self.t, self.t))
        self.t.grid(row = myRow, column = 0)
