# OTHERS.PY



from Book import *

HEIGHT = 600
WIDTH = 400
# We only have one column of books, so we can make currRow global


# CLASS SCROLLABLE FRAME


"""
Based on
   https://web.archive.org/web/20170514022131id_/http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame
   https://stackoverflow.com/questions/47850849/how-to-convert-this-example-from-python2-to-python3
"""
class ScrollableFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """
    # TODO Use repeatinterval on the arrow buttons to make this not bad.
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



# CLASS MAINWINDOW

class MainWindow:
    def __init__(self, master, sourceBookList, root):
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

        self.sourceBookList = sourceBookList

        # Create book objects in the debugWindow and add them to the bookArr array and booklistframe
        for index, item in enumerate(sourceBookList):
            title = item[0]
            tagList = item[1]
            rating = item[2]
            newBook = Book(booklistframe.interior, title, tagList, index+1, rating) 
            BookList.append(newBook)

        # ADD BOOK BUTTON AND FUNCTIONS

        B = tk.Button(root, text="Add Book", command = lambda: MainWindow.addBookPrompt(self, root, booklistframe)) # Note that we only list the addBook function (no parantheses), we do not actually invoke it by listing the name with parantheses.
        B.place(x = 60, y = 300)

    """
    Creates a dialogue exchange to collect information to construct a new book
    Passes this information to addBook
    """
    def addBookPrompt(self, root, booklistframe): # The function that the add book button activates. It gets a new book from the user and passes it to addBook
        global sourceBookList
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
        MainWindow.addBook(self, newBook, tagList, booklistframe, rating, self.sourceBookList)

    # Precondition: a string of the form "tag1,tag2,tag3"
    # Postcondition: a list of the form [tag1, tag2, tag3]
    def parse_tags(tags):
        tagList = tags.strip().split(',')
        for tag in tagList:
            tag = tag.strip()
        return tagList 

    #precondition:
    #   newbookname is a string representing the name of the new book
    #   tags is a list of strings representing the tags the book should have
    #   booklistframe is the scrollable frame that the book should appear in
    #   rating is a double ranging from 0 to 100 representing the book's quality
    #   sourcebooklist is the master list of books the program manages


    #poscondition:

    #   this function adds a string to sourcebooklist that looks like this:
    #   ['title', ['tag1','tag2','tag3'], 100.0]

    def addBook(self, newBookName, tags, booklistframe, rating, sourceBookList):
        newBook = Book(booklistframe.interior, newBookName, tags, 0, rating) 
        BookList.append(newBook)
        attrList = []
        attrList.append(newBookName) # Append title
        attrList.append(tags)
        attrList.append(rating) # Append rating
        sourceBookList.append(attrList)

    # Shows the user a popup window explaining that they made an input error
    """
    TODO: Modify this so that the user can cancel inputting the information by (for example) closing the window or pressing "cancel."
    """
    def inputErr(self):
        tk.messagebox.showerror("Wrong input.", "Wrong input format. Try Again.")
