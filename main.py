## FILE MAIN.PY

from others import *
from miscfuncs import *

## DIAGNOSTICS

# import json
# print(globals())


bookArr = []

root = tk.Tk() # Set tkinter root

# Format: {{title, {tag1, tag2, tag3}}... } This is stored in sourcebooklist
sourceBookList = parse_source(SOURCE) # Parse_source is the function that introduces the extra characters

window = MainWindow(root, sourceBookList, root) # Draw Main Window

# GUI Event Loop

root.mainloop()
try:
    root.protocol("WM_DELETE_WINDOW", on_closing(root, window.sourceBookList, SOURCE))
except tkinter.TclError:
    pass
