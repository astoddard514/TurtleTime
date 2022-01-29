# Turtle time game for kids

from tkinter import *
from tkinter import ttk
import turtle
import tools 



# Set up screen
root = Tk()
root.title('Turtle Time')
root.geometry('1500x900')
# tools.center(root) # center window on screen
root.config(bg= 'indigo')

class Shapes:

    def triangle(self):
        pass
    def square(self):
        pass
    def pentagon(self):
        pass
    def hexagon(self):
        pass
    def septagon(self):
        pass
    def octogon(self):
        pass
    def star(self): # include user inputs for sides/angles
        pass
    def spirograph(self): # fancy design with options for inputs
        pass
    def cute(self):
        pass

class Custom:

    def custom_inputs(self):
        pass

class Movements:

    def forward(self):
        pass
    def backward(self):
        pass
    def right(self):
        pass
    def left(self):
        pass


# Canvas on left
canvas = Canvas(root, width= 800, height= 800)

canvas.grid(rowspan=12, column=0, padx=50, pady=50)

# Frames on right

# Create turtle
tansy= turtle.RawTurtle(canvas)
tansy.shape("turtle")
tansy.resizemode("auto")
tansy.width(5)

tansy.color("#013220")
tansy.forward(100)
tansy.right(45)
tansy.forward(100)
tansy.right(45)
tansy.forward(100)
tansy.right(45)

# Buttons

ft= 'tahoma 10 bold'
btn_style= ttk.Style()
btn_style.configure('TButton', background= 'cyan', forground= 'black', font=ft)


foward_btn= ttk.Button(root, text= 'Forward')
backward_btn= ttk.Button(root, text= 'Backward')
right_btn= ttk.Button(root, text= 'Left')
left_btn= ttk.Button(root, text= 'Right')


foward_btn.grid(row= 1, column=6)
backward_btn.grid(row=3, column=6)
right_btn.grid(row=2, column=7)
left_btn.grid(row=2, column=5)

# Labels

# Inputs



# Global frame 
  # Penup/Pendown
  # Color
  # Arrows 

# Choose a shape frame
  # Triangle
  # Square
  # Parallelogram
  # Star/Spirograph
  # Spiral
  # Something cute

# Custom parameter div - experiment with range, length, angle inputs (run button for div)
  # Custom inputs frame
  # Range = Entry(Custom frame)
  # Range.pack()

root.mainloop()







