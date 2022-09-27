# Getting started with Tkinter
from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel = Label(root, text="Hello World!")

# Showing it onto screen
myLabel.pack()

root.mainloop()