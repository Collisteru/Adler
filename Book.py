# CLASS BOOK


from titleLabel import *
from query import *

# Class representing the book as it appears in booklistframe.
class Book(tk.Frame):
    tags = []
    # parent: parent in which to pack
    # title: the title of the book
    # tags: a list of strings representing the book's tags
    # index: the number of the book to be inserted
    def __init__(self, parent, Title, tags, index, rating):
        global currRow # Make sure to declare currRow as global within the class
        self.title = Title
        currRow += 1;
        if(index == 0):
            index = currRow
        for tagIndex, tag in enumerate(tags):
            self.tags.append(tag)
            self.tagLabel = tagLabel(tag, parent, index, tagIndex + 1)
        tk.Frame.__init__(self, parent)

        # Arrange layout

        self.titleLabel = titleLabel(Title, parent, index)

    def printBook(self):
        print("{0} has the following tags: ".format(self.title))
        for tag in self.tags:
            print(tag)

    def getTitle(self):
        return self.title

    def getTags(self):
        return self.tags


    # Makes a query object that can later call this object's setTitle() method.
    def makeTitleQuery(self):
        titleQuery = query("Edit Title", "What should the new title be?", origin = self)

    # Called by a query method we've made with makeTitleQuery
    def setTitle(self, newTitle):
        oldTitle = self.title
        self.title = newTitle
        self.titleLabel.setTitle(newTitle)

    def setTags(self, newTags):
        print("Called Book.setTags!")
        self.tags = newTags

    def addTag(self, tag):
        self.tags.append(tag)

    # Add info popup that triggers when you click on a book
    # Pass in the top level in the window hierarchy as root
    def infoPopup(self, root):
        newWindow = tk.Toplevel()
        newWindow.attributes('-topmost', 'true') # This keeps newWindow on top of all other windows in the tkinter application
        newWindow.title("Modify {0}".format(self.title))
        newWindow.geometry("300x300")
        label = tk.Label(newWindow, text="You are modifying {0}.".format(self.title))
        label.grid(row=0, column=0)

        # Grab_set prevents users from interacting with the original window.  At the moment it causes bugs, so we will not use it.
        # newWindow.grab_set()
