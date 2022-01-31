# Turtle time game for kids

# Learning resources: 
# https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1
# https://www.youtube.com/watch?v=lETQ3mvuzkQ

from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
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

    def set_color():
        tansy.color('<<ComboboxSelected>>')

    def penup():
        tansy.penup()
    def pendown():
        tansy.pendown()

    def forward():
        tansy.forward(100)
    def backward():
        tansy.backward(100)

    def rotate_left():
        tansy.left(20)
    def rotate_right():
        tansy.right(20)

    def clear_canvas():
        tansy.clear()
        tansy_default()

# Button styling

ft= 'Helvetica 15 bold'
btn_style= ttk.Style()
btn_style.configure('TButton', background= 'black', forground= 'black', font=ft)
    

# Canvas
canvas = Canvas(root, width= 800, height= 700)
canvas.grid(row=0, rowspan= 3, column=0, padx=50, pady=50)

game_label = Label(canvas, text="Turtle Time", font= 'Helvetica 30 bold', fg= "green", background= "white")
game_label.place(relx= 0.5, y=50, anchor = 'n')

clear_btn= Button(canvas, text="Clear Canvas", command = Controls.clear_canvas)
clear_btn.place(x= 650, y= 650)


# Create turtle
tansy= turtle.RawTurtle(canvas)
def tansy_default():
    tansy.shape("turtle")
    tansy.resizemode("auto")
    tansy.width(3)
    tansy.color("green")
tansy_default()

# Draw a Shape Frame
draw_a_shape = LabelFrame(root, text="DRAW A SHAPE", font= 'Helvetica 15 bold', padx=25, pady=25, background= '#340f4f', fg= "white", labelanchor= 'n') # padding inside of frame
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

build_a_shape = LabelFrame(root, text="BUILD A SHAPE", font= 'Helvetica 15 bold', padx=25, pady=25, background= '#340f4f', fg= "white", labelanchor= 'n') # padding inside of frame
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

controls = LabelFrame(root, text="CONTROLS", font= 'Helvetica 15 bold',  background= '#340f4f', fg= "white", labelanchor= 'n', padx= 25, pady= 25) # padding inside of frame
controls.grid(column= 1, row=2)

colors= ['red', 'purple', 'yellow',
        'pink', 'blue', 'lightblue', 
        'brown', 'white', 'orange']

cbox= ttk.Combobox(controls, values= colors)
cbox.config(font= ft, width= 8)
cbox.set('Color')
cbox.grid(row= 1, column= 1, padx= 20, pady= 10)
cbox['state']= 'readonly'
# cbox.bind('<<ComboboxSelected>>', command= Controls.set_color)

penup_btn= ttk.Button(controls, text= 'Pen Up', style= 'TButton', width= 7, command= Controls.penup)
pendown_btn= ttk.Button(controls, text= 'Pen Down', style= 'TButton', width= 7, command= Controls.pendown)
foward_btn= ttk.Button(controls, text= 'Forward', style= 'TButton', width= 8, command= Controls.forward)
backward_btn= ttk.Button(controls, text= 'Backward', style= 'TButton', width= 9, command= Controls.backward)

penup_btn.grid(row= 2, column= 1, padx= 25, pady=10)
pendown_btn.grid(row= 3, column= 1, padx= 25, pady= 10)
foward_btn.grid(row= 2, column=4, padx=10, pady= 10)
backward_btn.grid(row= 3, column=4, padx= 10, pady= 10)


left_turn_arrow = Image.open(r"C:/Users/angel/Desktop/Coding/Turtle game/TurtleTime/Images/LeftRotateArrow.png")
resize_left_arrow = left_turn_arrow.resize((50, 50))
left_arrow = ImageTk.PhotoImage(resize_left_arrow)

right_turn_arrow = Image.open(r"C:/Users/angel/Desktop/Coding/Turtle game/TurtleTime/Images/RightRotateArrow.png")
resize_right_arrow = right_turn_arrow.resize((50, 50))
right_arrow = ImageTk.PhotoImage(resize_right_arrow)


left_turn_btn = ttk.Button(controls, image= left_arrow, command= Controls.rotate_left)
left_turn_btn.grid(row= 2, rowspan= 2,  column= 3)
right_turn_btn = ttk.Button(controls, image= right_arrow, command= Controls.rotate_right)
right_turn_btn.grid(row= 2, rowspan= 2, column= 5)





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







