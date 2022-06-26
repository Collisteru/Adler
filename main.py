## FILE MAIN.PY
# !/usr/bin/python3



from others import *

## DIAGNOSTICS

# import json
# print(globals())

# Printing definitely works!
# print("printTest")

window = MainWindow(root, sourceBookList, root) # Draw Main Window

# GUI Event Loop

root.mainloop()
try:
    root.protocol("WM_DELETE_WINDOW", on_closing(root, window.sourceBookList, SOURCE))
except tkinter.TclError:
    pass
