# Turtle time game for kids

# Learning resources: 
# https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1
# https://www.youtube.com/watch?v=lETQ3mvuzkQ

from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
import turtle


# Set up screen
root = Tk()
root.title('Turtle Time')
root.geometry('1500x800+100+100')
root.config(bg= '#340f4f')



class Shapes:

    def formula(sides):
        angle = 360/sides
        for side in range(sides):
            tansy.forward(100)
            tansy.left(angle)

    def triangle():
        Shapes.formula(3)
    def square():
        Shapes.formula(4)
    def pentagon():
        Shapes.formula(5)
    def hexagon():
        Shapes.formula(6)
    def septagon():
        Shapes.formula(7)
    def octogon():
        Shapes.formula(8)

    radius = 50

    def circle():
        radius = 50
        tansy.circle(radius)

    def ellipse():
        tansy.seth(-45)
        radius = 100
        for i in range(2):
            tansy.circle(radius, 90)
            tansy.circle(radius//2, 90)

        
    def star(): # include user inputs for sides/angles?
        for i in range(5):
            tansy.forward(100)
            tansy.right(144)

    def spirograph(): # fancy design with options for inputs?
        pass
    def cute():
        pass

class Custom:
    
    # custom_sides.get() 

    def custom_inputs(self):
        pass

class Controls:

    def forward(self):
        pass
    def backward(self):
        pass
    def right(self):
        pass
    def left(self):
        pass

    def clear_canvas():
        tansy.clear()
        tansy_default()

# Canvas
canvas = Canvas(root, width= 800, height= 700)
canvas.grid(row=0, rowspan= 3, column=0, padx=50, pady=50)

clear_btn= Button(canvas, text="Clear Canvas", command = Controls.clear_canvas)
clear_btn.place(x= 650, y= 650)

# Create turtle
tansy= turtle.RawTurtle(canvas)
def tansy_default():
    tansy.shape("turtle")
    tansy.resizemode("auto")
    tansy.width(5)
    tansy.color("green")
tansy_default()

# Buttons

ft= 'Helvetica 15 bold'
btn_style= ttk.Style()
btn_style.configure('TButton', background= 'black', forground= 'black', font=ft)

# Draw a Shape Frame
draw_a_shape = LabelFrame(root, text="DRAW A SHAPE", padx=50, pady=50, background= '#340f4f') # padding inside of frame
draw_a_shape.grid(column= 1, row=0,)

triangle_btn= ttk.Button(draw_a_shape, text= 'Triangle', style= 'TButton', command = Shapes.triangle)
square_btn= ttk.Button(draw_a_shape, text= 'Square', style= 'TButton', command = Shapes.square)
circle_btn= ttk.Button(draw_a_shape, text= 'Circle', style= 'TButton', command = Shapes.circle)
ellipse_btn= ttk.Button(draw_a_shape, text= 'Ellipse', style= 'TButton', command = Shapes.ellipse)
pentagon_btn= ttk.Button(draw_a_shape, text= 'Pentagon', style= 'TButton', command = Shapes.pentagon)
hexagon_btn= ttk.Button(draw_a_shape, text= 'Hexagon', style= 'TButton', command = Shapes.hexagon)
septagon_btn= ttk.Button(draw_a_shape, text= 'Septagon', style= 'TButton', command = Shapes.septagon)
octagon_btn= ttk.Button(draw_a_shape, text= 'Octagon', style= 'TButton', command = Shapes.octogon)
star_btn= ttk.Button(draw_a_shape, text= 'Star', style= 'TButton', command = Shapes.star)
spirograph_btn= ttk.Button(draw_a_shape, text= 'Spirograph', style= 'TButton', command = Shapes.spirograph)
cute_btn= ttk.Button(draw_a_shape, text= 'Cute', style= 'TButton', command = Shapes.cute)


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

custom_sides = Entry(root)  
custom_sides.grid()
custom_sides.insert(0, "Choose a #: 0-100 ") # default text in input field

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







