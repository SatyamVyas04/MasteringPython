# Using Buttons to run certain functions
from tkinter import *
root = Tk()

def click():
    myLabel = Label(root, text="You've clicked a button1!!!1")
    myLabel.pack()

myButton = Button(root, text="ClickMe", command=click)
myButton.pack()

root.mainloop()