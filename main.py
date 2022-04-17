from tkinter import *


listOfBooks = ["The Grapes of Math", "The Sterling Stopwatch", "How to get rich selling rice on the internet", "Galois Theory for Dummies", "Postmodern Anthropology"]


class MainWindow:
	def __init__(self, master):
		self.master = master
		master.title("Adler")
		master.geometry('400x300+400+300')

# Add Label
		self.label = Label(master, text="The Book Management Program")
		self.label.pack(pady=10)

# Add Booklist

		booklist = Booklist(self, mast)

# TestFunc

	def testFunc(self):
		print("hello!")


def makeMainBookList(root, listOfBooks):
	booklistLabel = Label(root, text = "Main Reading List")
	booklist = Listbox(root)
	for index, book in enumerate(listOfBooks):
		booklist.insert(index, book)
	booklist.pack()



root = Tk()
window = MainWindow(root)
window.testFunc()
root.mainloop()
