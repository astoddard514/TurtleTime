# Turtle time game for kids

# Learning resources: 
# https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1
# https://www.youtube.com/watch?v=lETQ3mvuzkQ

from tkinter import *
from tkinter import ttk
import turtle


# Set up screen
root = Tk()
root.title('Turtle Time')
root.geometry('1500x800+100+100')
root.config(bg= '#340f4f')





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
canvas = Canvas(root, width= 800, height= 700)
canvas.grid(row=0, rowspan= 3, column=0, padx=50, pady=50)



# Create turtle
tansy= turtle.RawTurtle(canvas)
tansy.shape("turtle")
tansy.resizemode("auto")
tansy.width(5)
tansy.color("#013220")
tansy.forward(100)

# Buttons

ft= 'Helvetica 15 bold'
btn_style= ttk.Style()
btn_style.configure('TButton', background= 'black', forground= 'black', font=ft)

# Draw a Shape Frame
draw_a_shape = LabelFrame(root, text="DRAW A SHAPE", padx=50, pady=50, background= '#340f4f') # padding inside of frame
draw_a_shape.grid(column= 1, row=0,)

triangle_btn= ttk.Button(draw_a_shape, text= 'Triangle', style= 'TButton')
square_btn= ttk.Button(draw_a_shape, text= 'Square', style= 'TButton')
circle_btn= ttk.Button(draw_a_shape, text= 'Circle', style= 'TButton')
ellipse_btn= ttk.Button(draw_a_shape, text= 'Ellipse', style= 'TButton')
pentagon_btn= ttk.Button(draw_a_shape, text= 'Pentagon', style= 'TButton')
hexagon_btn= ttk.Button(draw_a_shape, text= 'Hexagon', style= 'TButton')
septagon_btn= ttk.Button(draw_a_shape, text= 'Septagon', style= 'TButton')
octagon_btn= ttk.Button(draw_a_shape, text= 'Octagon', style= 'TButton')
star_btn= ttk.Button(draw_a_shape, text= 'Star', style= 'TButton')
spirograph_btn= ttk.Button(draw_a_shape, text= 'Spirograph', style= 'TButton')
cute_btn= ttk.Button(draw_a_shape, text= 'Cute', style= 'TButton')


triangle_btn.grid(row= 1, column=1)
square_btn.grid(row= 2, column=1)
circle_btn.grid(row= 3, column=1)
ellipse_btn.grid(row= 4, column=1)
pentagon_btn.grid(row= 1, column= 2)
hexagon_btn.grid(row= 2, column= 2)
septagon_btn.grid(row= 3, column= 2)
octagon_btn.grid(row= 4, column= 2)
star_btn.grid(row= 1, column= 3)
spirograph_btn.grid(row= 2, column= 3)
cute_btn.grid(row= 3, column= 3)

# Build a Shape Frame

build_a_shape = LabelFrame(root, text="BUILD A SHAPE", padx=50, pady=50, background= '#340f4f') # padding inside of frame
build_a_shape.grid(column= 1, row=1)

triangle_btn= ttk.Button(build_a_shape, text= 'Triangle', style= 'TButton')
square_btn= ttk.Button(build_a_shape, text= 'Square', style= 'TButton')
circle_btn= ttk.Button(build_a_shape, text= 'Circle', style= 'TButton')
ellipse_btn= ttk.Button(build_a_shape, text= 'Ellipse', style= 'TButton')
pentagon_btn= ttk.Button(build_a_shape, text= 'Pentagon', style= 'TButton')
hexagon_btn= ttk.Button(build_a_shape, text= 'Hexagon', style= 'TButton')
septagon_btn= ttk.Button(build_a_shape, text= 'Septagon', style= 'TButton')
octagon_btn= ttk.Button(build_a_shape, text= 'Octagon', style= 'TButton')
star_btn= ttk.Button(build_a_shape, text= 'Star', style= 'TButton')
spirograph_btn= ttk.Button(build_a_shape, text= 'Spirograph', style= 'TButton')
cute_btn= ttk.Button(build_a_shape, text= 'Cute', style= 'TButton')


triangle_btn.grid(row= 1, column=1)
square_btn.grid(row= 2, column=1)
circle_btn.grid(row= 3, column=1)
ellipse_btn.grid(row= 4, column=1)
pentagon_btn.grid(row= 1, column= 2)
hexagon_btn.grid(row= 2, column= 2)
septagon_btn.grid(row= 3, column= 2)
octagon_btn.grid(row= 4, column= 2)
star_btn.grid(row= 1, column= 3)
spirograph_btn.grid(row= 2, column= 3)
cute_btn.grid(row= 3, column= 3)

# Controls Frame

controls = LabelFrame(root, text="CONTROLS", padx=50, pady=50, background= '#340f4f') # padding inside of frame
controls.grid(column= 1, row=2)

colors= ['red', 'purple', 'yellow',
        'pink', 'blue', 'lightblue', 
        'brown', 'white', 'orange']

pen_color= ttk.Combobox(controls, values= colors)
pen_color.config(font= ft, width= 10)
pen_color.set('Change Color')
pen_color.grid(row= 1, column= 1)
pen_color['state']= 'readonly'

penup_btn= ttk.Button(controls, text= 'Pen Up', style= 'TButton')
pendown_btn= ttk.Button(controls, text= 'Pen Up', style= 'TButton')

foward_btn= ttk.Button(controls, text= 'Forward', style= 'TButton')
backward_btn= ttk.Button(controls, text= 'Backward', style= 'TButton')
right_btn= ttk.Button(controls, text= 'Left', style= 'TButton')
left_btn= ttk.Button(controls, text= 'Right', style= 'TButton')

penup_btn.grid(row= 2, column= 1)
pendown_btn.grid(row= 3, column= 1)
foward_btn.grid(row= 1, column=3)
backward_btn.grid(row= 3, column=3)
left_btn.grid(row= 2, column=2)
right_btn.grid(row= 2, column=4)







# Labels

# Inputs

# Colors





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







