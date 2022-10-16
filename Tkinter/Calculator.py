from cgitb import text
from tkinter import *

root = Tk()
root.title("Simple Calculator") # renaming the Tk window

e = Entry(root, width=50, borderwidth=5) # Creating the Bar where numbers show
e.grid(row=0, column=0, columnspan=4, rowspan=2, padx=10, pady=10) # displaying it

def click(text): # writing what the Buttons do
    # e.delete(0, END)
    e.insert(1, text)

# Creating the buttons
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: click("1"), fg="yellow")
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: click("2"), fg="yellow")
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: click("3"), fg="yellow")
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: click("4"), fg="yellow")
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: click("5"), fg="yellow")
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: click("6"), fg="yellow")
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: click("7"), fg="yellow")
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: click("8"), fg="yellow")
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: click("9"), fg="yellow")
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: click("0"), fg="yellow") 
bcls = Button(root, text="cls", padx=35, pady=20, command=lambda: click("C"), fg="Blue") 
bequal = Button(root, text="=", padx=40, pady=20, command=lambda: click("="), fg="Black")
badd = Button(root, text="+", padx=40, pady=20, command=lambda: click("+"), fg="Black")
bsub = Button(root, text="-", padx=40, pady=20, command=lambda: click("-"), fg="Black")
bmult = Button(root, text="*", padx=40, pady=20, command=lambda: click("*"), fg="Black")
bdiv = Button(root, text="/", padx=40, pady=20, command=lambda: click("/"), fg="Black")


# Placing the buttons in the Tk window
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=1)
bcls.grid(row=5, column=0)
bequal.grid(row=5, column=2)
badd.grid(row=2, column=3)
bsub.grid(row=3, column=3)
bmult.grid(row=4, column=3)
bdiv.grid(row=5, column=3)

root.mainloop()