from tkinter import *


root = Tk() 

def myClick():
    myLabel = Label(root, text="Look I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick) # state, padx, pady after text; when calling functions with command, leave out the function parenthesis. Color can also be changed in this set (fg=foreground color, bg=background color)
myButton.pack()

root.mainloop()