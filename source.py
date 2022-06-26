# SOURCE.PY



from setup import *

TESTSOURCE = "./source2.txt"
SOURCE = "./source.txt"

sourceBookList = parse_source(SOURCE) # Parse_source is the function that introduces the extra characters

BookList = [] # List of Book objects to be populated later

root = tk.Tk() # Set tkinter root
