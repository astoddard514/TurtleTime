# https://www.youtube.com/watch?v=7A_csP9drJw

from tkinter import *

root = Tk() 

# entry widget for input fields
e = Entry(root) # can add parameters for width, fg, bg, borderwidth,  
e.pack()
e.insert(0, "Enter your name: ") # default text in input field

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick) # state, padx, pady after text; when calling functions with command, leave out the function parenthesis. Color can also be changed in this set (fg=foreground color, bg=background color)
myButton.pack()

root.mainloop()