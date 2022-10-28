# Learning to take Input
from tkinter import *
root = Tk()

def click():
    myLabel = Label(root, text="Welcome " + e.get())
    myLabel.pack()

#Taking Entry
e = Entry(root, width=50, bg="blue")
e.insert(0, "Your Name...")
e.pack()

myButton = Button(root, text="Enter your Name and Click me...", command=click, fg="white")
myButton.pack()


root.mainloop()