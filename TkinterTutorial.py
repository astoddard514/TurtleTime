from tkinter import *

# Root widget, your main window
root = Tk() 

# Creating a label widget
myLabel = Label(root, text="Hello World!")
# Shoving it onto the screen (pack = only as big as content)
myLabel.pack()

# A GUI is always looping in order to notice any interaction, create a loop for our root window
root.mainloop()