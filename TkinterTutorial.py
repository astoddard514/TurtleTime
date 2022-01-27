from tkinter import *

# Root widget, your main window
root = Tk() 

# 1 Creating a thing
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Angela")
# 2 Put the thing onto the screen (pack = only as big as content)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# But these can actually be coded in this format:
mylabel3 = Label(root, text="Label 3").grid(row=0, column=2)
myLabel4 = Label(root, text="Label 4").grid(row=1, column=3)
    # might not be as clean when widgets become more complicated

# A GUI is always looping in order to notice any interaction, create a loop for our root window
root.mainloop()